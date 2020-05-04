

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'search.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPalette
from PyQt5.QtCore import Qt
from api import Api, Login, Employee, UserManager, ShoppingCart
import sys

class Ui_MainWindow(object):
    def __init__(self):
        self.prompt_confirm = False
        self.search_attempt = Api()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 621)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 401, 601))
        self.stackedWidget.setObjectName("stackedWidget")
# 
#  $$$$$$\  $$\                                     $$\    $$\                    $$\           $$\       $$\                     
# $$  __$$\ $$ |                                    $$ |   $$ |                   \__|          $$ |      $$ |                    
# $$ /  \__|$$ | $$$$$$\   $$$$$$$\  $$$$$$$\       $$ |   $$ |$$$$$$\   $$$$$$\  $$\  $$$$$$\  $$$$$$$\  $$ | $$$$$$\   $$$$$$$\ 
# $$ |      $$ | \____$$\ $$  _____|$$  _____|      \$$\  $$  |\____$$\ $$  __$$\ $$ | \____$$\ $$  __$$\ $$ |$$  __$$\ $$  _____|
# $$ |      $$ | $$$$$$$ |\$$$$$$\  \$$$$$$\         \$$\$$  / $$$$$$$ |$$ |  \__|$$ | $$$$$$$ |$$ |  $$ |$$ |$$$$$$$$ |\$$$$$$\  
# $$ |  $$\ $$ |$$  __$$ | \____$$\  \____$$\         \$$$  / $$  __$$ |$$ |      $$ |$$  __$$ |$$ |  $$ |$$ |$$   ____| \____$$\ 
# \$$$$$$  |$$ |\$$$$$$$ |$$$$$$$  |$$$$$$$  |         \$  /  \$$$$$$$ |$$ |      $$ |\$$$$$$$ |$$$$$$$  |$$ |\$$$$$$$\ $$$$$$$  |
#  \______/ \__| \_______|\_______/ \_______/           \_/    \_______|\__|      \__| \_______|\_______/ \__| \_______|\_______/                                                                                                                            
# 

###################################################################################################################################
#######################                             page 0 - login                                          #######################
###################################################################################################################################

        self.page_0 = QtWidgets.QWidget()
        self.page_0.setObjectName("page_1")
        self.stackedWidget.addWidget(self.page_0)
        self.groupBoxLI = QtWidgets.QGroupBox(self.page_0)
        self.groupBoxLI.setGeometry(QtCore.QRect(10,10,381,581))
        self.groupBoxLI.setObjectName("groupBoxLI")
        self.username_textbox = QtWidgets.QLineEdit(self.groupBoxLI)
        self.username_textbox.setGeometry(QtCore.QRect(120, 180, 141, 31))
        self.username_textbox.setObjectName("username_textbox")
        self.password_textbox = QtWidgets.QLineEdit(self.groupBoxLI)
        self.password_textbox.setGeometry(QtCore.QRect(120, 260, 141, 31))
        self.password_textbox.setObjectName("password_textbox")
        self.password_textbox.setEchoMode(QtWidgets.QLineEdit.Password)
        self.username_label = QtWidgets.QLabel(self.groupBoxLI)
        self.username_label.setGeometry(QtCore.QRect(120, 140, 141, 41))
        self.username_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.username_label.setAlignment(QtCore.Qt.AlignCenter)
        self.username_label.setObjectName("username_label")
        self.password_label = QtWidgets.QLabel(self.groupBoxLI)
        self.password_label.setGeometry(QtCore.QRect(120, 220, 141, 41))
        self.password_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.password_label.setAlignment(QtCore.Qt.AlignCenter)
        self.password_label.setObjectName("password_label")
        self.login_button = QtWidgets.QPushButton(self.groupBoxLI)
        self.login_button.setGeometry(QtCore.QRect(144, 310, 91, 23))
        self.login_button.setObjectName("login_button")
        self.create_account_button = QtWidgets.QPushButton(self.groupBoxLI)
        self.create_account_button.setGeometry(QtCore.QRect(144, 350, 91, 23))
        self.create_account_button.setObjectName("create_account_button")
        self.label = QtWidgets.QLabel(self.groupBoxLI)
        self.label.setGeometry(QtCore.QRect(50, 430, 281, 141))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../images/login_shaq.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.logo_login = QtWidgets.QLabel(self.page_0)
        self.logo_login.setGeometry(QtCore.QRect(90, 20, 220, 120))
        self.logo_login.setText("")
        self.logo_login.setPixmap(QtGui.QPixmap("../images/Inno.png"))
        self.logo_login.setScaledContents(True)
        self.logo_login.setObjectName("logo_login")
        self.failure_notif = QtWidgets.QLabel(self.groupBoxLI)
        self.failure_notif.setGeometry(QtCore.QRect(120, 390, 141, 31))
        self.failure_notif.setText("")
        self.failure_notif.setAlignment(QtCore.Qt.AlignCenter)
        self.failure_notif.setObjectName("failure_notif")

###################################################################################################################################
#######################                             page 1 - create account                                 #######################
###################################################################################################################################

        self.page_1 = QtWidgets.QWidget()
        self.page_1.setObjectName("page_1_5")
        self.stackedWidget.addWidget(self.page_1)
        self.groupBoxCA = QtWidgets.QGroupBox(self.page_1)
        self.groupBoxCA.setGeometry(QtCore.QRect(10,190,381,381))
        self.groupBoxCA.setObjectName("groupBoxCA")
        self.Username = QtWidgets.QLabel(self.groupBoxCA)
        self.Username.setGeometry(QtCore.QRect(30,40,91,16))    
        self.Username.setObjectName("Username")
        self.UserInput = QtWidgets.QLineEdit(self.groupBoxCA)
        self.UserInput.setGeometry(QtCore.QRect(160,40,211,31))
        self.UserInput.setObjectName("UserInput")
        self.Password = QtWidgets.QLabel(self.groupBoxCA)
        self.Password.setGeometry(QtCore.QRect(30,150,91,16))
        self.Password.setObjectName("Password")
        self.PassInput = QtWidgets.QLineEdit(self.groupBoxCA)
        self.PassInput.setGeometry(QtCore.QRect(160,150,211,31))
        self.PassInput.setObjectName("PassInput")
        self.PassInput.setEchoMode(QtWidgets.QLineEdit.Password)
        self.CancelButton = QtWidgets.QPushButton(self.groupBoxCA)
        self.CancelButton.setGeometry(QtCore.QRect(10,260,121,31))
        self.CancelButton.setObjectName("CancelButton")
        self.CreateButton = QtWidgets.QPushButton(self.groupBoxCA)
        self.CreateButton.setGeometry(QtCore.QRect(250,260,121,31))
        self.CreateButton.setObjectName("CreateButton")
        self.Instructions = QtWidgets.QLabel(self.groupBoxCA)
        self.Instructions.setGeometry(QtCore.QRect(10,200,331,41))
        self.Instructions.setObjectName("Instructions")
        self.photo = QtWidgets.QLabel(self.page_1)
        self.photo.setGeometry(QtCore.QRect(90, 20, 220, 120))
        self.photo.setText("")
        self.photo.setPixmap(QtGui.QPixmap("../images/Inno.png"))
        self.photo.setScaledContents(True)
        self.photo.setObjectName("photo")

