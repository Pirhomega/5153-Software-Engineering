# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'item.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from pymongo import MongoClient
from checkout import Ui_CheckoutWindow

cluster = MongoClient("mongodb+srv://mStanley:Jankitup32@innoventory-vvoxp.azure.mongodb.net/test?retryWrites=true&w=majority")
db = cluster["Innoventory"]
collection = db["Products"]

results = collection.find_one({"item": "Currants"})
name = results["item"]
value = str(results["quantity"])

class Ui_MainWindow(object):
    def __init__(self):
        pass

    def openWindow(self):
        self.item = name
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_CheckoutWindow(self.item)
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(610, 461)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.backButton = QtWidgets.QPushButton(self.centralwidget)
        self.backButton.setGeometry(QtCore.QRect(10, 380, 101, 31))
        self.backButton.setObjectName("backButton")
        self.addbutton = QtWidgets.QPushButton(self.centralwidget)
        self.addbutton.setGeometry(QtCore.QRect(430, 380, 101, 31))
        self.addbutton.setObjectName("addbutton")
        self.itemname = QtWidgets.QLabel(self.centralwidget)
        self.itemname.setGeometry(QtCore.QRect(10, 190, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.itemname.setFont(font)
        self.itemname.setObjectName("itemname")
        self.labeltext = QtWidgets.QLabel(self.centralwidget)
        self.labeltext.setGeometry(QtCore.QRect(230, 200, 321, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labeltext.setFont(font)
        self.labeltext.setObjectName("labeltext")
        self.itemdescription = QtWidgets.QLabel(self.centralwidget)
        self.itemdescription.setGeometry(QtCore.QRect(10, 240, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.itemdescription.setFont(font)
        self.itemdescription.setObjectName("itemdescription")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(230, 240, 341, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 160, 621, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(0, 340, 621, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.photo = QtWidgets.QLabel(self.centralwidget)
        self.photo.setGeometry(QtCore.QRect(160, 10, 221, 151))
        self.photo.setFrameShape(QtWidgets.QFrame.Box)
        self.photo.setLineWidth(2)
        self.photo.setText("")
        self.photo.setPixmap(QtGui.QPixmap("../Pictures/Saved Pictures/banana.jpg"))
        self.photo.setScaledContents(True)
        self.photo.setObjectName("photo")
        self.quantity = QtWidgets.QLabel(self.centralwidget)
        self.quantity.setGeometry(QtCore.QRect(10, 300, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.quantity.setFont(font)
        self.quantity.setObjectName("quantity")
        self.numitems = QtWidgets.QLabel(self.centralwidget)
        self.numitems.setGeometry(QtCore.QRect(230, 310, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.numitems.setFont(font)
        self.numitems.setObjectName("numitems")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 610, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.addbutton.clicked.connect(self.openWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Item"))
        self.backButton.setText(_translate("MainWindow", "Back"))
        self.addbutton.setText(_translate("MainWindow", "Add to Cart"))
        self.itemname.setText(_translate("MainWindow", "Name:"))
        self.labeltext.setText(_translate("MainWindow", name))
        self.itemdescription.setText(_translate("MainWindow", "Description:"))
        self.label.setText(_translate("MainWindow", "Description"))
        self.quantity.setText(_translate("MainWindow", "Quantity: "))
        self.numitems.setText(_translate("MainWindow", value))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
