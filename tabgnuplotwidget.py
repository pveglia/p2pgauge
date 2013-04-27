#!/usr/bin/env python

"""
The TabGnuplotWidget is a enriched QTabWidget.

It takes a directory as parameter and creates a tab for each subdirectory.
Every subdirectory is supposed to contain either some pngs pictures or some
gnuplot scripts or a file named postprocess.py.

Each tab displays the pngs found in the corresponding directory using the
FigureView widget. You can scroll among pictures with the key 'PgUp', 'PgDown'
and with 'End' you have the showcase view.

There is a drawing thread which every now and then (actually every refresh
msec) execute the postprocess.py and gnuplot scripts, if any, found in the
directory of the current tab. This scripts hopefully update the pngs which
are then repainted on the screen.

See the main function at the end of the file for an example
"""

# additional library
from PyQt4 import QtCore, QtGui
import Gnuplot

import sys
import os
import os.path
import re
import glob
import operator
import subprocess
import errno

#GUI modules
import FigureView

refresh_mutex = QtCore.QMutex()

class DrawingThread (QtCore.QThread):
	"Thread which calls gnuplot to generate the pictures"

	#interval between execution of scripts in a directory
	refresh = 2000
	
	def __getPostProcess(self, path):
		"return the postprocess.py script"
		return glob.glob("%s/postprocess.py" % path)

	def __getScript(self, path, ext="sh"):
		"returns scripts in the current tab directory"
		return glob.glob("%s/*.%s" % (path, ext))

	def __executeShellScript(self, script, path):
		"change to the current tab directory and execute script"

		while True:
			try:
				p = subprocess.Popen("cd %s && %s" % (path,script), shell = True)
				break
			except OSError, e:
				if e.errno == errno.EINTR:
					continue
				else:
					raise
		sts = os.waitpid(p.pid, 0)
#		os.system("cd %s && %s" % (path,script))

	def __executeGpScript(self, script, path):
		"change to the current tab directory and execute script"

#		if path not in self.gp:
#			self.gp[path] = gp = Gnuplot.Gnuplot()
#		else:
#			gp = self.gp[path]

#		os.system('cd %s && gnuplot %s' % (path, script))
		while True:
			try:
				p = subprocess.Popen('cd %s && gnuplot %s' % (path, script), shell = True)
				break
			except OSError, e:
				if e.errno == errno.EINTR:
					continue
				else:
					raise
		sts = os.waitpid(p.pid, 0)
		#of = script[:-3]

		##this until scripts don't include this natively
		#gp = Gnuplot.Gnuplot(debug = self.debug)

		#terminal = "set terminal %s %s" % (FigureView.gnuplot_terminal, 
		#								   FigureView.gnuplot_terminal_opts)

		##XXX I don't know if the pathname works only in Ubuntu...
		#if self.skwidget.opts.screen_shot:
		#	terminal = terminal + \
		#		" font '/usr/share/fonts/truetype/ttf-dejavu/DejaVuSans.ttf' 14"

		#if self.skwidget.isMaximized():
		#	terminal = terminal + "giant size 1024,768 "

		#
		#gp("cd '%s'" % (path))
		#gp(terminal)
		#gp("set output '%s.%s'" % (of, FigureView.gnuplot_terminal))
		#gp("load '%s'" % (script))

	def __init__(self, skwidget, parent = None):
		"constructor: takes a reference to the main widget"
		QtCore.QThread.__init__(self, parent)
		self.skwidget = skwidget
		self.gp = {}
		self.debug = 0

		#self.__cd2CurrentDir(self.skwidget.dir)

	def run(self):
		"""
		main function of the thread, every refresh seconds executes
		scripts in the current tab directory
		"""

		counter = 0

		while(True):
			#print("%d Thread esegue" % (counter) )

			if self.skwidget.isFigureTab():
				#this tab must be refreshed
				path = self.skwidget.getCurrentTabDir()

				scripts = self.__getScript(path)
				postprocess = self.__getPostProcess(path)

				for i in postprocess:
					self.__executeShellScript(i, path)
				
				if len(scripts) != 0:
					#execute the scripts
					for i in scripts: 
						self.__executeShellScript(i, path)
				else:
					#try gnuplot
					scripts = self.__getScript(path, "gp")
				#	scripts.sort() 
				#	scripts.reverse()

					for i in scripts:
