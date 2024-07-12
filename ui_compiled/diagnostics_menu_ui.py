# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'diagnostics_menu.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QPushButton,
    QSizePolicy, QTextEdit, QWidget)
import os
import report_creation_ui
class Ui_Dialog(object):

    def save_report(self):
        self.window = QDialog()
        self.ui = report_creation_ui.Ui_Dialog()

        # self.ui.target_usage(target_usage)

        self.ui.setupUi(self.window)
        self.window.show()
        print("saving report")
    def launch_diagnostic_usb(self):#unused
        import win32com.client

        wmi = win32com.client.GetObject("winmgmts:")
        output = ""
        for usb in wmi.InstancesOf("Win32_USBHub"):
            output+=usb.DeviceID
    def launch_diagnostics(self):
        delimiter = ", "
        #=============
        output = delimiter.join(os.popen('ipconfig').readlines())
        output = output.encode('cp1251').decode('cp866')#fix encoding
        self.outputTextEdit.setText(output)
        print("diagnostic laaunched")
        self.launch_diagnostic_usb()
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(737, 461)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 261, 51))
        font = QFont()
        font.setPointSize(28)
        self.label.setFont(font)
        self.outputTextEdit = QTextEdit(Dialog)
        self.outputTextEdit.setObjectName(u"outputTextEdit")
        self.outputTextEdit.setGeometry(QRect(30, 70, 631, 321))
        self.savePushButton = QPushButton(Dialog, clicked = lambda: self.save_report())
        self.savePushButton.setObjectName(u"savePushButton")
        self.savePushButton.setGeometry(QRect(20, 410, 101, 41))
        self.launchDiagnosticPushButton = QPushButton(Dialog, clicked = lambda:self.launch_diagnostics())
        self.launchDiagnosticPushButton.setObjectName(u"launchDiagnosticPushButton")
        self.launchDiagnosticPushButton.setGeometry(QRect(270, 410, 141, 41))
        self.cancelPushButton = QPushButton(Dialog, clicked = lambda:Dialog.close())
        self.cancelPushButton.setObjectName(u"cancelPushButton")
        self.cancelPushButton.setGeometry(QRect(560, 410, 141, 41))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u0414\u0438\u0430\u0433\u043d\u043e\u0441\u0442\u0438\u043a\u0430", None))
        self.savePushButton.setText(QCoreApplication.translate("Dialog", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.launchDiagnosticPushButton.setText(QCoreApplication.translate("Dialog", u"\u0437\u0430\u043f\u0443\u0441\u0442\u0438\u0442\u044c \u0434\u0438\u0430\u0433\u043d\u043e\u0441\u0442\u0438\u043a\u0443", None))
        self.cancelPushButton.setText(QCoreApplication.translate("Dialog", u"\u043e\u0442\u043c\u0435\u043d\u0430", None))
    # retranslateUi