###################################################################################################################################
#######################                             page 2 - search page                                    #######################
###################################################################################################################################

        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.stackedWidget.addWidget(self.page_2)
        self.search_prompt_label = QtWidgets.QLabel(self.page_2)
        self.search_prompt_label.setGeometry(QtCore.QRect(90, 200, 211, 41))
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
        self.search_box = QtWidgets.QLineEdit(self.page_2)
        self.search_box.setGeometry(QtCore.QRect(60, 250, 271, 41))
        self.search_box.setObjectName("search_box")
        self.logo_search = QtWidgets.QLabel(self.page_2)
        self.logo_search.setGeometry(QtCore.QRect(90, 20, 220, 120))
        self.logo_search.setText("")
        self.logo_search.setPixmap(QtGui.QPixmap("../images/Inno.png"))
        self.logo_search.setScaledContents(True)
        self.logo_search.setObjectName("logo_search")

###################################################################################################################################
#######################                             page 3 - search results                                 #######################
###################################################################################################################################

        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.stackedWidget.addWidget(self.page_3)
        self.search_listWidget = QtWidgets.QListWidget(self.page_3)
        self.search_listWidget.setGeometry(QtCore.QRect(10, 10, 381, 521))
        self.search_listWidget.setObjectName("search_listWidget")
        self.search_back_button = QtWidgets.QPushButton(self.page_3)
        self.search_back_button.setGeometry(QtCore.QRect(10, 540, 101, 31))
        self.search_back_button.setObjectName("search_back_button")

###################################################################################################################################
#######################                             page 4 - item page                                      #######################
###################################################################################################################################

        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.stackedWidget.addWidget(self.page_4)
        self.item_back_button = QtWidgets.QPushButton(self.page_4)
        self.item_back_button.setGeometry(QtCore.QRect(10, 540, 101, 31))
        self.item_back_button.setObjectName("item_back_button")
        self.addbutton = QtWidgets.QPushButton(self.page_4)
        self.addbutton.setGeometry(QtCore.QRect(280, 540, 101, 31))
        self.addbutton.setObjectName("addbutton")
        self.addbutton.setEnabled(True)
        self.name = QtWidgets.QLabel(self.page_4)
        self.name.setGeometry(QtCore.QRect(10, 150, 121, 31))
        self.name.setObjectName("name")
        self.price = QtWidgets.QLabel(self.page_4)
        self.price.setGeometry(QtCore.QRect(140, 370, 81, 31))
        self.price.setObjectName("price")
        self.price_label = QtWidgets.QLabel(self.page_4)
        self.price_label.setGeometry(QtCore.QRect(10, 370, 121, 31))
        self.price_label.setObjectName("price_label")
        self.quantity = QtWidgets.QLabel(self.page_4)
        self.quantity.setGeometry(QtCore.QRect(10, 330, 121, 31))
        self.quantity.setObjectName("quantity")
        self.numitems = QtWidgets.QLabel(self.page_4)
        self.numitems.setGeometry(QtCore.QRect(140, 330, 81, 31))
        self.available_label = QtWidgets.QLabel(self.page_4)
        self.available_label.setGeometry(QtCore.QRect(10, 410, 121, 31))
        self.available_label.setObjectName("available_label")
        self.itemdescription = QtWidgets.QLabel(self.page_4)
        self.itemdescription.setGeometry(QtCore.QRect(10, 180, 121, 41))
        self.itemdescription.setObjectName("itemdescription")
        self.description_text = QtWidgets.QLabel(self.page_4)
        self.description_text.setGeometry(QtCore.QRect(140, 190, 251, 141))
        self.description_text.setScaledContents(True)
        self.description_text.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.description_text.setWordWrap(True)
        self.description_text.setObjectName("description_text")
        self.item_name = QtWidgets.QLabel(self.page_4)
        self.item_name.setGeometry(QtCore.QRect(140, 160, 251, 51))
        self.item_name.setScaledContents(True)
        self.item_name.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.item_name.setObjectName("item_name")
        self.available_status = QtWidgets.QLabel(self.page_4)
        self.available_status.setGeometry(QtCore.QRect(140, 410, 81, 31))
        self.available_status.setObjectName("available_status")
        self.item_line = QtWidgets.QFrame(self.page_4)
        self.item_line.setGeometry(QtCore.QRect(0, 130, 401, 16))
        self.item_line.setFrameShape(QtWidgets.QFrame.HLine)
        self.item_line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.item_line.setObjectName("item_line")
        self.item_line_2 = QtWidgets.QFrame(self.page_4)
        self.item_line_2.setGeometry(QtCore.QRect(0, 450, 401, 16))
        self.item_line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.item_line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.item_line_2.setObjectName("item_line_2")
        self.logo_item = QtWidgets.QLabel(self.page_4)
        self.logo_item.setGeometry(QtCore.QRect(90,10,220,120))
        self.logo_item.setText("")
        self.logo_item.setPixmap(QtGui.QPixmap("../images/Inno.png"))
        self.logo_item.setScaledContents(True)
        self.logo_item.setObjectName("logo_item")
        self.numitems.setObjectName("numitems")
        self.info_label = QtWidgets.QLabel(self.page_4)
        self.info_label.setGeometry(QtCore.QRect(130, 540, 131, 31))
        self.info_label.setText("")
        self.info_label.setAlignment(QtCore.Qt.AlignCenter)
        self.info_label.setObjectName("info_label")

