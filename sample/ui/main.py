#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets
import ManagerUI as uim

if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    m = uim.ManagerUI()
    m.start()
    sys.exit(app.exec_())
