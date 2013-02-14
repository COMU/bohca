#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4 import QtCore
from PyQt4 import QtGui
from ui_openscreen import Ui_MainWindow
from ui_SetupS import Ui_Dialog


class OtherScreen(QtGui.QDialog, Ui_Dialog):
      	def __init__(self):
		QtGui.QDialog.__init__(self)
		self.setupUi(self)
 
class MainWindow(QtGui.QMainWindow, Ui_MainWindow):
        def __init__(self):
                QtGui.QMainWindow.__init__(self)
                self.setupUi(self)
                self.otherscreen  = OtherScreen()

        @QtCore.pyqtSignature("bool")
        def on_pushButton_clicked(self):
                self.otherscreen.exec_()


