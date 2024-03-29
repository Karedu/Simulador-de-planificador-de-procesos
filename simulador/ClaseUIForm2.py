from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QListWidgetItem, QTableWidgetItem
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QBrush, QColor

from test2 import Ui_MainWindow 
import sys
import random
import copy

class ClaseUIDialog(QMainWindow, Ui_MainWindow):
    
    def __init__(self, parent=None):        
        super(ClaseUIDialog, self).__init__(parent)
        
        self.setupUi(self)       
        self.startEmulation.clicked.connect(self.non_preemptive_priority_algorithm)
        self.ButtonLoadProcess.clicked.connect(self.cargar_procesos)        
        self.ButtonGenerate.clicked.connect(self.generar_procesos)
        self.clearButton.clicked.connect(self.limpiar_ventanas)     
        
        self.startEmulation.setEnabled(False)
   
        
        self.proceso_anterior = None        
        self.startProcess = False
        
        self.contador = 1
        #Proceso de prueba
        # self.procesos = [ #Ejercicio Original a mano Resultados P1 P4 P5 P3 P2
        #     {'nombre': 'P1', 'llegada': 0, 'duracion': 4, 'prioridad': 2, 'tiempo_restante': 4},
        #     {'nombre': 'P2', 'llegada': 1, 'duracion': 3, 'prioridad': 3, 'tiempo_restante': 3},
        #     {'nombre': 'P3', 'llegada': 2, 'duracion': 1, 'prioridad': 4, 'tiempo_restante': 1},
        #     {'nombre': 'P4', 'llegada': 3, 'duracion': 5, 'prioridad': 5, 'tiempo_restante': 5},
        #     {'nombre': 'P5', 'llegada': 4, 'duracion': 2, 'prioridad': 5, 'tiempo_restante': 2}
            # ]
        self.procesos = [
        {'nombre': 'P1', 'llegada': 5, 'duracion': 4, 'prioridad': 4, 'tiempo_restante': 4},
        {'nombre': 'P2', 'llegada': 4, 'duracion': 8, 'prioridad': 1, 'tiempo_restante': 8},
        {'nombre': 'P3', 'llegada': 7, 'duracion': 5, 'prioridad': 2, 'tiempo_restante': 5},
        {'nombre': 'P4', 'llegada': 3, 'duracion': 6, 'prioridad': 7, 'tiempo_restante': 6},
        {'nombre': 'P5', 'llegada': 3, 'duracion': 3, 'prioridad': 3, 'tiempo_restante': 3},
        {'nombre': 'P6', 'llegada': 9, 'duracion': 11, 'prioridad': 0, 'tiempo_restante': 11},
        {'nombre': 'P7', 'llegada': 5, 'duracion': 4, 'prioridad': 6, 'tiempo_restante': 4}
    ]

        
        self.procesosAux = []          
        
       

    def non_preemptive_priority_algorithm(self):
        def ordenar_por_tiempo_de_llegada():
            return sorted(self.procesos, key=lambda x: x['llegada'])
        
        def ordenar_por_prioridad(cola):
            return sorted(cola, key=lambda x: x['prioridad'], reverse=True)
        
        def ejecutar_proceso(proceso_actual, tiempo_actual, tiempo_de_ejecucion):
            tiempo_actual += tiempo_de_ejecucion
            proceso_actual['tiempo_restante'] -= tiempo_de_ejecucion
            return tiempo_actual, proceso_actual
    
        self.procesos = ordenar_por_tiempo_de_llegada()
        
        tiempo_actual = 0
        cola = []  
        resultado = []  
        
        while self.procesos or cola:
            while self.procesos and self.procesos[0]['llegada'] <= tiempo_actual:
                cola.append(self.procesos.pop(0))      
            
            if cola:  
                cola = ordenar_por_prioridad(cola)
                proceso_actual = cola.pop(0)        
                tiempo_de_ejecucion = min(proceso_actual['duracion'], proceso_actual['tiempo_restante'])
                tiempo_actual, proceso_actual = ejecutar_proceso(proceso_actual, tiempo_actual, tiempo_de_ejecucion)
                
                resultado.append({
                    'nombre': proceso_actual['nombre'],
                    'inicio': tiempo_actual - tiempo_de_ejecucion,
                    'fin': tiempo_actual,
                    'prioridad': proceso_actual['prioridad']
                })
                
                processG = QListWidgetItem(str(proceso_actual['nombre']))         
                processG.setForeground(QBrush(QColor('white')))
                processG.setBackground(QBrush(QColor('darkgreen')))                
                self.ganntList.addItem(processG)
                
                print(f"Proceso {proceso_actual['nombre']} - Inicio: {tiempo_actual - tiempo_de_ejecucion} - Fin: {tiempo_actual} - Prioridad: {proceso_actual['prioridad']}")
                
                if proceso_actual['tiempo_restante'] > 0:
                    cola.append(proceso_actual)
                else:
                    processG = QListWidgetItem(str(tiempo_actual))          
                    processG.setForeground(QBrush(QColor('black')))
                    processG.setBackground(QBrush(QColor('yellow')))                    
                    self.ganntList.addItem(processG)
                    self.listaListos.addItem(proceso_actual['nombre'])
            else:  
                if self.procesos:  
                   
                    tiempo_actual = self.procesos[0]['llegada']
        
        self.startEmulation.setEnabled(False)
        return resultado
                
    def cargar_procesos(self):        
        
        self.processTable.setRowCount(len(self.procesos)) 
        self.processTable_2.setRowCount(len(self.procesosAux)) 
         
        for i, proceso in enumerate(self.procesos):
            self.processTable.setItem(i, 0, QTableWidgetItem(proceso['nombre']))
            self.processTable.setItem(i, 1, QTableWidgetItem(str(proceso['llegada'])))
            self.processTable.setItem(i, 2, QTableWidgetItem(str(proceso['duracion'])))
            self.processTable.setItem(i, 3, QTableWidgetItem(str(proceso['prioridad'])))
            self.processTable.setItem(i, 4, QTableWidgetItem(str(proceso['tiempo_restante'])))
            
        for i, procesoAux in enumerate(self.procesosAux):
            self.processTable_2.setItem(i, 0, QTableWidgetItem(procesoAux['nombre']))
            self.processTable_2.setItem(i, 1, QTableWidgetItem(str(procesoAux['llegada'])))
            self.processTable_2.setItem(i, 2, QTableWidgetItem(str(procesoAux['duracion'])))
            self.processTable_2.setItem(i, 3, QTableWidgetItem(str(procesoAux['prioridad'])))
            self.processTable_2.setItem(i, 4, QTableWidgetItem(str(procesoAux['tiempo_restante'])))
            
        self.startEmulation.setEnabled(True)
     
        print(self.procesos) 
            
    def generar_procesos(self):
                
        num_procesos = random.randint(1, 8)  
        prioridades = random.sample(range(0, 8), num_procesos)  
        self.procesos = []
        self.procesosAux = []

        for i in range(num_procesos):
            nombre = f'P{i+1}'
            llegada = random.randint(0, 10)  #que sea almenos 1, 0 en arrive
            duracion = random.randint(1, 12)
            prioridad = prioridades[i]
            tiempo_restante = duracion

            proceso = {'nombre': nombre, 'llegada': llegada, 'duracion': duracion, 'prioridad': prioridad, 'tiempo_restante': tiempo_restante}
            self.procesos.append(proceso)
        self.procesosAux = copy.deepcopy(self.procesos)
    
    def limpiar_ventanas(self):
       self.listaListos.clear()
       self.ganntList.clear()
       self.processTable.setRowCount(0)
       self.processTable_2.setRowCount(0)
       self.tiempo_actual = 0
             

def main():
    
    app = QApplication(sys.argv)
    
    ventana = ClaseUIDialog()    
    ventana.setWindowTitle("Algoritmo de prioridad no Expulsivo")
    ventana.show()    
    app.exec_()
    
    print("Terminado!")
    
if __name__ == "__main__":
    main()
