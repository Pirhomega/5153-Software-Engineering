# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'item_mod.ui'
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
        self.backButton = QtWidgets.QPushButton(self.centralwidget)
        self.backButton.setGeometry(QtCore.QRect(10, 540, 101, 31))
        self.backButton.setObjectName("backButton")
        self.addbutton = QtWidgets.QPushButton(self.centralwidget)
        self.addbutton.setGeometry(QtCore.QRect(280, 540, 101, 31))
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
        self.labeltext.setGeometry(QtCore.QRect(140, 200, 251, 111))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labeltext.setFont(font)
        self.labeltext.setScaledContents(True)
        self.labeltext.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.labeltext.setWordWrap(True)
        self.labeltext.setObjectName("labeltext")
        self.itemdescription = QtWidgets.QLabel(self.centralwidget)
        self.itemdescription.setGeometry(QtCore.QRect(10, 300, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.itemdescription.setFont(font)
        self.itemdescription.setObjectName("itemdescription")
        self.description_text = QtWidgets.QLabel(self.centralwidget)
        self.description_text.setGeometry(QtCore.QRect(140, 310, 251, 131))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.description_text.setFont(font)
        self.description_text.setScaledContents(True)
        self.description_text.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.description_text.setWordWrap(True)
        self.description_text.setObjectName("description_text")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 170, 401, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(0, 510, 401, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.photo = QtWidgets.QLabel(self.centralwidget)
        self.photo.setGeometry(QtCore.QRect(10, 10, 381, 151))
        self.photo.setFrameShape(QtWidgets.QFrame.Box)
        self.photo.setLineWidth(2)
        self.photo.setText("")
        self.photo.setPixmap(QtGui.QPixmap("../Pictures/Saved Pictures/banana.jpg"))
        self.photo.setScaledContents(True)
        self.photo.setObjectName("photo")
        self.quantity = QtWidgets.QLabel(self.centralwidget)
        self.quantity.setGeometry(QtCore.QRect(10, 450, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.quantity.setFont(font)
        self.quantity.setObjectName("quantity")
        self.numitems = QtWidgets.QLabel(self.centralwidget)
        self.numitems.setGeometry(QtCore.QRect(140, 450, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.numitems.setFont(font)
        self.numitems.setObjectName("numitems")
        self.info_label = QtWidgets.QLabel(self.centralwidget)
        self.info_label.setGeometry(QtCore.QRect(130, 540, 131, 31))
        self.info_label.setText("")
        self.info_label.setAlignment(QtCore.Qt.AlignCenter)
        self.info_label.setObjectName("info_label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Item"))
        self.backButton.setText(_translate("MainWindow", "Back"))
        self.addbutton.setText(_translate("MainWindow", "Add to Cart"))
        self.itemname.setText(_translate("MainWindow", "Name:"))
        self.labeltext.setText(_translate("MainWindow", "Name of item"))
        self.itemdescription.setText(_translate("MainWindow", "Description:"))
        self.description_text.setText(_translate("MainWindow", "Description"))
        self.quantity.setText(_translate("MainWindow", "Quantity: "))
        self.numitems.setText(_translate("MainWindow", "Number"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
