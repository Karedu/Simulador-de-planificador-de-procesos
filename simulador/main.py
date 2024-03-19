import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication

# iniciar la aplicación
app = QApplication(sys.argv)

# cargar los archivos .ui
main = uic.loadUi("main_window.ui")
process_planner = uic.loadUi("process_window.ui")

def algoritmo1():
    main.hide()
    process_planner.label_2.setText(main.algoritmo1.text())
    process_planner.show()

def algoritmo2():
    main.hide()
    process_planner.label_2.setText(main.algoritmo2.text())
    process_planner.show()

def algoritmo3():
    main.hide()
    process_planner.label_2.setText(main.algoritmo3.text())
    process_planner.show()

def algoritmo4():
    main.hide()
    process_planner.label_2.setText(main.algoritmo4.text())
    process_planner.show()

def algoritmo5():
    main.hide()
    process_planner.label_2.setText(main.algoritmo5.text())
    process_planner.show()

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

main.show()
sys.exit(app.exec())