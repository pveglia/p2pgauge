set terminal png `cat ../option`
set output '01_scatter.RTT.png'

set style rect fc lt -1 fs solid 0.15 noborder
set xran [0:5000]
# set yran [1:1e6]
set logs y
set arrow from `cat scatter_RTT.MEDIAN`, gr 0 to `cat scatter_RTT.MEDIAN`, gr 1 nohead
set object 1 rect from gr 0, gr 0 to `cat scatter_RTT.MEDIAN`, gr 1
# set arrow from 0, 1 to 1000, 1 nohead
set xlabel "RTT (ms)"
set ylabel "Bytes exchanged"

set title "Threshold = `cat scatter_RTT.MEDIAN` (median), \
PP PEERS = `cat scatter_RTT.PEER_POT`% BYTES = `cat scatter_RTT.BYTE_POT`%"

# safelog(x) = (x > 0 )? log(x) : -log(-x)

plot 'scatter_RTT.DATA' u 1:($2 > 0 ? $2 : 1/0) t 'TX' w p pt 7 ps 2,\
'' u 1:($2 < 0 ? -$2 : 1/0) t 'RX' w p pt 7 ps 2


