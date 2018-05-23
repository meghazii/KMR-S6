# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qtDesigner/mainProg.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(944, 622)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 49, 921, 281))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textBrowser = QtWidgets.QTextBrowser(self.verticalLayoutWidget)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(430, 490, 511, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.previousButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.previousButton.setObjectName("previousButton")
        self.horizontalLayout.addWidget(self.previousButton)
        self.nextButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.nextButton.setObjectName("nextButton")
        self.horizontalLayout.addWidget(self.nextButton)
        self.leaveButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.leaveButton.setObjectName("leaveButton")
        self.horizontalLayout.addWidget(self.leaveButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 944, 25))
        self.menubar.setObjectName("menubar")
        self.menuFichier = QtWidgets.QMenu(self.menubar)
        self.menuFichier.setObjectName("menuFichier")
        self.menuOutils = QtWidgets.QMenu(self.menubar)
        self.menuOutils.setObjectName("menuOutils")
        self.menuA_Propos = QtWidgets.QMenu(self.menubar)
        self.menuA_Propos.setObjectName("menuA_Propos")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionRun = QtWidgets.QAction(MainWindow)
        self.actionRun.setObjectName("actionRun")
        self.actionQuitter = QtWidgets.QAction(MainWindow)
        self.actionQuitter.setObjectName("actionQuitter")
        self.actionPas_pas = QtWidgets.QAction(MainWindow)
        self.actionPas_pas.setObjectName("actionPas_pas")
        self.menuFichier.addSeparator()
        self.menuFichier.addAction(self.actionRun)
        self.menuFichier.addSeparator()
        self.menuFichier.addAction(self.actionPas_pas)
        self.menuFichier.addSeparator()
        self.menuFichier.addAction(self.actionQuitter)
        self.menubar.addAction(self.menuFichier.menuAction())
        self.menubar.addAction(self.menuOutils.menuAction())
        self.menubar.addAction(self.menuA_Propos.menuAction())

        self.retranslateUi(MainWindow)
        self.leaveButton.clicked.connect(MainWindow.close)
        self.nextButton.clicked.connect(MainWindow.doItWhenNextIsPressed)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Cantarell\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600; font-style:italic;\">Lorem Ipsum about l\'extraction de motif</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.previousButton.setText(_translate("MainWindow", "Précédent"))
        self.nextButton.setText(_translate("MainWindow", "Suivant"))
        self.leaveButton.setText(_translate("MainWindow", "Quitter"))
        self.menuFichier.setTitle(_translate("MainWindow", "Fichier"))
        self.menuOutils.setTitle(_translate("MainWindow", "Outils"))
        self.menuA_Propos.setTitle(_translate("MainWindow", "A Propos"))
        self.actionRun.setText(_translate("MainWindow", "Exécuter"))
        self.actionQuitter.setText(_translate("MainWindow", "Quitter"))
        self.actionPas_pas.setText(_translate("MainWindow", "Pas à pas"))

    def doItWhenNextIsPressed(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.nextButton.setText(_translate("MainWindow", "Oui"))
