#!/usr/bin/env python

import sys
import math
import glob
import os
from optparse import OptionParser
import re


def kiviat():

	id_graph = graph.split(' ')[-1].rstrip('\n') # id of kiviat graph
	kiviat_name = "".join(["kiviat.",id_graph,".gp"])

	PARAM, n_curves = load_parameters()

	#for i in PARAM:
	#	print PARAM[i].value
		
	id_param = 0
	n_param = str(len(PARAM))
	f = open(kiviat_name,"w")
	f.write(
	"#! xgp -wp\n\n"

	"set terminal png `cat ../option`\n"
	"set output '" + kiviat_name.replace(".gp",".png")+"'\n"
	"set parametric\n"\
	"set xran [-12:12]\n"\
	"set yran [-12:12]\n"\
	"set border 0\n"\
	"set size square\n"\
	"unset xtics\n"\
	"unset ytics\n\n"\
	"#set cbrange [0:10]\n"
	"#set cbtics(0,1,2,3,4,5,6,7,8,9,10)\n\n"\

	"a(x1,y1,x2,y2) = ((y2-y1)/(x2-x1))\n"\
	"b(x1,y1,x2,y2) = (y1-(((y2-y1)/(x2-x1))*x1))\n\n"

	"step=2*pi/" + n_param + "\n"\
	"delta=pi/90\n"\
	"unset arrow\n\n")
	

	
	for param in PARAM:
		
		f.write(
		"N=" + str(id_param) + "\n"\
		" theta=" + str(id_param) + "*step + pi/" + n_param + "\n"\
  		" x=10*cos(theta)\n"\
  		" y=10*sin(theta)\n"\
		" set arrow from 0,0 to x,y lw 1 nohead front\n")


		f.write(" set label '" + PARAM[param].label + "' at 12*cos(theta+delta),12*sin(theta+delta)\n"
					" set label '" + PARAM[param].max + "' at 11*cos(theta+delta), 11*sin(theta+delta)\n")

		for k,value in enumerate(PARAM[param].value):
			f.write(" rho" + str(k) + "=(" + value + ' + 0.0' + ")/(" + PARAM[param].max + " + 0.0)*10.0; # rho=val/max*10\n"\
  					" x" + str(id_param) + "_" + str(k) + "=rho" + str(k) + "*cos(theta)\n"\
  					" y" + str(id_param) + "_" + str(k) + "=rho" + str(k) + "*sin(theta)\n\n")
		id_param += 1

	f.write("set multiplot\n\n")
	
	nParam = int(n_param)
	i = 0
	while i < nParam:
		c = n_curves - 1
		while c >= 0:
			next = i + 1
			if next == nParam:
				next = 0
		
			f.write(
				"plot [t=x"+str(i)+"_"+str(c)+":x"+str(next)+"_"+str(c)+"]"+\
				      "t,a(x"+str(i)+"_"+str(c)+",y"+str(i)+"_"+str(c)+",x"+str(next)+"_"+str(c)+",y"+str(next)+"_"+str(c)+")*t + b(x"+str(i)+\
					"_"+str(c)+",y"+str(i)+"_"+str(c)+",x"+str(next)+"_"+str(c)+",y"+str(next)+"_"+str(c)+") t '' w l lt 1 lc "+str(c+1)+" lw 4 \n\n"
				)
				
			c = c -1
		i+=1
	

	f_curves = open (graph.rstrip('\n').split(' ')[1], "r")
	for k,curve in enumerate(f_curves):
		curve = curve.rstrip("\n")
		if k == 0:
			f.write("set key left top Lef rev; plot [t=0:0] (1/0),(1/0) t '"  + curve + "' w l lt 1 lc " + str(k+1) + " lw 4 ,")
			first = 0
		if k > 0 and k < n_curves - 1:
			f.write("(1/0),(1/0) t  '"+ curve + "' w l lt 1 lc " + str(k+1) + " lw 4,")
		if k == n_curves-1:
			f.write("(1/0),(1/0) t  '"+ curve + "' w l lt 1 lc " + str(k+1) + " lw 4\n")
	f.write("unset multiplot\n")
	
	f.close()




def read_data(cap,p): # it reads the value of paramter p in the capture cap
	f_cap = open (cap,"r")
	for line in f_cap.read:
		line = line.rstrip("\n").split(" ")
		nameParam = line[0]
		if nameParam == p:
			f_cap.close()
			return float(line[1])


class Axe:
	def __init__(self):
		self.label = None
		self.max = None
		self.value = []

def load_parameters ():
	n_curves = 0
	f_data  = open("kiviat.DATA","r")
	patterns = [] # this vector contains the curves to put on the kiviat diagram
	f_curves = open(graph.split()[1],"r")
	f_axes = open(graph.split()[0],"r")
	for curve in f_curves:
		patterns.append(curve.rstrip('\n')) 
		n_curves += 1
	f_curves.close()
	PARAM = {}
	for line in f_axes:
		if line[0] == "#":
			continue
		line = line.rstrip('\n').split()
		axe = line[0]
#		print "axe: %s" % line[0]
		PARAM[axe] = Axe()
		PARAM[axe].label = line[1]
#		print "label: %s" % line[1]
		PARAM[axe].max = line[2]
#		print "max: %s" % line[2]

	for line in f_data:
		if line.rstrip() == "":
			continue
		param = line.rstrip('\n').split()[0].split('_')[0] # I read the name of the parameter
		for p in patterns:
			if param in PARAM and line.split(" ")[0] == param + '_' + p: # I check if the current line match one of the curves contained in patterns
				value = line.rstrip("\n").split(" ")[1] # I read the value
				PARAM[param].value.insert(patterns.index(p),value) # I insert the value in the dictionary in the same order given in the vector patterns
				#break
	f_data.close()
	f_axes.close()
	return PARAM, n_curves

def read_parameters():
	pass

if __name__ == "__main__":

	f_conf = open("kiviat.conf","r")

	for graph in f_conf:	
		kiviat()
	f_conf.close()

	print >> open("description.txt", "w"), \
		"POT Kiviat: #probed_peers_tot=%s, #probed_peers_last=%s" % (\
		open("t_p_peers.dat").read().rstrip(),
		open("c_p_peers.dat").read().rstrip() )

