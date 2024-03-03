import logging
import random
from PySide6 import QtWidgets
from PySide6.QtGui import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PySide6.QtCore import QTimer, QEventLoop
from Main_W import Ui_MainWindow
from vent_p import Ui_Ventana_Procesos

logging.basicConfig(level=logging.INFO)


class VentanaProcesos(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Ventana_Procesos()
        self.ui.setupUi(self)
        self.ui.acept.clicked.connect(self.abrirMainWindow)

    def abrirMainWindow(self):
        self.no_procesos = self.ui.spinBox.value()
        self.hide()
        self.main_window = MainWindow(self.no_procesos)
        self.main_window.show()


class MainWindow(QMainWindow):
    def __init__(self, no_procesos):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.no_procesos = no_procesos
        self.bloqueados = []
        self.terminados = []
        self.listos = []
        self.count = 0
        self.timer = QTimer(self)
        self.timer.start(1000)
        self.seconds = 0
        self.teclaPresionada = False
        self.teclaPresionadaI = False
        self.teclaPresionadaP = False
        self.teclaPresionadaC = False
        self.ui.Comenzar.clicked.connect(self.cargar_datos_proceso)
        self.bloqueados_timer = QTimer(self)
        self.bloqueados_timer.timeout.connect(self.funcion_bloqueados)

    def updateTimer(self):
        self.seconds += 1
        self.ui.lcdNumber_2.display(self.seconds)

    def cargar_datos_proceso(self):
        print("Inicio")
        for i in range(self.no_procesos):
            id = i + 1
            tiempo = random.randint(1, 5)
            operadores = ['+', '-', '*', '/']
            operador = random.choice(operadores)
            num1 = random.randint(1, 20)
            num2 = random.randint(1, 20)
            print(tiempo)
            proceso = {
                "id": id,
                "tiempo": tiempo,
                "operador": operador,
                "num1": num1,
                "num2": num2,
            }
            self.listos.append(proceso)
        self.mostrar_en_tabla()

    def mostrar_en_tabla(self):

        self.ui.table_pListos.setColumnCount(3)
        num_procesos = len(self.listos)
        max_procesos_mostrados = min(num_procesos, 3)
        self.ui.table_pListos.setRowCount(max_procesos_mostrados)

        for i in range(max_procesos_mostrados):  # Iterar sobre las primeras 3 filas de la tabla
            proceso = self.listos[i]  # Obtener el proceso de la lista
            id = proceso.get('id', '')
            tiempo = proceso.get('tiempo', '')
            operador = proceso.get('operador', '')

            # Actualizar los elementos de la tabla en la fila i
            self.ui.table_pListos.setItem(i, 0, QTableWidgetItem(str(id)))
            self.ui.table_pListos.setItem(i, 1, QTableWidgetItem(str(tiempo)))
            self.ui.table_pListos.setItem(i, 2, QTableWidgetItem(operador))

        self.tablaEjecucion()  # Llamar a tablaEjecucion después de mostrar los procesos en la tabla

    def tablaEjecucion(self):

        self.ui.table_pEjecucion.setColumnCount(5)
        for i, p_a in enumerate(self.listos):
            QApplication.processEvents()
            self.ui.table_pListos.removeRow(0)
            id = p_a.get('id', '')
            tiempo = p_a.get('tiempo', 0)
            op1 = p_a.get('num1', '')
            op2 = p_a.get('num2', '')
            op = p_a.get('operador', '')
            operacion = f"{op1} {op} {op2}"


            loop = QEventLoop()
            self.ui.table_pEjecucion.setRowCount(1)
            self.ui.table_pEjecucion.setItem(0, 0, QTableWidgetItem(str(id)))
            self.ui.table_pEjecucion.setItem(0, 1, QTableWidgetItem(operacion))
            self.ui.table_pEjecucion.setItem(0, 2, QTableWidgetItem(str(tiempo)))
            self.ui.table_pEjecucion.setItem(0, 3, QTableWidgetItem(str(tiempo)))
            self.ui.table_pEjecucion.setItem(0, 4, QTableWidgetItem(str(tiempo)))


            # Evento Bloqueo-------------------
            if self.teclaPresionada:
                self.teclaPresionada = True

                self.bloqueados.append(p_a)
                self.listos.pop(i)
                continue
            # ---------------------------------

            # Evento interrumpir--------------
            if self.teclaPresionadaI:
                self.teclaPresionadaI = True
                self.terminados.append(p_a)
            #----------------------------------

            #Evento pausar-------------
            #-------------------------
            #Evento continuar----------
            #-------------------------
            QTimer.singleShot(tiempo * 1000, loop.exit)
            loop.exec_()

            self.terminados.append(p_a)  # Añadir el proceso a la lista de terminados

            self.Tabla_Terminados()  # Actualizar la tabla de procesos terminados


    def funcion_bloqueados(self):
        print(self.bloqueados)
        self.ui.table_pEjecucion.clearContents()
        self.ui.table_pBloqueados.setRowCount(3)
        self.ui.table_pBloqueados.setColumnCount(2)  # Establecer el número de filas
        for i, proceso in enumerate(self.bloqueados):
            id_ = proceso.get('id', '')
            tiempo_bloqueado = 5

            self.ui.table_pBloqueados.setItem(i, 0, QTableWidgetItem(str(id_)))
            self.ui.table_pBloqueados.setItem(i, 1, QTableWidgetItem(str(tiempo_bloqueado)))
            self.bloqueados_timer.start(tiempo_bloqueado * 1000)
            self.ui.table_pBloqueados.removeRow(1)


    def Tabla_Terminados(self):

        self.ui.table_pTerminados.setRowCount(len(self.terminados))  # Establecer el número de filas
        for i, proceso in enumerate(self.terminados):
            id_ = proceso.get('id', '')
            op1 = proceso.get('num1', '')
            op2 = proceso.get('num2', '')
            op = proceso.get('operador', '')
            operacion = f"{op1} {op} {op2}"
            resultado = self.calcular_resultado(op1, op2, op)

            self.ui.table_pTerminados.setItem(i, 0, QTableWidgetItem(str(id_)))
            self.ui.table_pTerminados.setItem(i, 1, QTableWidgetItem(str(operacion)))
            self.ui.table_pTerminados.setItem(i, 2, QTableWidgetItem(str(resultado)))
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

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_B:
            print("PresionB")
            self.teclaPresionada = True
            self.funcion_bloqueados()
        if event.key() == Qt.Key_I:
            print("Presion_I")
            self.teclaPresionadaI = True
            self.tabla_TerminadosI()


if __name__ == "__main__":
    app = QApplication([])
    ventana_procesos = VentanaProcesos()
    ventana_procesos.show()
    app.exec()
