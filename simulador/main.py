# import sys
# from PyQt6 import uic
# from PyQt6.QtWidgets import QApplication
# from PyQt6.QtCore import QTimer
# from queue import Queue
# import time
# from PyQt6.QtCore import QThread,pyqtSignal


# # iniciar la aplicación
# app = QApplication(sys.argv)

# # cargar los archivos .ui
# main = uic.loadUi("main_window.ui")
# process_planner = uic.loadUi("process_window.ui")
# timer = QTimer()


# class Hilo(QThread):
#     new_value = pyqtSignal(int)
#     def __init__(self):
#         super(Hilo,self).__init__()

#     def run(self):
#         for i in range(1,11):
#             self.new_value.emit(i)
#             time.sleep(1)


# def simular():

#     quantum = 4
#     # processes = [
#     #         {"name": "P1", "burst_time": 5, "arrival_time": 0 , "completed": False, "total_time": 0, "current_time": 0},
#     #         {"name": "P2", "burst_time": 2, "arrival_time": 2 , "completed": False, "total_time": 0, "current_time": 0},
#     #         {"name": "P3", "burst_time": 8, "arrival_time": 4 , "completed": False, "total_time": 0, "current_time": 0},
#     # ]
#     # for process in processes:
#     #     time.sleep(2)
#     #     agregar()

#     hilo = Hilo()
#     hilo.new_value.connect(agregar)
#     hilo.start()

#     hilo.wait()
#     # results = simulate_round_robin(processes, quantum)

# def saludo():

#     print("hola")
# def agregar(new_value):
#     process_planner.listaListos.addItem("data")
# def esperar():
#     print("esperando")

# def simulate_round_robin(processes, quantum):

#     completed_processes = []
#     prepared_queue = Queue()
#     processes_quantity = len(processes)
#     clock_cycle = 0
#     processes.sort(key=lambda process: process["arrival_time"])
#     prepared_queue.put(processes[0])

#     print("Entra al sistema: ",clock_cycle)
#     print("Ejecutando tarea.......... ",processes[0])
#     print("")

#     while True:

#         time.sleep(1)
#         process = prepared_queue.get()
#         print("")
#         print("")
#         print(f"Inicia la tarea en el ciclo {clock_cycle}..........  {process}")
#         print("")
#         time.sleep(1)
#         task_cycles = 0

#         while task_cycles <= quantum:

#             task_cycles = task_cycles + 1
#             clock_cycle = clock_cycle + 1

#             time.sleep(1)
#             process["current_time"] = process["current_time"] + 1

#             if process["burst_time"] == process["current_time"]:
#                 process["completed"] = True

#             print("Ciclo: ",clock_cycle)
#             print("Ejecutando tarea.......... ",process)
#             time.sleep(1)
#             print("")

#             if(process["completed"] == True):
#                 print(f"Tarea {process["name"]} ya esta completada")
#                 process["total_time"] = clock_cycle
#                 completed_processes.append(process)
#                 process_planner.listaListos.addItem(process["name"])
#                 for data in processes:
#                     if data['name'] == process["name"]:
#                         processes.remove(data)
#                         break

#                 if  processes_quantity == len(completed_processes) :
#                     print("entro")
#                     return completed_processes
#                 break

#             time.sleep(1)
#             print("")

#             for compare_process in processes:
#                 if compare_process["name"] == process["name"]:
#                     continue
#                 if compare_process["arrival_time"] == clock_cycle:
#                     prepared_queue.put(compare_process)
#                     time.sleep(1)
#                     print("LLEGO TAREA, Se agrega a  la cola de tareas el proceso.......... ",compare_process)
#                     queue_active = True
#                     break

#             time.sleep(1)
#             print("")
#             if task_cycles == 4 and process["completed"] != True:
#                 process["total_time"] = clock_cycle
#                 print("")
#                 time.sleep(1)
#                 print("NO TERMINO, Se agrega a  la cola de tareas el proceso.......... ",process)
#                 print("")
#                 prepared_queue.put(process)
#                 queue_active = True
#                 break

#         time.sleep(1)
#         print("")
#         time.sleep(1)


# def calculate_promedy(processes):
#     # Calcular promedio de tiempos
#     average_waiting_time = 0
#     average_service_time = 0
#     average_CPU_time = 0
#     for data in processes:

#         CPU_time = data["total_time"] - data["arrival_time"]
#         waiting_time = CPU_time - data["burst_time"]
#         service_time = data["burst_time"] / CPU_time

#         average_CPU_time = average_CPU_time + CPU_time
#         average_waiting_time = average_waiting_time + waiting_time
#         average_service_time = average_service_time + service_time

#     quantity = len(processes)
#     # print("QUANTITY",quantity)
#     average_CPU_time = average_CPU_time / quantity
#     average_waiting_time = average_waiting_time / quantity
#     average_service_time = average_service_time / quantity

#     return {
#         "average_CPU_time": average_CPU_time,
#         "average_waiting_time": average_waiting_time,
#         "average_service_time": average_service_time,
#     }


# # processes = [
# #     {"name": "P1", "burst_time": 5, "arrival_time": 0 , "completed": False, "total_time": 0, "current_time": 0},
# #     {"name": "P2", "burst_time": 2, "arrival_time": 2 , "completed": False, "total_time": 0, "current_time": 0},
# #     {"name": "P3", "burst_time": 8, "arrival_time": 4 , "completed": False, "total_time": 0, "current_time": 0},
# # ]
# # quantum = 4
# # results = simulate_round_robin(processes, quantum)
# # print(results)
# # averages = calculate_promedy(results)
# # print(averages)

