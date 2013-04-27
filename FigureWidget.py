# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FigureWidget.ui'
#
# Created: Wed Jul 29 14:06:22 2009
#      by: PyQt4 UI code generator 4.4.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_FigureWidget(object):
    def setupUi(self, FigureWidget):
        FigureWidget.setObjectName("FigureWidget")
        FigureWidget.resize(658, 528)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(FigureWidget.sizePolicy().hasHeightForWidth())
        FigureWidget.setSizePolicy(sizePolicy)
        FigureWidget.setMinimumSize(QtCore.QSize(658, 528))
        FigureWidget.setMaximumSize(QtCore.QSize(10000, 10000))
        FigureWidget.setBaseSize(QtCore.QSize(658, 528))
        self.vboxlayout = QtGui.QVBoxLayout(FigureWidget)
        self.vboxlayout.setObjectName("vboxlayout")
        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setObjectName("hboxlayout")
        self.figureTitle = QtGui.QLabel(FigureWidget)
        self.figureTitle.setObjectName("figureTitle")
        self.hboxlayout.addWidget(self.figureTitle)
        self.figureNumber = QtGui.QLabel(FigureWidget)
        self.figureNumber.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.figureNumber.setObjectName("figureNumber")
        self.hboxlayout.addWidget(self.figureNumber)
        self.vboxlayout.addLayout(self.hboxlayout)
        self.line = QtGui.QFrame(FigureWidget)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.vboxlayout.addWidget(self.line)
        self.figureStack = QtGui.QStackedWidget(FigureWidget)
        self.figureStack.setMinimumSize(QtCore.QSize(640, 480))
        self.figureStack.setMaximumSize(QtCore.QSize(10000, 10000))
        self.figureStack.setObjectName("figureStack")
        self.page_3 = QtGui.QWidget()
        self.page_3.setObjectName("page_3")
        self.figureStack.addWidget(self.page_3)
        self.page_4 = QtGui.QWidget()
        self.page_4.setObjectName("page_4")
        self.figureStack.addWidget(self.page_4)
        self.vboxlayout.addWidget(self.figureStack)

        self.retranslateUi(FigureWidget)
        self.figureStack.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(FigureWidget)

    def retranslateUi(self, FigureWidget):
        FigureWidget.setWindowTitle(QtGui.QApplication.translate("FigureWidget", "FigureWidget", None, QtGui.QApplication.UnicodeUTF8))
        self.figureTitle.setText(QtGui.QApplication.translate("FigureWidget", "Titolo della figura", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    FigureWidget = QtGui.QWidget()
    ui = Ui_FigureWidget()
    ui.setupUi(FigureWidget)
    FigureWidget.show()
    sys.exit(app.exec_())

