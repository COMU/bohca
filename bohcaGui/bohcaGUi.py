import sys, os
from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QSystemTrayIcon
#import Settpro
import File_Notify

#project_path = os.environ('HOME')
#print project_path
#icon_path = project_path + '/bohca' 
project_home_dir = "/home/mehtap/bohca"
log_file = project_home_dir + "/bohca.log"
log_file_copy = project_home_dir + "/bohcacopy.log"
icon_path= project_home_dir + "/icons/Flock_icon.png"
workspace_path = "/home/mehtap/Desktop/bohca/"
BASEDIR = "/home/mehtap/Desktop/bohca/"



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
      


if __name__ == '__main__':
     main()


