from PyQt5.QtWidgets import QApplication, QLineEdit, QMainWindow, QWidget, QHBoxLayout, QLabel, QPushButton
import sys
from PyQt5 import QtGui
from PyQt5.QtCore import QRect
from pandas.core.window import Window
from influxdb import InfluxDBClient
import pandas as pd

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "Create Db"
        self.left = 500
        self.top = 200
        self.width = 300
        self.height = 250
        self.iconName = 'home.png'

        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        hbox = QHBoxLayout()
        self.linedit = QLineEdit(self)
        self.linedit.move(30, 50)
        self.linedit.setFont(QtGui.QFont('SanSerif', 15))
        self.button = QPushButton('Create Database', self)
        self.button.move(100, 120)

        self.button.clicked.connect(self.onPressed)

        hbox.addWidget(self.linedit)

        self.label= QLabel(self)
        self.label.setFont(QtGui.QFont('SanSerif', 15))
        hbox.addWidget(self.label)
        self.show()

    def onPressed(self):

        client = InfluxDBClient(host='localhost', port=8086)
        client.create_database(self.linedit.text())

        client.switch_database(self.linedit.text())
        file_path = r'C:\Users\hp\Desktop\C2ImportCalEventSample.csv'
        csvReader = pd.read_csv(file_path)
        print(csvReader.shape)
        print(csvReader.columns)

        for row_index, row in csvReader.iterrows():
            c = 0
            c = c+1

            tags = row[0]
            fieldValue = row[c]
            json_body = [{
                "measurement": "table1",
                "tags": {
                    "Reference": tags

                },
                "fields": {
                    "value": row[2],
                    "Start Time": row[c]
                }
            }]

            print(json_body)
            client.write_points(json_body)

if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())

