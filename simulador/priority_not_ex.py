# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'priority_not_ex.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1179, 883)
        MainWindow.setStyleSheet("QWidget#centralwidget{\n"
"background-color: qlineargradient(spread:pad, x1:0.092, y1:0.908909, x2:1, y2:0, stop:0.477273 rgba(26, 76, 107, 255), stop:0.943182 rgba(9, 32, 82, 255));}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser_7 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_7.setGeometry(QtCore.QRect(110, 20, 931, 31))
        self.textBrowser_7.setObjectName("textBrowser_7")
        self.ButtonLoadProcess = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonLoadProcess.setGeometry(QtCore.QRect(580, 440, 211, 61))
        self.ButtonLoadProcess.setObjectName("ButtonLoadProcess")
        self.startEmulation = QtWidgets.QPushButton(self.centralwidget)
        self.startEmulation.setGeometry(QtCore.QRect(610, 500, 151, 61))
        self.startEmulation.setObjectName("startEmulation")
        self.ButtonGenerate = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonGenerate.setGeometry(QtCore.QRect(610, 380, 151, 61))
        self.ButtonGenerate.setObjectName("ButtonGenerate")
        self.labelCPU_3 = QtWidgets.QLabel(self.centralwidget)
        self.labelCPU_3.setGeometry(QtCore.QRect(570, 750, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Bauhaus 93")
        font.setPointSize(18)
        self.labelCPU_3.setFont(font)
        self.labelCPU_3.setCursor(QtGui.QCursor(QtCore.Qt.WaitCursor))
        self.labelCPU_3.setAutoFillBackground(False)
        self.labelCPU_3.setStyleSheet("background-color: yellow;")
        self.labelCPU_3.setObjectName("labelCPU_3")
        self.textBrowser_6 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_6.setGeometry(QtCore.QRect(600, 740, 221, 51))
        self.textBrowser_6.setObjectName("textBrowser_6")
        self.listaListos = QtWidgets.QListWidget(self.centralwidget)
        self.listaListos.setGeometry(QtCore.QRect(820, 310, 256, 261))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.listaListos.setFont(font)
        self.listaListos.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.SizeVerCursor))
        self.listaListos.setObjectName("listaListos")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(70, 270, 261, 31))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.textBrowser_5 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_5.setGeometry(QtCore.QRect(600, 670, 221, 41))
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.labelCPU = QtWidgets.QLabel(self.centralwidget)
        self.labelCPU.setGeometry(QtCore.QRect(610, 320, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Bauhaus 93")
        font.setPointSize(18)
        self.labelCPU.setFont(font)
        self.labelCPU.setCursor(QtGui.QCursor(QtCore.Qt.WaitCursor))
        self.labelCPU.setAutoFillBackground(False)
        self.labelCPU.setStyleSheet("background-color: yellow;")
        self.labelCPU.setObjectName("labelCPU")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(640, 270, 121, 31))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_3.setGeometry(QtCore.QRect(820, 270, 271, 31))
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.labelCPU_2 = QtWidgets.QLabel(self.centralwidget)
        self.labelCPU_2.setGeometry(QtCore.QRect(570, 670, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Bauhaus 93")
        font.setPointSize(18)
        self.labelCPU_2.setFont(font)
        self.labelCPU_2.setCursor(QtGui.QCursor(QtCore.Qt.WaitCursor))
        self.labelCPU_2.setAutoFillBackground(False)
        self.labelCPU_2.setStyleSheet("background-color: green;")
        self.labelCPU_2.setObjectName("labelCPU_2")
        self.processTable_2 = QtWidgets.QTableWidget(self.centralwidget)
        self.processTable_2.setGeometry(QtCore.QRect(60, 310, 501, 261))
        self.processTable_2.setObjectName("processTable_2")
        self.processTable_2.setColumnCount(5)
        self.processTable_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.processTable_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.processTable_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.processTable_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.processTable_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.processTable_2.setHorizontalHeaderItem(4, item)
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_4.setGeometry(QtCore.QRect(570, 590, 401, 51))
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.ganntList = QtWidgets.QListWidget(self.centralwidget)
        self.ganntList.setGeometry(QtCore.QRect(60, 580, 501, 241))
        self.ganntList.setObjectName("ganntList")
        self.processTable = QtWidgets.QTableWidget(self.centralwidget)
        self.processTable.setGeometry(QtCore.QRect(210, 60, 711, 201))
        self.processTable.setObjectName("processTable")
        self.processTable.setColumnCount(5)
        self.processTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.processTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.processTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.processTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.processTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.processTable.setHorizontalHeaderItem(4, item)
        self.clearButton = QtWidgets.QPushButton(self.centralwidget)
        self.clearButton.setGeometry(QtCore.QRect(880, 690, 231, 61))
        self.clearButton.setObjectName("clearButton")
        self.ButtonAverages = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonAverages.setGeometry(QtCore.QRect(20, 130, 181, 61))
        self.ButtonAverages.setObjectName("ButtonAverages")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1179, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.textBrowser_7.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600;\">Simulador de procesos de prioridad (No Preventivo)</span></p></body></html>"))
        self.ButtonLoadProcess.setText(_translate("MainWindow", "Cargar procesos"))
        self.startEmulation.setText(_translate("MainWindow", "Comenzar emulacion"))
        self.ButtonGenerate.setText(_translate("MainWindow", "Generar procesos"))
        self.labelCPU_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"></p></body></html>"))
        self.textBrowser_6.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:7pt; font-weight:600;\">Tiempo en el que el proceso termino de ejecutarse y dio paso a otro</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7pt; font-weight:600;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7pt; font-weight:600;\"><br /></p></body></html>"))
        self.textBrowser_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">Procesos listos</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt; font-weight:600;\"><br /></p></body></html>"))
        self.textBrowser_5.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:7pt; font-weight:600;\">Procesos que se estan ejecutando</span></p></body></html>"))
        self.labelCPU.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600;\">CPU</span></p></body></html>"))
        self.textBrowser_3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">Procesos ya ejecutados</span></p></body></html>"))
        self.labelCPU_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"></p></body></html>"))
        item = self.processTable_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "CPU"))
        item = self.processTable_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "A.T"))
        item = self.processTable_2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "B.T"))
        item = self.processTable_2.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Prioridad"))
        item = self.processTable_2.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Tiempo restante"))
        self.textBrowser_4.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600;\">Diagrama de Gannt</span></p></body></html>"))
        item = self.processTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "CPU"))
        item = self.processTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "A.T"))
        item = self.processTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "B.T"))
        item = self.processTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Prioridad"))
        item = self.processTable.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Tiempo restante"))
        self.clearButton.setText(_translate("MainWindow", "Limpiar datos"))
        self.ButtonAverages.setText(_translate("MainWindow", "Ver promedios de tiempo"))
