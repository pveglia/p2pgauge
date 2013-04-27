"""This file defines a class which is the widget displaying the images
in the tabs"""

from PyQt4 import QtCore, QtGui
import FigureWidget
import glob
import os
import re

gnuplot_terminal = 'png'
gnuplot_terminal_opts = 'large'

class SingleFigure (QtGui.QWidget):
	"""This widget simply draws a pixmap"""

	def __init__(self, filename = "", parent = None):
		"Constructor"
		QtGui.QWidget.__init__(self, parent)
		self.pixmap = QtGui.QPixmap(filename)
		self.filename = filename;
		self.offset = QtCore.QPoint()

	def update(self):
		self.pixmap.load(self.filename)
		size = self.pixmap.size()
		self.resize(size)

	def setFile(self, filename):
		"set the name of the file which contains our images"
		self.filename = filename
		self.update()

	def paintEvent(self, event):
		"the event which paints the pixmap"
		painter = QtGui.QPainter(self)
		self.update()
		#painter.fillRect(self.rect(), QtCore.Qt.black)
		painter.drawPixmap(self.rect(), self.pixmap)
	
class ShowCaseWidget(QtGui.QWidget):
	"""Draw the show case mode"""

	confs = { 1: (1, 1),
	  2: (2, 1),
	  3: (3, 1),
	  4: (2, 2),
	  5: (2, 3),
	  6: (2, 3),
	  7: (2, 4)
	}

	suffix = '.tmb.png'

	def __init__(self, figure_view, stacked_widget, parent = None):
		"Constructor"
		QtGui.QWidget.__init__(self, parent)
		self.fw = figure_view
		self.sw = stacked_widget
		self.n = stacked_widget.count()

		self.make_mapping()
		self.calc_size(self.width(), self.height())
		self.make_rects(*self.size)
		self.make_pixmaps()

	def make_thumbnails(self):
		"this fuctions calls convert to build the thumbnails from png"
		for f in self.filenames:
			size =  "%dx%d!" % self.size
			cmd = "convert -resize %s %s %s" % (size, f, f + self.suffix)
			os.spawnl(os.P_WAIT, "/usr/bin/convert", 
				*cmd.split())

	def make_pixmaps(self):
		"create the pixmaps qt objects used to paint the figures"
		self.pixmaps = []

		self.filenames = [self.sw.widget(i).filename for i in range(self.n)]
		self.make_thumbnails()
		self.pixmaps = [QtGui.QPixmap(f + self.suffix) for f in self.filenames]

	def make_mapping(self):
		"calculates the number of rows and columns"

		if self.n in self.confs:
			self.row, self.col = self.confs[self.n]
		else:
			print >>sys.stderr, \
				"number of widgets for showcase unknown. guessing"
			self.row = 3 
			self.col = self.n / 3
			if self.row * self.col != self.n:
				self.col += 1

	def make_rects(self, w, h, border = 5):
		"make the qt rect objects used to paint the figures"

		res = []
		for row in range(self.row):
			for col in range(self.col):
				r = QtCore.QRect(
					col * (w + border), row * (h + border), #top left corner
					w, h) #size
				res.append(r)

		self.rects = res

	def calc_size(self, w, h, border = 5):
		"calculates the thumbnails size"
		w = (w - (self.col - 1)*border) / self.col
		h = (h - (self.row - 1)*border) / self.row
		
		self.size = (w, h)

	def update(self):
		"rebuild the thumbnails and the pixmaps"
		self.make_thumbnails()
		for p, f in zip(self.pixmaps, self.filenames):
			p.load(f + self.suffix)

	def paintEvent(self, event):
		self.update()
		painter = QtGui.QPainter(self)

		for r, p in zip(self.rects, self.pixmaps):
			painter.drawPixmap(r, p)

	def mouseDoubleClickEvent(self, event):
		point = event.pos()

		for num, rect in enumerate(self.rects):
			if rect.contains(point):
				break

		row = num / self.row
		col = num / self.col
		index = row * self.col + col

		self.fw.setCurrentIndex(index)

