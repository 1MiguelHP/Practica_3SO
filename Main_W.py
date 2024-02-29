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
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(90, 50, 141, 16))
        font = QFont()
        font.setFamilies([u"Segoe Print"])
        font.setPointSize(12)
        font.setBold(True)
        self.label.setFont(font)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(410, 380, 141, 16))
        self.label_2.setFont(font)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(400, 40, 201, 16))
        self.label_3.setFont(font)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(720, 50, 201, 16))
        self.label_4.setFont(font)
        self.lcdNumber = QLCDNumber(self.centralwidget)
        self.lcdNumber.setObjectName(u"lcdNumber")
        self.lcdNumber.setGeometry(QRect(150, 0, 64, 23))
        self.lcdNumber_2 = QLCDNumber(self.centralwidget)
        self.lcdNumber_2.setObjectName(u"lcdNumber_2")
        self.lcdNumber_2.setGeometry(QRect(170, 720, 64, 23))
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 0, 141, 16))
        self.label_5.setFont(font)
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(60, 720, 81, 16))
        self.label_6.setFont(font)
        self.Comenzar = QPushButton(self.centralwidget)
        self.Comenzar.setObjectName(u"Comenzar")
        self.Comenzar.setGeometry(QRect(860, 680, 161, 61))
        self.Comenzar.setFont(font)
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
        self.table_pListos.setGeometry(QRect(40, 80, 311, 531))
        font1 = QFont()
        font1.setFamilies([u"Segoe Print"])
        self.table_pListos.setFont(font1)
        self.table_pListos.setStyleSheet(u"QHeaderView::section {\n"
"    background-color: #333333; /* Un color de fondo m\u00e1s claro o m\u00e1s oscuro seg\u00fan tu tema */\n"
"    color: #FFFFFF; /* Un color de texto que contraste bien con el fondo */\n"
"    padding: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"}\n"
"QHeaderView::section {\n"
"    font-size: 9pt; /* Un tama\u00f1o m\u00e1s grande de texto */\n"
"    font-family: \"Segoe Print\"; /* Cambia a la fuente que prefieras */\n"
"    \n"
"}\n"
"")
        self.table_pListos_2 = QTableWidget(self.centralwidget)
        if (self.table_pListos_2.rowCount() < 5):
            self.table_pListos_2.setRowCount(5)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table_pListos_2.setVerticalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.table_pListos_2.setVerticalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.table_pListos_2.setVerticalHeaderItem(2, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.table_pListos_2.setVerticalHeaderItem(3, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.table_pListos_2.setVerticalHeaderItem(4, __qtablewidgetitem7)
        self.table_pListos_2.setObjectName(u"table_pListos_2")
        self.table_pListos_2.setGeometry(QRect(380, 80, 281, 161))
        self.table_pListos_2.setFont(font1)
        self.table_pListos_2.setStyleSheet(u"QHeaderView::section {\n"
"    background-color: #333333; /* Un color de fondo m\u00e1s claro o m\u00e1s oscuro seg\u00fan tu tema */\n"
"    color: #FFFFFF; /* Un color de texto que contraste bien con el fondo */\n"
"    padding: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"}\n"
"QHeaderView::section {\n"
"    font-size: 9pt; /* Un tama\u00f1o m\u00e1s grande de texto */\n"
"    font-family: \"Segoe Print\"; /* Cambia a la fuente que prefieras */\n"
"    \n"
"}\n"
"")
        self.table_pListos_3 = QTableWidget(self.centralwidget)
        if (self.table_pListos_3.columnCount() < 2):
            self.table_pListos_3.setColumnCount(2)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.table_pListos_3.setHorizontalHeaderItem(0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.table_pListos_3.setHorizontalHeaderItem(1, __qtablewidgetitem9)
        self.table_pListos_3.setObjectName(u"table_pListos_3")
        self.table_pListos_3.setGeometry(QRect(400, 410, 211, 231))
        self.table_pListos_3.setFont(font1)
        self.table_pListos_3.setStyleSheet(u"QHeaderView::section {\n"
"    background-color: #333333; /* Un color de fondo m\u00e1s claro o m\u00e1s oscuro seg\u00fan tu tema */\n"
"    color: #FFFFFF; /* Un color de texto que contraste bien con el fondo */\n"
"    padding: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"}\n"
"QHeaderView::section {\n"
"    font-size: 9pt; /* Un tama\u00f1o m\u00e1s grande de texto */\n"
"    font-family: \"Segoe Print\"; /* Cambia a la fuente que prefieras */\n"
"    \n"
"}\n"
"")
        self.table_pListos_4 = QTableWidget(self.centralwidget)
        if (self.table_pListos_4.columnCount() < 3):
            self.table_pListos_4.setColumnCount(3)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.table_pListos_4.setHorizontalHeaderItem(0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.table_pListos_4.setHorizontalHeaderItem(1, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.table_pListos_4.setHorizontalHeaderItem(2, __qtablewidgetitem12)
        self.table_pListos_4.setObjectName(u"table_pListos_4")
        self.table_pListos_4.setGeometry(QRect(710, 90, 321, 531))
        self.table_pListos_4.setFont(font1)
        self.table_pListos_4.setStyleSheet(u"QHeaderView::section {\n"
"    background-color: #333333; /* Un color de fondo m\u00e1s claro o m\u00e1s oscuro seg\u00fan tu tema */\n"
"    color: #FFFFFF; /* Un color de texto que contraste bien con el fondo */\n"
"    padding: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"}\n"
"QHeaderView::section {\n"
"    font-size: 9pt; /* Un tama\u00f1o m\u00e1s grande de texto */\n"
"    font-family: \"Segoe Print\"; /* Cambia a la fuente que prefieras */\n"
"    \n"
"}\n"
"")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1090, 22))
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
        ___qtablewidgetitem3 = self.table_pListos_2.verticalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem4 = self.table_pListos_2.verticalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"OPER", None));
        ___qtablewidgetitem5 = self.table_pListos_2.verticalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"TME", None));
        ___qtablewidgetitem6 = self.table_pListos_2.verticalHeaderItem(3)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"TT", None));
        ___qtablewidgetitem7 = self.table_pListos_2.verticalHeaderItem(4)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"TR", None));
        ___qtablewidgetitem8 = self.table_pListos_3.horizontalHeaderItem(0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem9 = self.table_pListos_3.horizontalHeaderItem(1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"TTB", None));
        ___qtablewidgetitem10 = self.table_pListos_4.horizontalHeaderItem(0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem11 = self.table_pListos_4.horizontalHeaderItem(1)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"OPER", None));
        ___qtablewidgetitem12 = self.table_pListos_4.horizontalHeaderItem(2)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"RL", None));
    # retranslateUi

