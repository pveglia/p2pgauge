#!/usr/bin/env python

"""
Usage: ./P2PDemo.py directory
"""

# additional library
from PyQt4 import QtCore, QtGui

#GUI modules
import FigureView
#import P2PDemoTabView
import p2pdemo_mainWindow

#standard modules
from optparse import OptionParser
import sys
import os
import os.path
import re
import signal
import glob
import getopt
from subprocess import *
import tempfile
import time
from tabgnuplotwidget import TabGnuplotWidget
import processing

class P2PDemoWidget (TabGnuplotWidget):
	"""
	Main widget of the demo.

	Search the given directory ad creates a tab for each subdirectory.
	Each directory should contain a file named description.txt containing
	a line to be displayed above the figure
	"""

	def update_gui(self, ports=[], globalPeersInfo = {}):
		"update the port table in the conf tab"

		if len(ports) == 0:
			return
		table = self.ui.port_table
		for i in table.selectedRanges():
			table.setRangeSelected(i, False)

		port = self.ui.self_port.text()

		tot_pkts = tot_bytes = tot_rate = 0

		table.clearContents()
		for row, vals in enumerate(ports):
			selected = False

			for col, s in enumerate(vals):
				tabItem = QtGui.QTableWidgetItem(s)

				if col == 0 and (tabItem.text() == port or port == '*'):
					selected = True

				if selected:
					tabItem.setBackgroundColor(QtGui.QColor('#ffff00'))

				table.setItem(row, col, tabItem)

			# compute values for * port
			tot_pkts += int(vals[1])
			tot_bytes += int(vals[2])
			tot_rate += float(vals[3])

		# now set * port
		row = len(ports)
		color = (port == '*') and QtGui.QColor(255,0,0) or \
											QtGui.QColor(255,0,0,50)
		port_it = QtGui.QTableWidgetItem('*')
		port_it.setBackgroundColor(color)
		table.setItem(row, 0, port_it)
		pkt_it = QtGui.QTableWidgetItem(str(tot_pkts) )
		pkt_it.setBackgroundColor(color)
		table.setItem(row, 1, pkt_it)
		bytes_it = QtGui.QTableWidgetItem(str(tot_bytes))
		bytes_it.setBackgroundColor(color)
		table.setItem(row, 2, bytes_it)
		rate_it = QtGui.QTableWidgetItem(str(tot_rate))
		rate_it.setBackgroundColor(color)
		table.setItem(row, 3, rate_it)

		self.ui.self_as.setText(self.opts.myAS)
		self.ui.pub_ip.setText(self.opts.pubIP)

		# GUI is updated after the shift of CURR_PEERS in PREVIOUS_PEERS
		if globalPeersInfo["very_total_bytes"] > 0:
			contr_perc = float(globalPeersInfo["t_bytes"]) / globalPeersInfo["very_total_bytes"] * 100
		else:
			contr_perc = 0.0
		self.statusBar().showMessage("Total Peers =%d, total bytes=%.2e (%.1f%% w contrib), \
peers in last dt=%d, b=%d" % \
										(globalPeersInfo["t_peers"],
										 globalPeersInfo["very_total_bytes"],
										 contr_perc,
										 globalPeersInfo["p_peers"],
										 globalPeersInfo["p_bytes"]))

	def port_selected(self):
		"slot called when the user selects a new active port to watch"
		table = self.ui.port_table

		# selection is the selected row

		selection = table.selectedIndexes()
		if len(selection) == 0:
			return
		row = selection[0].row()

		try:
			port = table.item(row, 0).text()
		except:
			sys.stderr.write("\nWarning: empty record selected")
			return

		self.ui.self_port.setText(port)
		self.proc_thread.port = port


	def self_selected(self):
		"slot called when the user digits a new ip/port to watch"

		port = self.ui.self_port.text()
		ip = self.ui.self_ip.text()
		self.emit(QtCore.SIGNAL('socket_selected'), ip, port)

	def setup_conf_tab(self):
		"configure the conf tab"

		self.ui.self_ip.setText(self.opts.addr)
		self.ui.self_port.setText(self.opts.port)
		self.ui.self_cc.setText(self.opts.cc)

		self.ui.port_table.setRowCount(10)

		self.connect(self.ui.port_table, QtCore.SIGNAL("itemSelectionChanged()"),
					 self.port_selected)

		self.connect(self.ui.self_ip, QtCore.SIGNAL("editingFinished()"),
				     self.self_selected)

	def __init__(self, opts, parent = None, directory = ""):
		"constructor, takes the root directory"
		TabGnuplotWidget.__init__(self)

		self.dir = directory
		self.outdir = self.dir + "/demo.out"

		#self.flow_table_refresh = 500
		self.opts = opts
		opts.kiviat_index = []

		#setup the UI
		self.ui = p2pdemo_mainWindow.Ui_p2p_mainWindow()
		self.ui.setupUi(self)
		self.setup_gnuplot_widget(self.ui.CentralTabview, self.outdir, opts = self.opts)
		self.opts.tabs = self.tabs

		#setup the conf tab
		self.setup_conf_tab()

		#delete old gnuplot file in 31_geoip and 32_geoip and 40_Kiviat
		scripts = glob.glob(self.outdir + "/31_geoip/*.gp")
		for i in scripts:
			os.remove(i)

		scripts = glob.glob(self.outdir + "/32_geoip/*.gp")
		for i in scripts:
			os.remove(i)

		scripts = glob.glob(self.outdir + "/40_Kiviat/*.gp")
		for i in scripts:
			os.remove(i)


		self.setup_thread()
		self.setup_signals()


	def setup_thread(self):
		self.proc_thread = processing.ProcessingThread(self.opts)
		self.proc_thread.start()
		self.connect(self, QtCore.SIGNAL('socket_selected'), self.proc_thread.socket_changed)
		self.connect(self.proc_thread, QtCore.SIGNAL('update_gui'), self.update_gui)

	def setup_signals(self):
		self.connect(self.ui.snapshotButton, QtCore.SIGNAL("pressed()"),
			self.proc_thread.make_snapshot)

