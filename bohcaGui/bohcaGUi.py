import sys, os
from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QSystemTrayIcon
import subprocess

project_path = os.getenv('HOME')+'/Bohca'
icon_path= project_path + "/icons/Flock_icon.png"




class SystemTrayIcon(QtGui.QSystemTrayIcon):

    def __init__(self, icon , parent = None ):

        QtGui.QSystemTrayIcon.__init__(self, icon, parent)
        menu = QtGui.QMenu(parent)
        
        #menuye bir action eklendi
        exitAction = menu.addAction("Exit System")
        exitAction.activated.connect(self.close)
       
       
        self.setContextMenu(menu)
        if sys.platform == 'linux2':
 
  	       file=project_path
               if os.path.isdir(file):
                  #  os.mkdir(file+"/icons")
                    subprocess.call(["xdg-open", file])
               else:
                    os.mkdir(file)
                    os.mkdir(file+"/icons")
                    subprocess.call(["xdg-open", file])
        else:
               os.startfile(file)

    #exit actioninin cagirdigi fonksiyon
    def close(self):
        sys.exit()


def main():
   
    #uygulama icin widget olusturma
    app = QtGui.QApplication(sys.argv)
    app_widget = QtGui.QWidget()


    #trayicona bir simge verme
    trayIcon = SystemTrayIcon(QtGui.QIcon(icon_path),app_widget)
    trayIcon.show() 
    print "a0" 
    sys.exit(app.exec_())

if __name__ == '__main__':
     main()


