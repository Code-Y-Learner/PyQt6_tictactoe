from PyQt6.QtWidgets import QVBoxLayout, QSizePolicy, QMainWindow, QFrame, QPushButton, QApplication, QLineEdit
import PyQt6.QtGui as qtg
from PyQt6 import uic
from PyQt6 import QtCore
import sys


class UI(QMainWindow):
    def __init__(self):
        super(UI,self).__init__()

        #load the ui file
        uic.loadUi('hide.ui',self)
        self.setWindowTitle('Tic tac toe')

        self.my_layout = self.findChild(QVBoxLayout,"formLayoutWidget")
        self.frame = self.findChild(QFrame,'frame')
        self.edit = self.findChild(QLineEdit,"lineEdit")
        self.button = self.findChild(QPushButton,"pushButton")
        self.button.setFixedSize(350,100)

        self.button.clicked.connect(self.hide)
        self.show()
        self.hidden = False
    def hide(self):
        if self.hidden:
            self.frame.show()
            self.hidden = False
            self.resize(400, 250)
        else:
            self.frame.hide()
            self.hidden = True
            self.resize(400, 150)



app = QApplication([])
UIWindow = UI()
#Run the app

app.exec()