

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'search.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie
from api import Api, Login, UserManager, ShoppingCart
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

        # login page code (page 1)
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
        self.login_button.setGeometry(QtCore.QRect(154, 310, 101, 23))
        self.login_button.setObjectName("login_button")
        self.label = QtWidgets.QLabel(self.page_1)
        self.label.setGeometry(QtCore.QRect(60, 440, 291, 151))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../images/login_shaq.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.failure_notif = QtWidgets.QLabel(self.page_1)
        self.failure_notif.setGeometry(QtCore.QRect(130, 390, 151, 31))
        self.failure_notif.setText("")
        self.failure_notif.setAlignment(QtCore.Qt.AlignCenter)
        self.failure_notif.setObjectName("failure_notif")
        self.create_account_button = QtWidgets.QPushButton(self.page_1)
        self.create_account_button.setGeometry(QtCore.QRect(154, 350, 101, 23))
        self.create_account_button.setObjectName("create_account_button")

        # create account code (page 1.5)
        self.page_1_5 = QtWidgets.QWidget()
        self.page_1_5.setObjectName("page_1_5")
        self.stackedWidget.addWidget(self.page_1_5)      
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10,190,381,381))
        self.groupBox.setObjectName("groupBox")
        self.Username = QtWidgets.QLabel(self.groupBox)
        self.Username.setGeometry(QtCore.QRect(30,40,91,16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)     
        self.Username.setFont(font)
        self.Username.setObjectName("Username")
        self.UserInput = QtWidgets.QLineEdit(self.groupBox)
        self.UserInput.setGeometry(QtCore.QRect(160,40,211,31))
        self.UserInput.setObjectName("UserInput")
        self.Password = QtWidgets.QLabel(self.groupBox)
        self.Password.setGeometry(QtCore.QRect(30,150,91,16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.Password.setFont(font)
        self.Password.setObjectName("Password")
        self.Passinput = QtWidgets.QLineEdit(self.groupBox)
        self.Passinput.setGeometry(QtCore.QRect(160,150,211,31))
        self.Passinput.setObjectName("Passinput")
        self.Passinput.setEchoMode(QtWidgets.QLineEdit.Password)
        self.CancelButton = QtWidgets.QPushButton(self.groupBox)
        self.CancelButton.setGeometry(QtCore.QRect(10,260,121,31))
        self.CancelButton.setObjectName("CancelButton")
        self.CreateButton = QtWidgets.QPushButton(self.groupBox)
        self.CreateButton.setGeometry(QtCore.QRect(250,260,121,31))
        self.CreateButton.setObjectName("CreateButton")
        self.Instructions = QtWidgets.QLabel(self.groupBox)
        self.Instructions.setGeometry(QtCore.QRect(10,200,331,41))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.Instructions.setFont(font)
        self.Instructions.setObjectName("Instructions")
        self.photo = QtWidgets.QLabel(self.centralwidget)
        self.photo.setGeometry(QtCore.QRect(110,10,181,171))
        self.photo.setText("")
        self.photo.setPixmap(QtGui.QPixmap("Charles_Barkley.jpg"))
        self.photo.setScaledContents(True)
        self.photo.setObjectName("photo")

        # search page code (page 2)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.stackedWidget.addWidget(self.page_2)
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

        # search results code (page 3)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.stackedWidget.addWidget(self.page_3)
        self.listWidget = QtWidgets.QListWidget(self.page_3)
        self.listWidget.setGeometry(QtCore.QRect(10, 10, 381, 521))
        self.listWidget.setObjectName("listWidget")
        self.backButton1 = QtWidgets.QPushButton(self.page_3)
        self.backButton1.setGeometry(QtCore.QRect(10, 540, 101, 31))
        self.backButton1.setObjectName("backButton1")

        # item page code (page 4)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.stackedWidget.addWidget(self.page_4)
        self.backButton = QtWidgets.QPushButton(self.page_4)
        self.backButton.setGeometry(QtCore.QRect(10, 540, 101, 31))
        self.backButton.setObjectName("backButton")
        self.addbutton = QtWidgets.QPushButton(self.page_4)
        self.addbutton.setGeometry(QtCore.QRect(280, 540, 101, 31))
        self.addbutton.setObjectName("addbutton")
        self.name = QtWidgets.QLabel(self.page_4)
        self.name.setGeometry(QtCore.QRect(10, 190, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.name.setFont(font)
        self.name.setObjectName("name")
        self.item_name = QtWidgets.QLabel(self.page_4)
        self.item_name.setGeometry(QtCore.QRect(140, 200, 251, 111))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.item_name.setFont(font)
        self.item_name.setScaledContents(True)
        self.item_name.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.item_name.setWordWrap(True)
        self.item_name.setObjectName("item_name")
        self.itemdescription = QtWidgets.QLabel(self.page_4)
        self.itemdescription.setGeometry(QtCore.QRect(10, 300, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.itemdescription.setFont(font)
        self.itemdescription.setObjectName("itemdescription")
        self.description_text = QtWidgets.QLabel(self.page_4)
        self.description_text.setGeometry(QtCore.QRect(140, 310, 251, 131))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.description_text.setFont(font)
        self.description_text.setScaledContents(True)
        self.description_text.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.description_text.setWordWrap(True)
        self.description_text.setObjectName("description_text")
        self.line = QtWidgets.QFrame(self.page_4)
        self.line.setGeometry(QtCore.QRect(0, 170, 401, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.page_4)
        self.line_2.setGeometry(QtCore.QRect(0, 510, 401, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.photo = QtWidgets.QLabel(self.page_4)
        self.photo.setGeometry(QtCore.QRect(10, 10, 381, 151))
        self.photo.setFrameShape(QtWidgets.QFrame.Box)
        self.photo.setLineWidth(2)
        self.photo.setText("")
        self.photo.setPixmap(QtGui.QPixmap("../images/surprise_shaq.jpg"))
        self.photo.setScaledContents(True)
        self.photo.setObjectName("photo")
        self.quantity = QtWidgets.QLabel(self.page_4)
        self.quantity.setGeometry(QtCore.QRect(10, 450, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.quantity.setFont(font)
        self.quantity.setObjectName("quantity")
        self.numitems = QtWidgets.QLabel(self.page_4)
        self.numitems.setGeometry(QtCore.QRect(140, 450, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.numitems.setFont(font)
        self.numitems.setObjectName("numitems")

####################################################################################################

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        # sets the starting page to index 0 when app is started
        self.stackedWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # when login button is pressed, call login method
        self.login_button.clicked.connect(self.login)

        # when the user clicks the 'create account' button from the main page
        self.create_account_button.clicked.connect(lambda: self.switch_page(1))

        # Connect the createuser button with the checkinput function
        self.CreateButton.clicked.connect(self.checkinput)
                
        # when button is pressed, call search method
        self.search_button.clicked.connect(self.search_products)

        # if an item is clicked, go to item's page
        self.listWidget.itemClicked.connect(self.display_item_page)

        # # when back buttons are pressed, call switch to previous page
        # self.backButton.clicked.connect(lambda: self.switch_page(self.page_3))
        self.backButton.clicked.connect(lambda: self.switch_page(self.stackedWidget.currentIndex()-1))
        self.backButton1.clicked.connect(lambda: self.switch_page(self.stackedWidget.currentIndex()-1))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.search_prompt_label.setText(_translate("MainWindow", "What are you looking for?"))
        self.search_button.setText(_translate("MainWindow", "Search"))
        self.username_label.setText(_translate("MainWindow", "Username"))
        self.password_label.setText(_translate("MainWindow", "Password"))
        self.login_button.setText(_translate("MainWindow", "Login"))
        self.create_account_button.setText(_translate("MainWindow", "Create Account"))
        self.groupBox.setTitle(_translate("MainWindow", "Input field"))
        self.Username.setText(_translate("MainWindow", "Username"))
        self.Password.setText(_translate("MainWindow", "Password"))
        self.CancelButton.setText(_translate("MainWindow", "Back"))
        self.CreateButton.setText(_translate("MainWindow", "Create User"))
        self.Instructions.setText(_translate("MainWindow", "Please enter the username and password for your new account."))
        self.backButton.setText(_translate("MainWindow", "Back"))
        self.backButton1.setText(_translate("MainWindow", "Back"))
        self.addbutton.setText(_translate("MainWindow", "Add to Cart"))
        self.name.setText(_translate("MainWindow", "Name:"))
        self.item_name.setText(_translate("MainWindow", ""))
        self.itemdescription.setText(_translate("MainWindow", "Description:"))
        self.description_text.setText(_translate("MainWindow", "Description"))
        self.quantity.setText(_translate("MainWindow", "Quantity: "))
        self.numitems.setText(_translate("MainWindow", ""))

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
            self.switch_page(1)
        else:
            self.failure_notif.setText("Failed attempt.\nPlease try again.")
    
    # If the user does something weird, tell them off.
    def error(self, cause):
        self.photo.setPixmap(QtGui.QPixmap("../images/Mad_Charlie.jpg"))

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

            self.gif = QMovie('../images/Success.gif')
            self.photo.setMovie(self.gif)
            self.gif.start()
        

    # readjusts label sizes so text inside will not overflow
    def update(self, widget):
        widget.adjustSize()

    # run an item search using the API
    def search_products(self):
        if not self.search_box.document().isEmpty():
            search_string = self.search_box.toPlainText()
            search_attempt = Api()
            self.search_result = search_attempt.search({"item": search_string})
            if self.search_result != [[]]:
                self.switch_page(2)
                self.display_results()
            else:
                self.no_results_notif.setText("No results found")

    # print search results to a list widget
    def display_results(self):
        self.listWidget.clear()
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
        # if the argument 'next_page' is an integer, 
        if isinstance(self.next_page, int):
            self.stackedWidget.setCurrentIndex(self.next_page)
        else:
            self.stackedWidget.setCurrentWidget(self.next_page)
    
    def display_item_page(self, item):
        # print("Item in row", self.listWidget.row(item), "was clicked!")
        detail_string = ""
        self.switch_page(3)
        # print(self.search_result[0][0])
        self.item_name.setText(self.search_result[0][self.listWidget.row(item)]["item"])
        if "details" in self.search_result[0][self.listWidget.row(item)]:
            for num in range(0,len(self.search_result[0][self.listWidget.row(item)]["details"])):
                detail_string += str(self.search_result[0][self.listWidget.row(item)]["details"]["name" + str(num)]) + "\n"
        self.description_text.setText(detail_string)
        self.numitems.setText(str(self.search_result[0][self.listWidget.row(item)]["quantity"]))
        self.update(self.item_name)
        self.update(self.description_text)
        # print(item.text())
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())