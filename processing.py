#!/usr/bin/env python

import math
import sys
import time
import os
import re
from optparse import OptionParser
import operator
import packet
import string
from PyQt4 import QtCore, QtGui
from numpy import median
from subprocess import *
from scipy.stats.stats import pearsonr
from geolocalization import Geolocalization
from distribution import Distribution
from helper_threads import *
import printer
import histo
from mathhelper import *

#geolicalization global object
geo = Geolocalization()
			
def make_socket(addr, port):
	return "%s %s" % (addr, port)

def matchSocket(socketa, socketb):
	# Function to match socket given that is possible to have the * on port
	ipa, porta = socketa.split()
	ipb, portb = socketb.split()
	if ipa == ipb and (porta == portb or porta == '*' or portb == '*'):
		return True
	else:
		return False
		
class Port:
	"collects information for calculating the PDF and the CDF of external ports"

	def update(self, line, current_socket):
		"increments the number of times that a port is used by a peer"		
		
		socket1 = line[3]+' '+line[4]
		socket2 = line[5]+' '+line[6]

		if current_socket != socket1 and current_socket != socket2:
			return

		if current_socket == socket1:
			port = int(line[6])
		else:
			port = int(line[4])

		value = self.PORTS.get(port)
		self.PORTS[port] = value + 1

	def write_distribution(self):
		"writes the values of PDF and CDF"
		distr = Distribution()
		pdf = distr.PDF(self.PORTS)
		f_port = open("demo.out/20_extport/pdf_port.DATA","w")
		for i in pdf:
			if i[1] > 0:
				f_port.write(str(i[0]) + ' ' + str(i[1]) + '\n')

		f_port.close()

		
	def __init__(self):
		self.PORTS = dict({})
		i = 0
		while i <= 65535:
			dict_elem = dict({i:0})
			self.PORTS.update(dict_elem)
			i = i +1
		return


class PeerCounters:
	def __init__(self, peer="", id=0):
		self.socket = peer
		self.id = id
		self.pkts_rec = 0
		self.bytes_rec = 0 
		self.pkts_sent = 0
		self.bytes_sent = 0 
		self.cc, self.continent_id = None, None
		self.ASN = "nt"
		self.sAS = None
		self.sCC = None
		self.NET = None
		self.RTT = None
		self.CAP = None
		self.HOP = None
		self.CapProbeOn = False
		self.CapPstaus = -1
	
	def update(self, new):
		self.pkts_rec    +=  new.pkts_rec   
		self.bytes_rec   +=  new.bytes_rec  
		self.pkts_sent   +=  new.pkts_sent  
		self.bytes_sent  +=  new.bytes_sent 

	def to_string(self):
		return "%d %d %d %d %d\n" % (self.id, self.pkts_rec, self.pkts_sent, self.bytes_rec, self.bytes_sent)

class Peer():
	"performs statistics about peers, same peers, new peers and port fairness"
	
	def __init__(self, opts):
		self.opts = opts
		self.threadPool = QtCore.QThreadPool.globalInstance()
		self.PORTS = dict()
		self.PEERS = dict()
		self.CURRENT_PEERS = dict()
		self.PREVIOUS_PEERS = dict()
		self.SAME_PEERS = {}
		self.n_current_peers = 0
		self.average_peers = 0
		self.max_peers = 0
		#write("demo.out/40_Kiviat/max_peers.DATA",self.max_peers)
		self.n_new_peers = 0
		self.average_new_peers = 0
		self.max_new_peers = 0
		self.max_same_peers = 0
		#write("demo.out/40_Kiviat/max_same_peers.DATA",self.max_same_peers)
		self.n_same_peers = 0
		self.avg_same_peers = 0
		self.total_peers = 0
		self.max_fairness = 0
		self.avg_fairness = 0
		self.peers_id = 0
		self.peers_info = None
		self.capture = opts.capture
		self.use_capprobe = not opts.no_capprobe
		printer.printDebug(self.opts, "%sUsing caprobe" % ( (self.use_capprobe and "!" or "NOT " ) ) )
		self.opts.very_total_bytes = 0

		f_current_peers = open("demo.out/01_pattern/peers.DATA","w")
		f_current_peers.close()
		f_same_peers = open("demo.out/01_pattern/same_peers.DATA","w")
		f_same_peers.close()
		f_new_peers = open("demo.out/01_pattern/new_peers.DATA","w")
		f_new_peers.close()
		f_total_new_peers = open("demo.out/01_pattern/total_new_peers.DATA","w")
		f_total_new_peers.close()

	def writeInstantValues(self):
		f = open("demo.out/01_pattern/symmetry.DATA", 'w')
		a = self.PEERS.values()
		a.sort(lambda x, y: cmp(x.id, y.id) ) # sorts the peers 
		for i in a:
			f.write(i.to_string())
		f.close()

	def get_lpm(self, peer):
		my_ip = [int(i) for i in self.opts.addr.split('.')]
		my_ip_32 = reduce(lambda x, y: (x << 8) + y, my_ip)
		other_ip = [int(i) for i in peer.split()[0].split('.')]
		other_32 = reduce(lambda x, y: (x << 8) + y, other_ip)

		found = False
		cursor = 32
		while(not found and cursor > 0):
			if ( (my_ip_32 & 1 << cursor) != (other_32 & 1 << cursor) ):
				found = True
			cursor -= 1
