# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'New_DB.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import null as null
from PyQt5 import QtCore, QtGui, QtWidgets
from influxdb import InfluxDBClient
import pandas as pd
from PyQt5.QtWidgets import QInputDialog, QLineEdit
import self

class Ui_OtherWindow(object):



    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(534, 270)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 10, 491, 201))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.frame)
        self.plainTextEdit.setGeometry(QtCore.QRect(190, 30, 271, 51))
        self.plainTextEdit.setStyleSheet("font-size:20px; font-family:Times New Roman;")

        self.lineedit= self.plainTextEdit.setObjectName("plainTextEdit")


        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(80, 30, 111, 41))
        self.label.setStyleSheet("font-size:15px;font-family:Tomes New Roman")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(240, 110, 141, 31))
        self.pushButton.setStyleSheet("font-size:15px; font-family:Times New Roman;")
        self.pushButton.setObjectName("pushButton")


        self.pushButton.clicked.connect(self.create_db)


        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 534, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)




    def create_db(self):
        client = InfluxDBClient(host='localhost', port=8086)
        client.use_database("demo")

        file_path = r'C:\Users\hp\Desktop\C2ImportCalEventSample.csv'
        csvReader = pd.read_csv(file_path)
        print(csvReader.shape)
        print(csvReader.columns)

        for row_index, row in csvReader.iterrows():
            tags = row[0]
            fieldValue = row[2]

            json_body = [{
                "measurement": "table7",
                "tags": {
                    "Reference": tags
                },
                "fields": {
                    "value": fieldValue
                }
            }]

            print(json_body)
            client.write_points(json_body)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Enter DB Name"))
        self.pushButton.setText(_translate("MainWindow", "Create"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QOtherWindow()
    ui = Ui_OtherWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

