set terminal png `cat ../option`
set output "01_rtt.png"
set style rect fc lt -1 fs solid 0.15 noborder



set xlabel "RTT (ms)"
set ylabel "CDF"
set key b r

plot \
'peer.RTT.DATA' 	u 1:3   	t 'peer-wise' 	w  l lw 3, \
'bytes.RTT.DATA'	u 1:3   	t 'byte-wise'	w  l lw 3

