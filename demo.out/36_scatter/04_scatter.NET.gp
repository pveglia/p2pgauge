set terminal png `cat ../option`
set output '04_scatter.NET.png'
set style rect fc lt -1 fs solid 0.15 noborder

set xran [0:32]
set logs y
#set yran [-2000000:1000000]
set arrow from 16, gr 0 to 16, gr 1 nohead
# set arrow from 0, 0 to 32, 0 nohead
set xlabel "# Common bits in IP address (Longest prefix match)"
set ylabel "Bytes exchanged"
set object 1 rect from 16, gr 0 to gr 1, gr 1

set title "Threshold = 16 (fixed), PP PEERS = `cat scatter_NET.PEER_POT`% \
BYTES = `cat scatter_NET.BYTE_POT`%"

plot 'scatter_NET.DATA' u 1:($2 > 0 ? $2 : 1/0) t 'TX' w p pt 7 ps 2,\
'' u 1:($2 < 0 ? -$2 : 1/0) t 'RX' w p pt 7 ps 2

