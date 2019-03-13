from PyQt5.QtWidgets import QApplication, QLineEdit, QMainWindow, QWidget, QHBoxLayout, QLabel
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
        self.linedit.setFont(QtGui.QFont('SanSerif', 15))
        self.linedit.returnPressed.connect(self.onPressed)

        hbox.addWidget(self.linedit)

        self.label= QLabel(self)
        self.label.setFont(QtGui.QFont('SanSerif', 15))
        hbox.addWidget(self.label)
        self.show()

    def onPressed(self):

        client = InfluxDBClient(host='localhost', port=8086)
        client.switch_database(self.linedit.text())

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

if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())

