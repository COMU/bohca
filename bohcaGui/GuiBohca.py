import sys, os
import pynotify
from PyQt4 import QtGui,QtCore
from PyQt4.QtGui import QSystemTrayIcon
import logging
import time
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler



project_home_dir = "/home/mehtap/bohca"
log_file = project_home_dir + "/bohca.log"
icon_path= project_home_dir + "/icons/Flock_icon.png"
workspace_path = "/home/mehtap/Desktop/bohca/"

class SystemTrayIcon(QtGui.QSystemTrayIcon):
    def __init__(self, icon , parent = None ):
        
        QtGui.QSystemTrayIcon.__init__(self, icon, parent)
        menu = QtGui.QMenu(parent)
        exitAction = menu.addAction("Exit System")
        exitAction.activated.connect(self.close)

        self.setContextMenu(menu)
      
    def close(self):
        sys.exit()

 
def Notification():
        
    logging.basicConfig(filename = log_file ,level = logging.INFO,
                           format = '%(asctime)s - %(message)s-',
                           datefmt = '%Y-%m-%d %H:%M:%S' )
    
    event_handler = LoggingEventHandler()
    observer = Observer()
    observer.schedule(event_handler, workspace_path , recursive=True)
    observer.start()
    try:
       while True:
         time.sleep(1)
         file = open ( log_file, "r" )
         loglines = file.readlines()
  

         loglines_without_swp = []


         for line in loglines:
             if line.split("\n")[0][-4:] == "swp-":
                 pass
             else :
                 loglines_without_swp.append(line.split("\n")[0])
         print loglines_without_swp
         notification = loglines_without_swp[-1].split(" ", 3)[-1]
         pynotify.init("uyari mesaji")
         msg = pynotify.Notification (notification)

         msg.show()

    except KeyboardInterrupt:
            observer.stop()
            observer.join()
#    file = open ( log_file, "r" )
#    loglines = file.readlines()
#    loglines_without_swp = []
#    
#     
#    for line in loglines:
#        if line.split("\n")[0][-4:] == "swp-":
#            pass
#        else :
#            loglines_without_swp.append(line.split("\n")[0])
#    print loglines_without_swp
#    notification = loglines_without_swp[-1].split(" ", 3)[-1] 
#    pynotify.init("uyari mesaji")
#    msg = pynotify.Notification (notification)
#    
#    msg.show()


def main():
   #uygulama icin widget olusturma
   app = QtGui.QApplication(sys.argv)
   app_widget = QtGui.QWidget()
   #trayicona bir simge verme
   trayIcon = SystemTrayIcon(QtGui.QIcon(icon_path),app_widget)
   trayIcon.show() 
   Notification()
   #trayIcon.show()
   sys.exit(app.exec_())
   
if __name__ == '__main__':
     main()
