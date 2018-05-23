# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets
import MainWindowUI as ui


class ManagerUI(QtWidgets.QMainWindow, ui.Ui_MainWindow):
    def __init__(self, parent=None):
        super(ManagerUI, self).__init__(parent)
        self.setupUi(self)

    def main(self):
        self.show()
