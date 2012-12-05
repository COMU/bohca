import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QDialog, QApplication, QPushButton, QLineEdit, QFormLayout,QSystemTrayIcon

class Example(QtGui.QWidget):
    def __init__(self):
            super(Example, self).__init__()
            self.initUI()

    def initUI(self):
        self.icon=QSystemTrayIcon()
        r=self.icon.isSystemTrayAvailable()
        print r
        self.icon.setIcon( QtGui.QIcon('/home/mehtap/Desktop/QT/icon/Flock_icon.png') )
        self.icon.show()
        self.icon.setVisible(True)
        self.setGeometry(300, 300, 250, 150)
        self.setWindowIcon(QtGui.QIcon('/home/mehtap/Desktop/QT/icon/Flock_icon.png'))
        #traySignal = "activated(QSystemTrayIcon::ActivationReason)"
       # traySignal="showDialog"
        #self.icon.connect(self.icon, QtCore.SIGNAL(traySignal), self.clicked) 
      # self.setWindowTitle('Message box')    
       # self.show()
        self.icon.activated.connect(self.showDialog)

       # self.show()

    def showDialog(self):
          fname = QtGui.QFileDialog.getOpenFileName(self, 'Open file',
                '/home')

    def closeEvent(self, event):


            reply = QtGui.QMessageBox.question(self, 'Message',"cikmak istediginizden emin misiniz?", QtGui.QMessageBox.Yes |
              QtGui.QMessageBox.No, QtGui.QMessageBox.No)

            if reply == QtGui.QMessageBox.Yes:
                     event.accept()
            else:
                     self.icon.show()

def main():

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

                                
