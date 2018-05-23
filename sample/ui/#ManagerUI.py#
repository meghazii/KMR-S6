# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets
import HomeUI as homeui
import AlgoUI as algoui


class ManagerUI(object):
    def __init__(self):
        super(ManagerUI, self).__init__()
        self.frame = []

    def start(self):
        self.homeFrame = homeui.HomeUI()
        self.homeFrame.start()
        self.frame.append(self.homeFrame)
        self.showAll()

    def addHome(self):
        self.frame.append(homeui.HomeUI())

    def addAlgo(self):
        self.frame.append(algoui.AlgoUI())

    def showAll(self):
        for i in self.frame:
            i.show()


class AlgoUI(QtWidgets.QMainWindow, algoui.Ui_AlgoWindow):
    def __init__(self, parent=None):
        super(AlgoUI, self).__init__(parent)
        self.setupUi(self)

    def main(self):
        self.show()
