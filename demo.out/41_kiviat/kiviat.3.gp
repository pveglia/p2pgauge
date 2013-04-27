#! xgp -wp

set terminal png `cat ../option`
set output 'kiviat.3.png'
set parametric
set xran [-12:12]
set yran [-12:12]
set border 0
set size square
unset xtics
unset ytics

#set cbrange [0:10]
#set cbtics(0,1,2,3,4,5,6,7,8,9,10)

a(x1,y1,x2,y2) = ((y2-y1)/(x2-x1))
b(x1,y1,x2,y2) = (y1-(((y2-y1)/(x2-x1))*x1))

step=2*pi/6
delta=pi/90
unset arrow

N=0
 theta=0*step + pi/6
 x=10*cos(theta)
 y=10*sin(theta)
 set arrow from 0,0 to x,y lw 1 nohead front
 set label 'CAP' at 12*cos(theta+delta),12*sin(theta+delta)
 set label '1' at 11*cos(theta+delta), 11*sin(theta+delta)
 rho0=(0.265353 + 0.0)/(1 + 0.0)*10.0; # rho=val/max*10
 x0_0=rho0*cos(theta)
 y0_0=rho0*sin(theta)

 rho1=(0.230927 + 0.0)/(1 + 0.0)*10.0; # rho=val/max*10
 x0_1=rho1*cos(theta)
 y0_1=rho1*sin(theta)

N=1
 theta=1*step + pi/6
 x=10*cos(theta)
 y=10*sin(theta)
 set arrow from 0,0 to x,y lw 1 nohead front
 set label 'sCC' at 12*cos(theta+delta),12*sin(theta+delta)
 set label '1' at 11*cos(theta+delta), 11*sin(theta+delta)
 rho0=(0.000000 + 0.0)/(1 + 0.0)*10.0; # rho=val/max*10
 x1_0=rho0*cos(theta)
 y1_0=rho0*sin(theta)

 rho1=(0.000000 + 0.0)/(1 + 0.0)*10.0; # rho=val/max*10
 x1_1=rho1*cos(theta)
 y1_1=rho1*sin(theta)

N=2
 theta=2*step + pi/6
 x=10*cos(theta)
 y=10*sin(theta)
 set arrow from 0,0 to x,y lw 1 nohead front
 set label 'RTT' at 12*cos(theta+delta),12*sin(theta+delta)
 set label '1' at 11*cos(theta+delta), 11*sin(theta+delta)
 rho0=(0.265353 + 0.0)/(1 + 0.0)*10.0; # rho=val/max*10
 x2_0=rho0*cos(theta)
 y2_0=rho0*sin(theta)

 rho1=(0.230927 + 0.0)/(1 + 0.0)*10.0; # rho=val/max*10
 x2_1=rho1*cos(theta)
 y2_1=rho1*sin(theta)

N=3
 theta=3*step + pi/6
 x=10*cos(theta)
 y=10*sin(theta)
 set arrow from 0,0 to x,y lw 1 nohead front
 set label 'HOP' at 12*cos(theta+delta),12*sin(theta+delta)
 set label '1' at 11*cos(theta+delta), 11*sin(theta+delta)
 rho0=(0.265353 + 0.0)/(1 + 0.0)*10.0; # rho=val/max*10
 x3_0=rho0*cos(theta)
 y3_0=rho0*sin(theta)

 rho1=(0.230927 + 0.0)/(1 + 0.0)*10.0; # rho=val/max*10
 x3_1=rho1*cos(theta)
 y3_1=rho1*sin(theta)

N=4
 theta=4*step + pi/6
 x=10*cos(theta)
 y=10*sin(theta)
 set arrow from 0,0 to x,y lw 1 nohead front
 set label 'sAS' at 12*cos(theta+delta),12*sin(theta+delta)
 set label '1' at 11*cos(theta+delta), 11*sin(theta+delta)
 rho0=(0.388471 + 0.0)/(1 + 0.0)*10.0; # rho=val/max*10
 x4_0=rho0*cos(theta)
 y4_0=rho0*sin(theta)

 rho1=(0.211260 + 0.0)/(1 + 0.0)*10.0; # rho=val/max*10
 x4_1=rho1*cos(theta)
 y4_1=rho1*sin(theta)

