#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui
from mainwindow import MainWindow

def main():
    app = QtGui.QApplication(sys.argv)

    mainWindow = MainWindow()
    mainWindow.show()

    return app.exec_()

if __name__ == "__main__":
    main()
