from PySide6.QtWidgets import QApplication, QMainWindow
from Main_W import Ui_MainWindow
from vent_p import Ui_Ventana_Procesos

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

class MainWindow(QMainWindow):
    def __init__(self, no_procesos):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.no_procesos = no_procesos
        self.ui.Comenzar.clicked.connect(self.prueba)

    def prueba(self):
        print("Número de procesos:", self.no_procesos)

if __name__ == "__main__":
    app = QApplication([])
    ventana_procesos = VentanaProcesos()
    ventana_procesos.show()
    app.exec()
