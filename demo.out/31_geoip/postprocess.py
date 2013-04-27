#!/usr/bin/env python

"""
This script calculates the percentage of peers in every continent and
creates the gnuplot scripts that display the world map with color
normalization and also every single continent map with
country color normalization
"""

import glob
import os
import re
import sys
import stat

class GeoData:
        "geoip data"

        def acquireData(self):
                """It checks if geoip.data exists and if it's not empty.
                Then it reads geoip.data row by row and keeps track
                of number of peers in every continent"""

                try:
                        file_info = os.stat(self.file)
                except:
                        print "geoip.data not available yet"
                        sys.stderr.write('postprocess.py in geoip says: Warning, geodata does not exist yet\n')
                        sys.exit()

                if file_info.st_size < 2:
                        return False  # geodata is empty


# we copy the file in current.DATA so that we avoid incongruity having a file that changes meanwhile we performs statistics
                os.system("cp "+self.file+" current.DATA")
                # os.system("cp ../30_geoip/geoip.UNK geoip.UNK.DATA")
                f = open("current.DATA",'r')

                for row, line in enumerate(f):
                        line = line.rstrip('\n')

                        for col, s in enumerate(line.split()):
                                if col > 0:
                                        self.continents[col-1] += int(s)

                f.close()

        # calculation of total number of peers
                for i, c in enumerate(self.continents):
                        self.total_peers += c

                try:
                        f_unk = open('geoip.UNK.DATA', "r")
                        line = f_unk.readline().rstrip('\n')
                        self.unknown_peers = line.split()[2]
                except:
                        self.unknow_peers = 0

                return True

        def percentageWorld(self):
                "calculates the percentage of peers for every continent"

                for i, c in enumerate(self.continents):
                        if c == 0:
                                self.percentage[i] = 0
                        else:
                                if self.total_peers != 0:
                                        self.percentage[i] = round(self.continents[i]*100/self.total_peers,2)

                return self.percentage



        def percentageContinent(self, countries, column):
                """calculates the percentage of peers relative
                to the continent for each country encountered in geoip.data"""
                f = open("current.DATA",'r')

                for row, line in enumerate(f):
                        line = line.rstrip('\n')

                        for col, s in enumerate(line.split()):
                                # if it is the first column get the country code
                                if col == 0:
                                        cc = s
                                # if the column is the one corresponding to the continent
                                # we are analyzing then.........
                                if (col == column):
                                        # if the country code is found in the hash......
                                        if cc in countries:
                                                # if the number of peers in the continent is greater than 0
                                                if self.continents[col - 1] > 0:
                                                        # associate to country cc the percentage relative to the continent
                                                        f = dict({cc: float(s)*100/self.continents[col-1]})
                                                        # add update this element in the dictionary
                                                        countries.update(f)
                #tot = 0
                #for i in countries.iteritems():
                #       tot += i[1]
                #if tot > 100.1:
                #       sys.stderr.write("Fatal error, the percentage of continent in the column " + str(column) + " has a total percentage = "+ str(tot) + '\n')

                return countries


                f.close()


        def __init__(self,filename):
                self.file = filename # file that contains the geogrphic data
                # vector that contains the number of peers in each continent
                # Asia, Europe, North America, Oceania, SouthAmerica, Unknown
                self.continents = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
                self.percentage = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
                self.total_peers = 0
                self.unknown_peers = 0

class Continent:
                def getPolygons(self):
                        # open the directory with polygons from continent
                        os.chdir('./' + self.name + '/polygons/')
                        # put in the list 'cc' the countrycodes
                        polygons = glob.glob('*')
                        # go back to main directory
                        os.chdir('..')
                        os.chdir('..')
                        return polygons

                def getCountries(self):
                        # open the directory with countries from continent
                        os.chdir('./' + self.name + '/countries/')
                        # put in the list 'cc' the countrycodes
                        cc = glob.glob('*')
                        # go back to main directory
                        os.chdir('..')
                        os.chdir('..')
                        countries = dict({})
                        # countries is a dictionary (or hash) with country code and number of peers,
                        # initialized at 0
                        countries = countries.fromkeys(cc, 0)
                        return countries

                def __init__(self, name, percentage, directory, xlabel, ylabel):
                        self.name = name
                        self.percentage = percentage
                        self.directory = directory
                        self.xlabel = xlabel
                        self.ylabel = ylabel

