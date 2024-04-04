from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QListWidgetItem, QTableWidgetItem
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QBrush, QColor

from priority_ex import Ui_MainWindow 
import sys
import random
import copy

class ClaseUIDialog(QMainWindow, Ui_MainWindow):
    
    def __init__(self, parent=None):        
        super(ClaseUIDialog, self).__init__(parent)
        
        self.setupUi(self)
        self.Button1.clicked.connect(self.test_process)
        self.ButtonLoadProcess.clicked.connect(self.cargar_procesos)
        self.Button1.hide()
        self.ButtonGenerate.clicked.connect(self.generate_processes)
        self.clearButton.clicked.connect(self.show_averages)        
        
        self.previous_process = None        
        self.startProcess = False
        
        self.counter = 1
           
        
        self.processes = [
            {'nombre': 'P1', 'llegada': 0, 'duracion': 11, 'prioridad': 2, 'tiempo_restante': 11},
            {'nombre': 'P2', 'llegada': 5, 'duracion': 28, 'prioridad': 0, 'tiempo_restante': 28},
            {'nombre': 'P3', 'llegada': 12, 'duracion': 2, 'prioridad': 3, 'tiempo_restante': 2},
            {'nombre': 'P4', 'llegada': 2, 'duracion': 10, 'prioridad': 1, 'tiempo_restante': 10},
            {'nombre': 'P5', 'llegada': 9, 'duracion': 16, 'prioridad': 4, 'tiempo_restante': 16}
        ]  
        
        self.auxiliary_processes = []      
        self.processes.sort(key=lambda x: (x['llegada'], x['prioridad']))
        self.current_time = 0
        self.timer = QTimer()
        self.timer.timeout.connect(self.test_process)   

    def test_process(self):      #TableGannt  
    
        if self.processes:
            proceso = min((p for p in self.processes if p['llegada'] <= self.current_time), key=lambda x: x['prioridad'], default=None)                     
                   
            if proceso is None:
                self.current_time = min(p['llegada'] for p in self.processes)
            else:
                if self.previous_process and self.previous_process != proceso['nombre']:                                     
                    processG = QListWidgetItem(str(self.current_time))          
                    processG.setForeground(QBrush(QColor('black')))
                    processG.setBackground(QBrush(QColor('yellow')))                    
                    self.ganntList.addItem(processG)               
                
                proceso['tiempo_restante'] -= 1
                self.current_time += 1

                if proceso['tiempo_restante'] == 0:
                    self.listaListos.addItem(proceso['nombre'])
                    self.processes.remove(proceso)
                    
                self.previous_process = proceso['nombre']
                
                processG = QListWidgetItem(str(proceso['nombre']))         
                processG.setForeground(QBrush(QColor('white')))
                processG.setBackground(QBrush(QColor('darkgreen')))                
                self.ganntList.addItem(processG)
                self.labelCPU.setText(proceso['nombre'])
                
                self.timer.start(200)
                self.cargar_procesos()             
                  
        else:
            processG = QListWidgetItem(str(self.current_time))          
            processG.setForeground(QBrush(QColor('black')))
            processG.setBackground(QBrush(QColor('yellow')))                    
            self.ganntList.addItem(processG)   
            self.timer.stop()
        
       
                    
            
    def cargar_procesos(self):
        
        self.Button1.show()
        self.processTable.setRowCount(len(self.processes)) 
        self.processTable_2.setRowCount(len(self.auxiliary_processes)) 
         
        for i, proceso in enumerate(self.processes):
            self.processTable.setItem(i, 0, QTableWidgetItem(proceso['nombre']))
            self.processTable.setItem(i, 1, QTableWidgetItem(str(proceso['llegada'])))
            self.processTable.setItem(i, 2, QTableWidgetItem(str(proceso['duracion'])))
            self.processTable.setItem(i, 3, QTableWidgetItem(str(proceso['prioridad'])))
            self.processTable.setItem(i, 4, QTableWidgetItem(str(proceso['tiempo_restante'])))
            
        for i, procesoAux in enumerate(self.auxiliary_processes):
            self.processTable_2.setItem(i, 0, QTableWidgetItem(procesoAux['nombre']))
            self.processTable_2.setItem(i, 1, QTableWidgetItem(str(procesoAux['llegada'])))
            self.processTable_2.setItem(i, 2, QTableWidgetItem(str(procesoAux['duracion'])))
            self.processTable_2.setItem(i, 3, QTableWidgetItem(str(procesoAux['prioridad'])))
            self.processTable_2.setItem(i, 4, QTableWidgetItem(str(procesoAux['tiempo_restante'])))
            
    def generate_processes(self):
                
        processes = random.randint(1, 8)  
        priorities = random.sample(range(0, 8), processes)  
        self.processes = []
        self.auxiliary_processes = []

        for i in range(processes):
            name = f'P{i+1}'
            arrive = random.randint(0, 10)  #que sea almenos 1, 0 en arrive
            duration = random.randint(1, 12)
            priority = priorities[i]
            resting_time = duration

            process = {'nombre': name, 'llegada': arrive, 'duracion': duration, 'prioridad': priority, 'tiempo_restante': resting_time}
            self.processes.append(process)
        self.auxiliary_processes = copy.deepcopy(self.processes)
        self.ButtonLoadProcess.setEnabled(True)
        
    
    def show_averages(self):
        self.listaListos.clear()
        self.ganntList.clear()
        self.processTable.setRowCount(0)
        self.processTable_2.setRowCount(0)
        self.current_time = 0
        
        self.Button1.setEnabled(False)
        self.ButtonLoadProcess.setEnabled(False)
        
    
def main():
    
    app = QApplication(sys.argv)
    
    ventana = ClaseUIDialog()    
    ventana.setWindowTitle("Algoritmo de prioridad Expulsivo")
    ventana.show()    
    app.exec_()
    
if __name__ == "__main__":
    main()
