#!/usr/bin/env python
# encoding: utf-8
"""


This script can be used to compute pdf, cdf and ccdf.

The data file can be passed through the -f flag or piped to the stdin.

File or streams can be formatted in a tabular fashion and the -c flag is used to
specify the right column to analyze.

Other option are:
	-f open the file specified
	-c --col use the values as the colon to analyze
	-b describe bins to use start:end:step
	-w bins width
	-l limits the data in a given range (e.i. -l 0,1600)
	-g logscale

It can also be used calling:
def make_histo(tmp_vec, bins, outStr, limits, width, log):

Created by Paolo Veglia on 2008-04-30.
"""

import sys
import getopt
from scipy import *
import types


help_message = '''
The help message goes here.
Usage: histo.py [-f file] -c column -b num_bins -l low_lim,upp_lim
'''
percentils = (0.01, 0.05, 0.1, 0.25, 0.5, 0.75, 0.9, 0.95, 0.99)


class Usage(Exception):
	def __init__(self, msg):
		self.msg = msg

class Cumulator:
	def __init__(self):
		self.__cum__ = 0.0
	def sum(self, val):
		self.__cum__ += val
		return self.__cum__

def makeBins(str, log):
	if not log:
		_bins = str.split(':')
		res = arange(float(_bins[0]), float(_bins[1]), float(_bins[2]))
	else:
		_bins = str.split(':')
		a = arange(float(_bins[0]), float(_bins[1]), float(_bins[2]))
		res = [2**i for i in a]
	return res

def BinarySearch(a, val, l, h):
	"""Recursive function to find value """
	# print >>sys.stderr, "Value to find: " + str(val) + "L, H: "+ str(l) + ", "+ str(h)
	if (h == l):
		# print >>sys.stderr, "Trovato nel limite, ritornato: " + str(l)
		# print >>sys.stderr, "Bins: " + str(a[l]) + ", " + str(a[l+1]) 
		return int(l)
	mid = ( l + h ) / 2
	if( val >= a[mid] and val < a[mid+1] ):
		# bin found
		# print >>sys.stderr, "Trovato!! ritornato: " + str(mid)
		return int(mid)
	elif ( val < a[mid] ):
		return BinarySearch(a, val, l, mid)
	else:
		return BinarySearch(a, val, mid+1, h)
			 
def histogram3(a, bins):
	"""
	This is an extended implementation of stats.histogram. It differs from the original one because
	the first argument can be a 2D array where the first column is the values of the sample and second column
	is the number of occurencies of that sample.
	TODO: describe the algorithm.
	"""
	_b_size = len(bins)
	_c = 0.0
	_res = [0]*len(bins)
	
	if ( _b_size == 0):
		print >>sys.stderr, "Bins array wrong!!!!"
		sys.exit(-2)
	# Iterate over the array
	for i in a:
		# get the right position
		if type(i) == types.ListType or type(i) == types.TupleType:
			_t = True # Is a tuple or a list
			_pos = BinarySearch(bins, i[0], 0, len(bins)-1)
		else:
			_t = False
			_pos = BinarySearch(bins, i, 0, len(bins)-1)
		_res[_pos] += _t and i[1] or 1 	# _t ? i[1] : 1
		_c += _t and i[1] or 1			# if it is not a tuple it counts 1
	return _res, _c

def readStream(stream, col):
	tmp_vec = []
	max_val = 0
	_index = None
	_w_in = None

	if (col != None):
		if( col.find(':') > 0):
			_cols = col.split(':')
			_index = int(_cols[0])
			_w_in = int(_cols[1])
		else:
			_index = int(col)
			_w_in = None

	for i in stream:
		if i[0] == '#':
			#print "analizing column: " + i.split()[col - 1]
			continue
		fields = i.split()
		if _index == None:
			if len(fields) > 1:
				print "Input contains multiple column, please specify one"
				sys.exit(-2)
			else:
				_index = 0
		if(_w_in != None):
			_weight = int(fields[_w_in - 1])	
		else:
			_weight = 1
		if len(fields) < _index:
			print >> sys.stderr, "[histo.py] Warning: wrong number of fields"
			sys.exit(-1)
		try:
			tmp_vec.append([float(fields[_index - 1]), _weight]) 
		except Exception, e:
			print >> sys.stderr, "Caught an exception: " + str(e)
			print >> sys.stderr, "Line: %s" % i
			print >> sys.stderr, "i[0]: %s" % i[0]
	return tmp_vec

