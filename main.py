from PyQt6.QtWidgets import QLabel, QMainWindow, QPushButton, QApplication
from PyQt6 import uic


class UI(QMainWindow):
    def __init__(self):
        super(UI,self).__init__()

        #load the ui file
        uic.loadUi('toe.ui',self)
        self.setWindowTitle('Tic tac toe')

        self.counter = 0
        for i in range(1,11):
            setattr(self, f"button{i}" , self.findChild(QPushButton,f"pushButton_{i}"))
        self.button_list = [self.button1,self.button2,self.button3,self.button4,self.button5,self.button6,self.button7,self.button8,self.button9]
        self.label = self.findChild(QLabel,"label")
        for button in self.button_list:
            button.clicked.connect(lambda *args, b=button : self.clicker(b))
        self.button10.clicked.connect(self.reset)
        self.show()

    def clicker(self, button):
        if self.counter % 2 ==0:
            button.setText("X")
            self.label.setText("now 'O's turn")
        else:
            button.setText("O")
            self.label.setText("now 'X's turn")
        button.setEnabled(False)
        self.check_win()
        self.counter += 1
        if self.counter == 9:
            self.finish()
            self.label.setText("Tie try again")

    def reset(self):
        for button in self.button_list:
            button.setText("")
            button.setEnabled(True)
            button.setStyleSheet('QPushButton {color: #797979;}')
        self.counter = 0

    def check_win(self):
        #row win
        for i in range(1,10,3):
            if getattr(self,f"button{i}").text() !='' and getattr(self,f"button{i}").text() == getattr(self,f"button{i+1}").text() == getattr(self,f"button{i+2}").text():
                self.finish(getattr(self,f"button{i}"),getattr(self,f"button{i+1}"),getattr(self,f"button{i+2}"))
        # column win
        for i in range(1,4):
            if getattr(self,f"button{i}").text() !='' and getattr(self,f"button{i}").text() == getattr(self,f"button{i+3}").text() == getattr(self,f"button{i+6}").text():
                self.finish(getattr(self,f"button{i}"), getattr(self,f"button{i+3}"), getattr(self,f"button{i+6}"))
        # cross win
        if self.button1.text() != '' and self.button5.text() == self.button1.text() == self.button9.text():
            self.finish(self.button1,self.button5,self.button9)
        if self.button3.text() != '' and self.button3.text() == self.button5.text() == self.button7.text():
                self.finish(self.button3,self.button5,self.button7)
    def finish(self,*args):
        for button in args:
            button.setStyleSheet('QPushButton {color: red;}')
        for button in self.button_list:
            button.setEnabled(False)
        if self.counter %2 == 0:
            self.label.setText("'X' win")
        else:
            self.label.setText("'O' win")

app = QApplication([])
UIWindow = UI()
#Run the app

app.exec()

