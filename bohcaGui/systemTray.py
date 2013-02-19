import sys, os
from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QSystemTrayIcon
import subprocess
from File_Notify import *
from FileTranslate.handler import *

project_path = os.getenv('HOME')+'/bohca'
icon_path="/icons/Flock_icon.png"




class SystemTrayIcon(QtGui.QSystemTrayIcon):

    def __init__(self, icon , parent = None ):

        QtGui.QSystemTrayIcon.__init__(self, icon, parent)
        menu = QtGui.QMenu(parent)
        
        #menuye bir action eklendi
        exitAction = menu.addAction("Exit System")
        exitAction.activated.connect(self.close)
       
       
        self.setContextMenu(menu)

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
    file = "/home/mehtap/bohca/bohcaGui/File_Notify.py" 
    subprocess.call(["python",file]) 
    sys.exit(app.exec_())

if __name__ == '__main__':
     main()



