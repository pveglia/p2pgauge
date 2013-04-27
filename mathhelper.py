from math import *
import histo

# Bhattacharyya coefficient of two PDFs
# D(B) = sum(sqrt(p(x)q(x)))
def bhatta(v1, v2):
	sum = 0.0
	for p,q in zip(v1,v2):
		sum += sqrt(p * q)
	res = sqrt(1 - sum)
	# print "BATTA === %f ===" % res
	return res


# Kullback Leibler divergence of two PDFs
# DKL(P||Q) = sum( P(i)*log( P(i)/Q(i) ) )
#
# NOTE: discarding null samples is not a bug since q=0 ==> p=0 

def kulb(peer_pdf, byte_pdf):
	res = sum( [p * log(p/q) for p,q in zip(peer_pdf, byte_pdf) if q != 0.0] )
	# print "KULL === %f ===" % res
	return res 
