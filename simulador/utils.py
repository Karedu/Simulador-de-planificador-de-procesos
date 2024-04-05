import random

# Clase de metodos auxiliares

# Se uso el decorador @staticmethod para definir metodos estaticos, que no reciben una referencia implicita a la instancia de la clase (no tiene self como primer parametro) y
# por lo tanto no dependen del estado de una instancia particular de la clase y pueden ser invocados directamente desde la clase Utils sin necesidad de crear una instancia de ella

class Utils:


    # Metodo para generar procesos con valores aleatorios
    @staticmethod
    def generar_valores_aleatorios(quantity):
        processes = []
        for i in range(1, quantity + 1):
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

    # Metodo para calcular los promedio de tiempos de los procesos
    @staticmethod
    def calculate_promedy(wigets,processes):
        average_waiting_time = 0
        average_service_time = 0
        average_CPU_time = 0

        for data in processes:
            CPU_time = data["total_time"] - data["arrival_time"]
            waiting_time = CPU_time - data["burst_time"]
            service_time = data["burst_time"] / CPU_time

            average_CPU_time += CPU_time
            average_waiting_time += waiting_time
            average_service_time += service_time

        quantity = len(processes)
        average_CPU_time /= quantity
        average_waiting_time /= quantity
        average_service_time /= quantity

        wigets.listaPromedios.addItem(f"Cantidad de procesos completados:  {quantity}")
        wigets.listaPromedios.addItem(f"Tiempo promedio en CPU:  {average_CPU_time}")
        wigets.listaPromedios.addItem(f"Tiempo promedio de llegada:  {average_waiting_time}")
        wigets.listaPromedios.addItem(f"Tiempo promedio de servicio:  {average_service_time}")

        return {
            "average_CPU_time": average_CPU_time,
            "average_waiting_time": average_waiting_time,
            "average_service_time": average_service_time,
            "quantity": quantity,
        }
    
    # Agrega un item al wiget llamado listaListos correspondiente a la cola de listos
    @staticmethod
    def rewrite_list(mutex,wigets,message):
        mutex.lock()
        wigets.listaListos.clear()
        for (data) in message:
            print(data)
            wigets.listaListos.addItem(f"{data["name"]} / Burst: {data["burst_time"]} / Arrival: {data["arrival_time"]}")
        mutex.unlock()

    # Actualiza la vista de la lista de la cola de bloqueados
    @staticmethod
    def rewrite_bloqued_list(mutex,wigets,message):
        mutex.lock()
        wigets.listaBloqueados.clear()
        for (data) in message:
            print(data)
            wigets.listaBloqueados.addItem(f"{data["name"]} / Burst: {data["burst_time"]} / Arrival: {data["arrival_time"]}")
        mutex.unlock()

    # Limpia la vista de la cola de listos 
    @staticmethod
    def clear_totalList(mutex,wigets):
        mutex.lock() 
        wigets.listaListos.clear()
        mutex.unlock()
    
    # Muestra los detalles en pantalla de lo que mandemos en mensaje
    @staticmethod
    def show_details(mutex,wigets,message):
        mutex.lock()
        wigets.label_detalles.setText(message)
        mutex.unlock()

    # Muestra el tiempo que le falta para completarse el proceso
    @staticmethod
    def show_timeToComplete(mutex,wigets,data):
        mutex.lock()
        wigets.tiempoRestante.setText(str(data["time_to_completed"]))
        mutex.unlock()

    # Limpia la vista de tiempo por completarse
    @staticmethod
    def clear_timeToComplete(mutex,wigets):
        mutex.lock()
        wigets.tiempoRestante.setText("")
        mutex.unlock()      

    # Agregar proceso el widget a la cola de listos
    @staticmethod
    def show_process(mutex,wigets,data):
        mutex.lock()
        wigets.listaListos.addItem(f"{data["name"]} / Burst: {data["burst_time"]} / Arrival: {data["arrival_time"]}")
        mutex.unlock()

    # Muestra en pantalla el proceso actual en CPU 
    @staticmethod
    def show_cpu(mutex,wigets,message):
        mutex.lock()
        wigets.label_CPU.setText(message)
        mutex.unlock()

    # Limpia lo que hay actualmente en el widget de CPU 
    @staticmethod
    def remove_cpu(mutex,wigets):
        mutex.lock()
        wigets.label_CPU.setText("")
        mutex.unlock()

    # Remueve el primer item de la cola de listos
    @staticmethod  
    def remove_process(mutex,wigets):
        mutex.lock()
        wigets.listaListos.takeItem(0)
        mutex.unlock()

    # Remueve el primer item de la cola de bloqueados 
    @staticmethod
    def remove_block_process(mutex,wigets):
        mutex.lock()
        wigets.listaBloqueados.takeItem(0)
        mutex.unlock()

    # Muestra el ciclo de reloj actual en el widget
    @staticmethod
    def show_clock(mutex,wigets,message):
        mutex.lock()
        wigets.label_11.setText(str(message))
        mutex.unlock()
    
    # Agregar un proceso al widget correspondiente a la lista de completados
    @staticmethod
    def show_completed(mutex,wigets,data):
        mutex.lock()
        wigets.listaCompletados.addItem(f"{data["name"]} / Burst: {data["burst_time"]} / Arrival: {data["arrival_time"]}")
        mutex.unlock()

    # Agregar un proceso al widget correspondiente a la lista de bloqueados
    @staticmethod
    def show_bloqued(mutex,wigets,data):
        mutex.lock()
        wigets.listaBloqueados.addItem(f"{data["name"]} / Burst: {data["burst_time"]} / Arrival: {data["arrival_time"]} / Block: {data["time_blocked"]}")
        mutex.unlock()
    
    # Muestra todos los procesos creados en el widget asignado para mostrar los procesos creados
    @staticmethod
    def show_listProcess(mutex,wigets,process):
        mutex.lock()
        for data in process:
            wigets.listaTodosProcesos.addItem(f"{data["name"]} / Burst: {data["burst_time"]} / Arrival: {data["arrival_time"]}")
        mutex.unlock()
        
    # Limpia el widget que muestra la lista de procesos totales
    @staticmethod
    def clear_all_process(mutex,wigets):
        mutex.lock()
        wigets.listaTodosProcesos.clear()
        mutex.unlock()

    # Limpia el widget que muestra la lista de completados
    @staticmethod
    def clear_completes_process(mutex,wigets):
        mutex.lock()
        wigets.listaCompletados.clear()
        mutex.unlock()

    # Limpia el widget que muestra la lista de promedios
    @staticmethod
    def clear_promedy_data(mutex,wigets):
        mutex.lock()
        wigets.listaPromedios.clear()
        mutex.unlock()
    
    # activa boton de de iniciar simulacion
    @staticmethod
    def activate_button(wigets):
        wigets.play.setEnabled(True)

    # desactiva boton de de iniciar simulacion
    @staticmethod 
    def disable_button(wigets):
        wigets.play.setEnabled(False)