###################################################################################################################################
#######################                             page 5 - shopping cart                                  #######################
###################################################################################################################################

        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.stackedWidget.addWidget(self.page_5)
        self.remove_button = QtWidgets.QPushButton(self.page_5)
        self.remove_button.setGeometry(QtCore.QRect(270, 430, 101, 31))
        self.remove_button.setObjectName("remove_button")
        self.cart_back_button = QtWidgets.QPushButton(self.page_5)
        self.cart_back_button.setGeometry(QtCore.QRect(20, 530, 101, 41))
        self.cart_back_button.setObjectName("cart_back_button")
        self.cart_listWidget = QtWidgets.QListWidget(self.page_5)
        self.cart_listWidget.setGeometry(QtCore.QRect(20, 69, 360, 241))
        self.cart_listWidget.setObjectName("cart_listWidget")
        self.users_sc = QtWidgets.QLabel(self.page_5)
        self.users_sc.setGeometry(QtCore.QRect(20, 15, 360, 40))
        self.users_sc.setAlignment(QtCore.Qt.AlignCenter)
        self.users_sc.setObjectName("users_sc")
        self.total_label = QtWidgets.QLabel(self.page_5)
        self.total_label.setGeometry(QtCore.QRect(30, 320, 41, 31))
        self.total_label.setObjectName("total_label")
        self.sc_line = QtWidgets.QFrame(self.page_5)
        self.sc_line.setGeometry(QtCore.QRect(0, 355, 400, 16))
        self.sc_line.setFrameShape(QtWidgets.QFrame.HLine)
        self.sc_line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.sc_line.setObjectName("sc_line")
        self.sc_line_2 = QtWidgets.QFrame(self.page_5)
        self.sc_line_2.setGeometry(QtCore.QRect(0, 500, 400, 16))
        self.sc_line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.sc_line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.sc_line_2.setObjectName("sc_line_2")
        self.cost_label = QtWidgets.QLabel(self.page_5)
        self.cost_label.setGeometry(QtCore.QRect(150, 320, 100, 31))
        self.cost_label.setAlignment(QtCore.Qt.AlignCenter)
        self.cost_label.setObjectName("cost_label")
        self.item_prompt = QtWidgets.QLabel(self.page_5)
        self.item_prompt.setGeometry(QtCore.QRect(0, 360, 400, 70))
        self.item_prompt.setAlignment(QtCore.Qt.AlignCenter)
        self.item_prompt.setObjectName("item_prompt")
        self.chng_quan_button = QtWidgets.QPushButton(self.page_5)
        self.chng_quan_button.setGeometry(QtCore.QRect(20, 430, 101, 31))
        self.chng_quan_button.setObjectName("chng_quan_button")
        self.checkout_button = QtWidgets.QPushButton(self.page_5)
        self.checkout_button.setGeometry(QtCore.QRect(270, 530, 101, 41))
        self.checkout_button.setObjectName("checkout_button")
        self.quantity_spin = QtWidgets.QSpinBox(self.page_5)
        self.quantity_spin.setGeometry(QtCore.QRect(50, 470, 42, 22))
        self.quantity_spin.setObjectName("quantity_spin")
        self.quantity_spin.setMinimum(1)
        self.quantity_spin.setValue(1)

###################################################################################################################################
#######################                             FONT SETTING                                            #######################
###################################################################################################################################

        # set the fonts
        self.font = QtGui.QFont()
        self.font.setFamily("Onyx")
        self.font.setPointSize(20)
        self.username_label.setFont(self.font)
        self.password_label.setFont(self.font)
        self.search_prompt_label.setFont(self.font)
        self.users_sc.setFont(self.font)
        
        self.font.setFamily("MS Shell Dlg 2")
        self.font.setPointSize(9)
        self.font.setBold(True)
        self.font.setWeight(75)
        self.Username.setFont(self.font)
        self.Password.setFont(self.font)

        self.font.setPointSize(7)
        self.font.setBold(True)
        self.font.setWeight(75)
        self.Instructions.setFont(self.font)
        
        self.font.setPointSize(12)
        self.font.setBold(True)
        self.font.setWeight(75)
        self.price.setFont(self.font)
        self.price_label.setFont(self.font)
        self.quantity.setFont(self.font)
        self.available_label.setFont(self.font)
        self.itemdescription.setFont(self.font)
        self.name.setFont(self.font)
        self.item_name.setFont(self.font)

        self.font = QtGui.QFont()
        self.font.setPointSize(12)
        self.description_text.setFont(self.font)
        self.available_status.setFont(self.font)
        self.numitems.setFont(self.font)
        
        self.font = QtGui.QFont()
        self.font.setPointSize(10)
        self.page_5.setFont(self.font)
        self.remove_button.setFont(self.font)
        self.cart_back_button.setFont(self.font)
        self.chng_quan_button.setFont(self.font)
        self.checkout_button.setFont(self.font)

###################################################################################################################################
#######################                             MENU BAR SETUP                                          #######################
###################################################################################################################################

        MainWindow.setCentralWidget(self.centralwidget)
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

        # set all the menu buttons to disabled until a user logs in
        self.actionShopping_Cart.setEnabled(False)
        self.actionChange_Username.setEnabled(False)
        self.actionChange_Password.setEnabled(False)
        self.actionLogout.setEnabled(False)