#		print "Host: %s, lpm= %d" % (".".join(str(i) for i in other_ip), 32 - cursor)
		return 32 - cursor

	def count_peers(self, current_socket, pkt):
		"counts the number of peers in delta T"
	
		socket1 = pkt.ips + ' ' + pkt.ps
		socket2 = pkt.ipd + ' ' + pkt.pd

		if not matchSocket(current_socket, socket1) and \
			not matchSocket(current_socket, socket2):
			return

		if matchSocket(current_socket, socket1):
			peer = socket2
			dir = '+'
		else:
			peer = socket1
			dir = '-'

		if peer not in self.CURRENT_PEERS:
			self.CURRENT_PEERS[peer] = PeerCounters(peer)

		p = self.CURRENT_PEERS[peer]

		self.opts.very_total_bytes += int(pkt.size)
		if dir == '-':
			p.pkts_rec += 1
			p.bytes_rec += int( pkt.size )
		else:
			p.pkts_sent += 1
			p.bytes_sent += int( pkt.size )

		# as soon I discover that a peer is not probe I start a thread to make capprobe
		if peer not in self.PEERS \
		   and p.CapProbeOn == False \
		   and ( p.pkts_rec > 1 \
		         or p.pkts_sent > 1): 
				 # i.e. this peer is not probe

			p.CapProbeOn = True
			if not self.use_capprobe and peer in self.peers_info:
				p.CAP, p.HOP, p.RTT = self.peers_info[peer]
				printer.printDebug(self.opts, "Peer %s, %s %s %s" % (peer, 
					str(self.peers_info[peer][0]), 
					str(self.peers_info[peer][1]), 
					str(self.peers_info[peer][2])))
				p.CapPstaus = 0
			elif self.use_capprobe:
				capthread = CapProbeThread(p, self.opts)
				self.threadPool.start(capthread)


		self.n_current_peers = len(self.CURRENT_PEERS)
		
		return

	def filter_peers_and_count(self, T):
		# I delete from the dictionary of peers the probe peers
		wrong_peers = [socket for socket, counters in self.CURRENT_PEERS.iteritems() \
							  if counters.pkts_rec < self.opts.contr_thresh or \
							  counters.pkts_sent < self.opts.contr_thresh]
		for socket in wrong_peers:
			del self.CURRENT_PEERS[socket]
		
		self.n_new_peers += 0
		self.n_same_peers += 0

		for p, counters in self.CURRENT_PEERS.iteritems():
			if p not in self.PREVIOUS_PEERS:
				if p not in self.PEERS:
					#a new peer is found!!!!
					self.PEERS[p] = counters
					self.PEERS[p].id = self.peers_id
					self.peers_id += 1
					self.n_new_peers += 1 
					self.PEERS[p].cc, self.PEERS[p].continent_id = geo.geolocalize(p.split()[0])
					self.PEERS[p].sCC = (self.PEERS[p].cc == self.opts.cc and 1 or 0)
					self.PEERS[p].NET = self.get_lpm(p) # get longest prefix match
