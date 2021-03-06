
from PyQt5.QtWidgets import (QPushButton, QMainWindow, QTextEdit,
                             QAction, QWidget, QVBoxLayout, QLabel,
                             QHBoxLayout, QMessageBox, QDesktopWidget,
                             QLineEdit, QGridLayout)

from PyQt5.QtGui import QIcon


class Widget(QWidget):

    def __init__(self):
        super(Widget, self).__init__()

        self.initUI()


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        exitAct = QAction(QIcon('./data/exit.jpg'), 'Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(self.close)

        startAct = QAction(QIcon('./data/run.png'), 'Run', self)
        startAct.setShortcut('Ctrl+R')
        startAct.setStatusTip('Run benchmark')
        startAct.triggered.connect(self.close)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        toolsMenu = menubar.addMenu('&Tools')
        helpMenu = menubar.addMenu('&Help')
        fileMenu.addAction(startAct)
        fileMenu.addAction(exitAct)

        toolbar = self.addToolBar('Exit')
        toolbar.addAction(startAct)
        toolbar.addAction(exitAct)
        """
        okButton = QPushButton("OK")
        cancelButton = QPushButton("Cancel")

        self.addWidget(okButton)

        self.setLayout(vbox)    """

        self.resize(1280, 720)
        self.setWindowTitle('Algorithmique de texte - Exctraction de motif')
        self.show()

    def addReview(self):
        title = QLabel('Title')
        author = QLabel('Author')
        review = QLabel('Review')

        titleEdit = QLineEdit()
        authorEdit = QLineEdit()
        reviewEdit = QTextEdit()

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(title, 1, 0)
        grid.addWidget(titleEdit, 1, 1)

        grid.addWidget(author, 2, 0)
        grid.addWidget(authorEdit, 2, 1)

        grid.addWidget(review, 3, 0)
        grid.addWidget(reviewEdit, 3, 1, 5, 1)

        self.setLayout(grid)

        return grid

    def addBox(self):
        okButton = QPushButton("OK")
        cancelButton = QPushButton("Cancel")

    def closeEvent(self, event):

        reply = QMessageBox.question(self, 'Message', "Are you sure to quit?",
                                     QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