###################################################################################################################################
#######################                               Button SETUP                                          #######################
###################################################################################################################################

        # when login button is pressed, call login method
        self.login_button.clicked.connect(self.login)

        # when the user clicks the 'create account' button from the main page
        self.create_account_button.clicked.connect(self.clear_page)

        # Connect the createuser button with the createAcc function
        self.CreateButton.clicked.connect(self.createAcc)

        # Return user to login screen
        self.CancelButton.clicked.connect(lambda: self.switch_page(0))
                
        # when button is pressed, call search method
        self.search_button.clicked.connect(self.search_products)

        # logs a user out
        self.actionLogout.triggered.connect(self.logout)

        # if an item is clicked, go to item's page
        self.search_listWidget.itemClicked.connect(self.display_item_page)

        # adds an item the user's shopping cart
        self.addbutton.clicked.connect(self.add_to_shoppingcart)

        # navigate to the user's shopping cart
        self.actionShopping_Cart.triggered.connect(self.show_shoppingcart)

        # go back to the search results page from the shopping cart
        self.cart_back_button.clicked.connect(lambda: self.switch_page(2))

        # removes an item from the user's cart
        self.remove_button.clicked.connect(self.remove_item)

        # updates an item's quantity to what is designated in quantity box
        self.chng_quan_button.clicked.connect(self.change_quan)

        # asks the user if they want to purchase items
        self.checkout_button.clicked.connect(self.checkout)

        # # displays an item's page by performing a query on the database,
        # # that way, the item page displays current info
        # self.item_page_button.clicked.connect(self.cart_display_page)

        # # when back buttons are pressed, call switch to previous page
        self.item_back_button.clicked.connect(lambda: self.switch_page(self.stackedWidget.currentIndex()-1))
        self.search_back_button.clicked.connect(lambda: self.switch_page(self.stackedWidget.currentIndex()-1))

        # call function that initializes all button and label text
        self.retranslateUi(MainWindow)

        # sets the starting page to index 0 when app is started
        self.stackedWidget.setCurrentIndex(0)

        # Searches recursively for all child objects of the given object, and connects matching signals from them to slots of object that follow the following form:
        #       ``void on_<object name>_<signal name>(<signal parameters>)``;
        # See https://doc.qt.io/qt-5/qmetaobject.html#connectSlotsByName
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

#
# $$\      $$\                         $$\                                 $$$$$$$$\                              $$\     $$\                               
# $$$\    $$$ |                        $$ |                                $$  _____|                             $$ |    \__|                              
# $$$$\  $$$$ | $$$$$$\  $$$$$$\$$$$\  $$$$$$$\   $$$$$$\   $$$$$$\        $$ |   $$\   $$\ $$$$$$$\   $$$$$$$\ $$$$$$\   $$\  $$$$$$\  $$$$$$$\   $$$$$$$\ 
# $$\$$\$$ $$ |$$  __$$\ $$  _$$  _$$\ $$  __$$\ $$  __$$\ $$  __$$\       $$$$$\ $$ |  $$ |$$  __$$\ $$  _____|\_$$  _|  $$ |$$  __$$\ $$  __$$\ $$  _____|
# $$ \$$$  $$ |$$$$$$$$ |$$ / $$ / $$ |$$ |  $$ |$$$$$$$$ |$$ |  \__|      $$  __|$$ |  $$ |$$ |  $$ |$$ /        $$ |    $$ |$$ /  $$ |$$ |  $$ |\$$$$$$\  
# $$ |\$  /$$ |$$   ____|$$ | $$ | $$ |$$ |  $$ |$$   ____|$$ |            $$ |   $$ |  $$ |$$ |  $$ |$$ |        $$ |$$\ $$ |$$ |  $$ |$$ |  $$ | \____$$\ 
# $$ | \_/ $$ |\$$$$$$$\ $$ | $$ | $$ |$$$$$$$  |\$$$$$$$\ $$ |            $$ |   \$$$$$$  |$$ |  $$ |\$$$$$$$\   \$$$$  |$$ |\$$$$$$  |$$ |  $$ |$$$$$$$  |
# \__|     \__| \_______|\__| \__| \__|\_______/  \_______|\__|            \__|    \______/ \__|  \__| \_______|   \____/ \__| \______/ \__|  \__|\_______/ 
#

    # adds the 'change quantity' and 'change availability' buttons to the item page
    # for the employee
    def prepEmployee(self):
        # add the Change Quantity buttons and spin box and the Make Available button
        self.item_quan_spinBox = QtWidgets.QSpinBox(self.page_4)
        self.item_quan_spinBox.setGeometry(QtCore.QRect(11,470,101,22))
        self.item_quan_spinBox.setObjectName("item_quan_spinBox")
        self.item_quan_spinBox.setMinimum(1)
        self.item_quan_spinBox.setMaximum(999999)
        self.item_chng_quan = QtWidgets.QPushButton(self.page_4)
        self.item_chng_quan.setGeometry(QtCore.QRect(10, 500, 101, 31))
        self.item_chng_quan.setObjectName("item_chng_quan")
        self.item_mk_avail_button = QtWidgets.QPushButton(self.page_4)
        self.item_mk_avail_button.setGeometry(QtCore.QRect(280, 500, 101, 31))
        self.item_mk_avail_button.setObjectName("item_mk_avail_button")
        # put text into the buttons
        _translate = QtCore.QCoreApplication.translate
        self.item_chng_quan.setText(_translate("MainWindow", "Change Quantity"))
        self.item_mk_avail_button.setText(_translate("MainWindow", "Make Available"))
        # employees do not add items to their carts since they don't have any
        self.addbutton.setEnabled(False)
        # create the employee object from the API python file
        self.employee_object = Employee()
        # add functionality to employee buttons
        self.item_chng_quan.clicked.connect(self.employee_change_quan)
        self.item_mk_avail_button.clicked.connect(self.employee_change_avail)

        # change the color of the background
        self.page_2.setAutoFillBackground(True)
        self.page_3.setAutoFillBackground(True)
        self.page_4.setAutoFillBackground(True)
        p2 = self.page_2.palette()
        p3 = self.page_3.palette()
        p4 = self.page_4.palette()
        p2.setColor(self.page_2.backgroundRole(), Qt.cyan)
        p3.setColor(self.page_3.backgroundRole(), Qt.cyan)
        p4.setColor(self.page_4.backgroundRole(), Qt.cyan)
        self.page_2.setPalette(p2)
        self.page_3.setPalette(p3)
        self.page_4.setPalette(p4)

    # initializes all the buttons and labels to the appropriate text
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Innoventory"))
        self.search_prompt_label.setText(_translate("MainWindow", "What are you looking for?"))
        self.search_button.setText(_translate("MainWindow", "Search"))
        self.username_label.setText(_translate("MainWindow", "Username"))
        self.password_label.setText(_translate("MainWindow", "Password"))
        self.login_button.setText(_translate("MainWindow", "Login"))
        self.create_account_button.setText(_translate("MainWindow", "Create Account"))
        # self.groupBoxCA.setTitle(_translate("MainWindow", "Input field"))
        self.Username.setText(_translate("MainWindow", "Username"))
        self.Password.setText(_translate("MainWindow", "Password"))
        self.CancelButton.setText(_translate("MainWindow", "Cancel"))
        self.CreateButton.setText(_translate("MainWindow", "Create User"))
        self.item_back_button.setText(_translate("MainWindow", "Back"))
        self.search_back_button.setText(_translate("MainWindow", "Back"))
        self.addbutton.setText(_translate("MainWindow", "Add to Cart"))
        self.name.setText(_translate("MainWindow", "Name:"))
        self.item_name.setText(_translate("MainWindow", "Name of item"))
        self.itemdescription.setText(_translate("MainWindow", "Description:"))
        self.description_text.setText(_translate("MainWindow", "Description"))
        self.quantity.setText(_translate("MainWindow", "Quantity: "))
        self.numitems.setText(_translate("MainWindow", "999999"))
        self.remove_button.setText(_translate("MainWindow", "Remove Item"))
        self.cart_back_button.setText(_translate("MainWindow", "Back"))
        self.users_sc.setText(_translate("MainWindow", "Your Shopping Cart"))
        self.total_label.setText(_translate("MainWindow", "Total: "))
        self.cost_label.setText(_translate("MainWindow", "cost"))
        self.item_prompt.setText(_translate("MainWindow", "Click an item to iteract"))
        # self.item_page_button.setText(_translate("MainWindow", "Go to item page"))
        self.chng_quan_button.setText(_translate("MainWindow", "Update Quantity"))
        self.checkout_button.setText(_translate("MainWindow", "Checkout"))
        self.menuYour_Shopping_Cart.setTitle(_translate("MainWindow", "Your Account"))
        self.menuUpdate_Credentials.setTitle(_translate("MainWindow", "Update Credentials"))
        self.actionShopping_Cart.setText(_translate("MainWindow", "Shopping Cart"))
        self.actionChange_Username.setText(_translate("MainWindow", "Change Username"))
        self.actionChange_Password.setText(_translate("MainWindow", "Change Password"))
        self.actionLogout.setText(_translate("MainWindow", "Logout"))
        self.price_label.setText(_translate("MainWindow", "Price:"))
        self.price.setText(_translate("MainWindow", "$"))
        self.available_label.setText(_translate("MainWindow", "Available?"))
        self.available_status.setText(_translate("MainWindow", "Yes/No"))
