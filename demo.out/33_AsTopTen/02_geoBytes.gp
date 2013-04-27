set terminal png `cat ../option`
set output '02_geoBytes.png'

set ylab "Number of Bytes"
set xlab "Autonomous system number [ASn]"
set title "`cat tot_bytes.DATA` geolocalized bytes, `cat unk.bytes.DATA` unknown"

#  +-------+
#  |       |
#  |   0   |
#  |       |
#  +-------+


###########
set key below
set style data histogram
set style histogram rowstacked
set boxwidth 0.9
set style fill solid border -1
set xrange [-0.5:9.5]
# set xtics rotate by -45 

plot 'geobytes.DATA' u 2:xtic(1) t 'Africa' lt 1, \
'' u 3 lt 2 t 'Asia',\
'' u 4 lt 3 t 'Europe',\
'' u 5 lt 4 t 'NorthAmerica',\
'' u 6 lt 5 t 'Oceania',\
'' u 7 lt 6 t 'SouthAmerica',\
'' u 8 lt 7 t 'Unknown',\
'' u 9  lt 1 t '', \
'' u 10  lt 2 t '', \
'' u 11 lt 3 t '', \
'' u 12 lt 4 t '', \
'' u 13 lt 5 t '', \
'' u 14 lt 6 t '',\
'' u 15 lt 7 t ''


#  +-------+
#  |       |
#  |   0   |
#  |       |
#  +-------+
#set origin 0.00,0.00
#set size   1.00,0.50
#
#set title ""
#set key below
#set ylab "Number of Bytes\n(logscale)"
#
#plot 'geobytes.log10.DATA' u 2:xtic(1) t 'Africa' lt 1, \
#'' u 3 lt 2 t 'Asia',\
#'' u 4 lt 3 t 'Europe',\
#'' u 5 lt 4 t 'NorthAmerica',\
#'' u 6 lt 5 t 'Oceania',\
#'' u 7 lt 6 t 'SouthAmerica',\
#'' u 8  lt 1 t '', \
#'' u 9  lt 2 t '', \
#'' u 10 lt 3 t '', \
#'' u 11 lt 4 t '', \
#'' u 12 lt 5 t '', \
#'' u 13 lt 6 t ''

