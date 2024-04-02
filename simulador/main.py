import sys
import time
import random
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication
from Procesos import Process, ticket_randon, win_process, del_ticket_process
from QRunnable import Worker
from PyQt6.QtCore import *

threadpool = QThreadPool()
# iniciar la aplicacion
app = QApplication(sys.argv)

# cargar los archivos .ui
main = uic.loadUi("main_window.ui")
process_planner_3 = uic.loadUi("process_window_3.ui")
process_planner_6 = uic.loadUi("process_window_6.ui")

# variables para la configuracion del simulador
num_process = 1
speed = 1
stop = False

def algoritmo1():
    pass

def algoritmo2():
    pass

def simulation_algoritmo3():
    # Simulacion con generacion de procesos aleatorios
    global stop
    global speed
    # inicializando variables
    list_ticket = []
    list_waiting = []
    process_running = []
    list_terminated = []
    list_blocked = []
    clock_time = 0
    n_process = num_process
    c_process = 0
    add_waiting_time = 0
    # Desabilitar el boton al iniciar la simulacion
    process_planner_3.play.setEnabled(False)
    process_planner_3.stop.setEnabled(True)
    # limpiar la lista previa
    process_planner_3.listWidget.clear()
    process_planner_3.listWidget_2.clear()
    process_planner_3.label_12.setText("")
    process_planner_3.label_13.setText("")
    process_planner_3.label_10.setText(str(clock_time))
    process_planner_3.t_proc_comp.setText("Total de procesos completados: ")
    process_planner_3.t_total.setText("Tiempo total: ")
    in_cpu = 0
    while (len(list_waiting) > 0 or len(process_running) > 0 or len(list_blocked) > 0 or n_process > 0) and not(stop):        
        # 0. Todos los procesos completados del cpu a terminados
        if len(process_running) != 0:
            if process_running[0].terminated:
                process_running[0].completion_time = process_running[0].wait_time + process_running[0].burst_time
                list_terminated.append(process_running[0])
                process_planner_3.listWidget_2.addItem(str(process_running[0]))
                process_running.remove(process_running[0])
                process_planner_3.label_12.setText("")
            # Actualizar lista de terminados
            process_planner_3.listWidget_2.clear()
            for process in list_terminated:
                process_planner_3.listWidget_2.addItem(str(process))
            time.sleep(speed/2)
        # 1.  Seleccion del proceso ganador
        if len(process_running) == 0 and len(list_waiting) != 0:
            win_ticket = random.choice(list_ticket)
            process_planner_3.label_13.setText(str(win_ticket))            
            in_cpu = win_process(win_ticket, list_waiting)            
            # Pasar el proceso ganador al CPU y eliminarlos de listos
            process_running.append(list_waiting[in_cpu])
            list_ticket = del_ticket_process(process_running[0].ticket, list_ticket)
            process_running[0].running = True           
            process_planner_3.listWidget.clear()
            list_waiting.remove(list_waiting[in_cpu])
            process_planner_3.label_12.setText(str(process_running[0]))
            time.sleep(speed/2)
        # Actualizar lista de listos
        process_planner_3.listWidget.clear()
        for process in list_waiting:
            process_planner_3.listWidget.addItem(str(process))
            process.wait_time += 1 
        # 2. Ejucutar el primer proceso en la lista de bloqueado
        if len(list_blocked) != 0:
            if list_blocked[0].block_time == 0:
                #pasar proceso de bloqueado a lista de espera
                list_blocked[0].blocked = False
                list_blocked[0].give_ticket(ticket_randon(random.randint(1,3),list_ticket))
                list_waiting.append(list_blocked[0])
                list_blocked.remove(list_blocked[0])
            else:
                list_blocked[0].block_time -= 1
        # Acualizar lista de bloqueados
            process_planner_3.listWidget_3.clear()
            for process in list_blocked:
                process_planner_3.listWidget_3.addItem(str(process))
            time.sleep(speed/2)
        # 3. Creacion de procesos random
        if (random.randint(1,4) == 1 or len(list_waiting) == 0) and n_process > 0 and clock_time > 0:
            print("PROCESO CREADO")
            c_process += 1
            n_process -= 1
            process_planner_3.label_19.setText(str(c_process)+"/"+str(num_process))
            list_waiting.append(Process(str(c_process),random.randint(1,5),clock_time))
            list_waiting[-1].give_ticket(ticket_randon(random.randint(1,3),list_ticket))
            process_planner_3.listWidget.addItem(str(list_waiting[-1]))
        time.sleep(speed/2)       
        # Actualizar procesos en espera
        process_planner_3.listWidget.clear()
        for process in list_waiting:
            process_planner_3.listWidget.addItem(str(process))
        time.sleep(speed/2)
        # 4. Ejecuto proceso en CPU 
        if len(process_running) != 0:
            # Bloquear proceso en cpu en caso de cumplirse lo siguiente
            if random.randint(1,5) == 1:
                print("PROCESO BLOQUEADO")
                process_running[0].running = False
                process_running[0].ticket.clear()
                list_blocked.append(process_running[0])
                process_running.clear()
                list_blocked[-1].blocked = True
                list_blocked[-1].lock_number += 1 
                list_blocked[-1].block_time = random.randint(1,5)
                list_blocked[-1].time_blocked += list_blocked[-1].block_time
                #Mostrar cambios en pantalla
                process_planner_3.label_12.clear()
                process_planner_3.listWidget_3.addItem(str(list_blocked[-1]))  
            else:
                # Tiempo de procesamiento
                process_running[0].time_cpu += process_running[0].run()
                process_planner_3.label_12.setText(str(process_running[0]))
        time.sleep(speed)
        clock_time += 1
        process_planner_3.label_10.setText(str(clock_time))
    # Fin de la simulacion
    print("fin de la simulacion")
    process_planner_3.label_10.setText(str(clock_time))
    for process in list_terminated:
        add_waiting_time += process.wait_time
    # Mostrar resultados de la simulacion
    if len(list_terminated) != 0:
        process_planner_3.t_espera.setText("Tiempo promedio de espera: "+str(round(add_waiting_time/len(list_terminated),2)))
    process_planner_3.t_proc_comp.setText("Total de procesos completados: "+str(len(list_terminated))+"/"+str(c_process))
    process_planner_3.t_total.setText("Tiempo total: "+str(clock_time))
    # Habilitar y reiniciar valores de la simulacion
    stop = False
    process_planner_3.play.setEnabled(True)
    process_planner_3.stop.setEnabled(False)