# def algoritmo1():
#     main.hide()
#     process_planner.label_2.setText(main.algoritmo1.text())
#     process_planner.show()


# def algoritmo2():
#     main.hide()
#     process_planner.label_2.setText(main.algoritmo2.text())
#     process_planner.show()

# def algoritmo3():
#     main.hide()
#     process_planner.label_2.setText(main.algoritmo3.text())
#     process_planner.show()

# def algoritmo4():
#     main.hide()
#     process_planner.label_2.setText(main.algoritmo4.text())
#     process_planner.show()

# def algoritmo5():
#     main.hide()
#     process_planner.label_2.setText(main.algoritmo5.text())
#     process_planner.show()

# def algoritmo6():
#     main.hide()
#     process_planner.label_2.setText(main.algoritmo6.text())
#     process_planner.show()

# def regresar():
#     process_planner.hide()
#     main.show()

# def salir():
#     pass
# # botones de los algoritmos
# process_planner.agregarProceso.clicked.connect(saludo)
# process_planner.simular.clicked.connect(simular)

# main.algoritmo1.clicked.connect(algoritmo1)
# main.algoritmo2.clicked.connect(algoritmo2)
# main.algoritmo3.clicked.connect(algoritmo3)
# main.algoritmo4.clicked.connect(algoritmo4)
# main.algoritmo5.clicked.connect(algoritmo5)
# main.algoritmo6.clicked.connect(algoritmo6)

# main.salir.clicked.connect(salir)
# process_planner.regresar.clicked.connect(regresar)

# main.show()
# sys.exit(app.exec())

import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from queue import Queue  # Python Standard Library


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, processes, quantum):
        super().__init__()

        self.list_widget = QtWidgets.QListWidget()
        self.setCentralWidget(self.list_widget)

        self.processes = processes.copy()  # Copy for safety
        self.processes.sort(key=lambda process: process["arrival_time"])
        self.quantum = quantum
        self.processes_quantity = len(processes)
        self.completed_processes = []
        self.prepared_queue = Queue()  # Using Python's `queue` library
        self.prepared_queue.put(processes[0])
        self.process = processes[0]

        self.clock_cycle = 0
        self.timer = QtCore.QTimer()
        self.timer.setInterval(2000)  # Simulate time passage (adjust as needed)
        self.timer.timeout.connect(self.simulate_round_robin)
        self.task_cycles = 0
        self.timer.start()

    def simulate_round_robin(self):
        # while True:

        # if self.prepared_queue.empty() and all(process["completed"] for process in self.processes):
        #     self.show_process("Simulación finalizada")
        #     self.timer.stop()
        #     return

        # if self.prepared_queue.empty():
        #     process = self.processes.pop(0)
        #     self.prepared_queue.put(process)
        #     self.show_process(f"Entra al sistema en el ciclo {self.clock_cycle}: {process}")


        self.task_cycles = self.task_cycles + 1
        self.clock_cycle += 1

        self.show_process(
            f"Inicia la tarea en el ciclo {self.clock_cycle}: {self.process }"
        )

        self.process["current_time"] += 1

        # if self.process["burst_time"] == self.process["current_time"]:
        #     self.show_process(f"Tarea {self.process ['name']} completada")
        #     self.timer.stop()
        #     return

        if self.process ["burst_time"] == self.process ["current_time"]:
            self.process ["completed"] = True
            self.completed_processes.append(self.process)
            self.show_process(f"Tarea {self.process ['name']} completada")

            # for i, data in enumerate(self.processes):
            #     if data["name"] == self.process ["name"]:
            #         del self.processes[i]
            #         break
            for data in self.processes:
                if data['name'] == self.process["name"]:
                    self.processes.remove(data)
                    break
            self.process  = self.prepared_queue.get()
            if  self.processes_quantity == len(self.completed_processes) :
                self.show_process("Simulación finalizada")
                self.timer.stop()
                return 
            return

        # if len(self.completed_processes) == len(self.processes):
        #     self.show_process("Simulación finalizada")
        #     self.timer.stop()
        #     return
        #     break

        # self.show_process(f"Ciclo {self.clock_cycle}: Ejecutando {process}")

        for compare_process in self.processes:
            if compare_process["arrival_time"] == self.clock_cycle:
                self.prepared_queue.put(compare_process)
                self.show_process(f"Llega tarea en el ciclo {self.clock_cycle}: {compare_process}")

        if self.task_cycles == self.quantum and not self.process["completed"]:
            self.prepared_queue.put(self.process)
            self.show_process(f"Tarea sin terminar, vuelve a la cola: {self.process}")
            self.task_cycles = 0
            self.process  = self.prepared_queue.get()

        # if self.task_cycles == self.quantum:
        #     self.task_cycles = 0
        #     self.process  = self.prepared_queue.get()

    def show_process(self, message):
        self.list_widget.addItem(message)


if __name__ == "__main__":
    processes = [
        {
            "name": "P1",
            "burst_time": 5,
            "arrival_time": 0,
            "completed": False,
            "current_time": 0,
        },
        # {"name": "P2", "burst_time": 2, "arrival_time": 2, "completed": False, "current_time": 0},
        # {"name": "P3", "burst_time": 8, "arrival_time": 4, "completed": False, "current_time": 0},
    ]
    quantum = 4

    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow(processes, quantum)
    window.show()
    sys.exit(app.exec())
