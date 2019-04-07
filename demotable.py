import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtCore
from influxdb import InfluxDBClient

class UserInterface(QMainWindow):

    def __init__(self):
        super(UserInterface, self).__init__()
        self.TaskBar()
        self.Buttons()

        self.table_widget = MyTable()

        close_button = QPushButton("Close", self)
        close_button.resize(100, 50)
        close_button.move(100, 900)
        close_button.setStyleSheet("QPushButton {font-size : 24px}")
        close_button.clicked.connect(self.add_data)

        self.widget = QWidget(self)
        layout = QGridLayout()
        self.widget.setLayout(layout)
        layout.addWidget(self.table_widget)
        layout.addWidget(close_button)

        self.setCentralWidget(self.widget)

    def TaskBar(self):
        self.setWindowTitle("Create Measurement")
        self.setGeometry(QDesktopWidget().screenGeometry())

    def Buttons(self):  
        close_button = QPushButton("Close", self)
        close_button.resize(100, 50)
        close_button.move(100, 800)
        close_button.setStyleSheet("QPushButton {font-size : 24px}")
        close_button.clicked.connect(self.add_data)

    def add_data(self):

        list= 'Name, ID, Age, Price, Number, Sales, Amount, Profit' 

        client =  InfluxDBClient('localhost' , 8086)

        client.create_database('demo')
        client.switch_database('demo')

        for list_name in list.split(', '):
            print(list_name)

            json_body=[{
                "measurement" : "demo",

                "fields" : {
                    list_name : ' '
                }
            }]
            client.write_points(json_body)        

class MyTable(QWidget):

    def __init__(self):
        super(MyTable, self).__init__()
        self.Table()

    def Table(self):
        self.mytable()
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tableWidget)
        self.setLayout(self.layout)
        self.show()

    def mytable(self):
        list= 'Name, ID, Age, Price, Number, Sales, Amount, Profit' 
        c=0
        for i in list.split(', '):
            c=c+1

        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(5)
        self.tableWidget.setColumnCount(c)
        self.tableWidget.setHorizontalHeaderLabels(list.split(', '))

        ##self.tableWidget.setItem(0, 0 , QTableWidgetItem("Hello"))
        self.tableWidget.move(300, 300)

    


def Main():
    qapplication_constructor = QApplication(sys.argv)
    gui = UserInterface()
    gui.show()
    sys.exit(qapplication_constructor.exec_())

if __name__ == "__main__":
    Main()