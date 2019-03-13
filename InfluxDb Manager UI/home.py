# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'home.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from NewDB import *

class Ui_MainWindow(object):


    def call_NewDB(self):
        self.create_db(self.window)


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1104, 632)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1104, 26))
        self.menubar.setObjectName("menubar")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuQuery = QtWidgets.QMenu(self.menubar)
        self.menuQuery.setObjectName("menuQuery")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        self.menuile = QtWidgets.QMenu(self.menubar)
        self.menuile.setObjectName("menuile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setToolTip("")
        self.toolBar.setStatusTip("")
        self.toolBar.setWhatsThis("")
        self.toolBar.setAutoFillBackground(False)
        self.toolBar.setAllowedAreas(QtCore.Qt.NoToolBarArea)
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        MainWindow.insertToolBarBreak(self.toolBar)
        self.actionProject = QtWidgets.QAction(MainWindow)
        self.actionProject.setObjectName("actionProject")
        self.actionFle = QtWidgets.QAction(MainWindow)
        self.actionFle.setObjectName("actionFle")
        self.actionNew_DB = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/new_database.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNew_DB.setIcon(icon)
        self.actionNew_DB.setObjectName("actionNew_DB")
        self.actionOpen_DB = QtWidgets.QAction(MainWindow)


        self.actionNew_DB.clicked.connect(self.create_db)


        self.actionOpen_DB.setObjectName("actionOpen_DB")
        self.actionSave = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/savefile.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave.setIcon(icon1)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_As = QtWidgets.QAction(MainWindow)
        self.actionSave_As.setObjectName("actionSave_As")
        self.actionExit = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExit.setIcon(icon2)
        self.actionExit.setObjectName("actionExit")
        self.actionQConsole = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/keyboard.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionQConsole.setIcon(icon3)
        self.actionQConsole.setObjectName("actionQConsole")
        self.actionConsole = QtWidgets.QAction(MainWindow)
        self.actionConsole.setObjectName("actionConsole")
        self.actionGraph = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icons/graph.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionGraph.setIcon(icon4)
        self.actionGraph.setObjectName("actionGraph")
        self.menuQuery.addAction(self.actionQConsole)
        self.menuQuery.addAction(self.actionConsole)
        self.menuQuery.addAction(self.actionGraph)
        self.menuile.addAction(self.actionNew_DB)
        self.menuile.addAction(self.actionOpen_DB)
        self.menuile.addAction(self.actionSave)
        self.menuile.addAction(self.actionSave_As)
        self.menuile.addSeparator()
        self.menuile.addAction(self.actionExit)
        self.menubar.addAction(self.menuile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuQuery.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.toolBar.addAction(self.actionNew_DB)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionSave)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionQConsole)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionGraph)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionExit)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuQuery.setTitle(_translate("MainWindow", "Console"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.menuile.setTitle(_translate("MainWindow", "File"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionProject.setText(_translate("MainWindow", "Project"))
        self.actionFle.setText(_translate("MainWindow", "File"))
        self.actionNew_DB.setText(_translate("MainWindow", "New DB"))
        self.actionOpen_DB.setText(_translate("MainWindow", "Open DB"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setStatusTip(_translate("MainWindow", "Save..."))
        self.actionSave.setWhatsThis(_translate("MainWindow", "Save"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionSave_As.setText(_translate("MainWindow", "Save As"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionQConsole.setText(_translate("MainWindow", "QConsole"))
        self.actionConsole.setText(_translate("MainWindow", "Console"))
        self.actionGraph.setText(_translate("MainWindow", "Graph"))
        self.actionGraph.setShortcut(_translate("MainWindow", "Ctrl+G"))






if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

