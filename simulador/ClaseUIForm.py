from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QListWidgetItem, QTableWidgetItem
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QBrush, QColor

from test1 import Ui_MainWindow 
import sys
import random

class ClaseUIDialog(QMainWindow, Ui_MainWindow):
    
    def __init__(self, parent=None):        
        super(ClaseUIDialog, self).__init__(parent)
        
        self.setupUi(self)
        self.Button1.clicked.connect(self.test_process)
        self.ButtonLoadProcess.clicked.connect(self.cargar_procesos)
        self.Button1.hide()
        self.ButtonGenerate.clicked.connect(self.generar_procesos)
        
        self.proceso_anterior = None

        
        self.startProcess = False
        
        self.contador = 1
        self.procesos = [
            {'nombre': 'P1', 'llegada': 0, 'duracion': 11, 'prioridad': 2, 'tiempo_restante': 11},
            {'nombre': 'P2', 'llegada': 5, 'duracion': 28, 'prioridad': 0, 'tiempo_restante': 28},
            {'nombre': 'P3', 'llegada': 12, 'duracion': 2, 'prioridad': 3, 'tiempo_restante': 2},
            {'nombre': 'P4', 'llegada': 2, 'duracion': 10, 'prioridad': 1, 'tiempo_restante': 10},
            {'nombre': 'P5', 'llegada': 9, 'duracion': 16, 'prioridad': 4, 'tiempo_restante': 16}
        ]       
        
        
        self.procesos.sort(key=lambda x: (x['llegada'], x['prioridad']))
        self.tiempo_actual = 0
        self.timer = QTimer()
        self.timer.timeout.connect(self.test_process)   

    def test_process(self):      #TableGannt  
         
        if self.procesos:
            proceso = min((p for p in self.procesos if p['llegada'] <= self.tiempo_actual), key=lambda x: x['prioridad'], default=None)                      
                   
            if proceso is None:
                self.tiempo_actual = min(p['llegada'] for p in self.procesos)
            else:
                if self.proceso_anterior and self.proceso_anterior != proceso['nombre']:
                    print(self.tiempo_actual)
                    
                    processG = QListWidgetItem(str(self.tiempo_actual))          
                    processG.setForeground(QBrush(QColor('black')))
                    processG.setBackground(QBrush(QColor('yellow')))
                    
                    self.list1.addItem(processG)


                print(f"{proceso['nombre']} ejecutándose en el tiempo {self.tiempo_actual}")
                self.timer.start(300)
                #self.cargar_procesos()
                
                processG = QListWidgetItem(str(proceso['nombre']))            
            
                processG.setForeground(QBrush(QColor('white')))
                processG.setBackground(QBrush(QColor('darkgreen')))
                
                self.list1.addItem(processG)
                              
                proceso['tiempo_restante'] -= 1
                self.tiempo_actual += 1

                if proceso['tiempo_restante'] == 0:
                    self.procesos.remove(proceso)

                self.proceso_anterior = proceso['nombre']
                  
        else:
            self.timer.stop()
        self.cargar_procesos()   
             
        
            
    def cargar_procesos(self):
        
        self.Button1.show()
        self.processTable.setRowCount(len(self.procesos))  
        for i, proceso in enumerate(self.procesos):
            self.processTable.setItem(i, 0, QTableWidgetItem(proceso['nombre']))
            self.processTable.setItem(i, 1, QTableWidgetItem(str(proceso['llegada'])))
            self.processTable.setItem(i, 2, QTableWidgetItem(str(proceso['duracion'])))
            self.processTable.setItem(i, 3, QTableWidgetItem(str(proceso['prioridad'])))
            self.processTable.setItem(i, 4, QTableWidgetItem(str(proceso['tiempo_restante'])))
            
    def generar_procesos(self):
        
        num_procesos = random.randint(0, 8)  
        prioridades = random.sample(range(0, 8), num_procesos)  
        self.procesos = []

        for i in range(num_procesos):
            nombre = f'P{i+1}'
            llegada = 0 if i == 0 else random.randint(1, 20)  #que sea almenos 1, 0 en arrive
            duracion = random.randint(1, 20)
            prioridad = prioridades[i]
            tiempo_restante = duracion

            proceso = {'nombre': nombre, 'llegada': llegada, 'duracion': duracion, 'prioridad': prioridad, 'tiempo_restante': tiempo_restante}
            self.procesos.append(proceso)
        
        
def main():
    
    app = QApplication(sys.argv)
    
    ventana = ClaseUIDialog()
    
    ventana.setWindowTitle("KKK")
    ventana.show()
    
    app.exec_()
    
if __name__ == "__main__":
    main()
