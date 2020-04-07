# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'search.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from api import Api, Login
import sys

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 401, 601))
        self.stackedWidget.setObjectName("stackedWidget")
        font = QtGui.QFont()
        font.setFamily("Onyx")
        font.setPointSize(16)

        # login page code
        self.page_1 = QtWidgets.QWidget()
        self.page_1.setObjectName("page_1")
        self.stackedWidget.addWidget(self.page_1)
        self.username_textbox = QtWidgets.QTextEdit(self.page_1)
        self.username_textbox.setGeometry(QtCore.QRect(130, 180, 151, 31))
        self.username_textbox.setObjectName("username_textbox")
        self.password_textbox = QtWidgets.QTextEdit(self.page_1)
        self.password_textbox.setGeometry(QtCore.QRect(130, 260, 151, 31))
        self.password_textbox.setObjectName("password_textbox")
        self.username_label = QtWidgets.QLabel(self.page_1)
        self.username_label.setGeometry(QtCore.QRect(130, 130, 151, 41))
        self.username_label.setFont(font)
        self.username_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.username_label.setAlignment(QtCore.Qt.AlignCenter)
        self.username_label.setObjectName("username_label")
        self.password_label = QtWidgets.QLabel(self.page_1)
        self.password_label.setGeometry(QtCore.QRect(130, 210, 151, 41))
        self.password_label.setFont(font)
        self.password_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.password_label.setAlignment(QtCore.Qt.AlignCenter)
        self.password_label.setObjectName("password_label")
        self.login_button = QtWidgets.QPushButton(self.page_1)
        self.login_button.setGeometry(QtCore.QRect(154, 320, 101, 23))
        self.login_button.setObjectName("login_button")
        self.label = QtWidgets.QLabel(self.page_1)
        self.label.setGeometry(QtCore.QRect(20, 400, 361, 181))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("login_shaq.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.failure_notif = QtWidgets.QLabel(self.page_1)
        self.failure_notif.setGeometry(QtCore.QRect(136, 360, 141, 31))
        self.failure_notif.setText("")
        self.failure_notif.setAlignment(QtCore.Qt.AlignCenter)
        self.failure_notif.setObjectName("failure_notif")

        # search page code
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.search_prompt_label = QtWidgets.QLabel(self.page_2)
        self.search_prompt_label.setGeometry(QtCore.QRect(90, 200, 211, 41))
        self.search_prompt_label.setFont(font)
        self.search_prompt_label.setAlignment(QtCore.Qt.AlignCenter)
        self.search_prompt_label.setObjectName("search_prompt_label")

        
        self.no_results_notif = QtWidgets.QLabel(self.page_2)
        self.no_results_notif.setGeometry(QtCore.QRect(146, 353, 101, 31))
        self.failure_notif.setText("")
        self.no_results_notif.setAlignment(QtCore.Qt.AlignCenter)
        self.no_results_notif.setObjectName("no_results_notif")

        self.search_button = QtWidgets.QPushButton(self.page_2)
        self.search_button.setGeometry(QtCore.QRect(150, 310, 91, 23))
        self.search_button.setObjectName("search_button")
        self.search_box = QtWidgets.QTextEdit(self.page_2)
        self.search_box.setGeometry(QtCore.QRect(60, 250, 271, 41))
        self.search_box.setObjectName("search_box")
        self.stackedWidget.addWidget(self.page_2)

        # search results code
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.listWidget = QtWidgets.QListWidget(self.page_3)
        self.listWidget.setGeometry(QtCore.QRect(10, 10, 381, 571))
        self.listWidget.setObjectName("listWidget")
        self.stackedWidget.addWidget(self.page_3)

        # page 4 code
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.stackedWidget.addWidget(self.page_4)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # when button is pressed, call login method
        self.login_button.clicked.connect(self.login)

        # make sure current page displaying is the search page
        self.switch_page(self.page_1)
                
        # when button is pressed, call search method
        self.search_button.clicked.connect(self.search_products)

        # if an item is clicked, go to item's page
        self.listWidget.itemClicked.connect(self.switch_temp)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.search_prompt_label.setText(_translate("MainWindow", "What are you looking for?"))
        self.search_button.setText(_translate("MainWindow", "Search"))
        self.username_label.setText(_translate("MainWindow", "Username"))
        self.password_label.setText(_translate("MainWindow", "Password"))
        self.login_button.setText(_translate("MainWindow", "Login"))

    # attempt to log in to Innoventory with username and password offered
    def login(self, MainWindow):
        username_password = {   'username': self.username_textbox.toPlainText(), 
                                "password": self.password_textbox.toPlainText()}
        log_in_attempt = Login()
        _, login_success = log_in_attempt.login(username_password)
        self.login_result(login_success)

    # allow user in if credentials are verified; block otherwise
    def login_result(self, login_success):
        self.login_success = login_success
        if self.login_success == True:
            self.switch_page(self.page_2)
        else:
            self.failure_notif.setText("Failed attempt.\nPlease try again.")

    # # readjusts label sizes so text inside will not overflow
    # def update(self, widget):
    #     widget.adjustSize()

    # run an item search using the API
    def search_products(self):
        if not self.search_box.document().isEmpty():
            search_string = self.search_box.toPlainText()
            search_attempt = Api()
            self.search_result = search_attempt.search({"item": search_string})
            if self.search_result != [[]]:
                self.switch_page(self.page_3)
                self.display_results()
            else:
                self.no_results_notif.setText("No results found")

    # print search results to a list widget
    def display_results(self):
        for result in self.search_result[0]:
            item_string = result["item"] + " "
            # if "details" in result:
            #     for num in range(0,len(result["details"])):
            #         item_string += str(result["details"]["name" + str(num)]) + " "
            item = QtWidgets.QListWidgetItem(item_string)
            self.listWidget.addItem(item)

    # will switch to widget representing page 'next_page'
    def switch_page(self, next_page):
        self.next_page = next_page
        self.stackedWidget.setCurrentWidget(self.next_page)
    
    def switch_temp(self, item):
        # print("Item in row", self.listWidget.row(item), "was clicked!")
        print(item.text())
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
