# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qtDesigner/algoWindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AlgoWindow(object):
    def setupUi(self, AlgoWindow):
        AlgoWindow.setObjectName("AlgoWindow")
        AlgoWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(AlgoWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout.addItem(spacerItem)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        AlgoWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AlgoWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName("menubar")
        self.menuFichier = QtWidgets.QMenu(self.menubar)
        self.menuFichier.setObjectName("menuFichier")
        self.menuOutils = QtWidgets.QMenu(self.menubar)
        self.menuOutils.setObjectName("menuOutils")
        self.menuA_propos = QtWidgets.QMenu(self.menubar)
        self.menuA_propos.setObjectName("menuA_propos")
        AlgoWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AlgoWindow)
        self.statusbar.setObjectName("statusbar")
        AlgoWindow.setStatusBar(self.statusbar)
        self.actionAccueil = QtWidgets.QAction(AlgoWindow)
        self.actionAccueil.setObjectName("actionAccueil")
        self.actionQuitter = QtWidgets.QAction(AlgoWindow)
        self.actionQuitter.setObjectName("actionQuitter")
        self.menuFichier.addAction(self.actionAccueil)
        self.menuFichier.addAction(self.actionQuitter)
        self.menubar.addAction(self.menuFichier.menuAction())
        self.menubar.addAction(self.menuOutils.menuAction())
        self.menubar.addAction(self.menuA_propos.menuAction())

        self.retranslateUi(AlgoWindow)
        QtCore.QMetaObject.connectSlotsByName(AlgoWindow)

    def retranslateUi(self, AlgoWindow):
        _translate = QtCore.QCoreApplication.translate
        AlgoWindow.setWindowTitle(_translate("AlgoWindow", "MainWindow"))
        self.label.setText(_translate("AlgoWindow", "Algorithme naif"))
        self.label_2.setText(_translate("AlgoWindow", "Algorithme KMR"))
        self.menuFichier.setTitle(_translate("AlgoWindow", "Fichier"))
        self.menuOutils.setTitle(_translate("AlgoWindow", "Outils"))
        self.menuA_propos.setTitle(_translate("AlgoWindow", "A propos"))
        self.actionAccueil.setText(_translate("AlgoWindow", "Accueil"))
        self.actionQuitter.setText(_translate("AlgoWindow", "Quitter"))

