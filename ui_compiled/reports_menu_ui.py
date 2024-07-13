# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'reprts_menu.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtSql import QSqlDatabase, QSqlQuery
from PySide6.QtWidgets import (QApplication, QDialog, QHeaderView, QLabel,
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QWidget)
from sqlalchemy import text, create_engine

from ui_compiled import report_edit_ui, settings
from ui_compiled.settings import DB_PATH
import pandas as pd

class Ui_Dialog(object):
    def report_delete(self):
        DB_PATH = settings.DB_PATH  # bezvremennoe reshenie
        VetDbConnnection = QSqlDatabase.addDatabase("QSQLITE")
        VetDbConnnection.setDatabaseName(DB_PATH)
        VetDbConnnection.open()
        VetTableQuery = QSqlQuery()
        sql_query = (f"DELETE FROM otchet WHERE pk ={self.tableWidget.item(self.tableWidget.currentRow(), 0).text()}")
        print(sql_query)

        VetTableQuery.prepare(sql_query)
        ass = VetTableQuery.exec()
        print("uspeh&", ass)

        VetDbConnnection.close()
        self.fill_reports_table()
    def open_report_edit(self):
        self.window = QDialog()
        self.ui = report_edit_ui.Ui_Dialog()

        self.ui.transfer_pk(self.tableWidget.item(self.tableWidget.currentRow(),0).text())

        self.ui.setupUi(self.window)
        self.window.show()
    def fill_reports_table(self):#fill example
        # loads the table

        TABLE_ROW_LIMIT = 10
        # -----------------cities_table------------------------
        vet_db_connection = create_engine(f'sqlite:///{DB_PATH}').connect()

        pandas_SQL_query = f'SELECT * FROM otchet'

        data_for_table = pd.read_sql(text(pandas_SQL_query), vet_db_connection).astype(str)
        self.tableWidget.setColumnCount(12)
        self.tableWidget.setRowCount(len(data_for_table))

        for col_num in range(len(data_for_table.columns)):
            for row_num in range(0, len(data_for_table)):
                self.tableWidget.setItem(row_num, col_num,
                                             QTableWidgetItem(data_for_table.iloc[row_num, col_num]))
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(638, 599)
        self.tableWidget = QTableWidget(Dialog)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(30, 60, 541, 441))
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 0, 351, 41))
        font = QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.openPushButton = QPushButton(Dialog, clicked = lambda:self.open_report_edit())
        self.openPushButton.setObjectName(u"openPushButton")
        self.openPushButton.setGeometry(QRect(10, 540, 141, 51))
        self.cancelPpushButton = QPushButton(Dialog)
        self.cancelPpushButton.setObjectName(u"cancelPpushButton")
        self.cancelPpushButton.setGeometry(QRect(500, 540, 121, 51))
        self.deletePushButton = QPushButton(Dialog, clicked = lambda:self.report_delete())
        self.deletePushButton.setObjectName(u"deletePushButton")
        self.deletePushButton.setGeometry(QRect(170, 540, 141, 51))
        self.fill_reports_table()
        self.fill_reports_table()

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u0441\u043e\u0445\u0440\u0430\u043d\u0451\u043d\u043d\u044b\u0435 \u043e\u0442\u0447\u0451\u0442\u044b", None))
        self.openPushButton.setText(QCoreApplication.translate("Dialog", u"\u043e\u0442\u043a\u0440\u044b\u0442\u044c", None))
        self.cancelPpushButton.setText(QCoreApplication.translate("Dialog", u"\u043e\u0442\u043c\u0435\u043d\u0430", None))
        self.deletePushButton.setText(QCoreApplication.translate("Dialog", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
    # retranslateUi

