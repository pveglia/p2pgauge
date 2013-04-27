"""
utility methods
"""
import sys

def printDebug(opts, str):
	if opts.debug:
		print >> sys.stdout, str
