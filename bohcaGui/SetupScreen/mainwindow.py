#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4 import QtCore
from PyQt4 import QtGui
from ui_mainwindow import Ui_MainWindow
import subprocess

class MainWindow(QtGui.QMainWindow, Ui_MainWindow):
	def __init__(self):
        	QtGui.QMainWindow.__init__(self)
        	self.setupUi(self)

	@QtCore.pyqtSignature("bool")
        def on_pushButton_2_clicked(self):
                QtGui.QMessageBox.warning(self,u"Attention",u"Are you sure want to exit the program ?",u"Yes", u"Cancel",0 ,2)
