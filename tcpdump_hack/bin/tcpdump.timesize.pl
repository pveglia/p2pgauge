#! /usr/bin/perl

for $FILE (@ARGV) {
    open TCPDUMP, "tcpdump.timesize -r $FILE |";
    while (<TCPDUMP>) {
       chomp; split;

       if( scalar(@_)==3 ) {
	  print "$_[0]$_[1] $_[2]\n";
       } else {   
	  print "0.@_\n";
       }
    } 
    close TCPDUMP;
}
