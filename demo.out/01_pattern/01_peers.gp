#! xgp -wp

set terminal png `cat ../option`
set output '01_peers.png'
set pointsize 0.25
set size 1, 1
set title ""
xmax = `tail -n 1 new_peers.DATA | cut -d" " -f 1`
set xrange [1:xmax+1]
set y2label  "Total number of peers"
set ylabel  "Number of peers in DT"
set y2tics
set xlabel "DT (5 sec)"
set key top left Left rev


plot "peers.DATA"  t "Number of peers in DT" w l,\
 "new_peers.DATA"   t "Number of new peers in DT" w l,\
 "same_peers.DATA"   t "Number of same peers in DT" w l,\
 "total_new_peers.DATA"  ax x1y2 t "Total number of contributors" w l



