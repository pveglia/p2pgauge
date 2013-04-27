USAGE

   ./P2PDemo.py -a ip-address [-r capture | -i interface] - p [port | '*'] [-C]
   [-c country-code] [-f filter] [-I interval] [-d] [-b info-file] [-t
   contr-threshold] `pwd`

ARGUMENTS DESCRIPTION

   -a  mandatory, used to specify the address of the endpoint generating P2P
	   traffic. Only packet with this address in src or dst field are analyzed.

   -r  capture file.

   -i  physical interface 

   -p  port to listen on. It can be the port number used by the application (if
	   known) or '*'. In this case all UDP traffic is analyzed. This option does
	   not have a permanent effect since the port can be chosen from the
	   configuration tab.

   -C  This flag inhibits the use of active probing. Required information are
	   loaded from info files. See '-b' flag

   -b  Specifies the name of info file. This option must be used in conjunction
	   with -C and -i or -r. By default, if -r is used, P2PGauge will try to
	   load data from a file whose name is 'capturefile.pcap.capprobe.txt'. Use
	   this option if you want to override this behaviour. This option can come
	   in hand traces are replyed with 'tcpreply'

   -c  Sets the country code in 2 char form (e.g. 'fr', 'us', etc.,)
   
   -P  Sets the public ip address of the gauging machine. By default the 
	   information is inferred automatically with the help of an external web 
	   server but in case of off-line runs it must be set

   -f  With this option it is possible to specify a filter for tcpdump

   -I  Time interval that drives the frequency of statistic computations

   -d  Turns on debbugging information

   -t  Sets the contributor threshold: only peers that actively contribute to
	   the video stream are probed. The euristic used is simple: a peer is a
	   contributor if n packets are sent/received from it. This option
	   configures the parameter n.


NOTES

P2PGauge is a tool to visualize the level of "network awareness" of a P2P
application. It can run both live and off-line. In the first case you must
specify a local interface where P2P traffic is present while in the latter a
capture name must be given. 

First tab works as a configuration tab. Here you can see how the application is
configured and you can choose the port on which analyze traffic.

On this tab there is also a "snapshot" button that: 
   * makes a tarball archive of the demo.out folder with plots and data file and
   * dumps information about each contacted peer. 
These informations are collected by active probing during the whole execution of
the tool and are essential to the functioning of the application.  Nevertheless
off-line runs can be also performed passing *.capprobe.txt files with '-b' flag.

During the start-up phase, P2PGauge will try to discover the public IP address
of the machine contacting a simple web server. If you have no connectivity
please use the '-P' flag. 

For what concerns other tabs please refer to published paper.

REFERENCES

  * Dario Rossi, Elisa Sottile, Silvio Valenti, Paolo Veglia, "Gauging the
	network friendliness of P2P applications," SIGCOMM'09 demo session,
	Barcelona, Spain, August 2009.

  * A. Horvath, M. Telek, D. Rossi, P. Veglia, D. Ciullo, M. A.  Garcia, E. 
	Leonardi and M. Mellia, "Network Awareness of P2P Live Streaming 
	Applications," In HOTP2P Workshop at IEEE IPDPS'09, Rome, Italy, May 2009.
  
  * R.  Kapoor, L.  J.  Chen, Li Lao, M.  Gerla, and M.  Y.  Sanadidi.
	"CapProbe: A Simple and Accurate Capacity Estimation Technique," In ACM
	SIGCOMM'04, Portland, USA, 2004  
  
  * MaxMind GeoLite, http://www.maxmind.com/

EXAMPLES 

Some usage example. Traces can be found in the complete archive under traces
folder.

Live experiment
   sudo ./P2PDemo.py -a x.y.z.k -p * -c 'fr' `pwd`

Bittorrent trace
   sudo ./P2PDemo.py -a 192.168.144.52 -r bittorent_ubuntu.pcap -p 49437 -C -c
   'fr' -P x.x.x.x `pwd`

PPLive trace
   sudo ./P2PDemo.py -a 192.168.1.2 -r pplive_cctv6.pcap -p 7773 -C -c
   'fr' -P x.x.x.x `pwd`

TVAnts trace
   sudo ./P2PDemo.py -a 192.168.1.2 -r tvants_cctv5.pcap -p 16800 -C -c
   'fr' -P x.x.x.x `pwd`

SopCast trace
   sudo ./P2PDemo.py -a 192.168.1.2 -r sopcast_cctv5.pcap -p 7531 -C -c
   'fr' -P x.x.x.x `pwd`
  
