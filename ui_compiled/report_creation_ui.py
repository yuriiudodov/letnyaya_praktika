# -*- coding: utf-8 -
import datetime

################################################################################
## Form generated from reading UI file 'report_creation.ui'
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
from PySide6.QtSql import QSqlQuery, QSqlDatabase
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QPlainTextEdit, QPushButton, QSizePolicy, QWidget)
from docx import Document
from datetime import datetime
from sqlalchemy import create_engine, text
from settings import DB_PATH
from ui_compiled import settings


class Ui_Dialog(object):
    def save_report_to_db(self):
        print("report saved")
        # bezvremennoe reshenie

    def debug_replace(self,template_path, output_path):
        doc = Document(template_path)
        for table in doc.tables:
            self.item1=table.cell(0, 1).text = self.datelineEdit.text()
            self.item2 =table.cell(1, 1).text = self.customerlineEdit.text()
            self.item3 =table.cell(2, 1).text = self.customerAddresslineEdit.text()
            self.item4 =table.cell(3, 1).text = self.phonelineEdit.text()
            self.item5 =table.cell(4, 1).text = self.workTypelineEdit.text()
            self.item6 =table.cell(5, 1).text = self.namelineEdit.text()
            self.item7 =table.cell(6, 1).text = self.variouslineEdit.text()
            self.item8 =table.cell(7, 1).text = self.buydatelineEdit.text()
            self.item9 =table.cell(8, 1).text = self.descriptionplainTextEdit.toPlainText()


            DB_PATH = settings.DB_PATH  # bezvremennoe reshenie
            VetDbConnnection = QSqlDatabase.addDatabase("QSQLITE")
            VetDbConnnection.setDatabaseName(DB_PATH)
            VetDbConnnection.open()
            VetTableQuery = QSqlQuery()

            # print(self.otdeLineEdit.text())
            today = datetime.now().strftime("%d %m %Y")
            now = datetime.now().strftime("%H %M %S")
            uid = today+" "+now

            doc.save(output_path+uid+'.docx')
            path = output_path+uid+'.docx'
            sql_query = (
                f"INSERT INTO otchet (date,customer, address,telephone, worktype,name,various,buydate,description, uid, path) VALUES"
                f" ('{self.item1}','{self.item2}','{self.item3}','{self.item4}','{self.item5}','{self.item6}','{self.item7}','{self.item8}','{self.item9}','{uid}', '{path}')  ")
            print(sql_query)

            VetTableQuery.prepare(sql_query)
            ass = VetTableQuery.exec()
            print("uspeh&", ass)



            VetDbConnnection.close()
            # Выполняем запрос с параметром


            #table.cell(8, 1).text = "problem"
    def save_report(self):
        self.debug_replace("C:\MHAD\zaya.docx", "C:\MHAD\zayavka.docx")#pyti tyt
        self.save_report_to_db()
        print("хуйняяяя")
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(868, 711)
        self.customerlineEdit = QLineEdit(Dialog)
        self.customerlineEdit.setObjectName(u"customerlineEdit")
        self.customerlineEdit.setGeometry(QRect(110, 130, 451, 21))
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 120, 78, 26))
        font = QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 50, 78, 26))
        self.label_2.setFont(font)
        self.customerAddresslineEdit = QLineEdit(Dialog)
        self.customerAddresslineEdit.setObjectName(u"customerAddresslineEdit")
        self.customerAddresslineEdit.setGeometry(QRect(180, 190, 311, 21))
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 190, 161, 26))
        self.label_3.setFont(font)
        self.phonelineEdit = QLineEdit(Dialog)
        self.phonelineEdit.setObjectName(u"phonelineEdit")
        self.phonelineEdit.setGeometry(QRect(100, 250, 221, 21))
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 240, 78, 26))
        self.label_4.setFont(font)
        self.workTypelineEdit = QLineEdit(Dialog)
        self.workTypelineEdit.setObjectName(u"workTypelineEdit")
        self.workTypelineEdit.setGeometry(QRect(430, 290, 301, 21))
        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 290, 431, 26))
        self.label_5.setFont(font)
        self.label_6 = QLabel(Dialog)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 340, 271, 26))
        self.label_6.setFont(font)
        self.namelineEdit = QLineEdit(Dialog)
        self.namelineEdit.setObjectName(u"namelineEdit")
        self.namelineEdit.setGeometry(QRect(290, 340, 391, 21))
        self.label_7 = QLabel(Dialog)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 390, 411, 26))
        self.label_7.setFont(font)
        self.variouslineEdit = QLineEdit(Dialog)
        self.variouslineEdit.setObjectName(u"variouslineEdit")
        self.variouslineEdit.setGeometry(QRect(420, 390, 301, 51))
        self.buydatelineEdit = QLineEdit(Dialog)
        self.buydatelineEdit.setObjectName(u"buydatelineEdit")
        self.buydatelineEdit.setGeometry(QRect(420, 460, 271, 21))
        self.label_8 = QLabel(Dialog)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 450, 411, 26))
        self.label_8.setFont(font)

        self.datelineEdit = QLineEdit(Dialog)
        self.datelineEdit.setObjectName(u"datelineEdit")
        self.datelineEdit.setGeometry(QRect(70, 50, 211, 21))
        today = datetime.now().strftime("%d.%m.%Y")
        self.datelineEdit.setText(today)

        self.label_9 = QLabel(Dialog)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(10, 500, 241, 26))
        self.label_9.setFont(font)
        self.descriptionplainTextEdit = QPlainTextEdit(Dialog)
        self.descriptionplainTextEdit.setObjectName(u"descriptionplainTextEdit")
        self.descriptionplainTextEdit.setGeometry(QRect(260, 500, 441, 181))
        self.savePushButton = QPushButton(Dialog, clicked = lambda: self.save_report())
        self.savePushButton.setObjectName(u"savePushButton")
        self.savePushButton.setGeometry(QRect(20, 630, 121, 61))
        self.cancelPushButton = QPushButton(Dialog)
        self.cancelPushButton.setObjectName(u"cancelPushButton")
        self.cancelPushButton.setGeometry(QRect(730, 620, 121, 61))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u0417\u0430\u043a\u0430\u0437\u0447\u0438\u043a", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u0414\u0430\u0442\u0430", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u0410\u0434\u0440\u0435\u0441 \u0437\u0430\u043a\u0430\u0437\u0447\u0438\u043a\u0430", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"\u0422\u0435\u043b\u0435\u0444\u043e\u043d", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"\u0422\u0438\u043f \u0440\u0430\u0431\u043e\u0442(\u0440\u0435\u043c\u043e\u043d\u0442, \u043e\u0431\u0441\u043b\u0443\u0436\u0438\u0432\u0430\u043d\u0438\u0435, \u0434\u0438\u0430\u0433\u043d\u043e\u0441\u0442\u0438\u043a\u0430)", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435 \u043e\u0431\u043e\u0440\u0443\u0434\u043e\u0432\u0430\u043d\u0438\u044f", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"\u041c\u0430\u0440\u043a\u0430, \u043c\u043e\u0434\u0435\u043b\u044c, \u0433\u043e\u0434 \u0432\u044b\u043f\u0443\u0441\u043a\u0430, \u0441\u0435\u0440\u0438\u0439\u043d\u044b\u0439 \u043d\u043e\u043c\u0435\u0440", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"\u0414\u0430\u0442\u0430 \u043f\u043e\u043a\u0443\u043f\u043a\u0438, \u0434\u0430\u0442\u0430 \u0432\u0432\u0435\u0434\u0435\u043d\u0438\u044f \u0432 \u044d\u043a\u0441\u043f\u043b\u0443\u0430\u0442\u0430\u0446\u0438\u044e", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u043d\u0435\u0438\u0441\u043f\u0440\u0430\u0432\u043d\u043e\u0441\u0442\u0438", None))
        self.savePushButton.setText(QCoreApplication.translate("Dialog", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.cancelPushButton.setText(QCoreApplication.translate("Dialog", u"\u043e\u0442\u043c\u0435\u043d\u0430", None))
    # retranslateUi

