#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import os
sys.path.append(os.path.abspath
                ("/home/imran/Workspace/git-project/KMR-S6/sample/ui/"))
from PyQt5.QtWidgets import QApplication
from display import Window
from test import Ui_Dialog

if __name__ == '__main__':

    app = QApplication(sys.argv)
    # mainWindow = Window()
    a = Ui_Dialog()
    sys.exit(app.exec_())
