# -*- coding: utf-8 -*-
import sys

sys.path.append("../algo/")

from NaifAlgo import NaifAlgo

from PyQt5 import QtCore, QtWidgets, QtGui


class HomeUI(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(HomeUI, self).__init__(parent)
        self.setObjectName("MainWindow")
        self.resize(867, 584)

        self.createAction()
        self.createToolbar()
        self.createMenubar()
        self.text = ''
        self.central_widget = QtWidgets.QStackedWidget()
        self.setCentralWidget(self.central_widget)

    def start(self):
        self.statusBar().showMessage('Prêt.')
        startWidget = StartingWidget(self)
        startWidget.startButton.clicked.connect(self.run)
        self.text = startWidget.myText
        print(startWidget.getText())
        self.central_widget.addWidget(startWidget)

    def home(self):
        self.statusBar().showMessage('Prêt.')
        homeWidget = StartingWidget(self)
        self.central_widget.addWidget(homeWidget)
        homeWidget.startButton.clicked.connect(self.ended)
        print(homeWidget.getText)
        self.text = homeWidget.myText
        self.central_widget.setCurrentWidget(homeWidget)

    def run(self):
        self.statusBar().showMessage('Traitement...')
        runWidget = RunningWidget(self)
        self.central_widget.addWidget(runWidget)
        self.central_widget.setCurrentWidget(runWidget)
        print(self.text)
        """algo = AlgoNaif(self.text)
        algo.completeExtraction(algo.getChaine())
        self.ended()"""

    def ended(self):
        self.statusBar().showMessage('Traitement terminé.')
        launchWidget = LaunchedWidget(self)
        self.central_widget.addWidget(launchWidget)
        self.central_widget.setCurrentWidget(launchWidget)

    def createAction(self):
        self.actionHome = QtWidgets.QAction(QtGui.QIcon('../../data/home.png'),
                                            '&Open', self)
        self.actionHome.setObjectName("actionHome")
        self.actionHome.setShortcut('Ctrl+H')
        self.actionHome.triggered.connect(self.home)

        self.actionOpen = QtWidgets.QAction(QtGui.QIcon('../../data/open.png'),
                                            '&Open', self)
        self.actionOpen.setObjectName("actionOpen")
        self.actionOpen.setShortcut('Ctrl+O')

        self.actionQuit = QtWidgets.QAction(QtGui.QIcon('../../data/exit.png'),
                                            '&Exit', self)
        self.actionQuit.setObjectName("actionQuitter")
        self.actionQuit.setShortcut('Ctrl+Q')
        self.actionQuit.triggered.connect(QtWidgets.qApp.quit)

        self.actionRun = QtWidgets.QAction(QtGui.QIcon('../../data/run.png'),
                                           '&Run', self)
        self.actionRun.setObjectName("actionRun")
        self.actionRun.setShortcut('Ctrl+R')
        self.actionRun.triggered.connect(self.run)

        self.actionAbout = QtWidgets.QAction(QtGui.QIcon
                                             ('../../data/about.png'),
                                             '&About', self)
        self.actionAbout.setObjectName("actionAbout")
        self.actionAbout.setShortcut('Ctrl+A')

    def toggleBar(self, state):
        if state:
            self.toolbar.toggleViewAction().trigger()
        else:
            self.toolbar.toggleViewAction().trigger()

    def createMenubar(self):
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 867, 25))
        self.menubar.setObjectName("menubar")

        self.menuFichier = QtWidgets.QMenu(self.menubar)
        self.menuFichier.setObjectName("menuFichier")
        self.menuOutils = QtWidgets.QMenu(self.menubar)
        self.menuOutils.setObjectName("menuOutils")
        self.menuA_Propos = QtWidgets.QMenu(self.menubar)
        self.menuA_Propos.setObjectName("menuA_Propos")

        self.setMenuBar(self.menubar)

        self.menuFichier.addSeparator()
        self.menuFichier.addAction(self.actionHome)
        self.menuFichier.addSeparator()
        self.menuFichier.addAction(self.actionOpen)
        self.menuFichier.addSeparator()
        self.menuFichier.addAction(self.actionQuit)
        self.menuFichier.addSeparator()

        self.menuOutils.addSeparator()
        self.menuOutils.addAction(self.actionRun)
        self.menuOutils.addSeparator()
        self.menuOutils.addAction(self.toolbarOn)
        self.menuOutils.addSeparator()

        self.menuA_Propos.addSeparator()
        self.menuA_Propos.addAction(self.actionAbout)
        self.menuA_Propos.addSeparator()

        self.menubar.addAction(self.menuFichier.menuAction())
        self.menubar.addAction(self.menuOutils.menuAction())
        self.menubar.addAction(self.menuA_Propos.menuAction())

        self.menuFichier.setTitle('Fichier')
        self.menuOutils.setTitle('Outils')
        self.menuA_Propos.setTitle('A Propos')
        self.actionHome.setText('Accueil')
        self.actionRun.setText('Exécuter')
        self.actionOpen.setText('Ouvrir')
        self.actionAbout.setText('A Propos')
        self.actionQuit.setText('Quitter')

    def createToolbar(self):
        self.toolbar = self.addToolBar('Home')
        self.toolbar.addAction(self.actionHome)
        self.toolbar = self.addToolBar('Open')
        self.toolbar.addAction(self.actionOpen)
        self.toolbar = self.addToolBar('Run')
        self.toolbar.addAction(self.actionRun)
        self.toolbar = self.addToolBar('About')
        self.toolbar.addAction(self.actionAbout)
        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(self.actionQuit)

        self.toolbarOn = QtWidgets.QAction('Barre d\'outils', self,
                                           checkable=True)
        self.toolbarOn.setChecked(False)
        self.toolbarOn.triggered.connect(self.toggleBar)


class StartingWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(StartingWidget, self).__init__(parent)

        layout = QtWidgets.QVBoxLayout()

        self.introWidget = QtWidgets.QLabel('Salut les amis')
        spacerItem1 = QtWidgets.QSpacerItem(40, 100, QtWidgets.QSizePolicy.
                                            Expanding, QtWidgets.QSizePolicy.
                                            Minimum)
        self.command = QtWidgets.QLabel('Inserer le texte à traiter dans le champ suivant : ')
        self.edit = QtWidgets.QTextEdit()
        self.saveButton = QtWidgets.QPushButton('Sauvergarder')
        self.saveButton.setEnabled(False)
        h2_layout = QtWidgets.QHBoxLayout()
        self.startButton = QtWidgets.QPushButton('Executer les deux algorithmes.')
        self.quitButton = QtWidgets.QPushButton('Quitter')

        self.myText = ''

        self.startButton.setEnabled(False)
        self.edit.textChanged.connect(self.canSave)
        self.saveButton.clicked.connect(self.saveTxt)

        layout.addWidget(self.introWidget)
        layout.addItem(spacerItem1)
        layout.addWidget(self.command)
        layout.addWidget(self.edit)
        layout.addWidget(self.saveButton)
        layout.addItem(spacerItem1)
        h2_layout.addWidget(self.startButton)
        h2_layout.addWidget(self.quitButton)
        layout.addLayout(h2_layout)

        self.setLayout(layout)
        # you might want to do self.button.click.connect(self.parent().login)

    def saveTxt(self):
        self.myText = self.edit.toPlainText()
        if (len(self.myText) > 0):
            self.startButton.setEnabled(True)
        else:
            self.startButton.setEnabled(False)
        self.saveButton.setEnabled(False)

    def canSave(self):
        self.saveButton.setEnabled(True)

    def getText(self):
        print(self.myText)
        return self.myText


class RunningWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(RunningWidget, self).__init__(parent)

        layout = QtWidgets.QVBoxLayout()

        self.introLabel = QtWidgets.QLabel('Lancement')
        h_layout = QtWidgets.QHBoxLayout()

        naifLabel = QtWidgets.QLabel('Algorithme naif')
        naifTpsLabel = QtWidgets.QLabel('Traitement...')
        naifCTpsLabel = QtWidgets.QLabel('O(n²2)')
        naifSpcLabel = QtWidgets.QLabel('Traitement...')
        naifCSpcLabel = QtWidgets.QLabel('O(1)')
        naifProgressBar = QtWidgets.QProgressBar()
        v1_layout = QtWidgets.QVBoxLayout()
        v1_layout.addWidget(naifLabel)
        v1_layout.addWidget(naifTpsLabel)
        v1_layout.addWidget(naifCTpsLabel)
        v1_layout.addWidget(naifSpcLabel)
        v1_layout.addWidget(naifCSpcLabel)
        v1_layout.addWidget(naifProgressBar)

        noneLabel = QtWidgets.QLabel('----VERSUS----')
        noneTpsLabel = QtWidgets.QLabel('<- Temps d\'execution ->')
        noneCTpsLabel = QtWidgets.QLabel('<- Complexité en temps ->')
        noneSpcLabel = QtWidgets.QLabel('<- Espace utilisé ->')
        noneCSpcLabel = QtWidgets.QLabel('<- Complexité en espace ->')
        none2Label = QtWidgets.QLabel('             ')
        none3Label = QtWidgets.QLabel('             ')
        v0_layout = QtWidgets.QVBoxLayout()
        v0_layout.addWidget(noneLabel)
        v0_layout.addWidget(noneTpsLabel)
        v0_layout.addWidget(noneCTpsLabel)
        v0_layout.addWidget(noneSpcLabel)
        v0_layout.addWidget(noneCSpcLabel)
        v0_layout.addWidget(none2Label)
        v0_layout.addWidget(none3Label)

        kmrLabel = QtWidgets.QLabel('Algorithme KMR')
        kmrTpsLabel = QtWidgets.QLabel('Traitement...')
        kmrCTpsLabel = QtWidgets.QLabel('O(n²2)')
        kmrSpcLabel = QtWidgets.QLabel('Traitement...')
        kmrCSpcLabel = QtWidgets.QLabel('O(1)')
        kmrProgressBar = QtWidgets.QProgressBar()
        v2_layout = QtWidgets.QVBoxLayout()
        v2_layout.addWidget(kmrLabel)
        v2_layout.addWidget(kmrTpsLabel)
        v2_layout.addWidget(kmrCTpsLabel)
        v2_layout.addWidget(kmrSpcLabel)
        v2_layout.addWidget(kmrCSpcLabel)
        v2_layout.addWidget(kmrProgressBar)

        h_layout.addLayout(v1_layout)
        h_layout.addLayout(v0_layout)
        h_layout.addLayout(v2_layout)

        layout.addWidget(self.introLabel)
        layout.addLayout(h_layout)
        self.setLayout(layout)


class LaunchedWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(LaunchedWidget, self).__init__(parent)

        layout = QtWidgets.QVBoxLayout()

        self.introLabel = QtWidgets.QLabel('Lancement')
        h_layout = QtWidgets.QHBoxLayout()
        naifLabel = QtWidgets.QLabel('Algorithme naif')
        naifTpsLabel = QtWidgets.QLabel('12 secondes')
        naifCTpsLabel = QtWidgets.QLabel('O(n²2)')
        naifSpcLabel = QtWidgets.QLabel('0.1 Ko')
        naifCSpcLabel = QtWidgets.QLabel('O(1)')
        naifProgressBar = QtWidgets.QProgressBar()
        v1_layout = QtWidgets.QVBoxLayout()
        v1_layout.addWidget(naifLabel)
        v1_layout.addWidget(naifTpsLabel)
        v1_layout.addWidget(naifCTpsLabel)
        v1_layout.addWidget(naifSpcLabel)
        v1_layout.addWidget(naifCSpcLabel)
        v1_layout.addWidget(naifProgressBar)

        noneLabel = QtWidgets.QLabel('----VERSUS----')
        noneTpsLabel = QtWidgets.QLabel('<- Temps d\'execution ->')
        noneCTpsLabel = QtWidgets.QLabel('<- Complexité en temps ->')
        noneSpcLabel = QtWidgets.QLabel('<- Espace utilisé ->')
        noneCSpcLabel = QtWidgets.QLabel('<- Complexité en espace ->')
        none2Label = QtWidgets.QLabel('             ')
        v0_layout = QtWidgets.QVBoxLayout()
        v0_layout.addWidget(noneLabel)
        v0_layout.addWidget(noneTpsLabel)
        v0_layout.addWidget(noneCTpsLabel)
        v0_layout.addWidget(noneSpcLabel)
        v0_layout.addWidget(noneCSpcLabel)
        v0_layout.addWidget(none2Label)

        kmrLabel = QtWidgets.QLabel('Algorithme KMR')
        kmrTpsLabel = QtWidgets.QLabel('12 secondes')
        kmrCTpsLabel = QtWidgets.QLabel('O(n²2)')
        kmrSpcLabel = QtWidgets.QLabel('0.1 Ko')
        kmrCSpcLabel = QtWidgets.QLabel('O(1)')
        kmrProgressBar = QtWidgets.QProgressBar()
        v2_layout = QtWidgets.QVBoxLayout()
        v2_layout.addWidget(kmrLabel)
        v2_layout.addWidget(kmrTpsLabel)
        v2_layout.addWidget(kmrCTpsLabel)
        v2_layout.addWidget(kmrSpcLabel)
        v2_layout.addWidget(kmrCSpcLabel)
        v2_layout.addWidget(kmrProgressBar)

        h_layout.addLayout(v1_layout)
        h_layout.addLayout(v0_layout)
        h_layout.addLayout(v2_layout)

        layout.addWidget(self.introLabel)
        layout.addLayout(h_layout)
        self.setLayout(layout)