class FigureView(QtGui.QWidget):
	"""The widget display the images in the tabs"""

	def listFiguresInDir(self):
		"return the list of png in the current directory"
		res = glob.glob(self.path + "/*." + gnuplot_terminal)
		return [x for x in res if x.find(ShowCaseWidget.suffix) == -1]

	def __init__(self, dir, subdir, parent = None, checkBox = False, gplotWidg = None):
		"""Constructor
		
		Takes the directory in which to find files to be represented"""

		QtGui.QWidget.__init__(self, parent)

		self.dir = dir
		self.subdir = subdir
		self.path = dir + "/" + subdir
		self.ui = FigureWidget.Ui_FigureWidget()
		self.ui.setupUi(self)
		self.gplotWidg = gplotWidg

		for i in range(self.ui.figureStack.count()):
			cw = self.ui.figureStack.currentWidget()
			self.ui.figureStack.removeWidget(cw)

		self.updateDescription()

		self.figures = []
		#remove current figures rather than initialize them
		files = self.listFiguresInDir()

		if checkBox == True:
			self.addCheckBox()
		self.showcase = None

	def addCheckBox(self):
		self.ui.groupBox1 = QtGui.QGroupBox(self)
		self.ui.groupBox1.setObjectName("groupBox1")
		self.ui.horizontalLayout1 = QtGui.QHBoxLayout(self.ui.groupBox1)
		self.ui.horizontalLayout1.setObjectName("horizontalLayout1")
		self.ui.time_label = QtGui.QLabel("Time:", self.ui.groupBox1)
		self.ui.horizontalLayout1.addWidget(self.ui.time_label)
		self.ui.t0 = QtGui.QCheckBox(self.ui.groupBox1)
		self.ui.t0.setObjectName("t0")
		self.ui.t0.setText("Since t0")
		self.ui.t0.setChecked(True)
		self.connect(self.ui.t0, QtCore.SIGNAL("stateChanged(int)"), self.gplotWidg.updateFigures)
		self.ui.horizontalLayout1.addWidget(self.ui.t0)
		self.ui.lastdt = QtGui.QCheckBox(self.ui.groupBox1)
		self.ui.lastdt.setObjectName("lastdt")
		self.ui.lastdt.setText("Last dT")
		self.connect(self.ui.lastdt, QtCore.SIGNAL("stateChanged(int)"), self.gplotWidg.updateFigures)
		self.ui.horizontalLayout1.addWidget(self.ui.lastdt)
		self.ui.vboxlayout.addWidget(self.ui.groupBox1)	

		self.ui.groupBox2 = QtGui.QGroupBox(self)
		self.ui.groupBox2.setObjectName("groupBox2")
		self.ui.horizontalLayout2 = QtGui.QHBoxLayout(self.ui.groupBox2)
		self.ui.horizontalLayout2.setObjectName("horizontalLayout2")
		self.ui.bytes_label = QtGui.QLabel("Bytes:", self.ui.groupBox2)
		self.ui.horizontalLayout2.addWidget(self.ui.bytes_label)
		self.ui.tot = QtGui.QCheckBox(self.ui.groupBox2)
		self.ui.tot.setObjectName("tot")
		self.ui.tot.setText("All")
		self.connect(self.ui.tot, QtCore.SIGNAL("stateChanged(int)"), self.gplotWidg.updateFigures)
		self.ui.horizontalLayout2.addWidget(self.ui.tot)
		self.ui.sent = QtGui.QCheckBox(self.ui.groupBox2)
		self.ui.sent.setObjectName("sent")
		self.ui.sent.setText("Transmitted")
		self.ui.sent.setChecked(True)
		self.ui.horizontalLayout2.addWidget(self.ui.sent)
		self.ui.rec = QtGui.QCheckBox(self.ui.groupBox2)
		self.ui.rec.setObjectName("rec")
		self.ui.rec.setText("Received")
		self.ui.rec.setChecked(True)
		self.ui.horizontalLayout2.addWidget(self.ui.rec)
		self.ui.vboxlayout.addWidget(self.ui.groupBox2)	



	def updateDescription(self):
		#set the description
		try:
			file = open(self.path + "/description.txt", "r")
			#file = open(self.path + "/title.tab", "r")
			description = file.readline().rstrip('\n')
			self.ui.figureTitle.setText(description)
			file.close()
		except IOError:
			print "%s: Description file not found" % self.path

	def setCurrentIndex(self, index):
		"set the index of the displayed figures"
		self.ui.figureStack.setCurrentIndex(index)

		if self.showcase and \
		   self.ui.figureStack.currentWidget() != self.showcase:
			self.ui.figureStack.removeWidget(self.showcase)
			self.showcase = None

		self.update_label()

	def update_label(self):
		"update the label displaying the current figure index"

		if self.showcase:
			self.ui.figureNumber.setText("")
			return

		index = self.ui.figureStack.currentIndex()
		count = self.ui.figureStack.count()
		self.ui.figureNumber.setText("%d/%d" % (index + 1, len(self.figures)))

	def initialize_figures(self):
		"get figures from associated directory"
		#print self.path + "/*." + gnuplot_terminal
		files = self.listFiguresInDir()
		files.sort()
		#files.reverse()

		for f in files:
			#print "adding figure %s" % (f)
			self.add_figure(f)

		self.update_label()
		self.updateDescription()

	def keyPressEvent(self, event):
		"If pageUp or pageDown change current figure"

		fs = self.ui.figureStack
		i = fs.currentIndex()
		key = event.key()

		if self.showcase:
			fs.removeWidget(self.showcase)
			self.showcase = None

		if key == QtCore.Qt.Key_PageDown or key == QtCore.Qt.Key_Down:
			if i < (len(self.figures) - 1):
				self.setCurrentIndex(i + 1)
		elif key == QtCore.Qt.Key_PageUp or key == QtCore.Qt.Key_Up:
			if i > 0:
				self.setCurrentIndex(i - 1)
		elif key == QtCore.Qt.Key_End:
			self.showcase = ShowCaseWidget(self, fs)
			index = fs.addWidget(self.showcase)
			self.setCurrentIndex(index) 
		else:
			event.ignore()
			return

		event.accept()
		

	def add_figure(self, filename):
		"""add a figure to this widget"""

		#if we already have the file do nothing
		if filename in (x for x, y in self.figures):
			return

		new_fig = SingleFigure(filename)

		regexp = re.compile("_(\d\d).%s" % gnuplot_terminal)
		res = regexp.search(filename) 
		if res:
			newn = int( res.groups()[0] )
		else:
			newn = len(self.figures)

		c = 0
		for (f, n) in self.figures:
			if newn < n:
				break
			c = c + 1
		
		self.figures.insert(c, (filename, newn))

		self.ui.figureStack.insertWidget(c, new_fig)
