set terminal png `cat ../option`
set output "03_cap.png"
set logscale x
set xran [0.1:100]
set style rect fc lt -1 fs solid 0.15 noborder

set key bottom right

set xlabel "Bottleneck capacity (Mbit/s)"
set ylabel "CDF"

plot \
'peer.CAP.DATA' 	u 1:3   	t 'peer-wise' 	w  l lw 3, \
'bytes.CAP.DATA'	u 1:3   	t 'byte-wise'	w  l lw 3

