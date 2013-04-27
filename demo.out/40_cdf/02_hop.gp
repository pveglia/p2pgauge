set terminal png `cat ../option`
set output "02_hop.png"
set style rect fc lt -1 fs solid 0.15 noborder

set key bottom right

set xlabel "HOP Distance"
set ylabel "CDF"

plot \
'peer.HOP.DATA' 	u 1:3   	t 'peer-wise' 	w  l lw 3, \
'bytes.HOP.DATA'	u 1:3   	t 'byte-wise'	w  l lw 3

