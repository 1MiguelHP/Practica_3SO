# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ventana_procesos.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QSpinBox, QStatusBar,
    QWidget)

class Ui_Ventana_Procesos(object):
    def setupUi(self, Ventana_Procesos):
        if not Ventana_Procesos.objectName():
            Ventana_Procesos.setObjectName(u"Ventana_Procesos")
        Ventana_Procesos.resize(398, 125)
        Ventana_Procesos.setStyleSheet(u"QWidget {\n"
"    background-color: #121212;\n"
"    color: #E0E0E0;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: #1E1E1E;\n"
"    border: 1px solid #292929;\n"
"    color: #BB86FC;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #292929;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    background-color: #1E1E1E;\n"
"    color: #E0E0E0;\n"
"    border: 1px solid #292929;\n"
"}\n"
"\n"
"QLabel {\n"
"    color: #E0E0E0;\n"
"}\n"
"\n"
"\n"
"")
        self.centralwidget = QWidget(Ventana_Procesos)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(160, 10, 101, 16))
        self.label.setStyleSheet(u"QLabel {\n"
"    font-family: \"Arial\"; /* Cambia \"Arial\" por la familia de fuentes que prefieras */\n"
"    font-size: 8pt; /* Ajusta el tama\u00f1o de la fuente seg\u00fan necesites */\n"
"    font-style: normal; /* Opciones: normal, italic */\n"
"    font-weight: bold; /* Opciones: normal, bold, 100, 200, ..., 900 */\n"
"    color: #E0E0E0; /* Ajusta el color del texto */\n"
"}\n"
"")
        self.spinBox = QSpinBox(self.centralwidget)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setGeometry(QRect(140, 40, 42, 22))
        self.acept = QPushButton(self.centralwidget)
        self.acept.setObjectName(u"acept")
        self.acept.setGeometry(QRect(220, 40, 75, 24))
        Ventana_Procesos.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Ventana_Procesos)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 398, 22))
        Ventana_Procesos.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Ventana_Procesos)
        self.statusbar.setObjectName(u"statusbar")
        Ventana_Procesos.setStatusBar(self.statusbar)

        self.retranslateUi(Ventana_Procesos)

        QMetaObject.connectSlotsByName(Ventana_Procesos)
    # setupUi

    def retranslateUi(self, Ventana_Procesos):
        Ventana_Procesos.setWindowTitle(QCoreApplication.translate("Ventana_Procesos", u"Simulador de Procesos", None))
        self.label.setText(QCoreApplication.translate("Ventana_Procesos", u"Agregar Procesos", None))
        self.acept.setText(QCoreApplication.translate("Ventana_Procesos", u"Aceptar", None))
    # retranslateUi

