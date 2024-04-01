import sys
import time
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QListWidgetItem
from algoritmo3 import Process, ticket_randon
from QRunnable import Worker
from PyQt6.QtCore import *

from robRobin import MainWindowRobin, startRobRobin
from FCFS import MainWindowFCFS, startFCFS
from SJF import MainWindowSJF, startSJF

threadpool = QThreadPool()

# iniciar la aplicación
app = QApplication(sys.argv)

# cargar los archivos .ui
main = uic.loadUi("main_window.ui")
process_planner = uic.loadUi("process_window.ui")
test_priority = uic.loadUi("test1.ui")

process_planner_1 = uic.loadUi("process_window_1.ui")
process_planner_2 = uic.loadUi("process_window_2.ui")
process_planner_5 = uic.loadUi("process_window_5.ui")

def algoritmo1():
    main.hide()
    window = MainWindowFCFS(process_planner_1)
    process_planner_1.play.clicked.connect(lambda: startFCFS(window))
    process_planner_1.label_2.setText(main.algoritmo1.text())
    process_planner_1.show()


def algoritmo2():
    main.hide()
    window = MainWindowSJF(process_planner_2)
    process_planner_2.play.clicked.connect(lambda: startSJF(window))
    process_planner_2.label_2.setText(main.algoritmo2.text())
    process_planner_2.show()


def clock_cpu():
    t = 0
    process_planner.label_10.setText(str(t))
    while t < 10:
        time.sleep(1)
        t += 1
        process_planner.label_10.setText(str(t))


def prueba():
    # Pass the function to execute
    worker = Worker(clock_cpu)  # Any other args, kwargs are passed to the run function
    # Execute
    threadpool.start(worker)


def clock_cpu2():
    t = 0
    process_planner.label_11.setText(str(t))
    while t < 10:
        time.sleep(1)
        t += 1
        process_planner.label_11.setText(str(t))


def prueba2():
    # Pass the function to execute
    worker2 = Worker(
        clock_cpu2
    )  # Any other args, kwargs are passed to the run function
    # Execute
    threadpool.start(worker2)


def algoritmo3():
    main.hide()
    list_ticket = []
    list_process = []
    list_process.append(Process("Pintar", 3, ticket_randon(3, list_ticket)))
    list_process.append(Process("Secar", 4, ticket_randon(5, list_ticket)))
    list_process.append(Process("Pulir", 2, ticket_randon(1, list_ticket)))
    list_process.append(Process("Tapizar", 3, ticket_randon(2, list_ticket)))

    process_planner.label_2.setText(main.algoritmo3.text())

    process_planner.play.pressed.connect(prueba)
    process_planner.play_2.pressed.connect(prueba2)

    # limpiar la lista previa
    process_planner.listWidget.clear()
    for process in list_process:
        add_process = process.name
        process_planner.listWidget.addItem(add_process)
    process_planner.show()


def algoritmo4():
    main.hide()
    process_planner.label_2.setText(main.algoritmo4.text())

    process_planner.show()


def algoritmo5():
    main.hide()
    quantum = 4
    window = MainWindowRobin(process_planner_5)
    process_planner_5.play.clicked.connect(lambda: startRobRobin(window))
    process_planner_5.label_2.setText(main.algoritmo5.text())
    process_planner_5.show()


def algoritmo6():
    main.hide()
    process_planner.label_2.setText(main.algoritmo6.text())
    process_planner.show()


def regresar():
    process_planner.hide()
    main.show()


def salir():
    pass


# botones de los algoritmos

main.algoritmo1.clicked.connect(algoritmo1)
main.algoritmo2.clicked.connect(algoritmo2)
main.algoritmo3.clicked.connect(algoritmo3)
main.algoritmo4.clicked.connect(algoritmo4)
main.algoritmo5.clicked.connect(algoritmo5)
main.algoritmo6.clicked.connect(algoritmo6)

main.salir.clicked.connect(salir)
process_planner.regresar.clicked.connect(regresar)
process_planner_1.regresar.clicked.connect(regresar)
process_planner_2.regresar.clicked.connect(regresar)
process_planner_5.regresar.clicked.connect(regresar)


main.show()
sys.exit(app.exec())
