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
from PySide6.QtWidgets import (QApplication, QDialog, QHeaderView, QLabel,
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_Dialog(object):
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
        self.openPushButton = QPushButton(Dialog)
        self.openPushButton.setObjectName(u"openPushButton")
        self.openPushButton.setGeometry(QRect(10, 540, 141, 51))
        self.cancelPpushButton = QPushButton(Dialog)
        self.cancelPpushButton.setObjectName(u"cancelPpushButton")
        self.cancelPpushButton.setGeometry(QRect(500, 540, 121, 51))
        self.deletePushButton = QPushButton(Dialog)
        self.deletePushButton.setObjectName(u"deletePushButton")
        self.deletePushButton.setGeometry(QRect(170, 540, 141, 51))

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