#					print "Peer %s, CC: %s, same CC: %s, Net: %s" % (p.split()[0],
#																	self.PEERS[p].cc,
#																	self.PEERS[p].sCC,
#																	self.PEERS[p].NET)
			else:
				#update old peer in db
				#copy old values in this peers
				self.PEERS[p].update(counters)
				old = self.PEERS[p]
				counters.RTT = old.RTT
				counters.ASN = old.ASN
				counters.CAP = old.CAP
				counters.HOP = old.HOP

			if p in self.PREVIOUS_PEERS:
				self.n_same_peers += 1
		
		return

	def print_geolocalization(self, T):
		"This function prints the geolocalization"
		
		res = {}

		#we sum all information from peers belonging to the same cc
		for peer in self.PEERS.values():
			if peer.cc in res:
				r = res[peer.cc]
				r['byte_in']  += peer.bytes_rec
				r['byte_out'] += peer.bytes_sent
				r['byte_tot'] += peer.bytes_sent + peer.bytes_rec
				if peer.bytes_rec > 0 :
					r['peer_in']  += 1
				if peer.bytes_sent > 0 :
					r['peer_out'] += 1
				r['peer_tot'] += 1
			else:
				r = {}
				r['byte_in']  = peer.bytes_rec
				r['byte_out'] = peer.bytes_sent
				r['byte_tot'] = peer.bytes_sent + peer.bytes_rec
				r['peer_in']  = (peer.bytes_rec  > 0 and 1 or 0)
				r['peer_out'] = (peer.bytes_sent > 0 and 1 or 0)
				r['peer_tot'] = 1
				r['continent_id'] = peer.continent_id
				res[peer.cc] = r
		
				
		#write the unknown peers in their own file
		if 'unk' in res:
			f = open('demo.out/31_geoip/geoip.UNK.DATA', 'w')
			r = res['unk']
			print >>f, "peer TOT %d" % r['peer_tot']
			print >>f, "peer IN %d"  % r['peer_in']
			print >>f, "peer OUT %d" % r['peer_out']
			print >>f, "byte TOT %d" % r['byte_tot']
			print >>f, "byte IN %d"  % r['byte_in']
			print >>f, "byte OUT %d" % r['byte_out']
			f.close()
			f = open('demo.out/31_geoip/unk.peers.DATA', 'w')
			print >>f, r['peer_tot']
			f.close()
			f = open('demo.out/31_geoip/unk.bytes.DATA', 'w')
			print >>f, r['byte_tot']
			f.close()
			del res['unk']

		tot_bytes = sum( [ x['byte_tot'] for x in res.values() ] )
		tot_peers = sum( [ x['peer_tot'] for x in res.values() ] )
		f = open('demo.out/31_geoip/tot_peers.DATA', 'w')
		print >>f, tot_peers
		f.close()
		f = open('demo.out/31_geoip/tot_bytes.DATA', 'w')
		print >>f, tot_bytes
		f.close()

		#lista di countrycode
		sorted_peers = res.keys()
		sorted_peers.sort( key = lambda x: res[x]['peer_tot'], reverse=True  )
		sorted_bytes = res.keys()
		sorted_bytes.sort( key = lambda x: res[x]['byte_tot'], reverse=True )

		#now I print all
		f_bytes = open('demo.out/31_geoip/geobytes.DATA', 'w')
		f_peers = open('demo.out/31_geoip/geopeers.DATA', 'w')

		for cc in sorted_peers:
			r = res[cc]
			vals = ['0'] * 14
			vals[ r['continent_id']     ] = str(r['peer_in'])
			vals[ r['continent_id'] + 7 ] = str(r['peer_out'])
			print >>f_peers, cc, " ".join(vals)

		for cc in sorted_bytes:
			r = res[cc]
			vals = ['0'] * 14
			vals[ r['continent_id']     ] = str(r['byte_in'])
			vals[ r['continent_id'] + 7 ] = str(r['byte_out'])
			print >>f_bytes, cc, " ".join(vals)

		f_bytes.close()
		f_peers.close()

		
		f_bytes = open('demo.out/31_geoip/geoip.byte.TOT.DATA', 'w')
		f_peers = open('demo.out/31_geoip/geoip.peer.TOT.DATA', 'w')

		for cc, r in res.iteritems():
			vals = ['0'] * 7
			vals[ r['continent_id']     ] = str(r['byte_tot'])
			print >>f_bytes, cc, " ".join(vals)

			vals = ['0'] * 7
			vals[ r['continent_id']     ] = str(r['peer_tot'])
			print >>f_peers, cc, " ".join(vals)
		
		f_bytes.close()
		f_peers.close()

		return

	def print_topTenAs(self, T):
		"This function prints the geolocalization"
		
		res = {}
		as_dir = "demo.out/33_AsTopTen" 

		#we sum all information from peers belonging to the same cc
		for peer in self.PEERS.values():
			if peer.ASN == "nt":
				continue
			if peer.ASN in res:
				r = res[peer.ASN]
				r['byte_in']  += peer.bytes_rec
				r['byte_out'] += peer.bytes_sent
				r['byte_tot'] += peer.bytes_sent + peer.bytes_rec
				if peer.bytes_rec > 0 :
					r['peer_in']  += 1
				if peer.bytes_sent > 0 :
					r['peer_out'] += 1
				r['peer_tot'] = r['peer_in'] + r['peer_out']
			else:
				r = {}
				r['byte_in']  = peer.bytes_rec
				r['byte_out'] = peer.bytes_sent
				r['byte_tot'] = peer.bytes_sent + peer.bytes_rec
				r['peer_in']  = (peer.bytes_rec  > 0 and 1 or 0)
				r['peer_out'] = (peer.bytes_sent > 0 and 1 or 0)
				r['peer_tot'] = r['peer_in'] + r['peer_out'] 
				r['continent_id'] = peer.continent_id
				res[peer.ASN] = r
		
				
		#write the unknown peers in a separate file
		if 'unk' in res:
			f = open("%s/geoip.UNK" % as_dir, 'w')
			r = res['unk']
			print >>f, "peer TOT %d" % r['peer_tot']
			print >>f, "peer IN %d"  % r['peer_in']
			print >>f, "peer OUT %d" % r['peer_out']
			print >>f, "byte TOT %d" % r['byte_tot']
			print >>f, "byte IN %d"  % r['byte_in']
			print >>f, "byte OUT %d" % r['byte_out']
			f.close()
			f = open("%s/unk.peers.DATA" % as_dir, 'w')
			print >>f, r['peer_tot']
			f.close()
			f = open("%s/unk.bytes.DATA" % as_dir, 'w')
			print >>f, r['byte_tot']
			f.close()
			del res['unk']

		tot_bytes = sum( [ x['byte_tot'] for x in res.values() ] )
		tot_peers = sum( [ x['peer_tot'] for x in res.values() ] )
		f = open("%s/tot_peers.DATA" % as_dir, 'w')
		print >>f, tot_peers
		f.close()
		f = open("%s/tot_bytes.DATA" % as_dir, 'w')
		print >>f, tot_bytes
		f.close()

		#lista di countrycode
		sorted_peers = res.keys()
		sorted_peers.sort( key = lambda x: res[x]['peer_tot'], reverse=True  )
		sorted_bytes = res.keys()
		sorted_bytes.sort( key = lambda x: res[x]['byte_tot'], reverse=True )

		#now I print all
		f_bytes = open("%s/geobytes.DATA" % as_dir, 'w')
		f_peers = open("%s/geopeers.DATA" % as_dir, 'w')

		for asn in sorted_peers:
			r = res[asn]
			asn_mod = re.sub("AS", "", asn)
			vals = ['0'] * 14
			try:
				vals[ r['continent_id']     ] = str(r['peer_in'])
				vals[ r['continent_id'] + 7 ] = str(r['peer_out'])
				print >>f_peers, asn_mod, " ".join(vals)
			except TypeError, e:
				print "exception"
				print asn
				print r['continent_id']

		for asn in sorted_bytes:
			r = res[asn]
			vals = ['0'] * 14
			asn_mod = re.sub("AS", "", asn)
			vals[ r['continent_id']     ] = str(r['byte_in'])
			vals[ r['continent_id'] + 7 ] = str(r['byte_out'])
			print >>f_bytes, asn_mod, " ".join(vals)

		f_bytes.close()
		f_peers.close()

		
		f_bytes = open("%s/geoip.byte.TOT.DATA" % as_dir, 'w')
		f_peers = open("%s/geoip.peer.TOT.DATA" % as_dir, 'w')

		for asn, r in res.iteritems():
			vals = ['0'] * 7
			vals[ r['continent_id']     ] = str(r['byte_tot'])
			print >>f_bytes, asn, " ".join(vals)

			vals = ['0'] * 7
			vals[ r['continent_id']     ] = str(r['peer_tot'])
			print >>f_peers, asn, " ".join(vals)
		
		f_bytes.close()
		f_peers.close()

		return

	def As(self,my_address,T):
		# my_as = geo.as_by_addr(my_address)
		for peer in self.CURRENT_PEERS:
			addr_peer = peer.split(' ')[0] # because peer contains also the port
			if self.CURRENT_PEERS[peer].ASN == "nt":
				asn = geo.as_by_addr(addr_peer)
				if asn != None:
					asn = asn.split(' ')[0]
				else:
					asn = "unk"
				self.CURRENT_PEERS[peer].ASN = asn
				sAS = (asn == self.opts.myAS and 1 or 0)
				self.CURRENT_PEERS[peer].sAS = sAS
