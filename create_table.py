import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget,QTableWidgetItem,QVBoxLayout,QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from influxdb import InfluxDBClient
 
class App(QWidget):
 
    def __init__(self):
        super().__init__()
        self.title = 'Create Measurement'
        self.left = 100
        self.top = 100
        self.width = 1000
        self.height = 800
        
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        
  
        list= 'Name, ID, Age, Price, Number, Sales, Amount, Profit' 
        self.createTable(list)

        ##Add box layout, add table to box layout and add box layout to widget
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tableWidget) 
        self.setLayout(self.layout) 
 
        ##Show widget
        self.show()
 
    def createTable(self,list):

        c=0
        for i in list.split(', '):
            c=c+1

        ##Create table
        ##print(c)
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(5)
        self.tableWidget.setColumnCount(c)
        self.tableWidget.setHorizontalHeaderLabels(list.split(', '))
        
        self.tableWidget.move(0,0)
 
    
        # table selection change
        self.tableWidget.doubleClicked.connect(self.on_click)
 
    @pyqtSlot()
    def on_click(self):
        print("\n")
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())
            ##rowPosition = self.tableWidget.rowCount()
            ##tableWidget.insertRow(rowPosition)
        client =  InfluxDBClient('localhost' , 8086)

        client.create_database('demo')
        client.switch_database('demo')

        json_body=[{
            "measurement" : 'demo',

            "fields" : {
                "col1" : currentQTableWidgetItem.text() 
            }
        }]

        client.write_points(json_body)

       
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())