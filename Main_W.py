# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Main_W.ui'
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QLCDNumber, QLabel,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QTableWidget, QTableWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1090, 808)
        MainWindow.setStyleSheet(u"QWidget {\n"
"    background-color: #121212;\n"
"    color: #E0E0E0;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: #1E1E1E;\n"
"    border: 1px solid #292929;\n"
"    color: #E0E0E0;\n"
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
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 30, 141, 16))
        font = QFont()
        font.setFamilies([u"Segoe Print"])
        font.setPointSize(12)
        font.setBold(True)
        self.label.setFont(font)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 520, 141, 16))
        self.label_2.setFont(font)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 290, 201, 16))
        self.label_3.setFont(font)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(600, 130, 201, 16))
        self.label_4.setFont(font)
        self.lcdNumber = QLCDNumber(self.centralwidget)
        self.lcdNumber.setObjectName(u"lcdNumber")
        self.lcdNumber.setGeometry(QRect(150, 0, 64, 23))
        self.lcdNumber_2 = QLCDNumber(self.centralwidget)
        self.lcdNumber_2.setObjectName(u"lcdNumber_2")
        self.lcdNumber_2.setGeometry(QRect(390, 30, 64, 23))
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 0, 141, 16))
        self.label_5.setFont(font)
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(380, 0, 81, 16))
        self.label_6.setFont(font)
        self.Comenzar = QPushButton(self.centralwidget)
        self.Comenzar.setObjectName(u"Comenzar")
        self.Comenzar.setGeometry(QRect(370, 660, 161, 61))
        self.Comenzar.setFont(font)
        self.Comenzar.setStyleSheet(u"QPushButton {\n"
"    background-color: #0B15F5; /* Color de fondo azul */\n"
"    color: #FFFFFF; /* Color de texto blanco */\n"
"    border: none; /* Elimina el borde */\n"
"    padding: 8px 16px; /* Ajusta el espaciado interno */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #4e97ff; /* Cambia el tono de azul al pasar el mouse */\n"
"}\n"
"")
        self.table_pListos = QTableWidget(self.centralwidget)
        if (self.table_pListos.columnCount() < 3):
            self.table_pListos.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.table_pListos.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table_pListos.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table_pListos.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.table_pListos.setObjectName(u"table_pListos")
        self.table_pListos.setGeometry(QRect(10, 60, 311, 211))
        font1 = QFont()
        font1.setFamilies([u"Segoe Print"])
        self.table_pListos.setFont(font1)
        self.table_pListos.setStyleSheet(u"QTableView {\n"
"    background-color: #535353; /* Cambia XXXXXX por el color de fondo deseado */\n"
"    color: #FFFFFF; /* Color de texto */\n"
"}\n"
"QHeaderView::section {\n"
"    background-color: #333333; /* Un color de fondo m\u00e1s claro o m\u00e1s oscuro seg\u00fan tu tema */\n"
"    color: #FFFFFF; /* Un color de texto que contraste bien con el fondo */\n"
"    padding: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"}\n"
"QHeaderView::section {\n"
"    background-color: #333333; /* Un color de fondo m\u00e1s claro o m\u00e1s oscuro seg\u00fan tu tema */\n"
"    color: #FFFFFF; /* Un color de texto que contraste bien con el fondo */\n"
"    padding: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"    font-size: 9pt; /* Un tama\u00f1o m\u00e1s grande de texto */\n"
"    font-family: \"Segoe Print\"; /* Cambia a la fuente que prefieras */\n"
"    font-weight: bold; /* Letras en negritas */\n"
"}\n"
"")
        self.table_pEjecucion = QTableWidget(self.centralwidget)
        if (self.table_pEjecucion.columnCount() < 5):
            self.table_pEjecucion.setColumnCount(5)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table_pEjecucion.setHorizontalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.table_pEjecucion.setHorizontalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.table_pEjecucion.setHorizontalHeaderItem(2, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.table_pEjecucion.setHorizontalHeaderItem(3, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.table_pEjecucion.setHorizontalHeaderItem(4, __qtablewidgetitem7)
        self.table_pEjecucion.setObjectName(u"table_pEjecucion")
        self.table_pEjecucion.setGeometry(QRect(10, 320, 511, 171))
        self.table_pEjecucion.setFont(font1)
        self.table_pEjecucion.setStyleSheet(u"QTableView {\n"
"    background-color: #535353; /* Cambia XXXXXX por el color de fondo deseado */\n"
"    color: #FFFFFF; /* Color de texto */\n"
"}\n"
"QHeaderView::section {\n"
"    background-color: #333333; /* Un color de fondo m\u00e1s claro o m\u00e1s oscuro seg\u00fan tu tema */\n"
"    color: #FFFFFF; /* Un color de texto que contraste bien con el fondo */\n"
"    padding: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"}\n"
"QHeaderView::section {\n"
"    background-color: #333333; /* Un color de fondo m\u00e1s claro o m\u00e1s oscuro seg\u00fan tu tema */\n"
"    color: #FFFFFF; /* Un color de texto que contraste bien con el fondo */\n"
"    padding: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"    font-size: 9pt; /* Un tama\u00f1o m\u00e1s grande de texto */\n"
"    font-family: \"Segoe Print\"; /* Cambia a la fuente que prefieras */\n"
"    font-weight: bold; /* Letras en negritas */\n"
"}")
        self.table_pBloqueados = QTableWidget(self.centralwidget)
        if (self.table_pBloqueados.columnCount() < 2):
            self.table_pBloqueados.setColumnCount(2)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.table_pBloqueados.setHorizontalHeaderItem(0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.table_pBloqueados.setHorizontalHeaderItem(1, __qtablewidgetitem9)
        self.table_pBloqueados.setObjectName(u"table_pBloqueados")
        self.table_pBloqueados.setGeometry(QRect(10, 550, 211, 161))
        self.table_pBloqueados.setFont(font1)
        self.table_pBloqueados.setStyleSheet(u"QTableView {\n"
"    background-color: #535353; /* Cambia XXXXXX por el color de fondo deseado */\n"
"    color: #FFFFFF; /* Color de texto */\n"
"}\n"
"QHeaderView::section {\n"
"    background-color: #333333; /* Un color de fondo m\u00e1s claro o m\u00e1s oscuro seg\u00fan tu tema */\n"
"    color: #FFFFFF; /* Un color de texto que contraste bien con el fondo */\n"
"    padding: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"}\n"
"QHeaderView::section {\n"
"    background-color: #333333; /* Un color de fondo m\u00e1s claro o m\u00e1s oscuro seg\u00fan tu tema */\n"
"    color: #FFFFFF; /* Un color de texto que contraste bien con el fondo */\n"
"    padding: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"    font-size: 9pt; /* Un tama\u00f1o m\u00e1s grande de texto */\n"
"    font-family: \"Segoe Print\"; /* Cambia a la fuente que prefieras */\n"
"    font-weight: bold; /* Letras en negritas */\n"
"}")
        self.table_pTerminados = QTableWidget(self.centralwidget)
        if (self.table_pTerminados.columnCount() < 3):
            self.table_pTerminados.setColumnCount(3)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.table_pTerminados.setHorizontalHeaderItem(0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.table_pTerminados.setHorizontalHeaderItem(1, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.table_pTerminados.setHorizontalHeaderItem(2, __qtablewidgetitem12)
        self.table_pTerminados.setObjectName(u"table_pTerminados")
        self.table_pTerminados.setGeometry(QRect(590, 160, 311, 461))
        self.table_pTerminados.setFont(font1)
        self.table_pTerminados.setStyleSheet(u"QTableView {\n"
"    background-color: #535353; /* Cambia XXXXXX por el color de fondo deseado */\n"
"    color: #FFFFFF; /* Color de texto */\n"
"}\n"
"QHeaderView::section {\n"
"    background-color: #333333; /* Un color de fondo m\u00e1s claro o m\u00e1s oscuro seg\u00fan tu tema */\n"
"    color: #FFFFFF; /* Un color de texto que contraste bien con el fondo */\n"
"    padding: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"}\n"
"QHeaderView::section {\n"
"    background-color: #333333; /* Un color de fondo m\u00e1s claro o m\u00e1s oscuro seg\u00fan tu tema */\n"
"    color: #FFFFFF; /* Un color de texto que contraste bien con el fondo */\n"
"    padding: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"    font-size: 9pt; /* Un tama\u00f1o m\u00e1s grande de texto */\n"
"    font-family: \"Segoe Print\"; /* Cambia a la fuente que prefieras */\n"
"    font-weight: bold; /* Letras en negritas */\n"
"}\n"
"")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1090, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Simulador de Procesos", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Procesos Listos", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Bloqueados", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Procesos en Ejecucion", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Procesos Terminados", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Nuevos Procesos", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Contador", None))
        self.Comenzar.setText(QCoreApplication.translate("MainWindow", u"Comenzar", None))
        ___qtablewidgetitem = self.table_pListos.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem1 = self.table_pListos.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"TME", None));
        ___qtablewidgetitem2 = self.table_pListos.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"TT", None));
        ___qtablewidgetitem3 = self.table_pEjecucion.horizontalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem4 = self.table_pEjecucion.horizontalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"OPE", None));
        ___qtablewidgetitem5 = self.table_pEjecucion.horizontalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"TME", None));
        ___qtablewidgetitem6 = self.table_pEjecucion.horizontalHeaderItem(3)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"TT", None));
        ___qtablewidgetitem7 = self.table_pEjecucion.horizontalHeaderItem(4)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"TR", None));
        ___qtablewidgetitem8 = self.table_pBloqueados.horizontalHeaderItem(0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem9 = self.table_pBloqueados.horizontalHeaderItem(1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"TTB", None));
        ___qtablewidgetitem10 = self.table_pTerminados.horizontalHeaderItem(0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem11 = self.table_pTerminados.horizontalHeaderItem(1)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"OPER", None));
        ___qtablewidgetitem12 = self.table_pTerminados.horizontalHeaderItem(2)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"RL", None));
    # retranslateUi

