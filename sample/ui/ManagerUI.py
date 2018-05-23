# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets
import UIMainWindow as ui


class UIManager(QtWidgets.QMainWindow, ui.Ui_MainWindow):
    def __init__(self, parent=None):
        super(UIManager, self).__init__(parent)
        self.setupUi(self)

    def main(self):
        self.show()
