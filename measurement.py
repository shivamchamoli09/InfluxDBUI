# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'measurement.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import tkinter as tk
from tkinter import filedialog
import csv  
import json
from influxdb import InfluxDBClient
import glob
import os

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(455, 215)
        self.measurement_name_line = QtWidgets.QLineEdit(Form)
        self.measurement_name_line.setGeometry(QtCore.QRect(150, 30, 271, 25))
        self.measurement_name_line.setObjectName("measurement_name_line")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(40, 30, 111, 17))
        self.label.setStyleSheet("font-family:Times New Roman; font-size:17px")
        self.label.setObjectName("label")
        self.import_csv_btn = QtWidgets.QPushButton(Form)
        self.import_csv_btn.setGeometry(QtCore.QRect(150, 110, 111, 25))
        self.import_csv_btn.setStyleSheet("font-family:Times New Roman; font-size:17px")
        self.import_csv_btn.setObjectName("import_csv_btn")

        self.import_csv_btn.clicked.connect(self.import_csv)

        self.done_btn = QtWidgets.QPushButton(Form)
        self.done_btn.setGeometry(QtCore.QRect(310, 110, 89, 25))
        self.done_btn.setStyleSheet("font-family:Times New Roman; font-size:17px")
        self.done_btn.setObjectName("done_btn")
       
        self.file_path_line = QtWidgets.QLineEdit(Form)
        self.file_path_line.setGeometry(QtCore.QRect(10, 180, 431, 25))
        self.file_path_line.setStyleSheet("font-family:Times New Roman;font-size:15px")
        self.file_path_line.setObjectName("file_path_line")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Measurement:"))
        self.import_csv_btn.setText(_translate("Form", "Import CSV"))
        self.done_btn.setText(_translate("Form", "Done"))

    def import_csv(self):
        root = tk.Tk()
        root.withdraw()

        self.file_path= filedialog.askopenfilename()

        self.file_path_line.setText(self.file_path)    

        self.done_btn.clicked.connect(self.create_measurement)

    def create_measurement(self):
        client =  InfluxDBClient('localhost' , 8086)
        client.create_database(self.measurement_name_line.text()) 
        client.switch_database(self.measurement_name_line.text())
            
        
        for filename in glob.glob(self.file_path):
            csvfile = os.path.splitext(filename)[0]
            jsonfile = csvfile + '.json'

        with open(csvfile+'.csv') as f:
            reader = csv.DictReader(f)
            rows = list(reader)

        with open(jsonfile, 'w') as f:
            json.dump(rows, f)

        client.write_points(jsonfile,  'demo')         


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

