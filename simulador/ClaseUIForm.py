from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QListWidgetItem, QTableWidgetItem
from PyQt5.QtCore import QTimer
from test1 import Ui_MainWindow 
import sys

class ClaseUIDialog(QMainWindow, Ui_MainWindow):
    
    def __init__(self, parent=None):        
        super(ClaseUIDialog, self).__init__(parent)
        
        self.setupUi(self)
        self.Button1.clicked.connect(self.test_process)
        self.ButtonLoadProcess.clicked.connect(self.cargar_procesos)
        
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

    def test_process(self):       
        if self.procesos:
            proceso = min((p for p in self.procesos if p['llegada'] <= self.tiempo_actual), key=lambda x: x['prioridad'], default=None)

            if proceso is None:
                self.tiempo_actual = min(p['llegada'] for p in self.procesos)
            else:
                print(f"{proceso['nombre']} ejecutándose en el tiempo {self.tiempo_actual}")
                self.timer.start(300)
                self.list1.addItem(QListWidgetItem(str(proceso['nombre'])))                
                proceso['tiempo_restante'] -= 1
                self.tiempo_actual += 1

                if proceso['tiempo_restante'] == 0:
                    self.procesos.remove(proceso)
                  
        else:
            self.timer.stop()  
            
    def cargar_procesos(self):
        self.processTable.setRowCount(len(self.procesos))  # Establecer el número de filas en la tabla
        for i, proceso in enumerate(self.procesos):
            self.processTable.setItem(i, 0, QTableWidgetItem(proceso['nombre']))
            self.processTable.setItem(i, 1, QTableWidgetItem(str(proceso['llegada'])))
            self.processTable.setItem(i, 2, QTableWidgetItem(str(proceso['duracion'])))
            self.processTable.setItem(i, 3, QTableWidgetItem(str(proceso['prioridad'])))
            self.processTable.setItem(i, 4, QTableWidgetItem(str(proceso['tiempo_restante'])))
        
def main():
    
    app = QApplication(sys.argv)
    
    ventana = ClaseUIDialog()
    
    ventana.setWindowTitle("KKK")
    ventana.show()
    
    app.exec_()
    
if __name__ == "__main__":
    main()