class Script:

        def create(self):
                        f = open(self.script, 'w')
                        f.write ('#! xgp -wp\n\n'\
                                        'set terminal png `cat ../option`\n'\
                                        'set output \'' + self.script.replace(".gp","")+ '.png\'\n'\
                                        'set size 1.0, 1.0\n'\
                                        'set origin 0.0, 0.0\n'\
                                        'set xrange [-180:180]\n'\
                                        'set yrange [-60:80]\n'\
                                        'unset logscale x\n'\
                                        'unset logscale y\n'\
                                        'unset grid\n'\
                                        'set title \'world breakdown (' + str(int(self.total_peers)) + ' geolocalized peers, ' + str(self.unknown_peers) + ' unknown)\'\n'\
                                        'set xlabel ''\n'\
                                        'set ylabel ''\n'\
                                        'set border 15\n'\
                                        'unset xzeroaxis\n'\
                                        'unset yzeroaxis\n'\
                                        'set xtics norotate border autofreq\n'\
                                        'set ytics norotate border autofreq\n'\
                                        'dirAf = "' + africa.directory + '"\n'\
                                        'dirEu = "'+ europe.directory + '"\n'\
                                        'dirNA = "' + north_america.directory + '"\n'\
                                        'dirA = "' + asia.directory + '"\n'\
                                        'dirO = "' + oceania.directory + '"\n'\
                                        'dirSA = "' + south_america.directory + '"\n'\
                                        'set label \'' + str(africa.percentage) + '%\' at ' + str(africa.xlabel) + ', ' + str(africa.ylabel) + ' center front\n'\
                                        'set label \'' + str(asia.percentage) + '%\' at ' + str(asia.xlabel) + ', ' + str(asia.ylabel) + ' center front\n'\
                                        'set label \'' + str(europe.percentage) + '%\' at ' + str(europe.xlabel) + ', ' + str(europe.ylabel) + ' center front\n'\
                                        'set label \'' + str(north_america.percentage) + '%\' at ' + str(north_america.xlabel) + ', ' + str(north_america.ylabel) + ' center front\n'\
                                        'set label \'' + str(oceania.percentage) + '%\' at ' + str(oceania.xlabel) + ', ' + str(oceania.ylabel) + ' center front\n'\
                                        'set label \'' + str(south_america.percentage) + '%\' at ' + str(south_america.xlabel) + ', ' + str(south_america.ylabel) + ' center front\n'\
                                        'set colorbox\n'\
                                        'set palette defined (0 "#ff0000", 1 "#f37a1e", 3 "#ffff00", 4 "#00ff00", 5 "#ffffff")\n'\
                                        'set palette negative\n'\
                                        'set cbrange [0:100]\n'\
                                        'set cblabel \'percentage of peers\'\n'\
                                        'set cbtics(0,10,20,30,40,50,60,70,80,90,100)\n\n'\
                                        'plot   ')
                        for polygon in africa.getPolygons():
                                f.write ('dirAf' + '.\'' + polygon + '\' index 0 t \'\' w filledcurves lc palette cb ' + str(africa.percentage) + ' , dirAf.\'' + polygon + '\' index 1 t \'\' w l lw 1 lt 1 lc rgb  \'black\',\\\n')
                        for polygon in asia.getPolygons():
                                f.write ('dirA' + '.\'' + polygon + '\' index 0 t \'\' w filledcurves lc palette cb ' + str(asia.percentage) + ' , dirA.\'' + polygon + '\' index 1 t \'\' w l lw 1 lt 1 lc rgb  \'black\',\\\n')
                        for polygon in europe.getPolygons():
                                f.write ('dirEu' + '.\'' + polygon + '\' index 0 t \'\' w filledcurves lc palette cb ' + str(europe.percentage) + ' , dirEu.\'' + polygon + '\' index 1 t \'\' w l lw 1 lt 1 lc rgb  \'black\',\\\n')
                        for polygon in north_america.getPolygons():
                                f.write ('dirNA' + '.\'' + polygon + '\' index 0 t \'\' w filledcurves lc palette cb ' + str(north_america.percentage) + ' , dirNA.\'' + polygon + '\' index 1 t \'\' w l lw 1 lt 1 lc rgb  \'black\',\\\n')
                        for polygon in oceania.getPolygons():
                                f.write ('dirO' + '.\'' + polygon + '\' index 0 t \'\' w filledcurves lc palette cb ' + str(oceania.percentage) + ' , dirO.\'' + polygon + '\' index 1 t \'\' w l lw 1 lt 1 lc rgb  \'black\',\\\n')
                        for polygon in south_america.getPolygons():
                                f.write ('dirSA' + '.\'' + polygon + '\' index 0 t \'\' w filledcurves lc palette cb ' + str(south_america.percentage) + ' , dirSA.\'' + polygon + '\' index 1 t \'\' w l lw 1 lt 1 lc rgb  \'black\'')

                        f.close()

        def __init__(self, script, total_peers,unknown_peers):
                self.script = script
                self.total_peers = total_peers
                self.unknown_peers = unknown_peers




