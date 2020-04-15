# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'checkout.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from pymongo import MongoClient

cluster = MongoClient("passwordinfo")
db = cluster["Innoventory"]
collection = db["Products"]

results = collection.find_one({"item": "Currants"})
value = str(results["quantity"])

class Ui_CheckoutWindow(object):

    def __init__(self, item):
        self.item = item

    def setupUi(self, CheckoutWindow):
        CheckoutWindow.setObjectName("CheckoutWindow")
        CheckoutWindow.resize(610, 461)
        font = QtGui.QFont()
        font.setPointSize(12)
        CheckoutWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(CheckoutWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 480, 56, 17))
        self.pushButton.setObjectName("pushButton")
        self.nobutton = QtWidgets.QPushButton(self.centralwidget)
        self.nobutton.setGeometry(QtCore.QRect(20, 360, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.nobutton.setFont(font)
        self.nobutton.setObjectName("nobutton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(440, 360, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 180, 351, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.itemname = QtWidgets.QLabel(self.centralwidget)
        self.itemname.setGeometry(QtCore.QRect(390, 190, 171, 21))
        self.itemname.setObjectName("itemname")
        self.Proceed = QtWidgets.QLabel(self.centralwidget)
        self.Proceed.setGeometry(QtCore.QRect(220, 280, 191, 41))
        self.Proceed.setObjectName("Proceed")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 170, 631, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(0, 330, 781, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.photo = QtWidgets.QLabel(self.centralwidget)
        self.photo.setGeometry(QtCore.QRect(190, 20, 211, 141))
        self.photo.setFrameShape(QtWidgets.QFrame.Box)
        self.photo.setLineWidth(2)
        self.photo.setText("")
        self.photo.setPixmap(QtGui.QPixmap("currants.jpg"))
        self.photo.setScaledContents(True)
        self.photo.setObjectName("photo")
        CheckoutWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(CheckoutWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 610, 18))
        self.menubar.setObjectName("menubar")
        CheckoutWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(CheckoutWindow)
        self.statusbar.setObjectName("statusbar")
        CheckoutWindow.setStatusBar(self.statusbar)

        self.retranslateUi(CheckoutWindow)
        QtCore.QMetaObject.connectSlotsByName(CheckoutWindow)

        # Button actions
        self.pushButton_2.clicked.connect(self.showcheckout)


    def retranslateUi(self, CheckoutWindow):
        _translate = QtCore.QCoreApplication.translate
        CheckoutWindow.setWindowTitle(_translate("CheckoutWindow", "MainWindow"))
        self.pushButton.setText(_translate("CheckoutWindow", "PushButton"))
        self.nobutton.setText(_translate("CheckoutWindow", "Back"))
        self.pushButton_2.setText(_translate("CheckoutWindow", "Yes"))
        self.label.setText(_translate("CheckoutWindow", "You are checking out the follow item: "))
        self.itemname.setText(_translate("CheckoutWindow", self.item))
        self.Proceed.setText(_translate("CheckoutWindow", "Proceed?"))

    def showcheckout(self):
        self.Proceed.setText("Item was added to cart!")
        self.Proceed.adjustSize()
        self.updatedb()

    def updatedb(self):
        myquery = {"item": self.item}
        newvalue = {"$inc": {"quantity": -1}}
        collection.update_one(myquery, newvalue)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CheckoutWindow = QtWidgets.QMainWindow()
    ui = Ui_CheckoutWindow("item")
    ui.setupUi(CheckoutWindow)
    CheckoutWindow.show()
    sys.exit(app.exec_())
