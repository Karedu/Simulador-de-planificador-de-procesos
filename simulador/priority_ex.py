# Form implementation generated from reading ui file 'priority_ex.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(750, 700)
        MainWindow.setMinimumSize(QtCore.QSize(750, 700))
        MainWindow.setMaximumSize(QtCore.QSize(750, 700))
        MainWindow.setStyleSheet("QWidget#centralwidget{\n"
"    background-color: rgb(2, 89, 81);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Button1 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.Button1.setGeometry(QtCore.QRect(580, 170, 121, 31))
        self.Button1.setObjectName("Button1")
        self.ganntList = QtWidgets.QListWidget(parent=self.centralwidget)
        self.ganntList.setGeometry(QtCore.QRect(30, 450, 301, 201))
        self.ganntList.setStyleSheet("color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 25, 62, 251), stop:1 rgba(255, 255, 255, 255));\n"
"background-color: rgb(255, 170, 0);\n"
"border-radius: 15px;")
        self.ganntList.setObjectName("ganntList")
        self.listaListos = QtWidgets.QListWidget(parent=self.centralwidget)
        self.listaListos.setGeometry(QtCore.QRect(490, 450, 241, 151))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.listaListos.setFont(font)
        self.listaListos.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.CursorShape.SizeVerCursor))
        self.listaListos.setStyleSheet("color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 25, 62, 251), stop:1 rgba(255, 255, 255, 255));\n"
"background-color: rgb(255, 170, 0);\n"
"border-radius: 15px;")
        self.listaListos.setObjectName("listaListos")
        self.processTable = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.processTable.setGeometry(QtCore.QRect(30, 110, 501, 131))
        self.processTable.setStyleSheet("background-color: rgb(255, 170, 0);\n"
"border-radius: 15px;")
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
        self.ButtonLoadProcess = QtWidgets.QPushButton(parent=self.centralwidget)
        self.ButtonLoadProcess.setGeometry(QtCore.QRect(580, 130, 121, 31))
        self.ButtonLoadProcess.setObjectName("ButtonLoadProcess")
        self.ButtonGenerate = QtWidgets.QPushButton(parent=self.centralwidget)
        self.ButtonGenerate.setGeometry(QtCore.QRect(580, 90, 121, 31))
        self.ButtonGenerate.setObjectName("ButtonGenerate")
        self.processTable_2 = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.processTable_2.setGeometry(QtCore.QRect(30, 280, 501, 121))
        self.processTable_2.setStyleSheet("\n"
"background-color: rgb(255, 170, 0);\n"
"border-radius: 15px;")
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
        self.labelCPU_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.labelCPU_2.setGeometry(QtCore.QRect(340, 480, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Bauhaus 93")
        font.setPointSize(18)
        self.labelCPU_2.setFont(font)
        self.labelCPU_2.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.WaitCursor))
        self.labelCPU_2.setAutoFillBackground(False)
        self.labelCPU_2.setStyleSheet("background-color: green;")
        self.labelCPU_2.setObjectName("labelCPU_2")
        self.labelCPU_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.labelCPU_3.setGeometry(QtCore.QRect(340, 560, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Bauhaus 93")
        font.setPointSize(18)
        self.labelCPU_3.setFont(font)
        self.labelCPU_3.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.WaitCursor))
        self.labelCPU_3.setAutoFillBackground(False)
        self.labelCPU_3.setStyleSheet("background-color: yellow;")
        self.labelCPU_3.setObjectName("labelCPU_3")
        self.textBrowser_5 = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.textBrowser_5.setGeometry(QtCore.QRect(370, 470, 101, 51))
        self.textBrowser_5.setStyleSheet("")
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.textBrowser_6 = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.textBrowser_6.setGeometry(QtCore.QRect(370, 540, 101, 71))
        self.textBrowser_6.setObjectName("textBrowser_6")
        self.clearButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.clearButton.setGeometry(QtCore.QRect(590, 620, 141, 31))
        self.clearButton.setObjectName("clearButton")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 40, 731, 31))
        self.label.setStyleSheet("font: 600 18pt \"Segoe UI Semibold\";\n"
"color: rgb(255, 85, 0);\n"
"text-align: center;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, -1, 731, 41))
        self.label_2.setStyleSheet("font: 24pt \"Sitka Text\";\n"
"color: white;")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(190, 250, 171, 21))
        self.label_3.setStyleSheet("font: 600 18pt \"Segoe UI Semibold\";\n"
"color: white;\n"
"text-align: center;")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(610, 250, 61, 21))
        self.label_4.setStyleSheet("font: 600 18pt \"Segoe UI Semibold\";\n"
"color: white;\n"
"text-align: center;")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(70, 400, 281, 41))
        self.label_5.setStyleSheet("font: 600 18pt \"Segoe UI Semibold\";\n"
"color: white;\n"
"text-align: center;")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(490, 400, 261, 41))
        self.label_6.setStyleSheet("font: 600 18pt \"Segoe UI Semibold\";\n"
"color: white;\n"
"text-align: center;")
        self.label_6.setObjectName("label_6")
        self.widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(550, 280, 181, 111))
        self.widget.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.301864, y1:0.744, x2:0, y2:0.989, stop:0.482955 rgba(255, 170, 0, 228), stop:0.943182 rgba(209, 178, 35, 237));\n"
