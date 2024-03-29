# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!
import sys

from McScrp import mcscrp
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget,QApplication
from requests import get


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1091, 620)
        self.text = QtWidgets.QLineEdit(Form)
        self.text.setGeometry(QtCore.QRect(22, 20, 321, 31))
        self.text.setObjectName("text")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(370, 21, 111, 31))
        self.comboBox.setObjectName("comboBox")
        self.scrp = QtWidgets.QPushButton(Form)
        self.scrp.setGeometry(QtCore.QRect(500, 20, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.scrp.setFont(font)
        self.scrp.setObjectName("scrp")
        self.progressBar = QtWidgets.QProgressBar(Form)
        self.progressBar.setGeometry(QtCore.QRect(640, 20, 301, 31))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(950, 20, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(20, 60, 1061, 501))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(480, 570, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.scrp.setText(_translate("Form", "Scraping Data"))
        self.pushButton_2.setText(_translate("Form", "Save Data"))
        self.pushButton_3.setText(_translate("Form", "About Me"))


class MainWindow(QWidget,Ui_Form):
    def __init__(self):
        super(MainWindow,self).__init__()
        QWidget.__init__(self)
        self.setupUi(self)
        self.scrp.clicked.connect(self.scrpping)

    def scrpping(self):
        sc = mcscrp()
        data = get(self.text.text()).text
        tags = sc.get_tags(data)
        self.tableWidget.setColumnCount(len(tags))
        self.tableWidget.setRowCount(len(tags))
        self.tableWidget.setHorizontalHeaderLabels(tags)
        for r,tag in enumerate(tags):
            for c,dt in enumerate(sc.scrp(data, tag)['txt']):
                self.tableWidget.setItem(c,r,QtWidgets.QTableWidgetItem(str(dt)))

app = QApplication(sys.argv)
frm = MainWindow()
frm.show()
app.exec_()