#
#  ________  ________  ________  _______           ________                             ___       ________  ________  ___  ________      
# |\   __  \|\   __  \|\   ____\|\  ___ \         |\   __  \                           |\  \     |\   __  \|\   ____\|\  \|\   ___  \    
# \ \  \|\  \ \  \|\  \ \  \___|\ \   __/|        \ \  \|\  \        ____________      \ \  \    \ \  \|\  \ \  \___|\ \  \ \  \\ \  \   
#  \ \   ____\ \   __  \ \  \  __\ \  \_|/__       \ \  \\\  \      |\____________\     \ \  \    \ \  \\\  \ \  \  __\ \  \ \  \\ \  \  
#   \ \  \___|\ \  \ \  \ \  \|\  \ \  \_|\ \       \ \  \\\  \     \|____________|      \ \  \____\ \  \\\  \ \  \|\  \ \  \ \  \\ \  \ 
#    \ \__\    \ \__\ \__\ \_______\ \_______\       \ \_______\                          \ \_______\ \_______\ \_______\ \__\ \__\\ \__\
#     \|__|     \|__|\|__|\|_______|\|_______|        \|_______|                           \|_______|\|_______|\|_______|\|__|\|__| \|__|
#
    # attempt to log in to Innoventory with username and password offered
    def login(self):
        if self.username_textbox.text() != "" and self.password_textbox.text() != "":
            user = Login()
            username_password = {  'username': self.username_textbox.text(), 
                                        'password': self.password_textbox.text()
                                    }
            _, login_success, self.userType = user.login(username_password)
            self.login_result(login_success, username_password)

    # allow user in if credentials are verified; block otherwise
    def login_result(self, login_success, username_password):
        # if the user logged in successfully and they are a customer
        if login_success and self.userType:
            # create the shopping cart object for shopping cart additions, removals, and modifications
            self.shopping_cart_object = ShoppingCart({'username': username_password['username']})
            # create a shopping cart copy to prevent multiple database queries (like when checking if an item is already in the cart before adding it)
            self.shopping_cart_list = self.shopping_cart_object.readShoppingcart()
            # re-enable menu bar buttons
            self.actionShopping_Cart.setEnabled(True)
            # self.actionChange_Username.setEnabled(True)
            # self.actionChange_Password.setEnabled(True)
            self.username_textbox.setText("")
            self.password_textbox.setText("")
            self.failure_notif.setText("")
            self.actionLogout.setEnabled(True)
            self.switch_page(2)
        # if the login was successful and the user is not a customer (i.e. an employee)
        elif login_success and not self.userType:
            # prepares the app for viewing by a employee
            self.prepEmployee()
            self.username_textbox.setText("")
            self.password_textbox.setText("")
            self.failure_notif.setText("")
            self.actionLogout.setEnabled(True)
            self.switch_page(2)
        else:
            self.failure_notif.setText("Failed attempt.\nPlease try again.")

    # log the user out and return them to the login page       
    def logout(self):
        if self.userType:
            self.actionShopping_Cart.setEnabled(False)
            self.actionChange_Username.setEnabled(False)
            self.actionChange_Password.setEnabled(False)
        self.actionLogout.setEnabled(False)
        self.switch_page(0)
