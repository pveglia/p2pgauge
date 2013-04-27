import GeoIP
from ccinfo import ccinfo
import string

class Geolocalization:
	def __init__(self):
		self.gi = GeoIP.new(GeoIP.GEOIP_MEMORY_CACHE)
		self.continent_id = dict( zip(['Africa','Asia','Europe','NorthAmerica','Oceania','SouthAmerica', 'unk'], range(7)) )
		self.As = GeoIP.open("/usr/local/share/GeoIP/GeoIPASNum.dat",GeoIP.GEOIP_MEMORY_CACHE)

 	def geolocalize(self, ip):
		cc =  self.gi.country_code_by_addr(ip)
		if not cc:
			return 'unk', 6
		cc = string.lower(cc)
		if cc in ccinfo:
			co = ccinfo[cc]['continent']
		else:
			cc,co = ['unk']*2
		return cc, self.continent_id[co] # return country code and numeric id of the continent

	def as_by_addr(self,ip):
		return self.As.org_by_addr(ip)

