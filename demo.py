# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'splitter.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QFrame, 
    QSplitter, QStyleFactory, QApplication ,QPushButton, QTextEdit,QLabel, QLineEdit)
from PyQt5.QtCore import Qt
import sys
textfrlabel = 'vcxvxc'
text1 = 'vcvc'
class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):      
       
        hbox = QHBoxLayout(self)

        topleft = QFrame(self)
        topleft.setFrameShape(QFrame.StyledPanel)
        #add button in left frame
        btn = QPushButton('button', topleft)
        btn.setFixedSize(50, 20)
        btn.move(50,50)
        
        
        
 
        topright = QFrame(self)
        topright.setFrameShape(QFrame.StyledPanel)
        #add text Edit in right frame
        
        self.text1=QLineEdit('table data',topright)
        self.text1.setFixedSize(100,100)
        self.text1.move(100,50)
       
        
      
        bottom = QFrame(self)
        bottom.setFrameShape(QFrame.StyledPanel)
        self.text2=QLineEdit(' ',bottom)
        self.text2.setFixedSize(1500,500)
        self.text2.move(50,50)
        btn.clicked.connect(self.aaaa)
         
        splitter1 = QSplitter(Qt.Horizontal)
        splitter1.addWidget(topleft)
        splitter1.addWidget(topright)

        splitter2 = QSplitter(Qt.Vertical)
        splitter2.addWidget(splitter1)
        splitter2.addWidget(bottom)

        hbox.addWidget(splitter2)
        self.setLayout(hbox)
        
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('QSplitter')
        self.show() 
       
    def aaaa(self):
        
        textfrlabel=self.text1.text()

        self.text2.setText(textfrlabel)


        
        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())