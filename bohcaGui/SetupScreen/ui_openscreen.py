# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'OpenScreen.ui'
#
# Created: Thu Feb  7 13:06:08 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys, os
#from ui_mainwindow import * 

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

default_path = os.getenv('HOME')+'/Bohca'


	        

class Ui_MainWindow(QtGui.QMainWindow):
   
         
     def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.setObjectName(_fromUtf8("MainWindow"))
        self.resize(612, 473)
        self.centralwidget = QtGui.QWidget(self)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(342, 130, 201, 27))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(340, 190, 201, 27))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 171, 151))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8("../../icons/Icon_Large_or_Small.png")))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(220, 130, 111, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(220, 190, 101, 21))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(310, 360, 98, 27))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../icons/gif_47_089.gif")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(460, 360, 98, 27))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("../../icons/gif_47_023.gif")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(250, 40, 261, 31))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(240, 260, 311, 20))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 612, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(self)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        self.setStatusBar(self.statusbar)

        self.retranslateUi(self)
	
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.close)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.check)
        QtCore.QMetaObject.connectSlotsByName(self)

     def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">User Name :</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Password :</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("MainWindow", "Next ->", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("MainWindow", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p><span style=\" font-size:22pt; font-weight:600;\">Welcome To Bohca</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p><span style=\" color:#ff0000;\">  Please enter your user name and password !</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
     def check(self):
		
		user_name = str(ui.lineEdit.text())
		user_password = str(ui.lineEdit_2.text())
		if user_name == "" or user_name == " ":  # Checked whether user name is empty
			ui.label_5.setText("<html><head/><body><p><span style=\" color:#ff0000;\">  You must filling fields !</span></p></body></html>")

		# in addition to we must compare user name and password in here !!

		if user_password == "" or user_password == " ": # Checked whether user password is empty
			ui.label_5.setText("<html><head/><body><p><span style=\" color:#ff0000;\">  You must filling fields !</span></p></body></html>")
		else:
			ui.label_5.setText("")
 #               next_object.path()
               # next_object = SelectPath()
                self.new_open()
                self.close()
     def new_open(self):
                self.new = Ui_MainWindow2()
                self.new.show()                  

        
 




                                
               
class Ui_MainWindow2(QtGui.QMainWindow):
    def __init__(self):
        super(Ui_MainWindow2,self).__init__()

        self.setObjectName(_fromUtf8("MainWindow"))
        self.resize(602, 339)
        self.centralwidget = QtGui.QWidget(self)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(310, 240, 98, 27))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icons/gif_47_089.gif")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(440, 240, 98, 27))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("icons/gif_47_023.gif")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, 130, 91, 31))
        self.label.setObjectName(_fromUtf8("label"))
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(280, 130, 271, 27))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 0, 171, 151))
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setPixmap(QtGui.QPixmap(_fromUtf8("Icon_Large_or_Small.png")))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(260, 40, 261, 51))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 602, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(self)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        self.setStatusBar(self.statusbar)

        self.retranslateUi(self)
        QtCore.QObject.connect(self.lineEdit, QtCore.SIGNAL(_fromUtf8("returnPressed()")), self.pushButton.click)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.close)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.path)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("MainWindow", "Next ->", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("MainWindow", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Current Path:</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Welcome to Bohca", None, QtGui.QApplication.UnicodeUTF8))

    def path(self):
                self.lineEdit.setText(default_path)

                path = str(self.lineEdit.text())
                self.lineEdit.clear()
                if path == "":
                        if sys.platform == 'linux2':
                                file_path = default_path
                                if os.path.isdir(file_path):
                                        subprocess.call(["xdg-open", file_path])
                                else:
                                        os.mkdir(file_path)
                                        subprocess.call(["xdg-open", file_path])
                        else:
                                os.startfile(file_path)
                else:
                        if sys.platform == 'linux2':
                                file_path = path
                                if os.path.isdir(file_path):
                                        subprocess.call(["xdg-open", file_path])
                                else:
                                        os.mkdir(file_path)
                                        subprocess.call(["xdg-open", file_path])
                        else:
                                os.startfile(file_path)





app = QtGui.QApplication(sys.argv)
ui = Ui_MainWindow()
ui.show()
sys.exit(app.exec_())
