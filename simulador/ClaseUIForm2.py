from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QListWidgetItem, QTableWidgetItem
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QBrush, QColor

from priority_not_ex import Ui_MainWindow 
import sys
import random
import copy

class ClaseUIDialog(QMainWindow, Ui_MainWindow):
    
    def __init__(self, parent=None):        
        super(ClaseUIDialog, self).__init__(parent)
        
        self.setupUi(self)       
        self.startEmulation.clicked.connect(self.non_preemptive_priority_algorithm)
        self.ButtonLoadProcess.clicked.connect(self.load_processes)        
        self.ButtonGenerate.clicked.connect(self.generate_processes)
        self.clearButton.clicked.connect(self.clean_windows)     
        self.ButtonAverages.clicked.connect(self.show_averages)
                
        self.proceso_anterior = None        
        self.startProcess = False
        self.startEmulation.setEnabled(False)  
        self.ButtonLoadProcess.setEnabled(False)
        self.ButtonAverages.setEnabled(False)
        
        self.contador = 1
        
        self.average_turning_time = 0
        self.average_waiting_time = 0 
       
        self.processes = []        
        self.auxProcesses = self.processes     
        
        self.finishTimesList = []        
        
        self.timer = QTimer()
        self.timer.timeout.connect(self.non_preemptive_priority_algorithm)      
        

    def non_preemptive_priority_algorithm(self):
        

        def sort_by_arrival_time():
            return sorted(self.processes, key=lambda x: x['llegada'])
        
        def sort_by_priority(stack):
            return sorted(stack, key=lambda x: x['prioridad'], reverse=True)
        
        def run_process(current_process, current_time, execution_time):
            current_time += execution_time
            current_process['tiempo_restante'] -= execution_time
            return current_time, current_process
    
        self.processes = sort_by_arrival_time()
        
        current_time = 0
        stack = []  
        result = []  
        
        while self.processes or stack:
            while self.processes and self.processes[0]['llegada'] <= current_time:
                stack.append(self.processes.pop(0))      
            
            if stack:  
                stack = sort_by_priority(stack)
                current_process = stack.pop(0)        
                execution_time = min(current_process['duracion'], current_process['tiempo_restante'])
                current_time, current_process = run_process(current_process, current_time, execution_time)
                
                
                result.append({
                    'nombre': current_process['nombre'],
                    'inicio': current_time - execution_time,
                    'fin': current_time,
                    'prioridad': current_process['prioridad']
                })                
                
                processG = QListWidgetItem(str(current_process['nombre']))         
                processG.setForeground(QBrush(QColor('white')))
                processG.setBackground(QBrush(QColor('darkgreen')))                
                self.ganntList.addItem(processG)
                
                #print(f"Proceso {current_process['nombre']} - Inicio: {current_time - execution_time} - Fin: {current_time} - Prioridad: {current_process['prioridad']}")
                
                if current_process['tiempo_restante'] > 0:
                    stack.append(current_process)
                else:
                    
                    processG = QListWidgetItem(str(current_time))          
                    processG.setForeground(QBrush(QColor('black')))
                    processG.setBackground(QBrush(QColor('yellow')))                    
                    self.ganntList.addItem(processG)
                    self.listaListos.addItem(current_process['nombre'])                      
                    
                    finishTimeItem = QListWidgetItem(f"{current_process['nombre']}: {current_time}")
                    
                    self.finishTimesList.append({
                        'nombre': current_process['nombre'],
                        'finalizado': current_time,
                        'tiempoGiro': current_time - current_process['llegada'],
                        'tiempoEspera': (current_time - current_process['llegada']) - current_process['duracion']
                     })                                                            
                          
            else:  
                if self.processes:  
                   
                    current_time = self.processes[0]['llegada']
                    
        
        self.startEmulation.setEnabled(False)        
        
        sum_tg = sum(proceso['tiempoGiro'] for proceso in self.finishTimesList)
        sum_te = sum(proceso['tiempoEspera'] for proceso in self.finishTimesList)

        self.average_turning_time = sum_tg / len(self.finishTimesList)
        self.average_waiting_time = sum_te / len(self.finishTimesList)
     
        self.ButtonAverages.setEnabled(True) #
        self.ButtonLoadProcess.setEnabled(False)

               
    def load_processes(self):        
        
        self.processTable.setRowCount(len(self.processes)) 
        self.processTable_2.setRowCount(len(self.auxProcesses)) 
         
        for i, process in enumerate(self.processes):
            self.processTable.setItem(i, 0, QTableWidgetItem(process['nombre']))
            self.processTable.setItem(i, 1, QTableWidgetItem(str(process['llegada'])))
            self.processTable.setItem(i, 2, QTableWidgetItem(str(process['duracion'])))
            self.processTable.setItem(i, 3, QTableWidgetItem(str(process['prioridad'])))
            self.processTable.setItem(i, 4, QTableWidgetItem(str(process['tiempo_restante'])))
            
        for i, auxProcess in enumerate(self.auxProcesses):
            self.processTable_2.setItem(i, 0, QTableWidgetItem(auxProcess['nombre']))
            self.processTable_2.setItem(i, 1, QTableWidgetItem(str(auxProcess['llegada'])))
            self.processTable_2.setItem(i, 2, QTableWidgetItem(str(auxProcess['duracion'])))
            self.processTable_2.setItem(i, 3, QTableWidgetItem(str(auxProcess['prioridad'])))
            self.processTable_2.setItem(i, 4, QTableWidgetItem(str(auxProcess['tiempo_restante'])))
            
        self.startEmulation.setEnabled(True)
     
   
            
    def generate_processes(self):
                
        num_processes = random.randint(1, 8)  
        priorities = random.sample(range(0, 8), num_processes)  
        self.processes = []
        self.auxProcesses = []
        self.ButtonLoadProcess.setEnabled(True)

        for i in range(num_processes):
            name = f'P{i+1}'
            arrive = random.randint(0, 10)  #que sea almenos 1, 0 en arrive
            duration = random.randint(1, 12)
            priority = priorities[i]
            resting_time = duration

            proceso = {'nombre': name, 'llegada': arrive, 'duracion': duration, 'prioridad': priority, 'tiempo_restante': resting_time}
            self.processes.append(proceso)
        self.auxProcesses = copy.deepcopy(self.processes)
    
    def clean_windows(self):
       self.listaListos.clear()
       self.ganntList.clear()
       self.processTable.setRowCount(0)
       self.processTable_2.setRowCount(0)
       self.current_time = 0
       
       self.ButtonAverages.setEnabled(False)
       
       
    def show_averages(self):
        boxOutPrint = QMessageBox()
        boxOutPrint.setIcon(QMessageBox.Information)
        boxOutPrint.setText(f"Tiempo promedio de giro: {self.average_turning_time:.2f}\nTiempo promedio de espera: {self.average_waiting_time:.2f}")
        boxOutPrint.setWindowTitle("Promedios")
        boxOutPrint.exec_()
             

def main():
    
    app = QApplication(sys.argv)
    
    window = ClaseUIDialog()    
    window.setWindowTitle("Algoritmo de prioridad no Expulsivo")
    window.show()    
    app.exec_()   
       
if __name__ == "__main__":
    main()
