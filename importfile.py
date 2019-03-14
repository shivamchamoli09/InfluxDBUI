# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'importfile.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from sqlalchemy import true


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 331)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayout = QtWidgets.QFormLayout(self.centralwidget)
        self.formLayout.setObjectName("formLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 5, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setStyleSheet("font-size:18px; font-family:Times New Roman")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 4, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 7, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setStyleSheet("font-size:18px; font-family:Times New Roman")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 6, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setStyleSheet("font-size:18px; font-family:Times New Roman")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.radioButton = QtWidgets.QRadioButton(self.frame)
        self.radioButton.setStyleSheet("font-size:20px; font-family: Times New Roman")
        self.radioButton.setObjectName("radioButton")
        self.gridLayout.addWidget(self.radioButton, 1, 0, 1, 1)

        self.radioButton.toggled.connect(lambda:self.existingdb(self.radioButton))


        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 3, 0, 1, 1)
        self.radioButton_2 = QtWidgets.QRadioButton(self.frame)
        self.radioButton_2.setStyleSheet("font-size:20px; font-family: Times New Roman")
        self.radioButton_2.setObjectName("radioButton_2")
        self.gridLayout.addWidget(self.radioButton_2, 0, 0, 1, 1)

        self.radioButton_2.toggled.connect(lambda:self.newdb(self.radioButton_2))


        self.formLayout.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Import CSV File"))
        self.label_2.setText(_translate("MainWindow", "Enter Existing Database Name:"))
        self.label_3.setText(_translate("MainWindow", "Enter Table Name:"))
        self.label.setText(_translate("MainWindow", "New Database Name:"))
        self.radioButton.setText(_translate("MainWindow", "Insert Into Existing Database"))
        self.radioButton_2.setText(_translate("MainWindow", "Create New Database"))

    def newdb(self, radioButton_2):
          if radioButton_2.isChecked():
            print("Hello")
            self.lineEdit_2.setInputMask("a")

    def existingdb(self, radioButton):
          if radioButton.isChecked():
            print("2")
            self.lineEdit.setInputMask("a")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

