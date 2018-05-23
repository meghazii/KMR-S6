# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets
import HomeUI as homeui
import AlgoUI as algoui


class ManagerUI(object):
    def __init__(self):
        super(ManagerUI, self).__init__()
        self.frame = []
        self.currFrame = 0

    def addHome(self):
        self.frame.append(homeui.HomeUI())

    def addAlgo(self):
        self.frame.append(AlgoUI())

    def showAll(self):
        for i in self.frame:
            i.show()


"""class HomeUI(QtWidgets.QMainWindow, homeui.HomeUI):
    def __init__(self, parent=None):
        super(HomeUI, self).__init__(parent)
        self.setupUi(self)

    def main(self):
        self.show()"""


class AlgoUI(QtWidgets.QMainWindow, algoui.Ui_AlgoWindow):
    def __init__(self, parent=None):
        super(AlgoUI, self).__init__(parent)
        self.setupUi(self)

    def main(self):
        self.show()