#				print "Peer: %s, asn: %s. Same AS? [%s]" % (addr_peer, asn, sAS)

	def calc_pot(self, comp, values, increments=None, threshold = None):
		if not values:
			return 0, 0
		if not threshold:
			threshold_ = median(values)
		else:
			threshold_ = threshold

		if increments == None:
			increments = [1] * len(values)

		num_v = den_v = 0
		num_i = den_i = 0

		for v, i in zip(values, increments):
			if comp(v, threshold_):
				num_i += i
				num_v += 1
			den_i += i
			den_v += 1
			
		# shall we put res_v = 0 if den == 0???
		if den_v == 0:
			res_v = 0
		else:
			res_v = float(num_v) / float(den_v)

		if den_i == 0:
			res_i = 0
		else:
			res_i = float(num_i) / float(den_i)

		return res_v, res_i

	def print_cap_probe_for_kiviat(self, peers, label):
		def print_single_metric(name, extractor, comp, threshold):
				val = [ float(extractor(p)) \
								for p in peers.itervalues() \
								if extractor(p)!= None ]
				# print name
				# print val

				sent_bytes = [ float(p.bytes_sent) \
								for p in peers.itervalues() \
								if extractor(p)!= None ]

				rec_bytes = [ float(p.bytes_rec) \
								for p in peers.itervalues() \
								if extractor(p)!= None ]

				tot_bytes = [ x + y for x,y in zip(sent_bytes, rec_bytes)]

				peer_pot, byte_pot = self.calc_pot(comp, val, tot_bytes, threshold = threshold)
				#strout = "%s_POT_TOT_PEER_%s %f\n" % (name, label, peer_pot)
				strout = "%s_POT_bytes_tot_%s %f\n" % (name, label, byte_pot)

				peer_pot, byte_pot = self.calc_pot(comp, val, rec_bytes, threshold = threshold)
				#strout += "%s_POT_RX_PEER_%s %f\n" % (name, label, peer_pot)
				strout += "%s_POT_bytes_rec_%s %f\n" % (name, label, byte_pot)

				peer_pot, byte_pot = self.calc_pot(comp, val, sent_bytes, threshold = threshold)
				#strout += "%s_POT_TX_PEER_%s %f\n" % (name, label, peer_pot)
				strout += "%s_POT_bytes_sent_%s %f\n" % (name, label, byte_pot)
				return strout

		strres = print_single_metric("RTT", lambda x: x.RTT, operator.lt, None)
		strres += print_single_metric("CAP", lambda x: x.CAP, operator.gt, None)
		strres += print_single_metric("HOP", lambda x: x.HOP, operator.lt, None)

		strres += print_single_metric("sCC", lambda x: x.sCC, operator.eq, 1)
		strres += print_single_metric("sAS", lambda x: x.sAS, operator.eq, 1)
		strres += print_single_metric("NET", lambda x: x.NET, operator.gt, 16)
		return strres

	def getOtherIndexes(self, peers, direction, feature):
		feat_map = {"sAS": "ASN", "sCC": "cc"}
		peers_dict = {}
		bytes_dict = {}
		tot_peers = tot_bytes = 0
		for p in peers:
			feat = eval("peers[p].%s" % feat_map[feature])
			if (feat != None):
				peers_dict[feat] = peers_dict.setdefault(feat, 0) + 1
				tot_peers += 1
				bytes_exch = eval("int(peers[p].%s)" % direction)
				bytes_dict[feat] = bytes_dict.setdefault(feat, 0) + bytes_exch
				tot_bytes += bytes_exch
		peers_norm = [float(i) / tot_peers for i in peers_dict.values()]
		bytes_norm = [float(i) / tot_bytes for i in bytes_dict.values()]

		# return bhatta, kullb	
		bc = bhatta(peers_norm, bytes_norm)
		kl = kulb(peers_norm, bytes_norm)
		return bc, kl
				

	def print_kiviats(self, peers, label):
		""" 
		Prints kiviat.DATA file with correlation between
		{RTT, HOP, CAP, sAS, sCC, NET} and {RX, TX, TOT} bytes
		"""

		# metrics = ["RTT", "HOP", "CAP", "sAS", "sCC", "NET"]
		metrics = ["CAP", "sCC", "RTT", "HOP", "sAS", "NET"]
		dir = ["bytes_rec", "bytes_sent", "bytes_tot"]

		metrics2 = {"CAP": ("0:100:0.05", False), "RTT": ("0:1000:10", False), \
				"HOP": ("1:50:1", False), "NET": ("1:32:1", False) }
		
		# calculate tot_bytes
		for i in peers:
			peers[i].bytes_tot = peers[i].bytes_rec + peers[i].bytes_sent

		strres = ""
		for i in dir:
			for j in metrics:
				# build a list of tuple [feat, dir],
				# the use of eval allow to cycle over list of features and directions
				values = [eval("[float(peers[k].%s), int(peers[k].%s)]" % (j,i)) for k in peers  \
							if eval("peers[k].%s" % (j,)) != None]
				if len(values) > 0:
					# Permutation of list of list, from n rows, 2 columns to 2xn
					feat, bytes_dir = zip(*values)

					# Correlation is computed for every metric
					corr = pearsonr(bytes_dir, feat)[0]
					if str(corr) == 'nan':
						corr = 0.0

					# Bhattacharyya and KL are computed only for metrics in metrics2 dictionary
					if j in metrics2:
						peer_pdf = histo.make_histo(feat, metrics2[j][0], None, None, None, metrics2[j][1])[0]
						bytes_pdf = histo.make_histo(values, metrics2[j][0], None, None, None, metrics2[j][1])[0]
						# Bhattacharyya
						try: 
							_bhatta = bhatta(peer_pdf,bytes_pdf)
						except Exception, e:
							print "Bhattacharyya failed", e
							_bhatta = 0.0
						# Kullback-leiber
						try:
							_kulb = kulb(peer_pdf,bytes_pdf)
						except Exception, e:
							print "Kullback-Leibler failed", e
							_kulb = 0.0
					else: # sAS and sCC need to be handled in another way
						_bhatta, _kulb = self.getOtherIndexes(peers, i, j)
				else: # there are no peers with this feature (e.g ping didn't replyed)
					corr = _bhatta = _kulb = 0.0

				# FInally print out results
				strres += "%s_CORR_%s_%s %f\n" % (j, i, label, corr + 1)
				strres += "%s_BHATTA_%s_%s %f\n" % (j, i, label, abs(_bhatta))
				strres += "%s_KULB_%s_%s %f\n" % (j, i, label, abs(_kulb))
		return strres



	def printConf(self, dir, descr):
		interval = ["t0", "lastdt"]
		direction = ["tot", "sent", "rec"]
		f = open("%s/%s.conf" % (dir,descr), "w")
		ui = self.opts.tabs[self.opts.kiviat_index[0]].ui
		for i in interval:
			for j in direction:
				if eval("ui.%s.isChecked() and ui.%s.isChecked()" % (i,j)):
					print >> f, "%s_bytes_%s_%s" % (descr, j, i)
		f.close()

	def printPDF(self):
		metrics = {"CAP": ("0:100:0.01", False), "RTT": ("0:1000:1", False), \
				"HOP": ("1:40:0.1", False), "NET": ("1:32:1", False)}
		peers = self.PEERS

		for i in peers:
			peers[i].bytes_tot = peers[i].bytes_rec + peers[i].bytes_sent
		
		for i in metrics:
			peer_matrix = [eval("float(peers[k].%s)" % i) for k in peers \
								if eval("peers[k].%s" % i) != None]
			bytes_matrix = [eval("[float(peers[k].%s), peers[k].bytes_tot]" % i) for k in peers \
								if eval("peers[k].%s" % i) != None]
			if len(peer_matrix) != 0:
				f = open("demo.out/40_cdf/peer.%s.DATA" % i, "w")
				f2 = open("demo.out/40_cdf/peer.%s.DATA.RAW" % i, "w")
				print >> f2, bytes_matrix
				histo.make_histo(peer_matrix, metrics[i][0], f, None, None, metrics[i][1])	
				f2.close()
				f.close
			if len(bytes_matrix) != 0:
				f = open("demo.out/40_cdf/bytes.%s.DATA" % i, "w")
				histo.make_histo(bytes_matrix, metrics[i][0], f, None, None, metrics[i][1])	
				f.close


	def print_kiviat_info(self,T):
		"Calculates the percentage over threshold of the parameters"

		# Print Kiviat configuration 
		self.printConf("demo.out/41_kiviat", "POT")
		self.printConf("demo.out/41_kiviat", "CORR")
		self.printConf("demo.out/41_kiviat", "BHATTA")
		self.printConf("demo.out/41_kiviat", "KULB")

		self.dumpPeersInfo("demo.out/41_kiviat")

		# kiviat data for tab 41
		outstr = self.print_cap_probe_for_kiviat(self.CURRENT_PEERS, "lastdt")
		outstr += self.print_cap_probe_for_kiviat(self.PEERS, "t0")

		# kiviat data for tab 42 (correlation)
		outstr += self.print_kiviats(self.CURRENT_PEERS, "lastdt")
		outstr += self.print_kiviats(self.PEERS, "t0")

		# Since the function is not too quick, I avoid to keep the file open
		fout = open("demo.out/41_kiviat/kiviat.DATA", "w")
		print >> fout, "%s" % outstr
		fout.close()

		# print [self.CURRENT_PEERS[i].RTT for i in self.CURRENT_PEERS if self.CURRENT_PEERS[i].RTT != None]

	def dumpPeersInfo(self,dir):
		info = self.getGlobalInfo("dumppeersinfo")
		for i in info:
			fout = open("%s/%s.dat" % (dir,i), "w")
			print >> fout, info[i]
			fout.close()

	def print_scatterplots(self):
		# hash used for the iteration. Each item is an array of [comparator, threshold]
		# If None is used as threshold value, then the median is used
		feat = {"CAP": [operator.ge, None], "NET": [operator.ge, 16], 
				"HOP" : [operator.le, None], "RTT": [operator.le, None]}
		for f in feat:
			data = []
			prs = self.PEERS
			for p in prs:
				res = eval("prs[p].%s" % f)
				if res != None:
					# fill data array (val, TX, RX)
					data.append([float(res), prs[p].bytes_sent, prs[p].bytes_rec])
			if len(data) > 0: # if not empty...
				# open output files and put handles in the vector
				out_files = [open("demo.out/36_scatter/scatter_%s.DATA" % f, 'w'),
							 open("demo.out/36_scatter/scatter_%s.MEDIAN" % f, 'w'),	
							 open("demo.out/36_scatter/scatter_%s.PEER_POT" % f, 'w'),
							 open("demo.out/36_scatter/scatter_%s.BYTE_POT" % f, 'w')]
				for i in data:
					# print data for gnuplot
					# val bytes_sent
					# val -bytes_rec
					print >> out_files[0], "%f %d\n%f -%d" % (i[0], i[1], i[0], i[2])
				# print threshold for gnuplot
				print >> out_files[1], str(median([i[0] for i in data]))
				# compute POT values and print them
				peer_pot, byte_pot = self.calc_pot(feat[f][0],  # comparator, first position in the array of features
											[i[0] for i in data], # values
											[i[2] + i[1] for i in data], # tot_bytes
											feat[f][1]) # threshold, second position in features array
				print >> out_files[2], "%.2f" % (peer_pot * 100,)
				print >> out_files[3], "%.2f" % (byte_pot * 100,)
				for i in out_files:
					i.close()
			

	def newT(self):
		self.PREVIOUS_PEERS = self.CURRENT_PEERS
		self.CURRENT_PEERS = {} 
		self.SAME_PEERS = {}
		self.PORTS = {}
		self.n_new_peers = 0
		self.n_current_peers = 0
		self.n_same_peers = 0

	def initialize_dict(self,dictionary):
		for i in dictionary.keys():
			del dictionary[i]
		
	def pattern(self,T): 
		"it makes the the graph of peers.gp"
		f_current_peers = open("demo.out/01_pattern/peers.DATA","a")
		f_current_peers.write(str(T) + ' ' + str(self.n_current_peers) + '\n')
		f_current_peers.close()

		f_same_peers = open("demo.out/01_pattern/same_peers.DATA","a")
		f_same_peers.write(str(T) + ' ' + str(self.n_same_peers) + '\n')
		f_same_peers.close()

		self.total_peers = len(self.PEERS.items())
		f_total_new_peers = open("demo.out/01_pattern/total_new_peers.DATA","a")
		f_total_new_peers.write(str(T) + ' ' + str(self.total_peers) + '\n')
		f_total_new_peers.close()

		f_new_peers = open("demo.out/01_pattern/new_peers.DATA","a")
		f_new_peers.write(str(T) + ' ' + str(self.n_new_peers) + '\n')
		f_new_peers.close()

	def getGlobalInfo(self, caller):
		t_prs = self.PEERS
		p_prs = self.PREVIOUS_PEERS
		c_prs = self.CURRENT_PEERS
		res = {}
		# Total peers
		res["t_peers"] = len(t_prs)
		res["t_p_peers"] = len([i for i in t_prs if t_prs[i].CapPstaus == 0])
		res["t_bytes"] = sum([t_prs[i].bytes_rec + t_prs[i].bytes_sent for i in t_prs])
		# Current
		res["c_peers"] = len(c_prs)
		res["c_p_peers"] = len([i for i in c_prs if c_prs[i].CapPstaus == 0])
		res["c_bytes"] = sum([c_prs[i].bytes_rec + c_prs[i].bytes_sent for i in c_prs])
		# Previous
		res["p_peers"] = len(p_prs)
		res["p_p_peers"] = len([i for i in p_prs if p_prs[i].CapPstaus == 0])
		res["p_bytes"] = sum([p_prs[i].bytes_rec + p_prs[i].bytes_sent for i in p_prs])
		res["very_total_bytes"] = self.opts.very_total_bytes

		return res
		