class ScriptC:

        def create(self, number_of_peers, total_peers, x1, x2, y1, y2, countries,d):

                        if total_peers > 0.1:
                                percentage = number_of_peers * 100 / total_peers
                        else:
                                percentage = 0
                        self.script.replace(".gp","")

                        f = open(self.script, 'w')
                        f.write ('#! xgp -wp\n\n'\
                                        'set terminal png `cat ../option`\n'\
                                        'set output \'' + self.script.replace(".gp","")+ '.png\'\n'\
                                        'set size 1.0, 1.0\n'\
                                        'set origin 0.0, 0.0\n'\
                                        'set xrange [' + str(x1) + ':' + str(x2) + ']\n'\
                                        'set yrange [' + str(y1) + ':' + str(y2) + ']\n'\
                                        'unset logscale x\n'\
                                        'unset logscale y\n'\
                                        'unset grid\n'\
                                        'set title \'' + \
                                        re.search('0._(.*)\.gp', self.script).group(1)+ \
                                        " breakdown ( " + str(int(number_of_peers)) + "/" + \
                                        str(int(total_peers)) + " peers, " + \
                                        str(round(percentage,2)) + "% of world peers)" '\'\n'\
                                        'set xlabel ''\n'\
                                        'set ylabel ''\n')
                        # check for every country within the continent if its percentage is greater than 0
                        for c in countries.iteritems():
                                # if percentage of country is greater than 0
                                if c[1] > 0:
                                        # calculate the coordinates of the label
                                        percentage_label = self.countryCenter(c[0])
                                        # add the label into the script
                                        f.write ('set label \'' + str(round(c[1],2)) + '%\' at ' + str(percentage_label[0]) + ', ' + str(percentage_label[1]) + ' center front font "medium"\n')
                        f.write('set border 15\n'\
                                        'unset xzeroaxis\n'\
                                        'unset yzeroaxis\n'\
                                        'set xtics norotate border autofreq\n'\
                                        'set ytics norotate border autofreq\n'\
                                        'dir = \'' + d + '\'\n'\
                                        'set colorbox\n'\
                                        'set palette defined (0 "#ff0000", 1 "#f37a1e", 3 "#ffff00", 4 "#00ff00", 5 "#ffffff")\n'\
                                        'set palette negative\n'\
                                        'set cbrange [0:100]\n'\
                                        'set cblabel \'percentage of peers within ' + re.sub('_0.\.gp', '', self.script) + '\'\n'\
                                        'set cbtics(0,10,20,30,40,50,60,70,80,90,100)\n\n'\
                                        'plot   ')

                        i = 0
                        for c in countries.iteritems():
                                if i < len(countries) - 1:
                                        f.write ('dir' + '.\'' + c[0] + '\' index 0 t \'\' w filledcurves lc palette cb ' + str(c[1]) + ' , dir.\''+ c[0] + '\' index 1 t \'\' w l lw 1 lt 1 lc rgb  \'black\',\\\n')
                                else:
                                        f.write ('dir' + '.\'' + c[0] + '\' index 0 t \'\' w filledcurves lc palette cb ' + str(c[1]) + ' , dir.\''+ c[0] + '\' index 1 t \'\' w l lw 1 lt 1 lc rgb  \'black\'')

                                i = i + 1
                        f.close()

        def countryCenter(self, country):
                script_stripped = re.search('0._(.*)\.gp', self.script).group(1)
                f = open(script_stripped + '/countries/' + country, 'r')
                i = 0.0
                x = 0.0
                y = 0.0
                for row, line in enumerate(f):
                                i = i + 1
                                line = line.rstrip('\n')
                                coordinates = line.split()
                                # if the coordinates is empty means that
                                # it encountered an empty line, so it finished
                                if len(coordinates) == 0:
                                        break
                                else:
                                        x = x + float(coordinates[0])
                                        y = y + float(coordinates[1])
                x = x / i
                y = y /i
                v = [x, y]
                return v


        def __init__(self, script):
                self.script = script


