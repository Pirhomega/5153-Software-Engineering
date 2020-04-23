# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'search.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 401, 581))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.search_prompt_label = QtWidgets.QLabel(self.page)
        self.search_prompt_label.setGeometry(QtCore.QRect(90, 200, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Onyx")
        font.setPointSize(16)
        self.search_prompt_label.setFont(font)
        self.search_prompt_label.setAlignment(QtCore.Qt.AlignCenter)
        self.search_prompt_label.setObjectName("search_prompt_label")
        self.search_button = QtWidgets.QPushButton(self.page)
        self.search_button.setGeometry(QtCore.QRect(150, 310, 91, 23))
        self.search_button.setObjectName("search_button")
        self.search_box = QtWidgets.QTextEdit(self.page)
        self.search_box.setGeometry(QtCore.QRect(60, 250, 271, 41))
        self.search_box.setObjectName("search_box")
        self.no_results_notif = QtWidgets.QLabel(self.page)
        self.no_results_notif.setGeometry(QtCore.QRect(146, 353, 101, 31))
        self.no_results_notif.setText("")
        self.no_results_notif.setObjectName("no_results_notif")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.listWidget = QtWidgets.QListWidget(self.page_2)
        self.listWidget.setGeometry(QtCore.QRect(10, 10, 381, 531))
        self.listWidget.setObjectName("listWidget")
        self.back = QtWidgets.QPushButton(self.page_2)
        self.back.setGeometry(QtCore.QRect(110, 550, 171, 23))
        self.back.setObjectName("back")
        self.stackedWidget.addWidget(self.page_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 400, 21))
        self.menuBar.setObjectName("menuBar")
        self.menuYour_Shopping_Cart = QtWidgets.QMenu(self.menuBar)
        self.menuYour_Shopping_Cart.setObjectName("menuYour_Shopping_Cart")
        self.menuUpdate_Credentials = QtWidgets.QMenu(self.menuYour_Shopping_Cart)
        self.menuUpdate_Credentials.setObjectName("menuUpdate_Credentials")
        MainWindow.setMenuBar(self.menuBar)
        self.actionShopping_Cart = QtWidgets.QAction(MainWindow)
        self.actionShopping_Cart.setObjectName("actionShopping_Cart")
        self.actionChange_Username = QtWidgets.QAction(MainWindow)
        self.actionChange_Username.setObjectName("actionChange_Username")
        self.actionChange_Password = QtWidgets.QAction(MainWindow)
        self.actionChange_Password.setObjectName("actionChange_Password")
        self.actionLogout = QtWidgets.QAction(MainWindow)
        self.actionLogout.setObjectName("actionLogout")
        self.menuUpdate_Credentials.addAction(self.actionChange_Username)
        self.menuUpdate_Credentials.addAction(self.actionChange_Password)
        self.menuYour_Shopping_Cart.addAction(self.actionShopping_Cart)
        self.menuYour_Shopping_Cart.addAction(self.menuUpdate_Credentials.menuAction())
        self.menuYour_Shopping_Cart.addAction(self.actionLogout)
        self.menuBar.addAction(self.menuYour_Shopping_Cart.menuAction())

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.search_prompt_label.setText(_translate("MainWindow", "What are you looking for?"))
        self.search_button.setText(_translate("MainWindow", "Search"))
        self.back.setText(_translate("MainWindow", "PushButton"))
        self.menuYour_Shopping_Cart.setTitle(_translate("MainWindow", "Your Account"))
        self.menuUpdate_Credentials.setTitle(_translate("MainWindow", "Update Credentials"))
        self.actionShopping_Cart.setText(_translate("MainWindow", "Shopping Cart"))
        self.actionChange_Username.setText(_translate("MainWindow", "Change Username"))
        self.actionChange_Password.setText(_translate("MainWindow", "Change Password"))
        self.actionLogout.setText(_translate("MainWindow", "Logout"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
