"""
This is a python module wich has similar functions to the perl's one
written by Dario Rossi for the NapaWine project
"""

import sys
from subprocess import Popen, PIPE
import traceback
import os

class FlowID:
	"class which manages the id of the peers flow"

	def __init__(self, ownIP):
		self.ownIP = ownIP
		self.idmap = {}
		self.counter = 0

	def __make_sign(self, p):

		if p.ips in self.ownIP:
			sign = "%s,%s" % (p.ips, p.ipd)
			out = "+"
			return (sign, out)

		sign = "%s,%s" % (p.ipd, p.ips)
		out = "-"
		return (sign, out)


	def getFlowID(self, p):
		"return the flow Id for this packet"
		sign, out = self.__make_sign(p)

		if sign in self.idmap:
			return "%s%d" % (out,self.idmap[sign])

		self.idmap[sign] = self.counter
		self.counter += 1

		return "%s%d" % (out,self.idmap[sign])

def open_capture(filename, payload=False, gzipped=False, filter=None):
	"Given a filename, this method opens a pipe between tcpdump.hack and returns the stream"
	if gzipped:
		cmd_str = "zcat %s | tcpdump.hack -n -tt -r-" % (filename)
	else:
		cmd_str = "tcpdump.hack -n -tt -r %s" % (filename)

	if payload:
		cmd_str += " -x"

	if filter:
		cmd_str += " '%s'" % (filter)

	print os.environ['PATH']
	try:
		input = Popen(cmd_str, shell=True, stdout=PIPE).stdout
	except Exception as e:
		traceback.print_exc()
	#input, dummy_out = subprocess.popen2(cmd_str)
	return input

def open_live_capture(interface, payload=False, filter=None):
	"Given a filename, this method opens a pipe between tcpdump.hack and returns the stream"
	cmd_str = "tcpdump.hack -n -tt -i %s" % (interface)

	if payload:
		cmd_str += " -x"

	if filter:
		cmd_str += " '%s'" % (filter)

	input = Popen(cmd_str, shell=True, stdout=PIPE).stdout
	#input, dummy_out = popen2(cmd_str)
	return input

class PacketException(Exception):
	pass

class Packet:
	"simple packet class if you don't need"

	def __init__(self, line):
		"initialize from a tcpdump.hack line"
		try:
			values = line.rstrip("\n").split()
			(self.time, self.size, self.proto,
			self.ips, self.ps, self.ipd, self.pd)  = values
		except:
			raise PacketException()
