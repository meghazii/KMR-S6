#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication
from display import (Window, Widget)

if __name__ == '__main__':

    app = QApplication(sys.argv)
    mainWindow = Window()
    sys.exit(app.exec_())
