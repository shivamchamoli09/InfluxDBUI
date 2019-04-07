# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'create_measurement.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd
from influxdb import InfluxDBClient
from influxdb import DataFrameClient

from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd
from influxdb import InfluxDBClient
from influxdb import DataFrameClient
from create_table import App

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(614, 300)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(0, 0, 611, 301))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.measurement_name = QtWidgets.QLineEdit(self.frame)
        self.measurement_name.setGeometry(QtCore.QRect(130, 60, 291, 22))
        self.measurement_name.setObjectName("measurement_name")
        self.field_name = QtWidgets.QLineEdit(self.frame)
        self.field_name.setGeometry(QtCore.QRect(130, 130, 291, 22))
        self.field_name.setObjectName("field_name")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(14, 60, 101, 20))
        self.label.setStyleSheet("font-family:Times New Roman; font-size:17px")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(60, 130, 55, 16))
        self.label_2.setStyleSheet("font-family:Times New Roman; font-size:17px")
        self.label_2.setObjectName("label_2")
        self.add_button = QtWidgets.QPushButton(self.frame)
        self.add_button.setGeometry(QtCore.QRect(480, 100, 93, 28))
        self.add_button.setObjectName("add_button")

        self.add_button.clicked.connect(self.create_measurement)


        self.done_button = QtWidgets.QPushButton(self.frame)
        self.done_button.setGeometry(QtCore.QRect(480, 190, 93, 28))
        self.done_button.setObjectName("done_button")

        self.done_button.clicked.connect(self.create_table)

        self.cancel_button = QtWidgets.QPushButton(self.frame)
        self.cancel_button.setGeometry(QtCore.QRect(480, 230, 93, 28))
        self.cancel_button.setObjectName("cancel_button")

        self.cancel_button.clicked.connect(sys.exit)

        self.field_names = QtWidgets.QLabel(self.frame)
        self.field_names.setGeometry(QtCore.QRect(10, 209, 431, 51))
        self.field_names.setStyleSheet("font-family:Times New Roman; font-size:17px")
        self.field_names.setText("")
        self.field_names.setObjectName("field_names")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Measurement:"))
        self.label_2.setText(_translate("Form", "Fields:"))
        self.add_button.setText(_translate("Form", "Add"))
        self.done_button.setText(_translate("Form", "Done"))
        self.cancel_button.setText(_translate("Form", "Cancel"))

    def create_measurement(self):
        self.field_names.setText(self.field_names.text()  + "" + self.field_name.text() + ", ")
        self.field_name.setText("")

        client =  InfluxDBClient('localhost' , 8086)

         ## client.create_database(self.measurement_name.text() )
       
         ##client = DataFrameClient('localhost', 8086, 'root', 'root', self.measurement_name.text())

    #############################################Create pandas DataFrame
        ## df = pd.DataFrame(data=list(range(30)),
           ##            index=pd.date_range(start='2018-11-16',
              ##                             periods=30, freq='H'), columns=['0'])


    #############################################Write DataFrame
         ##client.write_points(df,self.measurement_name.text())

   
    def create_table(self):
        self.window=QtWidgets.QWidget()
        self.ui= App()
        self.ui.__init__(self.window)
        self.window.move(self.centerPoint)
        self.window.show()
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

