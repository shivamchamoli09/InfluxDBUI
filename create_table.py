import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget,QTableWidgetItem,QVBoxLayout,QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from influxdb import InfluxDBClient
 
class App(QWidget):
    def show1(self,cols, measurement_name):
        self.list=cols
        self.measurement_name = measurement_name

        self.createTable(self.list, self.measurement_name)

        ##Add box layout, add table to box layout and add box layout to widget
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.save_btn) 
        self.layout.addWidget(self.add_row) 

        self.layout.addWidget(self.tableWidget) 
        self.setLayout(self.layout)
        print('a***')
        self.show()
 
    def __init__(self):
        super().__init__()
        self.title = 'Create Measurement'
        self.left = 100
        self.top = 100
        self.width = 1000
        self.height = 800
        print('a********************')
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        
  
 
    def createTable(self,list, measurement_name):
        ##print(measurement_name)
        self.measurement_name = measurement_name

        self.col_no=0
        for i in list.split(', '):
            self.col_no=self.col_no+1

        ##Create table

        self.save_btn = QPushButton("Save", self)
        self.add_row = QPushButton("Add Row", self)

        self.add_row.clicked.connect(self.add_rows)

        self.columns_name = list


        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(3)
        self.tableWidget.setColumnCount(self.col_no-1)
        self.field_name=list.split(', ')
        self.tableWidget.setHorizontalHeaderLabels(self.field_name)

        self.save_btn.clicked.connect(self.save_measurement)

        self.tableWidget.move(0,0)
 
            # table selection change
        #self.tableWidget.doubleClicked.connect(self.on_click)
 
    def save_measurement(self):
       ##print(measurement_name)

        client =  InfluxDBClient('localhost' , 8086)

        client.create_database('demo')
        client.switch_database('demo')

        ##col_name = list.split(", ")
        #print(measurement_name)
        points=list()
        json_body={}

        json_body["measurement"] = self.measurement_name
        fields={}

        for i in range(self.tableWidget.rowCount()):
            #print(self.tableWidget.rowCount())
            for j in range(self.col_no-1):
                self.value = self.tableWidget.item(i,j).text()
                #print(self.value)
                fields[self.field_name[j]]= self.value
                
                #print(self.field_name[self.field_count])
                #self.field_count=self.field_count + 1
                #if(self.field_count == (self.col_no-1)):
                 #   self.field_count = 0
                json_body['fields']=fields
                points.append(json_body)
                print(json_body)
            client.write_points(points)   

    def add_rows(self):
        row_position = self.tableWidget.rowCount()
        self.tableWidget.insertRow(row_position)    

                   
        

''' 
json_body=[{
                "measurement" : 'demo',
                "fields" : {
                    "col_name" : currentQTableWidgetItem.text() 
                }
            }]
       
'''