#
#  ________  ________  ________  _______            _____                             ________  ________  _______   ________  _________  _______           ________  ________  ________  ________  ___  ___  ________   _________   
# |\   __  \|\   __  \|\   ____\|\  ___ \          / __  \                           |\   ____\|\   __  \|\  ___ \ |\   __  \|\___   ___\\  ___ \         |\   __  \|\   ____\|\   ____\|\   __  \|\  \|\  \|\   ___  \|\___   ___\ 
# \ \  \|\  \ \  \|\  \ \  \___|\ \   __/|        |\/_|\  \        ____________      \ \  \___|\ \  \|\  \ \   __/|\ \  \|\  \|___ \  \_\ \   __/|        \ \  \|\  \ \  \___|\ \  \___|\ \  \|\  \ \  \\\  \ \  \\ \  \|___ \  \_| 
#  \ \   ____\ \   __  \ \  \  __\ \  \_|/__      \|/ \ \  \      |\____________\     \ \  \    \ \   _  _\ \  \_|/_\ \   __  \   \ \  \ \ \  \_|/__       \ \   __  \ \  \    \ \  \    \ \  \\\  \ \  \\\  \ \  \\ \  \   \ \  \  
#   \ \  \___|\ \  \ \  \ \  \|\  \ \  \_|\ \          \ \  \     \|____________|      \ \  \____\ \  \\  \\ \  \_|\ \ \  \ \  \   \ \  \ \ \  \_|\ \       \ \  \ \  \ \  \____\ \  \____\ \  \\\  \ \  \\\  \ \  \\ \  \   \ \  \ 
#    \ \__\    \ \__\ \__\ \_______\ \_______\          \ \__\                          \ \_______\ \__\\ _\\ \_______\ \__\ \__\   \ \__\ \ \_______\       \ \__\ \__\ \_______\ \_______\ \_______\ \_______\ \__\\ \__\   \ \__\
#     \|__|     \|__|\|__|\|_______|\|_______|           \|__|                           \|_______|\|__|\|__|\|_______|\|__|\|__|    \|__|  \|_______|        \|__|\|__|\|_______|\|_______|\|_______|\|_______|\|__| \|__|    \|__|
#
    # clears the input fields and labels on create account page
    def clear_page(self):
        self.UserInput.setText("")
        self.PassInput.setText("")
        self.Instructions.setText("Please enter the username and password for your new account")
        self.switch_page(1)

    # Once the user has filled in the input fields, check to see if they are
    # can create an account. If they can, create account
    def createAcc(self):
        username = self.UserInput.text()
        password = self.PassInput.text()

        # If the user is lazy
        if username == '' or password == '':
            self.error(0)
        
        # Upload the requested info into our database
        else:
            creation = UserManager()
            if creation.createUser({'username': username, 'password': password}):
                self.Instructions.setText("Success! Your account has been created!")
                self.CancelButton.setText("Login")

            else:
                self.error(1)

    # If the user does something weird, raise error.
    def error(self, cause):
        if cause == 0:
            self.Instructions.setText("Error: Please enter a value for username and password")
        elif cause == 1:
            self.Instructions.setText("Error: That username has already been taken")
#
#  ________  ________  ________  _______            _______                             ________  _______   ________  ________  ________  ___  ___     
# |\   __  \|\   __  \|\   ____\|\  ___ \          /  ___  \                           |\   ____\|\  ___ \ |\   __  \|\   __  \|\   ____\|\  \|\  \    
# \ \  \|\  \ \  \|\  \ \  \___|\ \   __/|        /__/|_/  /|        ____________      \ \  \___|\ \   __/|\ \  \|\  \ \  \|\  \ \  \___|\ \  \\\  \   
#  \ \   ____\ \   __  \ \  \  __\ \  \_|/__      |__|//  / /       |\____________\     \ \_____  \ \  \_|/_\ \   __  \ \   _  _\ \  \    \ \   __  \  
#   \ \  \___|\ \  \ \  \ \  \|\  \ \  \_|\ \         /  /_/__      \|____________|      \|____|\  \ \  \_|\ \ \  \ \  \ \  \\  \\ \  \____\ \  \ \  \ 
#    \ \__\    \ \__\ \__\ \_______\ \_______\       |\________\                           ____\_\  \ \_______\ \__\ \__\ \__\\ _\\ \_______\ \__\ \__\
#     \|__|     \|__|\|__|\|_______|\|_______|        \|_______|                          |\_________\|_______|\|__|\|__|\|__|\|__|\|_______|\|__|\|__|
#                                                                                         \|_________|                                                 
#
    # run an item search using the API
    def search_products(self):
        # only run the search if the textbox has text in it
        if self.search_box.text() != "":
            # since all items in the store are in lowercase, convert search string to lowercase too
            search_string = self.search_box.text().lower()
            self.search_result = self.parse_results(self.search_attempt.search({'item': search_string}))
            # if there are search results, switch to the next page
            if self.search_result != {}:
                self.no_results_notif.setText("")
                self.display_results()
                self.switch_page(3)
            # if no search results, let user know
            else:
                self.no_results_notif.setText("No results found")
        self.search_box.setText("")

    # Returns a dictionary of dictionaries from a search
    # Schema:
    # { 
    #       '0': {'item':<item name>, 'quantity':###, ...},
    #       '1': {'item':<item name>, 'quantity':###, ...}},
    #       '2': {'item':<item name>, 'quantity':###, ...}},
    #       ...
    # }
    def parse_results(self, result):
        items = {}
        counter = 0
        for doc in result:
            for item in doc:
                items[str(counter)] = item
                counter += 1
        return items
