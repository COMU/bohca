import sys
import os
import time
import logging
import subprocess
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QDialog, QApplication, QPushButton, QLineEdit, QFormLayout,QSystemTrayIcon


class SystemTrayIcon(QtGui.QSystemTrayIcon):

    def __init__(self, icon, parent=None):
        QtGui.QSystemTrayIcon.__init__(self, icon, parent)
        menu = QtGui.QMenu(parent)
        exitAction = menu.addAction("Exit System")
        exitAction.activated.connect(self.close)
        changeFileAction=menu.addAction("Show Changed files")
        changeFileAction.activated.connect(self.showChange)
        showFilesAction=menu.addAction("Show All Files")
        showFilesAction.activated.connect(self.showFiles)
        self.setContextMenu(menu)
    def showChange(self):
        changed= logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s - %(message)s',
                            datefmt='%Y-%m-%d %H:%M:%S')
        reply = QtGui.QMessageBox.question(self, 'Message',
           "Are you sure to quit?", QtGui.QMessageBox.Yes | 
           QtGui.QMessageBox.No, QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
              event.accept()
        else:
              event.ignore()  
       

        path = sys.argv[1] if len(sys.argv) > 1 else '.'
        event_handler = LoggingEventHandler()
        observer = Observer()
        observer.schedule(event_handler, path, recursive=True)
        observer.start()


        try:
             while True:
                 time.sleep(1)
               
        except KeyboardInterrupt:
            observer.stop()
        observer.join()
    def showFiles(self):
        
        if sys.platform == 'linux2':
  
                     os.system("xdg-open /home/mehtap/Desktop/bohca/")
        else:
                     os.startfile("/home/mehtap/Dekstop/bohca/")

    def close(self):
      
        sys.exit()
def main():
    app = QtGui.QApplication(sys.argv)

    w = QtGui.QWidget()
    trayIcon = SystemTrayIcon(QtGui.QIcon('Flock_icon.png'), w)
  
    trayIcon.show()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()
