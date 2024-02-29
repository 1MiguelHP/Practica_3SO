from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PySide6 import QtWidgets
from Main_W import Ui_MainWindow
from vent_p import Ui_Ventana_Procesos
import logging, random

logging.basicConfig(level=logging.INFO)
class VentanaProcesos(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Ventana_Procesos()
        self.ui.setupUi(self)
        self.ui.acept.clicked.connect(self.abrirMainWindow)
        self.no_procesos = None

    def abrirMainWindow(self):
        self.no_procesos = self.ui.spinBox.value()
        self.hide()
        self.main_window = MainWindow(self.no_procesos)
        self.main_window.show()

#Empezar logica de procesos ------------------------------------------------------------------------------

class Proceso():
    def __init__(self,id, tiempo, operador, num1, num2):
        self.id = id
        self.tiempo = tiempo
        self.operador = operador
        self.num1 = num1
        self.num2 = num2
        #comentados para prueba
#            listo = True
#            ejecucion = False
#            bloqueado = False

class MainWindow(QMainWindow):
    def __init__(self, no_procesos):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.no_procesos = no_procesos
        self.ui.Comenzar.clicked.connect(self.prueba)
        #Inicializaciones de procesos
        self.nuevos = []  # Para procesos recién creados
        self.listos = []  # Para procesos listos para ejecutarse
        self.ejecucion = []
        self.bloqueados = []  # Para procesos bloqueados esperando un evento
        self.terminados = []  # Para procesos que han completado su ejecución
        self.MAX_PROCESOS_EN_MEMORIA = 3
        self.count = 0


    def actualizarEstados(self):
        if self.totalProcesosEnMemoria() < self.MAX_PROCESOS_EN_MEMORIA:
            proceso_a_listo = self.nuevos.pop(0)
            self.listos.append(proceso_a_listo)
        #agregar logica para bloquedos y ejecucion

    def totalProcesosEnMemoria(self):
        total_en_memoria = len(self.listos)
        if self.ejecucion:
            total_en_memoria += 1
        total_en_memoria += len(self.bloqueados)
        return total_en_memoria
    def prueba(self):
        self.ui.lcdNumber.display(self.no_procesos)
        print("Número de procesos:", self.no_procesos)
        self.inicializarProcesos()
        self.procesar()

    def procesar(self):
        self.actualizarDisplayProcesosNuevos()
        for j in range(len(self.nuevos)):
            proceso_actual = self.nuevos[j]
            id = proceso_actual.id
            operador = proceso_actual.operador
            num1 = proceso_actual.num1
            num2 = proceso_actual.num2
            operacion = f"{num1} {operador} {num2}"
            resultado = self.calcular_resultado(num1, num2, operador)
            tiempo = proceso_actual.tiempo


    def inicializarProcesos(self):
        for i in range(self.no_procesos):
            id = i + 1
            tiempo = random.randint(1, 5)
            operadores = ['+', '-', '*', '/']
            operador = random.choice(operadores)
            num1 = random.randint(1, 20)
            num2 = random.randint(1, 20)
            n_proceso= Proceso(id,tiempo,operador,num1,num2)
            self.nuevos.append(n_proceso)
    def actualizarDisplayProcesosNuevos(self):
        self.ui.lcdNumber.display(str(len(self.nuevos)))
    def calcular_resultado(self, op_1, op_2, operando):
        if operando == '+':
            return op_1 + op_2
        elif operando == '-':
            return op_1 - op_2
        elif operando == '*':
            return op_1 * op_2
        elif operando == '/':
            return op_1 / op_2
        elif operando == '%':
            return op_1 % op_2
        else:
            return None

if __name__ == "__main__":
    app = QApplication([])
    ventana_procesos = VentanaProcesos()
    ventana_procesos.show()
    app.exec()
