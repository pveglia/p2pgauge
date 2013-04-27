set terminal png `cat ../option`
set output '02_scatter.HOP.png'
set style rect fc lt -1 fs solid 0.15 noborder

set logs y
# set xran [0:128]
# set yran [-2000000:1000000]
set arrow from `cat scatter_HOP.MEDIAN`, gr 0 to `cat scatter_HOP.MEDIAN`, gr 1 nohead
# set arrow from 0,0 to 128,0 nohead
set xlabel "HOP distance"
set ylabel "Bytes exchanged"
set object 1 rect from gr 0, gr 0 to `cat scatter_HOP.MEDIAN`, gr 1

set title "Threshold = `cat scatter_HOP.MEDIAN` (median), \
PP PEERS = `cat scatter_HOP.PEER_POT`% BYTES = `cat scatter_HOP.BYTE_POT`%"

plot 'scatter_HOP.DATA' u 1:($2 > 0 ? $2 : 1/0) t 'TX' w p pt 7 ps 2,\
'' u 1:($2 < 0 ? -$2 : 1/0) t 'RX' w p pt 7 ps 2

