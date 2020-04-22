# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_user.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie #For Gifs
from pymongo import MongoClient

cluster = MongoClient("Password")
db = cluster["Authen"]
collection = db["Users"]

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(40, 350, 541, 401))
        self.groupBox.setObjectName("groupBox")
        self.Username = QtWidgets.QLabel(self.groupBox)
        self.Username.setGeometry(QtCore.QRect(30, 100, 181, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)

        # Info for username and password section
        self.Username.setFont(font)
        self.Username.setObjectName("Username")
        self.UserInput = QtWidgets.QLineEdit(self.groupBox)
        self.UserInput.setGeometry(QtCore.QRect(240, 100, 211, 31))
        self.UserInput.setObjectName("UserInput")
        self.Password = QtWidgets.QLabel(self.groupBox)
        self.Password.setGeometry(QtCore.QRect(30, 220, 191, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.Password.setFont(font)
        self.Password.setObjectName("Password")
        self.Passinput = QtWidgets.QLineEdit(self.groupBox)
        self.Passinput.setGeometry(QtCore.QRect(240, 220, 211, 31))
        self.Passinput.setObjectName("Passinput")
        self.Passinput.setEchoMode(QtWidgets.QLineEdit.Password)

        # Labels and Buttons
        self.CancelButton = QtWidgets.QPushButton(self.groupBox)
        self.CancelButton.setGeometry(QtCore.QRect(20, 360, 121, 31))
        self.CancelButton.setObjectName("CancelButton")
        self.CreateButton = QtWidgets.QPushButton(self.groupBox)
        self.CreateButton.setGeometry(QtCore.QRect(400, 360, 121, 31))
        self.CreateButton.setObjectName("CreateButton")
        self.Instructions = QtWidgets.QLabel(self.groupBox)
        self.Instructions.setGeometry(QtCore.QRect(10, 280, 511, 41))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.Instructions.setFont(font)
        self.Instructions.setObjectName("Instructions")
        self.photo = QtWidgets.QLabel(self.centralwidget)
        self.photo.setGeometry(QtCore.QRect(180, 10, 291, 321))
        self.photo.setText("")
        self.photo.setPixmap(QtGui.QPixmap("Charles_Barkley.jpg"))
        self.photo.setScaledContents(True)
        self.photo.setObjectName("photo")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Connect the createuser button with the checkinput function
        self.CreateButton.clicked.connect(self.checkinput)

    # If the user does something weird, tell them off.
    def error(self, cause):
        self.photo.setPixmap(QtGui.QPixmap("Mad_Charlie.jpg"))

        if cause == 1:
            self.Instructions.setText("Error: Please enter a value for username and password")
            self.Instructions.adjustSize()
        
        elif cause == 2:
            self.Instructions.setText("Error: That username has already been taken.")
            self.Instructions.adjustSize()

    # Once the user has filled in the input fields, check to see if they are
    # compatible. If everything works out, then upload their information into the
    # "users" collection.
    def checkinput(self):
        username = self.UserInput.text()
        password = self.Passinput.text()

        # If the user is lazy
        if username == '' or password == '':
            self.error(1)

        # Make sure there are not any other accounts with this name
        elif collection.count_documents({"username": username}) > 0:
            self.error(2)
        
        # Upload the requested info into our database
        else:
            collection.insert_one({"username": username, "password": password})
            self.Instructions.setText("Success! Your account has been created!")
            self.Instructions.adjustSize()

            self.gif = QMovie('Success.gif')
            self.photo.setMovie(self.gif)
            self.gif.start()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Input field"))
        self.Username.setText(_translate("MainWindow", "Username"))
        self.Password.setText(_translate("MainWindow", "Password"))
        self.CancelButton.setText(_translate("MainWindow", "Back"))
        self.CreateButton.setText(_translate("MainWindow", "Create User"))
        self.Instructions.setText(_translate("MainWindow", "Please enter the username and password for your new account."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
