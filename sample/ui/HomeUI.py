# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../qtDesigner/homeWindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets


class HomeUI(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(HomeUI, self).__init__(parent)
        self.setObjectName("MainWindow")
        self.resize(867, 584)

        self.central_widget = QtWidgets.QStackedWidget()
        self.setCentralWidget(self.central_widget)

        start_widget = StartingWidget(self)
        start_widget.startButton.clicked.connect(self.launch)

        self.central_widget.addWidget(start_widget)

    def launch(self):
        launchWidget = LaunchedWidget(self)
        self.central_widget.addWidget(launchWidget)
        self.central_widget.setCurrentWidget(launchWidget)


class StartingWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(StartingWidget, self).__init__(parent)

        layout = QtWidgets.QVBoxLayout()

        self.introWidget = QtWidgets.QLabel()
        self.introWidget.setObjectName("label")
        self.introWidget.setText('Salut les amis')
        # spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        h_layout = QtWidgets.QHBoxLayout()
        self.naifCheckBox = QtWidgets.QCheckBox()
        self.naifCheckBox.setText('Algorithme naif')
        self.kmrCheckBox = QtWidgets.QCheckBox()
        self.kmrCheckBox.setText('Algorithme KMR')
        h2_layout = QtWidgets.QHBoxLayout()
        self.startButton = QtWidgets.QPushButton('Commencer')
        self.quitButton = QtWidgets.QPushButton('Quitter')

        layout.addWidget(self.introWidget)
        # layout.addWidget(spacerItem1)
        h_layout.addWidget(self.naifCheckBox)
        h_layout.addWidget(self.kmrCheckBox)
        layout.addLayout(h_layout)
        h2_layout.addWidget(self.startButton)
        h2_layout.addWidget(self.quitButton)
        layout.addLayout(h2_layout)

        self.setLayout(layout)
        # you might want to do self.button.click.connect(self.parent().login)


class LaunchedWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(LaunchedWidget, self).__init__(parent)
        layout = QtWidgets.QHBoxLayout()
        self.label = QtWidgets.QLabel('Lancement')
        layout.addWidget(self.label)
        self.setLayout(layout)