#						print "Eseguo: %s" % i
						self.__executeGpScript(i, path)

			self.msleep(self.refresh)
			counter += 1
		return

class TabGnuplotWidget(QtGui.QMainWindow):
	"The actual widget"
	
	def __init__(self, n_stable_tab = 1, figure_refresh = 200, parent = None):
		"constructor"
		QtGui.QWidget.__init__(self, parent)
		#path to tab title
		self.tab_title_file = "/title.tab"
		#number of tab that must not be refreshed
		self.n_stable_tab = n_stable_tab
		#interval between figure refreshing in msec
		self.figure_refresh = figure_refresh

	def setup_gnuplot_widget(self, tabview, outdir='.', drawing = True, opts = None):
		"set the actual QTabWidget and the directory"
		self.tabview = tabview
		self.outdir = outdir

		self.setup_tabs(opts)
		self.setup_timers()

		if drawing:
			self.drawer = DrawingThread(self)
			self.drawer.start()

	def getCurrentTabDir(self):
		"return the directory containing images for the current tab"
		return self.getCurrentWidget().path

	def isFigureTab(self):
		"returns true if the current widget is figure tab (must be refreshed)"
		return self.tabview.currentIndex() >= self.n_stable_tab
	
	def addFigureTab(self, subdir, opts):
		"add a new tab and create relative widget to window"

		#adding title to the tab
		try:
			title_file = open(self.outdir + "/" + subdir + self.tab_title_file, 'r')
			title = title_file.readline().rstrip("\n")
			title_file.close()
		except IOError:
			print "Cannot find title for tab %s" % (subdir)
			title = "undefined"

		withCheckBox = False
		if title.lower().find('kiviat') != -1:
			withCheckBox = True
		f = FigureView.FigureView(self.outdir, subdir, checkBox = withCheckBox, gplotWidg = self)

		index = self.tabview.addTab(f, title)
		self.tabs[index] = f

		if title.lower().find('kiviat') != -1:
			opts.kiviat_index.append(index)

	def setup_tabs(self, opts):
		"adds tabs from directories"

		self.tabs = {}
		regexp = re.compile("(\d\d)_")
		
		dirlist = []
		for i in os.listdir(self.outdir):
			#check if the directory starts with '.'
			if i[0] != "." and os.path.isdir(self.outdir + "/" + i):
				grps = regexp.search(i).groups()
				dirlist.append( (int(grps[0]), i) )

		dirlist.sort(cmp, key= lambda x: operator.getitem(x, 1))

		for dummy, i in dirlist:
			self.addFigureTab(i, opts)

	def getCurrentWidget(self):
		"return the widget corresponding to the current tab"
		return self.tabview.currentWidget()

	def setup_timers(self):
		"initializes timers from refreshing"
		#timer for the refreshing of figures
		self.fig_timer = QtCore.QTimer()
		self.fig_timer.setInterval(self.figure_refresh)
		self.connect(self.fig_timer, QtCore.SIGNAL("timeout()"), self.updateFigures)
		self.fig_timer.start()

	def updateFigures(self):
		"slot called from the timer wich refresh the current tab widget"
#		print "updating............."
		if(refresh_mutex.tryLock()):
			if self.isFigureTab():
				w = self.getCurrentWidget()
				w.initialize_figures()
				w.update()
			refresh_mutex.unlock()
		else:
			print "Something is already refreshing..."

	def keyPressEvent(self, event):
		"""
		pass the event to the current tab widget 
		in order to switch figure or make the show_case...
		"""

		self.getCurrentWidget().keyPressEvent(event)
		QtGui.QWidget.keyPressEvent(self, event)

def main():
	
	app = QtGui.QApplication(sys.argv)
	widget = TabGnuplotWidget(n_stable_tab = 0)
	tabw = myQTabWidget()
	widget.setup_gnuplot_widget(tabw, 'train.out/')
	tabw.show()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()
