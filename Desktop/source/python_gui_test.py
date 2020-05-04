#!C:\Users\Owner\AppData\Local\Programs\Python\Python36\python.exe

# HOW TO CONVERT .ui FILES TO PYTHON CODE
# pyuic5 -x <file.ui> -o <new_name.py>


from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class myWindow(QMainWindow):
    def __init__(self):
        super(myWindow, self).__init__()
        # set window position and size
        self.setGeometry(200,200,300,300)
        # sets the window title
        self.setWindowTitle("Test Window 1")
        self.initUI()

    def initUI(self):
        # create a label.
        # We use self instead of win, like before, because this class is now
        # the window object.
        # We make label and b1 "self" because we want to access them anywhere in the class object
        # by any of the member functions
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Test Label 1")
        self.label.move(50,50)

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("Test Button 1")
        # set an event to run on button click
        self.b1.clicked.connect(self.click)

    def click(self):
        self.label.setText("Button pressed oh mah goodness it works")
        self.update()
    
    def update(self):
        self.label.adjustSize()

app = QApplication(sys.argv)
# create a new window object
win = myWindow()
# display the window
win.show()
# makes sure window closes when exit button is hit
sys.exit(app.exec_())