def start_simulation3():
    worker = Worker(simulation_algoritmo3)
    threadpool.start(worker)

def algoritmo3():
    main.hide()
    process_planner_3.label_2.setText(main.algoritmo3.text())
    process_planner_3.play.pressed.connect(start_simulation3)
    process_planner_3.show()

def algoritmo4():
    pass

def algoritmo5():
    pass

def simulation_algoritmo6():
    global stop
    global speed
    # inicializando variables
    list_waiting = []
    process_running = []
    list_terminated = []
    list_blocked = [] 
    clock_time = 0
    n_process = num_process
    c_process = 0
    add_waiting_time = 0    
    # Desabilitar el boton al iniciar la simulacion
    process_planner_6.play.setEnabled(False)
    process_planner_6.stop.setEnabled(True)
    # limpiar la lista previa
    process_planner_6.listWidget.clear()
    process_planner_6.listWidget_2.clear()
    process_planner_6.listWidget_3.clear()
    process_planner_6.label_12.setText("")
    process_planner_6.label_13.setText("")
    process_planner_6.label_10.setText(str(clock_time))
    process_planner_6.t_proc_comp.setText("Total de procesos completados: ")
    process_planner_6.t_total.setText("Tiempo total: ")

    while (len(list_waiting) > 0 or len(process_running) > 0 or len(list_blocked) > 0 or n_process > 0) and not(stop):
        minor = 0
        # 0. Todos los procesos completados del cpu a terminados
        if len(process_running) != 0:
            if process_running[0].terminated:
                process_running[0].completion_time = process_running[0].wait_time + process_running[0].burst_time
                list_terminated.append(process_running[0])
                process_planner_6.listWidget_2.addItem(str(process_running[0]))
                process_running.remove(process_running[0])
                process_planner_6.label_12.setText("")
            # Actualizar lista de terminados
            process_planner_6.listWidget_2.clear()
            for process in list_terminated:
                process_planner_6.listWidget_2.addItem(str(process))
        # 1. Seleccion del proceso en listo con el menor tiempo en CPU 
        if len(list_waiting) != 0:            
            min_time_process = list_waiting[0].time_cpu
            for process in list_waiting:
                if process.time_cpu < min_time_process:
                    min_time_process = process.time_cpu
                    minor = list_waiting.index(process)
            # mostrando el proceso con el menor tiempo
            process_planner_6.label_13.setText("P." + str(list_waiting[minor].name))  
            if len(process_running) == 0:
                # Pasar el proceso con menor tiempo al CPU y eliminarlo de listos
                process_running.append(list_waiting[minor])
                process_running[0].running = True
                list_waiting.remove(list_waiting[minor])                
            # Si el tiempo del proceso en CPU es mayor a un proceso en espera
            elif process_running[0].time_cpu > list_waiting[minor].time_cpu:
                process_running[0].running = False
                list_waiting.append(process_running[0])
                process_running.clear()
                process_running.append(list_waiting[minor])
                list_waiting.remove(list_waiting[minor])          
            # mostrar proceso en cpu
            process_planner_6.label_12.setText(str(process_running[0]))            
        # Actualizar lista de listos
        process_planner_6.listWidget.clear()
        for process in list_waiting:
            process.wait_time += 1 
            process_planner_6.listWidget.addItem(str(process))
        time.sleep(speed/2)
        # 2. Ejecutar el primer proceso en la lista de bloqueado
        if len(list_blocked) != 0:
            if list_blocked[0].block_time == 0:
                #pasar proceso de bloqueado a lista de espera
                list_blocked[0].blocked = False
                list_waiting.append(list_blocked[0])
                list_blocked.remove(list_blocked[0])
            else:
                list_blocked[0].block_time -= 1
        # Acualizar lista de bloqueados
            process_planner_6.listWidget_3.clear()
            for process in list_blocked:
                process_planner_6.listWidget_3.addItem(str(process))
        # 3. Creacion de procesos random
        if (random.randint(1,4) == 1 or len(list_waiting) == 0) and n_process > 0 and clock_time > 0:
            print("PROCESO CREADO")
            c_process += 1
            n_process -= 1
            process_planner_6.label_19.setText(str(c_process)+"/"+str(num_process))
            list_waiting.append(Process(str(c_process),random.randint(1,5),clock_time))
            process_planner_6.listWidget.addItem(str(list_waiting[-1]))
        # Actualizar procesos en espera
        process_planner_6.listWidget.clear()
        for process in list_waiting:
            process_planner_6.listWidget.addItem(str(process))
        time.sleep(speed/2)        
        # 4. Ejecutar proceso en CPU 
        if len(process_running) > 0:
            # Bloquear proceso en cpu en caso de cumplirse lo siguiente
            if random.randint(1,5) == 1:
                print("PROCESO BLOQUEADO")
                process_running[0].running = False
                list_blocked.append(process_running[0])
                process_running.clear()
                list_blocked[-1].blocked = True
                list_blocked[-1].lock_number += 1 
                list_blocked[-1].block_time = random.randint(1,5)
                list_blocked[-1].time_blocked += list_blocked[-1].block_time
                # Mostrar cambios en pantalla
                process_planner_6.label_12.clear()
                process_planner_6.listWidget_3.addItem(str(list_blocked[-1]))  
            else:
                # Tiempo de procesamiento
                process_running[0].time_cpu += process_running[0].run()
                process_planner_6.label_12.setText(str(process_running[0]))
        process_planner_6.listWidget.clear()
        for process in list_waiting:
            process_planner_6.listWidget.addItem(str(process))       
        time.sleep(speed) 
        clock_time += 1
        process_planner_6.label_10.setText(str(clock_time))       
    # Fin de la simulacion
    print("fin de la simulación")
    process_planner_6.label_10.setText(str(clock_time))
    for process in list_terminated:
        add_waiting_time += process.wait_time
    # Mostrar resultados de la simulacion
    if len(list_terminated) != 0:
        process_planner_6.t_espera.setText("Tiempo promedio de espera: "+str(round(add_waiting_time/len(list_terminated),2)))
    process_planner_6.t_proc_comp.setText("Total de procesos completados: "+str(len(list_terminated))+"/"+str(c_process))
    process_planner_6.t_total.setText("Tiempo total: "+str(clock_time))
    # Habilitar y reiniciar valores de la simulación
    stop = False
    process_planner_6.play.setEnabled(True)
    process_planner_6.stop.setEnabled(False)