#
#  ________  ________  ________  _______           ________                             ________  _______   ________  ________  ________  ___  ___          ________  _______   ________  ___  ___  ___   _________  ________      
# |\   __  \|\   __  \|\   ____\|\  ___ \         |\_____  \                           |\   ____\|\  ___ \ |\   __  \|\   __  \|\   ____\|\  \|\  \        |\   __  \|\  ___ \ |\   ____\|\  \|\  \|\  \ |\___   ___\\   ____\     
# \ \  \|\  \ \  \|\  \ \  \___|\ \   __/|        \|____|\ /_        ____________      \ \  \___|\ \   __/|\ \  \|\  \ \  \|\  \ \  \___|\ \  \\\  \       \ \  \|\  \ \   __/|\ \  \___|\ \  \\\  \ \  \\|___ \  \_\ \  \___|_    
#  \ \   ____\ \   __  \ \  \  __\ \  \_|/__            \|\  \      |\____________\     \ \_____  \ \  \_|/_\ \   __  \ \   _  _\ \  \    \ \   __  \       \ \   _  _\ \  \_|/_\ \_____  \ \  \\\  \ \  \    \ \  \ \ \_____  \   
#   \ \  \___|\ \  \ \  \ \  \|\  \ \  \_|\ \          __\_\  \     \|____________|      \|____|\  \ \  \_|\ \ \  \ \  \ \  \\  \\ \  \____\ \  \ \  \       \ \  \\  \\ \  \_|\ \|____|\  \ \  \\\  \ \  \____\ \  \ \|____|\  \  
#    \ \__\    \ \__\ \__\ \_______\ \_______\        |\_______\                           ____\_\  \ \_______\ \__\ \__\ \__\\ _\\ \_______\ \__\ \__\       \ \__\\ _\\ \_______\____\_\  \ \_______\ \_______\ \__\  ____\_\  \ 
#     \|__|     \|__|\|__|\|_______|\|_______|        \|_______|                          |\_________\|_______|\|__|\|__|\|__|\|__|\|_______|\|__|\|__|        \|__|\|__|\|_______|\_________\|_______|\|_______|\|__| |\_________\
#                                                                                         \|_________|                                                                            \|_________|                         \|_________|
#
    # print search results to a list widget
    def display_results(self):
        # clear any pre-existing results from previous search
        self.search_listWidget.clear()
        for count in range(0,len(self.search_result)):
            # adds one item from 'search_result' to the search results list widget
            self.search_listWidget.addItem(QtWidgets.QListWidgetItem(self.search_result[str(count)]["item"].title()))
#
#  ________  ________  ________  _______           ___   ___                             ___  _________  _______   _____ ______           ________  ________  ________  _______      
# |\   __  \|\   __  \|\   ____\|\  ___ \         |\  \ |\  \                           |\  \|\___   ___\\  ___ \ |\   _ \  _   \        |\   __  \|\   __  \|\   ____\|\  ___ \     
# \ \  \|\  \ \  \|\  \ \  \___|\ \   __/|        \ \  \\_\  \        ____________      \ \  \|___ \  \_\ \   __/|\ \  \\\__\ \  \       \ \  \|\  \ \  \|\  \ \  \___|\ \   __/|    
#  \ \   ____\ \   __  \ \  \  __\ \  \_|/__       \ \______  \      |\____________\     \ \  \   \ \  \ \ \  \_|/_\ \  \\|__| \  \       \ \   ____\ \   __  \ \  \  __\ \  \_|/__  
#   \ \  \___|\ \  \ \  \ \  \|\  \ \  \_|\ \       \|_____|\  \     \|____________|      \ \  \   \ \  \ \ \  \_|\ \ \  \    \ \  \       \ \  \___|\ \  \ \  \ \  \|\  \ \  \_|\ \ 
#    \ \__\    \ \__\ \__\ \_______\ \_______\             \ \__\                          \ \__\   \ \__\ \ \_______\ \__\    \ \__\       \ \__\    \ \__\ \__\ \_______\ \_______\
#     \|__|     \|__|\|__|\|_______|\|_______|              \|__|                           \|__|    \|__|  \|_______|\|__|     \|__|        \|__|     \|__|\|__|\|_______|\|_______|
#                                                                                                                                                                                 
    # fills the item page with information from 'item'
    def display_item_page(self, item):
        self.item = item
        self.info_label.setText("")
        product = self.search_result[str(self.search_listWidget.row(self.item))]
        # print item name
        self.item_name.setText(product['item'].title())
        # print item details, which are stored in a list in the database
        detail_string = ""
        if "details" in product:
            for num in range(0,len(product["details"])):
                detail_string += '-' + str(product["details"]["name" + str(num)]) + "\n"
        else:
            detail_string = '-'
        self.description_text.setText(detail_string.title())
        # print product quantity
        if "quantity" in product:
            self.numitems.setText(str(product["quantity"]))
        else:
            self.numitems.setText("-")
        # print product availability
        if product['availability']:
            self.available_status.setText("Yes")
        else:
            self.available_status.setText("No")
        # print product price
        self.price.setText('$' + str('{0:.2f}'.format(product['price'])))
        # if user is an employee, change the text of the availability button and quantity spinbox
        if not self.userType:
            self.item_quan_spinBox.setValue(product['quantity'])
            if product['availability']:
                self.item_mk_avail_button.setText("Make Unavailable")
            else:
                self.item_mk_avail_button.setText("Make Available")
        self.switch_page(4)

    # change the quantity of an item
    def employee_change_quan(self):
        product = self.search_result[str(self.search_listWidget.row(self.item))]
        # changes the quantity of the product, returns the updated quantity, and updates quantity on item page
        new_quan = self.employee_object.change_quantity(product,self.item_quan_spinBox.value())
        self.numitems.setText(str(new_quan))
        self.search_result[str(self.search_listWidget.row(self.item))]['quantity'] = new_quan

    # change the quantity of an item
    def employee_change_avail(self):
        product = self.search_result[str(self.search_listWidget.row(self.item))]
        # if product is available, make it not
        if product['availability']:
            new_avail = self.employee_object.change_availability(product,False)
            self.search_result[str(self.search_listWidget.row(self.item))]['availability'] = new_avail
            self.available_status.setText("No")
            self.item_mk_avail_button.setText("Make Available")
        # if product is not available, make it available
        else:
            new_avail = self.employee_object.change_availability(product,True)
            self.search_result[str(self.search_listWidget.row(self.item))]['availability'] = new_avail
            self.item_mk_avail_button.setText("Make Unavailable")
            self.available_status.setText("Yes")

    # adds an item to the customer's shopping cart
    def add_to_shoppingcart(self):
        product = self.search_result[str(self.search_listWidget.row(self.item))]
        # prevents customers from adding items to their cart that are unavailable or aren't in stock
        if product['availability'] and product['quantity']:
            if (product not in self.shopping_cart_list):
                product['quantity'] = 1
                self.shopping_cart_object.addCart(product)
                # the shopping cart list will track all items in customer's shopping cart
                self.shopping_cart_list.append(product)
                self.info_label.setText("Added to cart!")
            else:
                self.info_label.setText("Already in cart!")
        else:
            self.info_label.setText("Product unavailable")
