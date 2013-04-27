set terminal png `cat ../option`
set output '03_scatter.CAP.png'
set style rect fc lt -1 fs solid 0.15 noborder

set logs y
set logscale x
set xran [0.01:100]
# set yran [-2000000:1000000]
set arrow from `cat scatter_CAP.MEDIAN`, gr 0 to `cat scatter_CAP.MEDIAN`, gr 1 nohead
# set arrow from 0,0 to 100,0 nohead
set xlabel "Bottleneck capacity (Mbit)"
set ylabel "Bytes exchanged"
set object 1 rect from `cat scatter_CAP.MEDIAN`, gr 0 to gr 1, gr 1

set title "Threshold = `cat scatter_CAP.MEDIAN` (median), \
PP PEERS = `cat scatter_CAP.PEER_POT`% BYTES = `cat scatter_CAP.BYTE_POT`%"

plot 'scatter_CAP.DATA' u 1:($2 > 0 ? $2 : 1/0) t 'TX' w p pt 7 ps 2,\
'' u 1:($2 < 0 ? -$2 : 1/0) t 'RX' w p pt 7 ps 2

