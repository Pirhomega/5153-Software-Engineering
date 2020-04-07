# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(403, 615)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.username_textbox = QtWidgets.QTextEdit(self.centralwidget)
        self.username_textbox.setGeometry(QtCore.QRect(130, 180, 151, 31))
        self.username_textbox.setObjectName("username_textbox")
        self.password_textbox = QtWidgets.QTextEdit(self.centralwidget)
        self.password_textbox.setGeometry(QtCore.QRect(130, 260, 151, 31))
        self.password_textbox.setObjectName("password_textbox")
        self.username_label = QtWidgets.QLabel(self.centralwidget)
        self.username_label.setGeometry(QtCore.QRect(130, 130, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Onyx")
        font.setPointSize(16)
        self.username_label.setFont(font)
        self.username_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.username_label.setAlignment(QtCore.Qt.AlignCenter)
        self.username_label.setObjectName("username_label")
        self.password_label = QtWidgets.QLabel(self.centralwidget)
        self.password_label.setGeometry(QtCore.QRect(130, 210, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Onyx")
        font.setPointSize(16)
        self.password_label.setFont(font)
        self.password_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.password_label.setAlignment(QtCore.Qt.AlignCenter)
        self.password_label.setObjectName("password_label")
        self.login_button = QtWidgets.QPushButton(self.centralwidget)
        self.login_button.setGeometry(QtCore.QRect(170, 320, 75, 23))
        self.login_button.setObjectName("login_button")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 400, 361, 181))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("login_shaq.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.failure_notif = QtWidgets.QLabel(self.centralwidget)
        self.failure_notif.setGeometry(QtCore.QRect(136, 360, 141, 21))
        self.failure_notif.setText("")
        self.failure_notif.setAlignment(QtCore.Qt.AlignCenter)
        self.failure_notif.setObjectName("failure_notif")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 403, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.username_label.setText(_translate("MainWindow", "Username"))
        self.password_label.setText(_translate("MainWindow", "Password"))
        self.login_button.setText(_translate("MainWindow", "Login"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