def main():
	parser = OptionParser()
	parser.add_option('-a', '--address', type='string', dest='addr', default='192.168.1.2')
	parser.add_option('-p', '--port', type='string', dest='port', default='7773')
	parser.add_option('-c', '--cc', type='string', dest='cc', default='us')
	parser.add_option('-r', '--capture', type='string', dest='capture', default=None)
	parser.add_option('-i', '--interface', type='string', dest='interface', default=None)
	parser.add_option('-f', '--filter', type='string', dest='filter', default='udp')
	parser.add_option('-I', '--interval', type='int', dest='interval', default=1)
	parser.add_option('-d', '--debug', action='store_true', dest='debug', default=False)
	parser.add_option('-C', '--no-capprobe', action='store_true', dest='no_capprobe', default=False)


	app = QtCore.QCoreApplication(sys.argv)
	opts, args = parser.parse_args()

	pubipT = PubIPThread(opts)
	pubipT.run()
	pubipT.wait()
	thread = ProcessingThread(opts)
	thread.run()
	sys.exit(app.exec_())

class ActivePorts:
	def __init__(self, addr, interval):
		self.addr = addr
		self.interval = interval
		self.ports = {} 

	def get_ports(self):
		res = []

		for port, values in self.ports.iteritems():
			bytes, packets = values
			rate = float(bytes)*8/ float(self.interval) / 1000
			res.append( (port, str(packets), str(bytes),  str(rate)) )
			res.sort(key = lambda x: int(x[2]), reverse = True )

		return res

	def reset(self):
		self.ports = {}

	def add_packet(self, pkt):
		
		if pkt.ips == self.addr:
			port = pkt.ps
			return  ### calculate only received data
		elif pkt.ipd == self.addr:
			port = pkt.pd
		else:
			return

		if port in self.ports:
			bytes, packets = self.ports[port]
		else:
			bytes, packets = (0, 0)

		bytes += int( pkt.size )
		packets += 1

		self.ports[port] = (bytes, packets)

