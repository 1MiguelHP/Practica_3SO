import logging
import random
from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PySide6.QtCore import QTimer
from Main_W import Ui_MainWindow
from vent_p import Ui_Ventana_Procesos

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
        self.tiempo_transcurrido = 0
        self.tiempo_restante = tiempo
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
        self.ejecucion = None
        self.bloqueados = []  # Para procesos bloqueados esperando un evento
        self.terminados = []  # Para procesos que han completado su ejecución
        self.MAX_PROCESOS_EN_MEMORIA = 3
        self.count = 0
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.revisarProcesos)
        self.timer.start(1000)  # Revisar cada segundo

    def revisarProcesos(self):
        if self.ejecucion:
            print(
                f"Proceso en ejecución: ID={self.ejecucion.id}, Tiempo Transcurrido={self.ejecucion.tiempo_transcurrido}, Tiempo Restante={self.ejecucion.tiempo_restante}")

            # ... (resto del código

            # Incrementar el tiempo transcurrido y calcular el tiempo restante
            self.ejecucion.tiempo_transcurrido += 1
            self.ejecucion.tiempo_restante = self.ejecucion.tiempo - self.ejecucion.tiempo_transcurrido
            # Si el proceso ha terminado, moverlo a la lista de terminados
            if self.ejecucion.tiempo_transcurrido >= self.ejecucion.tiempo:
                self.terminados.append(self.ejecucion)
                self.ejecucion = None
        self.actualizarTablaEjecucion()
        self.actualizarEstados()

    def actualizarEstados(self):
        # Mientras haya procesos nuevos y no se exceda la memoria máxima, mueve procesos a listos
        while self.nuevos and self.totalProcesosEnMemoria() < self.MAX_PROCESOS_EN_MEMORIA:
            proceso_a_listo = self.nuevos.pop(0)  # Saca el primer proceso de la lista de nuevos
            self.listos.append(proceso_a_listo)  # Añade el proceso a la lista de listos
            # Aquí se puede actualizar la UI para reflejar este cambio
            # lamando a un método que actualice la tabla de procesos listos
            self.actualizarTablaListos()
            if self.ejecucion is None and self.listos:
                self.ejecucion = self.listos.pop(0)  # Asigna directamente el proceso a ejecución
                self.actualizarTablaEjecucion()
            self.revisarProcesos()

    def actualizarTablaEjecucion(self):
        # Asegura que haya suficientes filas para los atributos del proceso
        self.ui.table_pListos_2.setRowCount(5)
        print(
            f" actualizarTablaEjecucion - Proceso en ejecución: ID={self.ejecucion.id}, Tiempo Transcurrido={self.ejecucion.tiempo_transcurrido}, Tiempo Restante={self.ejecucion.tiempo_restante}")

        # Si hay un proceso en ejecución, actualiza los valores de las filas en la columna
        if self.ejecucion:
            # Fila 0 para ID
            self.ui.table_pListos_2.setItem(0, 0, QTableWidgetItem(str(self.ejecucion.id)))
            # Fila 1 para OPER
            operacion = f"{self.ejecucion.num1} {self.ejecucion.operador} {self.ejecucion.num2}"
            self.ui.table_pListos_2.setItem(1, 0, QTableWidgetItem(operacion))
            # Fila 2 para TME (Tiempo Máximo Estimado)
            self.ui.table_pListos_2.setItem(2, 0, QTableWidgetItem(str(self.ejecucion.tiempo)))
            # Fila 3 para TT (Tiempo Transcurrido)
            self.ui.table_pListos_2.setItem(3, 0, QTableWidgetItem(str(self.ejecucion.tiempo_transcurrido)))
            # Fila 4 para TR (Tiempo Restante)
            tiempo_restante = max(self.ejecucion.tiempo_restante, 0)  # Asegura no tener valores negativos
            self.ui.table_pListos_2.setItem(4, 0, QTableWidgetItem(str(tiempo_restante)))
        else:
            # Si no hay proceso en ejecución, limpia la tabla
            for i in range(self.ui.table_pListos_2.rowCount()):
                self.ui.table_pListos_2.setItem(i, 0, QTableWidgetItem(""))

        # Ajusta el tamaño de las celdas para que los datos se muestren correctamente
        self.ui.table_pListos_2.resizeColumnsToContents()
        self.ui.table_pListos_2.resizeRowsToContents()

    def actualizarTablaListos(self):
        # Limpia la tabla primero
        self.ui.table_pListos.setRowCount(0)
        # Añade cada proceso listo a la tabla
        for proceso in self.listos:
            row_pos = self.ui.table_pListos.rowCount()
            self.ui.table_pListos.insertRow(row_pos)
            self.ui.table_pListos.setItem(row_pos, 0, QTableWidgetItem(str(proceso.id)))
            self.ui.table_pListos.setItem(row_pos, 1, QTableWidgetItem(str(proceso.tiempo)))
            # Añade otras celdas para tiempo, operador, num1, num2 si es necesario

    def totalProcesosEnMemoria(self):
        total = len(self.listos) + (1 if self.ejecucion else 0) + len(self.bloqueados)
        return total
    def prueba(self):
        self.ui.lcdNumber.display(self.no_procesos)
        print("Número de procesos:", self.no_procesos)
        self.inicializarProcesos()
        self.procesar()
        self.actualizarEstados()

    def procesar(self):
        pass


    def inicializarProcesos(self):
        for i in range(self.no_procesos):
            id = i + 1
            tiempo = random.randint(7, 18)
            operadores = ['+', '-', '*', '/']
            operador = random.choice(operadores)
            num1 = random.randint(1, 20)
            num2 = random.randint(1, 20)
            n_proceso= Proceso(id,tiempo,operador,num1,num2)
            self.nuevos.append(n_proceso)
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