#
#  ________  ________  ________  _______           ________                              ________  ___  ___  ________  ________  ________  ___  ________   ________          ________  ________  ________  _________   
# |\   __  \|\   __  \|\   ____\|\  ___ \         |\   ____\                            |\   ____\|\  \|\  \|\   __  \|\   __  \|\   __  \|\  \|\   ___  \|\   ____\        |\   ____\|\   __  \|\   __  \|\___   ___\ 
# \ \  \|\  \ \  \|\  \ \  \___|\ \   __/|        \ \  \___|_         ____________      \ \  \___|\ \  \\\  \ \  \|\  \ \  \|\  \ \  \|\  \ \  \ \  \\ \  \ \  \___|        \ \  \___|\ \  \|\  \ \  \|\  \|___ \  \_| 
#  \ \   ____\ \   __  \ \  \  __\ \  \_|/__       \ \_____  \       |\____________\     \ \_____  \ \   __  \ \  \\\  \ \   ____\ \   ____\ \  \ \  \\ \  \ \  \  ___       \ \  \    \ \   __  \ \   _  _\   \ \  \  
#   \ \  \___|\ \  \ \  \ \  \|\  \ \  \_|\ \       \|____|\  \      \|____________|      \|____|\  \ \  \ \  \ \  \\\  \ \  \___|\ \  \___|\ \  \ \  \\ \  \ \  \|\  \       \ \  \____\ \  \ \  \ \  \\  \|   \ \  \ 
#    \ \__\    \ \__\ \__\ \_______\ \_______\        ____\_\  \                            ____\_\  \ \__\ \__\ \_______\ \__\    \ \__\    \ \__\ \__\\ \__\ \_______\       \ \_______\ \__\ \__\ \__\\ _\    \ \__\
#     \|__|     \|__|\|__|\|_______|\|_______|       |\_________\                          |\_________\|__|\|__|\|_______|\|__|     \|__|     \|__|\|__| \|__|\|_______|        \|_______|\|__|\|__|\|__|\|__|    \|__|
#                                                    \|_________|                          \|_________|                                                                                                                
#
    # prepares the shopping cart page
    def show_shoppingcart(self):
        self.item_prompt.setText("Click an item to interact")
        self.init_shoppingcart()
        self.switch_page(5)

    # will fill the list widget on the shopping cart page with all the items in the 
    # user's shopping cart
    def init_shoppingcart(self):
        self.cart_listWidget.clear()
        for product in self.shopping_cart_list:
            item = QtWidgets.QListWidgetItem("Item: " + product['item'].title() + " | Count: " + str(product['quantity']) + " | Price: " + str('{0:.2f}'.format(product['price'])))
            self.cart_listWidget.addItem(item)
        self.findPrice()
    
    # calculates the total price of all items in cart and updates the cost_label
    def findPrice(self):
        total_price = 0.0
        for item in self.shopping_cart_list:
            total_price += item['price'] * item['quantity']
        self.cost_label.setText('$' + str('{0:.2f}'.format(total_price)))

    # Removes the selected item from the cart
    def remove_item(self):
        # only remove if an item is selected and if there are items in the cart
        if self.cart_listWidget.count() and self.cart_listWidget.currentRow() > -1:
            item = self.cart_listWidget.currentRow()
            # remove the item from the database shopping cart
            self.shopping_cart_object.removeCart(self.shopping_cart_list[item])
            # remove the item from the local shopping cart variable (database shopping cart copy)
            self.shopping_cart_list.pop(item)
            # get rid of the item from the list widget
            self.cart_listWidget.takeItem(item)
            self.findPrice()

    # changes the quantity of the item in the user's cart with the value in the quantity spin box
    def change_quan(self):
        # only change an item's quantity if there are items in the cart AND if an item is selected
        if self.cart_listWidget.count() and self.cart_listWidget.currentRow() > -1:
            item = self.cart_listWidget.currentRow()
            # updates quantity in database
            self.shopping_cart_object.changeQuan(self.shopping_cart_list[item], self.quantity_spin.value())
            # updates quantity in local shopping cart
            item = self.shopping_cart_list[item]
            item['quantity'] = self.quantity_spin.value()
            # updates the item in the list widget
            self.cart_listWidget.item(item).setText("Item: " + item['item'].title() + " | Count: " + str(item['quantity']) + " | Price: " + str('{0:.2f}'.format(item['price'])))
            # recalculate shopping cart total
            self.findPrice()

    # prompts user if they are sure they want to purchase the items in their cart.
    # After being prompted, they must click the prompt button again to confirm.
    # Empties the cart after purchase
    def checkout(self):
        # again, you can't buy items if there are none in your cart
        if self.cart_listWidget.count():
            if self.prompt_confirm == False:
                self.checkout_button.setText("Are you sure?")
                self.prompt_confirm = True
            else:
                self.item_prompt.setText("Thank you for your purchase!\nPress \"Back\" to return to search")
                self.prompt_confirm = False
                self.cart_listWidget.clear()
                self.shopping_cart_list = []
                self.shopping_cart_object.emptyCart()

#################################################################################################################

    # will switch to widget representing page 'next_page'.
    # 'next_page` can be a stacked_widget type or integer
    def switch_page(self, next_page):
        self.stackedWidget.setCurrentIndex(next_page)

#
#                             $$\      $$\           $$\           
#                             $$$\    $$$ |          \__|          
#                             $$$$\  $$$$ | $$$$$$\  $$\ $$$$$$$\  
#                             $$\$$\$$ $$ | \____$$\ $$ |$$  __$$\ 
#                             $$ \$$$  $$ | $$$$$$$ |$$ |$$ |  $$ |
#                             $$ |\$  /$$ |$$  __$$ |$$ |$$ |  $$ |
#                             $$ | \_/ $$ |\$$$$$$$ |$$ |$$ |  $$ |
#                             \__|     \__| \_______|\__|\__|  \__|
#                      
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())