def parse_opt():
	parser = OptionParser()
	parser.add_option('-a', '--address', type='string', dest='addr', default='192.168.0.15')
	parser.add_option('-p', '--port', type='string', dest='port', default='16800')
	parser.add_option('-c', '--cc', type='string', dest='cc', default='fr')
	parser.add_option('-r', '--capture', type='string', dest='capture', default=None)
	parser.add_option('-i', '--interface', type='string', dest='interface', default=None)
	parser.add_option('-f', '--filter', type='string', dest='filter', default='udp')
	parser.add_option('-I', '--interval', type='int', dest='interval', default=5)
	parser.add_option('-d', '--debug', action='store_true', dest='debug', default=False)
	parser.add_option('-s', '--screen_shot', action='store_true', dest='screen_shot', default=False)
	parser.add_option('-C', '--no-capprobe', action='store_true', dest='no_capprobe', default=False)
	parser.add_option('-b', '--capprobe-info', type='string', dest='pinfo_file', default=None)
	parser.add_option('-t', '--contr-threshold', type='int', dest='contr_thresh', default=2)
	parser.add_option('-P', '--public-ip', type='int', dest='pubIP', default=None)

	return parser.parse_args()

def main():
	app = QtGui.QApplication(sys.argv)
	opts, args = parse_opt()

	if len(args) != 1:
		directory = '.'
	else:
		directory = args[0]

	p2pWidget = P2PDemoWidget(opts, directory = directory)
	p2pWidget.show()
	#p2pWidget.connect(app, QtCore.SIGNAL("lastWindowClosed()"), p2pWidget.kill_processing)

	sys.exit(app.exec_())

if __name__ == "__main__":
	main()