def make_histo(tmp_vec, bins, outStr, limits, width, log):
	global percentils
		#now create a scipy array and build histograms
	#a = array(tmp_vec)
	
	#_bins = bins.split(':')
	#bins = arange(float(_bins[0]), float(_bins[1]), float(_bins[2]))
	bins = makeBins(bins, log)
	#histo, bmin, minw, pout = stats.histogram(a, numBins, limits)
	histo, _comp = histogram3(tmp_vec, bins)
	#print histo
	#bins = arange(bmin, minw * (numBins + 1), minw)
	#cdf, lowlim, binsize, pout = stats.cumfreq(histo)
	c = Cumulator()
	cdf = [c.sum(i) for i in histo]
	#print cdf
	#cdf = stats.cumsum(a)
	maxCum = max(cdf)
	assert (maxCum == _comp)
	#print maxCum
	pdf = [float(i) / maxCum for i in histo]
	cdf = [float(i) / maxCum for i in cdf]
	ccdf = [1 - i for i in cdf]
	if outStr != None:
		outStr.write("# Bins Histo CDF CCDF PDF\n")
		#print "lunghezze: " + str(len(bins)) + ", " + str(len(histo))
		for i in range(len(histo)):
			outStr.write("%.10f %.10f %.10f %.10f %.10f\n" % (bins[i], pdf[i], cdf[i], ccdf[i], float(histo[i])/maxCum))

	#print >> sys.stderr, cdf
	perc_res = {}
	for i in percentils:
		perc_res[i] = 0.0

	c = 0
	for i in range(len(cdf)):
		while c < len(percentils) and cdf[i] > percentils[c]:
			perc_res[percentils[c]] = bins[i]
			c += 1
		if c == len(percentils):
			break
	#print >> sys.stderr, perc_res

	assert (len(perc_res) == len(percentils)), "[make_histo] Size of returned dictionary doesn't correspond to size of percentils list"
	return (pdf, cdf, perc_res)

def main(argv=None):
	if argv is None:
		argv = sys.argv
	filename = output = None
	col = None
	Bins = None
	limits = None
	width = None
	log = False
	try:
		try:
			opts, args = getopt.getopt(argv[1:], "ho:vf:c:b:l:w:g", 
			["help", "output=", "file=", "col=", "bins=", "limits=", "width=", "log"])
		except getopt.error, msg:
			raise Usage(msg)
	
		# option processing
		for option, value in opts:
			if option == "-v":
				verbose = True
			if option in ("-h", "--help"):
				raise Usage(help_message)
			if option in ("-o", "--output"):
				output = value
			if option in ("-f", "--file"):
				filename = value
			if option in ("-c", "--column"):
				col = value
			if option in ("-b", "--bins"):
				Bins = value
			if option in ("-l", "--limits"):
				limits = value.split(',')
				limits = [int(i) for i in limits]
			if option in ("-w", "--width"):
				width = float(value)
			if option in ("-g", "--log"):
				log = True

	except Usage, err:
		print >> sys.stderr, sys.argv[0].split("/")[-1] + ": " + str(err.msg)
		print >> sys.stderr, "\t for help use --help"
		return 2

	#Check arguments
	if width == None:
		width = 1
	if output != None:
		#Open the output file
		try:
			outStr = open(output, 'w')
		except Exception, e:
			print "Errore in apertura output file" + str(e)
			sys.exit(-1)
	else:
		outStr = sys.stdout
				
	if Bins == None:
		print "Please specify bins#"
		sys.exit(-1)

	if filename == None:
		in_s = sys.stdin
	else:
		try:
			in_s = open(filename, 'r')
		except Exception, e:
			print "Errore in apertura file: " + str(e)	
			sys.exit(-1)

	

	#We have an input stream
	
	vec = readStream(in_s, col)
	make_histo(vec, Bins, outStr, limits, width, log)

if __name__ == "__main__":
	sys.exit(main())

