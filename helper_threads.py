from PyQt4 import QtCore
import re
from subprocess import *
import time
import errno
import printer

class CapProbeThread(QtCore.QRunnable):
	"Thread that makes the capprobe for retreiving RTT, CAP and HOP"

	ttl_re = re.compile("ttl=(\d+)")
	C_re   = re.compile("C= ([0-9.]+)")
	rtt_re = re.compile("rtt min/avg/max/mdev = (.*)/.*/.*/.*")

	def __init__(self, peer, opts):
		QtCore.QRunnable.__init__(self)
		self.peer = peer
		self.socket = peer.socket
		self.address, self.port = self.socket.split(' ')
		self.opts = opts

	def traceRoute(self):
		cmd = "traceroute -I -n -f 5 -q 1 %s | tail -n 1 | awk '{print $1}'" % self.address

		# XXX try except block needed
		res = None
		while True:
			try:
				printer.printDebug (self.opts, "traceroute!")
				res = Popen(cmd, stdout=PIPE, shell=True).communicate()[0].rstrip()
				break
			except OSError, e:
				if e.errno == errno.EINTR:
					print "Error traceroute"
					continue
				else:
					raise
		printer.printDebug (self.opts, "RES: %s" % res)
		if res and (res != '*' and res != '30'):
			self.peer.HOP = int(res)
		else:
			self.peer.HOP = None
			printer.printDebug (self.opts, "%s cannot traceroute" % self.address)
		# printer.printDebug (self.opts, "%s finito! HOP: %d" % (self.address, self.peer.HOP))
		# print "%s HOP %s" % (self.address, str(self.peer.HOP))

	def run(self):
		rtt = None
		hop = None
		cap = None

#		print "partito %s" % self.address
		cmd = "./ping -c 20 -i 0.5 -t 30 %s " % self.address
		while True:
			try:
				printer.printDebug (self.opts, "ping %s!" % self.address)
				p = Popen(cmd, shell=True, stdout=PIPE)
				break
			except OSError, e:
				if e.errno == errno.EINTR:
					print "Error ping"
					continue
				else:
					raise
		fcap = p.stdout

		# parsing of capprobe file
		while True:
			try:
				for line in fcap:

					# res = self.ttl_re.search(line)
					# if res:
					# 	ttl = int(res.groups()[0])
					# 	#print "%s TTL %d" % (self.address, ttl)
					# 	#if ttl > 30 and ttl < 129:
					# 	#	hop = 128 - ttl

					res = self.C_re.search(line)
					if res:
						cap = res.groups()[0]

					res = self.rtt_re.search(line)
					if res:
						rtt = res.groups()[0]
				break
			except OSError, e:
				if e.errno == errno.EINTR or e.errno == 0:
					continue
				else:
					raise
			except IOError, e:
				printer.printDebug(self.opts,  "Errore n %d" % e.errno)
				continue


		self.peer.CAP = cap
#		self.peer.HOP = hop #XXX only for windows peers
		self.peer.RTT = rtt

		status = p.wait()
		if  (hop and hop > 50) or not hop:
			# print "High HOP peer, running traceroute..."
			self.traceRoute()
			# print "finished tracerouting!"
		else:
			self.peer.HOP = hop #XXX only for windows peers
		self.peer.CapPstaus = status
		printer.printDebug (self.opts, "%s finito! %s %s %s w status: %s" % (self.address, cap, hop, rtt, status))


	def set_socket(self, socket):
		self.socket = socket
		self.address = socket.split(' ')[0]
		self.port = socket.split(' ')[1]


class TarThread(QtCore.QThread):
	def __init__(self, opts, parent = None):
		QtCore.QThread.__init__(self, parent)
		self.opts = opts

	def run(self):
		printer.printDebug (self.opts, "processo tar partito")
		# First make a copy of the output folder
		fname = "demo.out.%s.tgz" % (time.strftime("%d.%m.%Y_%H-%M"))
		#TODO check how to send in bg stdout
#		os.spawnv(os.P_NOWAIT, "/sw/bin/tar", ["tar", "cvzf", fname, "demo.out"])
		retc = call(["tar", "cvzf", fname, "demo.out"], stdout = file("/dev/null", 'w'))
		printer.printDebug(self.opts,  "processo tar finito")

class PubIPThread(QtCore.QThread):
	"""
	This class implement a QThread and has as a goal to acquire
	the public IP address of the machine. It contacts a web server with a php
	script that creates a page with the IP. Surely there are millions of way to
	do the same thing in a more elegant way but you know...
	"""
	def __init__(self, opts, parent = None):
		QtCore.QThread.__init__(self, parent)
		self.opts = opts

	def run(self):
		printer.printDebug(self.opts, "Thread partito!")
		import urllib2
		# To not hang up with this thread, there's a limited number of tries
		tries = 3
		got = False
		ip = "0.0.0.0"
		while tries > 0 and not got:
			try:
				printer.printDebug(self.opts, "trying to acquire pubip")
				# Comment out this line if you want to skip the request and
				# fill ip var with the value you want (must be in four dotted notation)
				ip = urllib2.urlopen("http://api.externalip.net/ip/").read()
				# ip = urllib2.urlopen("https://vinrouge.enst.fr/~paolo/pubip.php").read()
				print "Public ip: ", ip
				if ip != None:
					got = True
			except Exception,e:
				print "failed: tries left: %d" % (tries,)
				print e
				tries -= 1
		printer.printDebug(self.opts, "Ip pubblico: %s" % (ip,))
		self.opts.pubIP = ip
