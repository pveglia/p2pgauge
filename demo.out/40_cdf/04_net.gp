set terminal png `cat ../option`
set output "04_net.png"
set style rect fc lt -1 fs solid 0.15 noborder
# set logscale x

set key bottom right

set xlabel "# Common bits in IP address (Longest prefix match)"
set ylabel "CDF"

plot \
'peer.NET.DATA' 	u 1:3   	t 'peer-wise' 	w  l lw 3, \
'bytes.NET.DATA'	u 1:3   	t 'byte-wise'	w  l lw 3

