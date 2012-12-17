import sys
import os
import time
import logging
import subprocess
import pynotify
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QDialog, QApplication, QPushButton, QLineEdit, QFormLayout,QSystemTrayIcon
#from PyQt4 import QtGui

class SystemTrayIcon(QtGui.QSystemTrayIcon):

    def __init__(self, icon, parent=None):
     
        QtGui.QSystemTrayIcon.__init__(self, icon, parent)
        menu = QtGui.QMenu(parent)
        exitAction = menu.addAction("Exit System")
        exitAction.activated.connect(self.close)
        changeFileAction=menu.addAction("Show Changed files")
        
        changeFileAction.activated.connect(self.showChange)
        #changeFileAction.activated.connect(self,"activated(QSystemTrayIcon::ActivationReason)",self._activateRoutine)  
        #show=menu.addAction("merhaba",self.changeFileAction)
        showFilesAction=menu.addAction("Show All Files")
        showFilesAction.activated.connect(self.showFiles)
        self.setContextMenu(menu)
   

       
       
    def showChange(self):
 
       changed= logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s - %(message)s',
                            datefmt='%Y-%m-%d %H:%M:%S')
      
       path="/home/mehtap/Desktop/bohca/"
       event_handler = LoggingEventHandler()
       observer = Observer()
       observer.schedule(event_handler, path, recursive=True)
       observer.start()
        

       try:
             while True:
                 time.sleep(1)
               # print "sleep"
       except KeyboardInterrupt:
            observer.stop()
            observer.join()
    def showFiles(self):
       if sys.platform == 'linux2':
  
                     os.system("xdg-open /home/mehtap/Desktop/bohca/")
       else:
                     os.startfile("/home/mehtap/Dekstop/bohca/")
    def close(self):
       # self.icon.RemoveIcon()
       # self.icon.Destroy()
        sys.exit()
def main():
    app = QtGui.QApplication(sys.argv)

    w = QtGui.QWidget()
    trayIcon = SystemTrayIcon(QtGui.QIcon('Flock_icon.png'), w)
   # notification = Notify.Notification.new ("Title", "some text here", trayIcon)
   # notification.show ()
   #trayIcon.activated.connect(self.showFiles)
   # import pynotify
    pynotify.init ("Hello world")
    changed="merhaba"
   # changed= logging.basicConfig(level=logging.INFO,
   #                         format='%(asctime)s - %(message)s',
   #                         datefmt='%Y-%m-%d %H:%M:%S')
   # path="/home/mehtap/Desktop/bohca/"
   # event_handler = LoggingEventHandler()
   # observer = Observer()
   # observer.schedule(event_handler, path, recursive=True)
   # observer.start()


   # try:
   #          while True:
   #              time.sleep(1)
   #            # print "sleep"
   # except KeyboardInterrupt:
   #         observer.stop()
   #         observer.join()

    Hello=pynotify.Notification ("Hello world!","This is an example notification.","dialog-information")
    Hello.show ()
    trayIcon.show()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    
      main()