def start_simulation6():  
    worker = Worker(simulation_algoritmo6)
    threadpool.start(worker)
    
def number_process(num):
    global num_process
    num_process = num
    print(str(num_process))

def speed_simulation(sp):
    global speed
    speed = sp
    print(str(speed))

def stop_simulation():
    print("Simulación detenida")
    global stop
    stop = True
    #process_planner_6.stop.setCheckable(False)

def algoritmo6():
    main.hide()
    process_planner_6.stop.setEnabled(False)
    process_planner_6.label_2.setText(main.algoritmo6.text())
    process_planner_6.play.pressed.connect(start_simulation6)
    process_planner_6.play.setCheckable(True)    
    # global stop = True
    process_planner_6.show()

def back_to_menu():
    process_planner_3.hide()
    process_planner_6.hide()
    main.show()

# botones de los algoritmos
main.algoritmo1.clicked.connect(algoritmo1)
main.algoritmo2.clicked.connect(algoritmo2)
main.algoritmo3.clicked.connect(algoritmo3)
main.algoritmo4.clicked.connect(algoritmo4)
main.algoritmo5.clicked.connect(algoritmo5)
main.algoritmo6.clicked.connect(algoritmo6)
main.salir.clicked.connect(quit)
process_planner_3.regresar.clicked.connect(back_to_menu)
process_planner_6.regresar.clicked.connect(back_to_menu)
process_planner_3.stop.clicked.connect(stop_simulation)
process_planner_6.stop.clicked.connect(stop_simulation)
process_planner_3.spinBox.valueChanged.connect(number_process)
process_planner_6.spinBox.valueChanged.connect(number_process)
process_planner_3.spinBox_2.valueChanged.connect(speed_simulation)
process_planner_6.spinBox_2.valueChanged.connect(speed_simulation)
process_planner_3.salir.clicked.connect(quit)
process_planner_6.salir.clicked.connect(quit)

main.show()
sys.exit(app.exec())