class ProcessingThread(QtCore.QThread, ):
	def __init__(self, opts, parent = None):
		QtCore.QThread.__init__(self, parent)
		self.opts = opts
		self.addr = opts.addr
		self.port = opts.port
		QtCore.QThreadPool.globalInstance().setMaxThreadCount(50)
		#self.threadPool.setMaxThreadCount(50)


	def socket_changed(self, addr, port):
		self.addr = addr
		self.port = port

	def loadPeerInfo(self, capture):
		# Loads dumped info in a dictionary where "ip port" is the key
		# and items are list of [CAP, HOP, RTT]
		printer.printDebug(self.opts, "Loading peer_info from %s" % capture)
		info_ = {}
		try:
			f = open(capture, "r")	
		except:
			print "Problem opening file: no info available for capture"
			f = None
		if f:
			for i in f:
				if i[0] == '#':
					continue
				# i = i.replace('None', '0.0')
				fields = i.split()
					# XXX: HOP problem if None, all infos on the line are lost
				# info_["%s %s" % (fields[0], fields[1])] = [float(i) for i in fields[2:]]
				tmp_lst = []
				for fld in fields[2:]:
					try:
						parsed = float(fld)
					except Exception, e:
						printer.printDebug(self.opts, "[Warning] %s" % (e,))
						parsed = None
					tmp_lst.append(parsed)
				info_["%s %s" % (fields[0], fields[1])] = tmp_lst
			f.close()
		return info_


	def run(self):
		first = True
		n_pkts = 0
		i = 0
		T = 0 # Delta T

		print "building Peer"
		self.peer = Peer(self.opts)
		ports = Port()
		geo = Geolocalization()
		activePorts = ActivePorts( self.addr, self.opts.interval )

		# Discover public IP address of the probe
		# With high probability it is in the same network as the client.
		if self.opts.pubIP == None:
			print "pubIP thread started"
			pubipT = PubIPThread(self.opts)
			pubipT.run()
			pubipT.wait()
			print "pubIP thread finished"
		
		self.opts.myAS = geo.as_by_addr(self.opts.pubIP).split()[0]
		printer.printDebug(self.opts, "My AS: %s" % (self.opts.myAS,))

		if self.opts.pinfo_file == None and self.opts.capture:
			self.opts.pinfo_file = "%s.capprobe.txt" % self.opts.capture
		self.peer.peers_info = self.loadPeerInfo(self.opts.pinfo_file)
		if self.opts.interface:
			printer.printDebug(self.opts, "Opening live capture")
			f = packet.open_live_capture(self.opts.interface, filter=self.opts.filter)

		else:
			f = packet.open_capture(self.opts.capture, filter=self.opts.filter)

		while True:
#			for line in f:
			try:
				line = f.next()
			except StopIteration:
				print "Fine cattura"
				break
			except Exception, e:
				print "Mess in the readline " + str(e)
				continue

			try:
				pkt = packet.Packet(line)
			except packet.PacketException, p:
				continue

			# distributions are calculated every 100 packets
			if i == 100:
				# pktsize.distribution()
				# ports.write_distribution()
				i = 0
			i += 1
			n_pkts += 1

			socket_read = make_socket(self.addr, self.port)


			# if self.opts.debug:
			# 	print >>sys.stderr, n_pkts
		
			# This if will be true only with the very first packet seen
			# in order to memorize the timestamp
			if first:
				first = False
				beginTimestamp = float( pkt.time )	# the timestamp when the delta T begins	
				timestampFP = beginTimestamp # timestamp of first packet in general
				current_socket = socket_read

			currentTimestamp = float( pkt.time ) # read the current timestamp

			# if 5 sec have passed then I perform the statistic average of everything
			if currentTimestamp-beginTimestamp >= self.opts.interval:
				beginTimestamp = currentTimestamp
				T +=1 # DELTA T (5 sec)
					
				self.peer.filter_peers_and_count(T)
				gInfo = self.globalPeersInfo("new")
				self.peer.pattern(T)
				self.peer.writeInstantValues()
				self.peer.print_geolocalization(T)
				self.peer.print_topTenAs(T)
				self.peer.As(self.opts.addr,T)
				self.peer.printPDF()
				self.peer.print_kiviat_info(T)
				self.peer.print_scatterplots()
				self.peer.newT() # initialize the data 

				self.emit(QtCore.SIGNAL('update_gui'), 
							activePorts.get_ports(), gInfo)
				activePorts.reset()
					
			# if I change the socket I am analyzing then I reset everything
			if socket_read != current_socket:
				T = 0
				current_socket = socket_read
				beginTimestamp = float(line[0])
				ports = Port()
				self.peer = Peer(self.opts)
				self.peer.peers_info = self.loadPeerInfo(self.opts.pinfo_file)
				activePorts = ActivePorts( self.addr, self.opts.interval )


			self.peer.count_peers(current_socket, pkt)
			ports.update(line, current_socket)

			activePorts.add_packet(pkt)

	def make_snapshot(self):
		tarThread = TarThread(self.opts)
		tarThread.start()
		# Now dump to a file all RTT, CAP etc of measured peers
		outfName = "%s.capprobe.txt" % (self.opts.capture and self.opts.capture or "live")
		fout = open(outfName, 'w')
		print >> fout, "#IP PORT CAP HOP RTT"
		for p in self.peer.PEERS.values():
			paddr, pport = p.socket.split(' ')
			if p.CapPstaus == 0:
				print >> fout, "%s %s %s %s %s" % \
						(paddr, pport, p.CAP, p.HOP, p.RTT) 
		tarThread.wait()


	def globalPeersInfo(self, caller):
		return self.peer.getGlobalInfo(caller)

	def cb_changed(self, state):
		pass

if __name__ == "__main__":
		main()