N=5
 theta=5*step + pi/6
 x=10*cos(theta)
 y=10*sin(theta)
 set arrow from 0,0 to x,y lw 1 nohead front
 set label 'NET' at 12*cos(theta+delta),12*sin(theta+delta)
 set label '1' at 11*cos(theta+delta), 11*sin(theta+delta)
 rho0=(0.000000 + 0.0)/(1 + 0.0)*10.0; # rho=val/max*10
 x5_0=rho0*cos(theta)
 y5_0=rho0*sin(theta)

 rho1=(0.000000 + 0.0)/(1 + 0.0)*10.0; # rho=val/max*10
 x5_1=rho1*cos(theta)
 y5_1=rho1*sin(theta)

set multiplot

plot [t=x0_1:x1_1]t,a(x0_1,y0_1,x1_1,y1_1)*t + b(x0_1,y0_1,x1_1,y1_1) t '' w l lt 1 lc 2 lw 4 

plot [t=x0_0:x1_0]t,a(x0_0,y0_0,x1_0,y1_0)*t + b(x0_0,y0_0,x1_0,y1_0) t '' w l lt 1 lc 1 lw 4 

plot [t=x1_1:x2_1]t,a(x1_1,y1_1,x2_1,y2_1)*t + b(x1_1,y1_1,x2_1,y2_1) t '' w l lt 1 lc 2 lw 4 

plot [t=x1_0:x2_0]t,a(x1_0,y1_0,x2_0,y2_0)*t + b(x1_0,y1_0,x2_0,y2_0) t '' w l lt 1 lc 1 lw 4 

plot [t=x2_1:x3_1]t,a(x2_1,y2_1,x3_1,y3_1)*t + b(x2_1,y2_1,x3_1,y3_1) t '' w l lt 1 lc 2 lw 4 

plot [t=x2_0:x3_0]t,a(x2_0,y2_0,x3_0,y3_0)*t + b(x2_0,y2_0,x3_0,y3_0) t '' w l lt 1 lc 1 lw 4 

plot [t=x3_1:x4_1]t,a(x3_1,y3_1,x4_1,y4_1)*t + b(x3_1,y3_1,x4_1,y4_1) t '' w l lt 1 lc 2 lw 4 

plot [t=x3_0:x4_0]t,a(x3_0,y3_0,x4_0,y4_0)*t + b(x3_0,y3_0,x4_0,y4_0) t '' w l lt 1 lc 1 lw 4 

plot [t=x4_1:x5_1]t,a(x4_1,y4_1,x5_1,y5_1)*t + b(x4_1,y4_1,x5_1,y5_1) t '' w l lt 1 lc 2 lw 4 

plot [t=x4_0:x5_0]t,a(x4_0,y4_0,x5_0,y5_0)*t + b(x4_0,y4_0,x5_0,y5_0) t '' w l lt 1 lc 1 lw 4 

plot [t=x5_1:x0_1]t,a(x5_1,y5_1,x0_1,y0_1)*t + b(x5_1,y5_1,x0_1,y0_1) t '' w l lt 1 lc 2 lw 4 

plot [t=x5_0:x0_0]t,a(x5_0,y5_0,x0_0,y0_0)*t + b(x5_0,y5_0,x0_0,y0_0) t '' w l lt 1 lc 1 lw 4 

set key left top Lef rev; plot [t=0:0] (1/0),(1/0) t 'BHATTA_bytes_sent_lastdt' w l lt 1 lc 1 lw 4 ,(1/0),(1/0) t  'BHATTA_bytes_rec_lastdt' w l lt 1 lc 2 lw 4
unset multiplot
