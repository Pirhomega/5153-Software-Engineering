# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'search_prompt.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from api import Api

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.search_box = QtWidgets.QTextEdit(self.centralwidget)
        self.search_box.setGeometry(QtCore.QRect(70, 260, 261, 41))
        self.search_box.setObjectName("search_box")
        self.search_button = QtWidgets.QPushButton(self.centralwidget)
        self.search_button.setGeometry(QtCore.QRect(160, 320, 91, 23))
        self.search_button.setObjectName("search_button")
        self.search_prompt_label = QtWidgets.QLabel(self.centralwidget)
        self.search_prompt_label.setGeometry(QtCore.QRect(100, 210, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Onyx")
        font.setPointSize(16)
        self.search_prompt_label.setFont(font)
        self.search_prompt_label.setAlignment(QtCore.Qt.AlignCenter)
        self.search_prompt_label.setObjectName("search_prompt_label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # when button is pressed, call search method
        self.login_button.clicked.connect(self.search_products)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.search_button.setText(_translate("MainWindow", "Search"))
        self.search_prompt_label.setText(_translate("MainWindow", "What are you looking for?"))

    def search_products(self, MainWindow):
        username_password = {   'username': self.username_textbox.toPlainText(), 
                                "password": self.password_textbox.toPlainText()}
        log_in_attempt = Login()
        _, login_success = log_in_attempt.login(username_password)
        self.login_result(login_success)

    def login_result(self, login_success):
        self.login_success = login_success
        print(self.login_success)
        if self.login_success == True:
            self.login_button.setText("Success!")
        else:
            self.login_button.setText("Failed!")
        self.update()

    def update(self):
        self.label.adjustSize()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
