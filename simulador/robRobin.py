from QRunnable import Worker
from PyQt6.QtCore import *
from PyQt6.QtCore import QMutex
from queue import Queue
import time
import random

from utils import Utils
# La libreria Utils es una clase que usaremos como librerias de funciones auxiliares que usaremos utiles para procesos como ver en pantalla , borrar de pantalla , etc 
# Para mas detalles revisar el archivo "utils.py"

# Inicializo un treathpool para administrar y ejecutar todos los procesos que se van a ejecutar
threadpool = QThreadPool()

# Funcion que permitira iniciar la simulacion
def startRobRobin(windows):
        worker = Worker(windows.simulate_round_robin)
        threadpool.start(worker)

# Funcion que permitira detner la simulacion
def stopRobRobin(window):
    window.mutex.lock()
    window.stop_simulation()
    window.mutex.unlock()
# Clase principal que nos permite iniciar la simulacion del algoritmo RobRobin
class MainWindowRobin(Utils):

   # Inicializacion de la clases , pasamos en los parametro los wigets que usaremos en la ventana actual
    def __init__(self, process_planner_5):
        super().__init__()
        self.mutex = QMutex()
        self.wigets = process_planner_5
        self.quantum = 0
        self.pause_flag = False

    # Metodo para pausar la simulacion
    def stop_simulation(self):
        self.pause_flag = True

    # Metodo del algoritmo
    def simulate_round_robin(self):

        # Obtenemos el valor ingresado por el usuario en el wiget para determinar cuantas operaciones queremos generar y cual es el quantum escogido
        quantum = self.wigets.quatum.value()
        quantity_process = self.wigets.cantidad.value()
        if quantum == 0 or quantity_process == 0:
            return
        self.quantum = quantum
        self.pause_flag = False
        # Reiniciamos todas la vistas
        self.disable_button(self.wigets)
        self.clear_completes_process(self.mutex,self.wigets)
        self.clear_promedy_data(self.mutex,self.wigets)
        self.clear_totalList(self.mutex,self.wigets)
        self.clear_all_process(self.mutex,self.wigets)

       # Creamos la lista aleatoria y declaramos los arrays auxiliares que usaremos para procesar la data, ademas de variables a usar
        self.processes = self.generar_valores_aleatorios(quantity_process)
        print(self.processes)
        self.processes_quantity = len(self.processes)
        self.completed_processes = []
        self.bloqued_processes = []
        self.prepared_queue = Queue() 
        self.clock_cycle = 0
        self.total_block_time = 0

        # Mostramos todos los procesos que fueron creados
        self.show_listProcess(self.mutex,self.wigets,self.processes)

        # Buscamos en los procesos si hay algun proceso que llego en ciclo 0
        for compare_process in self.processes:
            if compare_process["arrival_time"] == 0:
                if self.pause_flag == True:
                    self.show_details(self.mutex,self.wigets,"Finalizo simulacion")
                    self.activate_button(self.wigets)
                    if not self.completed_processes:
                        self.wigets.listaPromedios.addItem(f"Cantidad de procesos completados:  0")
                        self.wigets.listaPromedios.addItem(f"Tiempo promedio en CPU:  0")
                        self.wigets.listaPromedios.addItem(f"Porcentaje de uso del procesador:  0")
                        self.wigets.listaPromedios.addItem(f"Tiempo promedio de llegada:  0")
                        self.wigets.listaPromedios.addItem(f"Tiempo promedio de servicio:  0")
                        self.wigets.listaPromedios.addItem(f"Tiempo promedio de bloqueo:  0")
                    else:
                        self.calculate_promedy(self.wigets,self.completed_processes,self.total_block_time,self.clock_cycle)
                    return
                self.prepared_queue.put(compare_process)
                self.show_process(self.mutex,self.wigets,compare_process)
                self.show_details(self.mutex,self.wigets,f"LLEGO TAREA {compare_process["name"]}, en ciclo {self.clock_cycle} Se agrega a  la cola de tareas el proceso...")
                time.sleep(2)

        # Empiezan validaciones y ciclos
        while True:
            if self.pause_flag == True:
                self.show_details(self.mutex,self.wigets,"Finalizo simulacion")
                self.activate_button(self.wigets)
                if not self.completed_processes:
                    self.wigets.listaPromedios.addItem(f"Cantidad de procesos completados:  0")
                    self.wigets.listaPromedios.addItem(f"Tiempo promedio en CPU:  0")
                    self.wigets.listaPromedios.addItem(f"Porcentaje de uso del procesador:  0")
                    self.wigets.listaPromedios.addItem(f"Tiempo promedio de llegada:  0")
                    self.wigets.listaPromedios.addItem(f"Tiempo promedio de servicio:  0")
                    self.wigets.listaPromedios.addItem(f"Tiempo promedio de bloqueo:  0")
                else:
                    self.calculate_promedy(self.wigets,self.completed_processes,self.total_block_time,self.clock_cycle)
                return
            # Verificamos si hay procesos en cola para ser ejecutados por el CPU
            if self.prepared_queue.empty():
                if self.pause_flag == True:
                    self.show_details(self.mutex,self.wigets,"Finalizo simulacion")
                    self.activate_button(self.wigets)
                    if not self.completed_processes:
                        self.wigets.listaPromedios.addItem(f"Cantidad de procesos completados:  0")
                        self.wigets.listaPromedios.addItem(f"Tiempo promedio en CPU:  0")
                        self.wigets.listaPromedios.addItem(f"Porcentaje de uso del procesador:  0")
                        self.wigets.listaPromedios.addItem(f"Tiempo promedio de llegada:  0")
                        self.wigets.listaPromedios.addItem(f"Tiempo promedio de servicio:  0")
                        self.wigets.listaPromedios.addItem(f"Tiempo promedio de bloqueo:  0")
                    else:
                        self.calculate_promedy(self.wigets,self.completed_processes,self.total_block_time,self.clock_cycle)
                    return
            
                # SINO continuamos ciclo
                self.remove_cpu(self.mutex,self.wigets)
                self.show_details(self.mutex,self.wigets,f"No han llegado mas tareas...")
                time.sleep(1)
                self.clock_cycle = self.clock_cycle + 1
                print("No hay tareas: ")
                print("Ciclo: ",self.clock_cycle)
                print("-----------------------------------------------------------------")
                self.show_clock(self.mutex,self.wigets,self.clock_cycle)

                # Verificamos si hay procesos bloqueados
                if not self.bloqued_processes:
                    # SI NO , no hacemos nada , continua proceso  
                    print("No hay procesos bloqueados...")
                else:
                    # SI si, le restamos el tiempo de espera bloqueado al proceso que este de primero en la cola de bloqueados
                    process_blocked = self.bloqued_processes[0]
                    process_blocked["time_blocked"] = process_blocked["time_blocked"] - 1

                    # Si el proceso bloqueado ya no tiene tiene tiempo bloqueado , se vuelve a reeencolar en la cola de listos
                    if process_blocked["time_blocked"] == 0:
                        self.remove_block_process(self.mutex,self.wigets)
                        self.bloqued_processes.pop(0)
                        self.show_details(self.mutex,self.wigets,f"TERMINO BLOQUEO DE {process_blocked["name"]}, Se agrega a  la cola de tareas el proceso...")
                        time.sleep(2)
                        self.prepared_queue.put(process_blocked)
                        self.show_process(self.mutex,self.wigets,process_blocked)

                # Verificamos si en el ciclo actual llego algun proceso y de haber alguno lo encolamos en la cola de listos
                for compare_process in self.processes:
                    if compare_process["arrival_time"] == self.clock_cycle:
                        self.prepared_queue.put(compare_process)
                        self.show_process(self.mutex,self.wigets,compare_process)
                        self.show_details(self.mutex,self.wigets,f"LLEGO TAREA {compare_process["name"]}, en ciclo {self.clock_cycle} Se agrega a  la cola de tareas el proceso...")
                        time.sleep(2)
                continue 

            # Sacamos el primer proceso que hya en cola
            process = self.prepared_queue.get()

            # Mostramos y actualziamos data en pantalla
            print(f"Inicia la tarea en el ciclo {self.clock_cycle}..........  {process}")
            self.show_details(self.mutex,self.wigets,f"Inicia la tarea {process["name"]}  en el ciclo {self.clock_cycle} ")
            self.show_clock(self.mutex,self.wigets,self.clock_cycle)
            self.show_timeToComplete(self.mutex,self.wigets,process)
            self.show_cpu(self.mutex,self.wigets,f"{process['name']}")
            time.sleep(2)
            self.remove_process(self.mutex,self.wigets)
            task_cycles = 0
            
            # Empiezan a correr los ciclos, con la condicion de que un ciclo solo podra ejecutar una cantidad de ciclos igual al quantum asignado
            while task_cycles <= self.quantum:
                
                if self.pause_flag == True:
                    self.show_details(self.mutex,self.wigets,"Finalizo simulacion")
                    self.activate_button(self.wigets)
                    if not self.completed_processes:
                        self.wigets.listaPromedios.addItem(f"Cantidad de procesos completados:  0")
                        self.wigets.listaPromedios.addItem(f"Tiempo promedio en CPU:  0")
                        self.wigets.listaPromedios.addItem(f"Porcentaje de uso del procesador:  0")
                        self.wigets.listaPromedios.addItem(f"Tiempo promedio de llegada:  0")
                        self.wigets.listaPromedios.addItem(f"Tiempo promedio de servicio:  0")
                        self.wigets.listaPromedios.addItem(f"Tiempo promedio de bloqueo:  0")
                    else:
                        self.calculate_promedy(self.wigets,self.completed_processes,self.total_block_time,self.clock_cycle)
                    return
                
                task_cycles = task_cycles + 1
                self.clock_cycle = self.clock_cycle + 1

                # Verificamos si no hay procesos bloqueados
                if not self.bloqued_processes:  

                    # SI NO , no hacemos nada , continua proceso 
                    print("No hay procesos bloqueados...")
                else:

                    # SI si, le restamos el tiempo de espera bloqueado al proceso que este de primero en la cola de bloqueados
                    process_blocked = self.bloqued_processes[0]
                    process_blocked["time_blocked"] = process_blocked["time_blocked"] - 1
                    self.total_block_time = self.total_block_time + self.total_block_time 
                    # Si el proceso bloqueado ya no tiene tiene tiempo bloqueado , se vuelve a reeencolar en la cola de listos
                    if process_blocked["time_blocked"] == 0:
                        self.remove_block_process(self.mutex,self.wigets)
                        self.bloqued_processes.pop(0)
                        self.show_details(self.mutex,self.wigets,f"TERMINO BLOQUEDO DE {process_blocked["name"]}, Se agrega a  la cola de tareas el proceso...")
                        time.sleep(2)
                        self.prepared_queue.put(process_blocked)
                        self.show_process(self.mutex,self.wigets,process_blocked)
                
                # Restamos 1 al tiempo que queda para que se complete el proceso    
                process["time_to_completed"] = process["time_to_completed"] - 1

                # Aumentamos la cantidad que ha recorrido el actual del proceso en 1
                process["current_time"] = process["current_time"] + 1

                # Si el tiempo para ser completado es 0 , significa que el proceso termino de procesarse , por lo que se le asigna a su parametro de completado como True
                if process["time_to_completed"] == 0:
                    process["completed"] = True

                # Mostramos ciclo actual en pantalla y ciclos por terminar  y proceso ejecutandose actualmente
                print("Ciclo: ",self.clock_cycle)
                self.show_clock(self.mutex,self.wigets,self.clock_cycle)
                self.show_timeToComplete(self.mutex,self.wigets,process)
                print("Sigue ejecutando tarea.......... ",process)
                self.show_details(self.mutex,self.wigets,f"Ejecutando tarea {process["name"]}...")
                time.sleep(2)
                print("")

                # Verificamos si en el ciclo actual llego algun proceso y de haber alguno lo encolamos en la cola de listos
                for compare_process in self.processes:
                    if compare_process["name"] == process["name"]:
                        continue
                    if compare_process["arrival_time"] == self.clock_cycle:
                        self.prepared_queue.put(compare_process)
                        self.show_process(self.mutex,self.wigets,compare_process)
                        print("LLEGO TAREA, Se agrega a  la cola de tareas el proceso...",compare_process)
                        self.show_details(self.mutex,self.wigets,f"LLEGO TAREA {compare_process["name"]}, Se agrega a  la cola de tareas el proceso...")
                        time.sleep(2)

                # Determinamos un posible bloqueo del 20%, cabe destacar que un proceso se puede bloquear incluso si se completa en el ciclo actual
                posibility_block = random.random()
                print(posibility_block)
                if  posibility_block < 0.2:    

                    # Si cae dentro de la condicion bloqueamos proceso

                    # Asignamos un tiempo de bloqueo aleatorio entre 1 y 10
                    time_block = random.randint(1, 10)
                    print(f"Proceso {process['name']} bloqueado por {time_block} ciclos")

                    # Recalculamos y asignamos los nuevos tiempos de espera y tiempo de bloqueo
                    process['time_blocked']  = time_block
                    newtime = process["burst_time"] - process["current_time"]
                    if newtime == 0 or process["time_to_completed"] == 0:
                        newtime = 1
                    process["time_to_completed"] = newtime
                    process["completed"] = False

                    # Sacamos el proceso del cpu y lo mandamos a la cola de bloqueados
                    self.show_details(self.mutex,self.wigets,f"Proceso {process['name']} bloqueado por {time_block} ciclos")
                    self.bloqued_processes.append(process)
                    self.remove_cpu(self.mutex,self.wigets)
                    self.clear_timeToComplete(self.mutex,self.wigets)
                    self.show_bloqued(self.mutex,self.wigets,process)
                    time.sleep(2)           
                    break; 

                # Si el proceso esta marcado como completado entra en la condicion
                if(process["completed"] == True):
                    
                    print(f"Tarea {process["name"]} ya esta completada")

                    # Lo sacamos el CPU y lo Asigamos a la lista  de completados y actualizamos las vistas 
                    self.show_details(self.mutex,self.wigets,f"Tarea {process["name"]} ya esta completada")
                    time.sleep(2)
                    self.remove_cpu(self.mutex,self.wigets)
                    self.clear_timeToComplete(self.mutex,self.wigets)
                    process["total_time"] = self.clock_cycle
                    self.completed_processes.append(process)
                    self.show_completed(self.mutex,self.wigets,process)

                    # La simulacion termina , solo si todos los procesos fueron completados
                    if  self.processes_quantity == len(self.completed_processes) :

                        # Actualizamos las vistas
                        self.remove_process(self.mutex,self.wigets)
                        self.activate_button(self.wigets)
                        self.show_details(self.mutex,self.wigets,"FIN SIMULACION")
                        # Calculamos e imprimimos los valores promedios de los tiempos de los procesos
                        self.calculate_promedy(self.wigets,self.completed_processes,self.total_block_time,self.clock_cycle)
                        return self.completed_processes
                    break
                
                # Comprobamos si el proceso ya excedio el cuanto asignado y no se completo, de ser verdadero esto , sacamos del CPU el proceso y reencolamos en la cola de listos
                if task_cycles == self.quantum and process["completed"] != True:
                    process["total_time"] = self.clock_cycle
                    print("")
                    print("NO TERMINO, Se agrega a  la cola de tareas el proceso.......... ",process)
                    # Actualizamos data en pantalla
                    self.show_details(self.mutex,self.wigets,f"NO TERMINO {process["name"]}, Se agrega a la cola de tareas el proceso...")
                    self.remove_cpu(self.mutex,self.wigets)
                    self.clear_timeToComplete(self.mutex,self.wigets)
                    time.sleep(2)
                    print("")
                    # Reeencolamos el proceso
                    self.prepared_queue.put(process)
                    self.show_process(self.mutex,self.wigets,process)
                    break            
            print("")
        return   

