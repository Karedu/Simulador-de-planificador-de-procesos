from QRunnable import Worker
from PyQt6.QtCore import *
from PyQt6.QtCore import QMutex
from queue import Queue
import time
import random

threadpool = QThreadPool()

def startSJF(windows):
        worker = Worker(windows.sjf)
        threadpool.start(worker)

class MainWindowSJF:

    def __init__(self,process_planner_2):
        super().__init__()
        self.mutex = QMutex()
        self.wigets = process_planner_2

    def sjf(self):
        
        quantity_process = self.wigets.cantidad.value()
        if quantity_process == 0:
            return
        
        self.disable_button()
        self.clear_completes_process()
        self.processes = self.generar_valores_aleatorios(quantity_process)
        self.process = self.processes[0]  
        self.processes_quantity = len(self.processes)
        self.completed_processes = []
        self.bloqued_processes = []
        self.processes_queue = []
        self.clock_cycle = 0
        self.show_listProcess(self.processes)
        for compare_process in self.processes:
            if compare_process["arrival_time"] == 0:
                self.processes_queue.append(compare_process)
                self.show_process(f"{compare_process["name"]} / Burst: {compare_process["burst_time"]} / Arrival: {compare_process["arrival_time"]}")
                self.show_details(f"1LLEGO TAREA {compare_process["name"]}, en ciclo {self.clock_cycle} Se agrega a  la cola de tareas el proceso...")
                time.sleep(2)

        self.rewrite_list(self.processes_queue)

        while True:

            if not self.processes_queue:
                self.remove_cpu()
                self.show_details(f"No han llegado mas tareas...")
                time.sleep(1)
                self.clock_cycle = self.clock_cycle + 1
                print("No hay tareas: ")
                print("Ciclo: ",self.clock_cycle)
                print("-----------------------------------------------------------------")
                self.show_clock(self.clock_cycle)

                if not self.bloqued_processes:  
                    print("No hay procesos bloqueados...")
                else:
                    # self.rewrite_bloqued_list(self.bloqued_processes) 
                    process_blocked = self.bloqued_processes[0]
                    process_blocked["time_blocked"] = process_blocked["time_blocked"] - 1
                    if process_blocked["time_blocked"] == 0:
                        self.remove_block_process()
                        self.bloqued_processes.pop(0)
                        self.show_details(f"TERMINO BLOQUEO DE {process_blocked["name"]}, Se agrega a  la cola de tareas el proceso...")
                        print(f"TERMINO BLOQUEO DE {process_blocked["name"]}, Se agrega a  la cola de tareas el proceso...")
                        time.sleep(2)
                        self.processes_queue.append(process_blocked)
                        self.show_process(process_blocked)

                for compare_process in self.processes:
                    if compare_process["arrival_time"] == self.clock_cycle:
                        self.processes_queue.append(compare_process)
                        self.show_process(f"{compare_process["name"]} / Burst: {compare_process["burst_time"]} / Arrival: {compare_process["arrival_time"]}")
                        self.show_details(f"2LLEGO TAREA {compare_process["name"]}, en ciclo {self.clock_cycle} Se agrega a  la cola de tareas el proceso...")
                        time.sleep(2)
                continue     


            process = min(self.processes_queue, key=lambda process: process["burst_time"])

            time.sleep(2)
            print(f"Inicia la tarea en el ciclo {self.clock_cycle}..........  {process}")
            self.show_details(f"Inicia la tarea {process["name"]}  en el ciclo {self.clock_cycle} ")
            
            time.sleep(2)
            for data in self.processes_queue:
                if data['name'] == process["name"]:
                    self.processes_queue.remove(data)
                    break 
            self.show_cpu(f"{process['name']}")
            self.show_timeToComplete(process)

            while True:
                
                self.rewrite_list(self.processes_queue)
                self.clock_cycle = self.clock_cycle + 1
                
                if not self.bloqued_processes:  
                    print("No hay procesos bloqueados...")
                else:
                    # self.rewrite_bloqued_list(self.bloqued_processes) 
                    process_blocked = self.bloqued_processes[0]
                    process_blocked["time_blocked"] = process_blocked["time_blocked"] - 1
                    if process_blocked["time_blocked"] == 0:
                        self.remove_block_process()
                        self.bloqued_processes.pop(0)
                        self.show_details(f"TERMINO BLOQUEO DE {process_blocked["name"]}, Se agrega a  la cola de tareas el proceso...")
                        time.sleep(2)
                        self.processes_queue.append(process_blocked)
                        self.show_process(process_blocked)

                process["time_to_completed"] = process["time_to_completed"] - 1
                process["current_time"] = process["current_time"] + 1

                if process["time_to_completed"] == 0:
                    process["completed"] = True

                print("Ciclo: ",self.clock_cycle)
                self.show_clock(self.clock_cycle)
                self.show_timeToComplete(process)
                print("Ejecutando tarea.......... ",process)
                self.show_details(f"Ejecutando tarea {process["name"]}...")

                time.sleep(2)
                print("")
                self.show_timeToComplete(process)
                for compare_process in self.processes:
                    if compare_process["name"] == process["name"]:
                        continue
                    if compare_process["arrival_time"] == self.clock_cycle:
                        # self.show_process(f"{compare_process["name"]} / Burst: {compare_process["burst_time"]} / Arrival: {compare_process["arrival_time"]}")
                        print("LLEGO TAREA, Se agrega a  la cola de tareas el proceso...",compare_process)
                        self.show_details(f"LLEGO TAREA {compare_process["name"]}, Se agrega a  la cola de tareas el proceso...")
                        self.processes_queue.append(compare_process)
                        time.sleep(2)

                # Posible bloqueo 20%
                posibility_block = random.random()
                print(posibility_block)
                if  posibility_block < 0.2:    

                    time_block = random.randint(1, 10)

                    print(f"Proceso {process['name']} bloqueado por {time_block} ciclos")
                    process['time_blocked']  = time_block
                    newtime = process["burst_time"] - process["current_time"]

                    if newtime == 0 or process["time_to_completed"] == 0:
                        newtime = 1

                    process["time_to_completed"] = newtime
                    process["completed"] = False
                    self.show_details(f"Proceso {process['name']} bloqueado por {time_block} ciclos")
                    
                    self.bloqued_processes.append(process)
                    self.show_bloqued(process)
                    time.sleep(2)           
                    break; 
                
                if(process["completed"] == True):

                    print(f"Tarea {process["name"]} ya esta completada")
                    self.show_details(f"Tarea {process["name"]} ya esta completada")
                    time.sleep(2)
                    self.remove_cpu()
                    self.clear_timeToComplete()
                    process["total_time"] = self.clock_cycle
                    self.completed_processes.append(process)
                    self.show_completed(process)

                    if  self.processes_quantity == len(self.completed_processes) :
                        self.remove_process()
                        self.activate_button()
                        self.show_details("FIN SIMULACION")
                        self.calculate_promedy(self.completed_processes)
                        return self.completed_processes
                    
                    break
                time.sleep(1)
            
            print("")
        return   


    def show_details(self, message):
        self.mutex.lock()
        self.wigets.label_detalles.setText(message)
        self.mutex.unlock()

    def remove_block_process(self):
        self.mutex.lock()
        self.wigets.listaBloqueados.takeItem(0)
        self.mutex.unlock()

    def rewrite_list(self,message):
        self.mutex.lock()
        self.wigets.listaListos.clear()
        for (data) in message:
            print(data)
            self.wigets.listaListos.addItem(f"{data["name"]} / Burst: {data["burst_time"]} / Arrival: {data["arrival_time"]}")
        self.mutex.unlock()

    def show_process(self, message):
        self.mutex.lock()
        self.wigets.listaListos.addItem(f"{message}")
        self.mutex.unlock()

    def show_cpu(self, message):
        self.mutex.lock()
        self.wigets.label_CPU.setText(message)
        self.mutex.unlock()

    def remove_cpu(self):
        self.mutex.lock()
        self.wigets.label_CPU.setText("")
        self.mutex.unlock()
    
    def remove_process(self):
        self.mutex.lock()
        self.wigets.listaListos.takeItem(0)
        self.mutex.unlock()

    def show_clock(self, message):
        self.mutex.lock()
        self.wigets.label_11.setText(str(message))
        self.mutex.unlock()

    def show_completed(self, data):
        self.mutex.lock()
        self.wigets.listaCompletados.addItem(f"{data["name"]} / Burst: {data["burst_time"]} / Arrival: {data["arrival_time"]}")
        self.mutex.unlock()

    def show_timeToComplete(self, data):
        self.mutex.lock()
        self.wigets.tiempoRestante.setText(str(data["time_to_completed"]))
        self.mutex.unlock()

    def show_listProcess(self, process):
        self.mutex.lock()
        for data in process:
            self.wigets.listaTodosProcesos.addItem(f"{data["name"]} / Burst: {data["burst_time"]} / Arrival: {data["arrival_time"]}")
        self.mutex.unlock()

    def show_bloqued(self, data):
        self.mutex.lock()
        self.wigets.listaBloqueados.addItem(f"{data["name"]} / Burst: {data["burst_time"]} / Arrival: {data["arrival_time"]} / Block: {data["time_blocked"]}")
        self.mutex.unlock()

    def clear_completes_process(self):
        self.mutex.lock()
        self.wigets.listaCompletados.clear()
        self.mutex.unlock()

    def clear_promedy_data(self):
        self.mutex.lock()
        self.wigets.listaPromedios.clear()
        self.mutex.unlock()

    def clear_timeToComplete(self):
        self.mutex.lock()
        self.wigets.tiempoRestante.setText("")
        self.mutex.unlock()   

    def activate_button(self):
        self.wigets.play.setEnabled(True)
    
    def disable_button(self):
        self.wigets.play.setEnabled(False)

    def generar_valores_aleatorios(self,quantity):
        processes = []
        for i in range(1, quantity+1):
            burst_time = random.randint(1, 5)
            proceso = {
                "name": f"P{i}",
                "burst_time": burst_time,  
                "arrival_time": random.randint(0, 10), 
                "completed": False,
                "current_time": 0,
                "time_to_completed": burst_time,
                "time_blocked": 0,
            }
            processes.append(proceso)
        return processes



    def calculate_promedy(self,processes):
        # Calcular promedio de tiempos
        average_waiting_time = 0
        average_service_time = 0
        average_CPU_time = 0
        
        for data in processes:

            CPU_time = data["total_time"] - data["arrival_time"]
            waiting_time = CPU_time - data["burst_time"]
            service_time = data["burst_time"] / CPU_time

            average_CPU_time = average_CPU_time + CPU_time
            average_waiting_time = average_waiting_time + waiting_time
            average_service_time = average_service_time + service_time
        
        quantity = len(processes)
        # print("QUANTITY",quantity)
        print(processes)
        average_CPU_time = average_CPU_time / quantity
        average_waiting_time = average_waiting_time / quantity
        average_service_time = average_service_time / quantity

        self.wigets.listaPromedios.addItem(f"Cantidad de procesos completados:  {quantity}")
        self.wigets.listaPromedios.addItem(f"Tiempo promedio en CPU:  {average_CPU_time}")
        self.wigets.listaPromedios.addItem(f"Tiempo promedio de llegada:  {average_waiting_time}")
        self.wigets.listaPromedios.addItem(f"Tiempo promedio de servicio:  {average_service_time}")
        
        return {
            "average_CPU_time": average_CPU_time,
            "average_waiting_time": average_waiting_time,
            "average_service_time": average_service_time,
        }