if __name__ == "__main__":

        geodata = GeoData('../31_geoip/geoip.peer.TOT.DATA')
        if geodata.acquireData() == False:
                #sys.stderr.write('postprocess.py in geoip says: Warning, geodata is empty\n')
                sys.exit()

        percentage = geodata.percentageWorld()

        # create an object for every continent with relative information
        africa = Continent('africa',percentage[0], './africa/polygons/', 17, 13)
        asia = Continent('asia', percentage[1], './asia/polygons/', 80, 45)
        europe = Continent('europe', percentage[2], './europe/polygons/', 20, 50,)
        north_america = Continent('north_america', percentage[3], './north_america/polygons/', -100, 50)
        oceania = Continent('oceania', percentage[4], './oceania/polygons/', 140, -25)
        south_america = Continent('south_america', percentage[5], './south_america/polygons/', -60, -10)
        script = Script('01_world.gp', geodata.total_peers, geodata.unknown_peers)
        script.create()

        if os.getuid() == 0:
                os.chmod('01_world.gp', stat.S_IRWXO)

        africa_countries = africa.getCountries()
        africa_countries = geodata.percentageContinent(africa_countries, 1)
        c = ScriptC('05_africa.gp')
        c.create(geodata.continents[0], geodata.total_peers, -21, 63, -35, 38, africa_countries,'./africa/countries/')

        if os.getuid() == 0:
                os.chmod('05_africa.gp', stat.S_IRWXO)

        asia_countries = asia.getCountries()
        asia_countries = geodata.percentageContinent(asia_countries, 2)
        c = ScriptC('04_asia.gp')
        c.create(geodata.continents[1], geodata.total_peers, 25, 180, 0, 80, asia_countries,'./asia/countries/')
        if os.getuid() == 0:
                os.chmod('04_asia.gp', stat.S_IRWXO)

        europe_countries = europe.getCountries()
        europe_countries = geodata.percentageContinent(europe_countries, 3)
        c = ScriptC('02_europe.gp')
        c.create(geodata.continents[2], geodata.total_peers, -25, 41, 34, 72, europe_countries, './europe/countries/')
        if os.getuid() == 0:
                os.chmod('02_europe.gp', stat.S_IRWXO)

        n_america_countries = north_america.getCountries()
        n_america_countries = geodata.percentageContinent(n_america_countries, 4)
        c = ScriptC('03_north_america.gp')
        c.create(geodata.continents[3], geodata.total_peers, -140,-12, 14, 83.5, n_america_countries, './north_america/countries/')
        if os.getuid() == 0:
                os.chmod('03_north_america.gp', stat.S_IRWXO)

        oceania_countries = oceania.getCountries()
        oceania_countries = geodata.percentageContinent(oceania_countries, 5)
        c = ScriptC('06_oceania.gp')
        c.create(geodata.continents[4], geodata.total_peers, 113,179, -42, 0, oceania_countries, './oceania/countries/')
        if os.getuid() == 0:
                os.chmod('06_oceania.gp', stat.S_IRWXO)

        s_america_countries = south_america.getCountries()
        s_america_countries = geodata.percentageContinent(s_america_countries, 6)
        c = ScriptC('07_south_america.gp')
        c.create(geodata.continents[5], geodata.total_peers, -83,-34, -56, 13, s_america_countries, './south_america/countries/')
        if os.getuid() == 0:
                os.chmod('07_south_america.gp', stat.S_IRWXO)
