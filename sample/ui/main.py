#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets
import UIManager as uim

if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    mainWindow = uim.UIManager()
    mainWindow.main()
    sys.exit(app.exec_())