"border-radius: 15px;\n"
"padding: 2px;\n"
"")
        self.widget.setObjectName("widget")
        self.labelCPU = QtWidgets.QLabel(parent=self.widget)
        self.labelCPU.setGeometry(QtCore.QRect(10, 10, 161, 91))
        font = QtGui.QFont()
        font.setFamily("Bauhaus 93")
        font.setPointSize(18)
        self.labelCPU.setFont(font)
        self.labelCPU.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.WaitCursor))
        self.labelCPU.setAutoFillBackground(False)
        self.labelCPU.setStyleSheet("background-color: yellow;")
        self.labelCPU.setObjectName("labelCPU")
        self.label_7 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(120, 70, 341, 31))
        self.label_7.setStyleSheet("font: 600 18pt \"Segoe UI Semibold\";\n"
"color: white;\n"
"text-align: center;")
        self.label_7.setObjectName("label_7")
        self.ButtonAverages = QtWidgets.QPushButton(parent=self.centralwidget)
        self.ButtonAverages.setGeometry(QtCore.QRect(410, 620, 161, 31))
        self.ButtonAverages.setObjectName("ButtonAverages")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 750, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Button1.setText(_translate("MainWindow", "Comenzar emulacion"))
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
        self.ButtonLoadProcess.setText(_translate("MainWindow", "Cargar procesos"))
        self.ButtonGenerate.setText(_translate("MainWindow", "Generar procesos"))
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
        self.labelCPU_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"></p></body></html>"))
        self.labelCPU_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"></p></body></html>"))
        self.textBrowser_5.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:7pt; font-weight:600;\">Procesos que se estan ejecutando</span></p></body></html>"))
        self.textBrowser_6.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:7pt; font-weight:600;\">Tiempo en el que el proceso termino de ejecutarse y dio paso a otro</span></p></body></html>"))
        self.clearButton.setText(_translate("MainWindow", "Reiniciar simulación"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-style:italic;\">Simulador de procesos de prioridad ( Preventivo)</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Simulador de Planificación de Procesos</p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "Procesos listos"))
        self.label_4.setText(_translate("MainWindow", "CPU"))
        self.label_5.setText(_translate("MainWindow", "Diagrama de Gannt"))
        self.label_6.setText(_translate("MainWindow", "Procesos terminados"))
        self.labelCPU.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p>Procesos/procesos bloqueados</p></body></html>"))
        self.ButtonAverages.setText(_translate("MainWindow", "Resultados de la simulación"))
