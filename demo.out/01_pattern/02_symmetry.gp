#! xgp -wp

set terminal png `cat ../option`
set output '02_symmetry.png'

set pointsize 1
set size 1, 1
set lmargin 8

set ylabel "packets"
set xlabel "peer identifier"
set multiplot layout 2,1

set title "exchanged packets"

plot "symmetry.DATA"  u 1:3 t "out" w boxes,\
	 "symmetry.DATA" u 1:(-$2) t "in" w boxes

set title "exchanged bytes"

plot "symmetry.DATA"  u 1:5 t "out" w boxes,\
	 "symmetry.DATA" u 1:(-$4) t "in" w boxes

