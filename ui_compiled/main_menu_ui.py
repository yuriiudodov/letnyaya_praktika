# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_menu.ui'
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
    QSizePolicy, QWidget)
import diagnostics_menu_ui
from ui_compiled import reports_menu_ui


class Ui_Dialog(object):
    def open_diagnostics_menu(self):
        self.window = QDialog()
        self.ui = diagnostics_menu_ui.Ui_Dialog()

        #self.ui.target_usage(target_usage)

        self.ui.setupUi(self.window)
        self.window.show()
    def open_reports_menu(self):
        self.window = QDialog()
        self.ui = reports_menu_ui.Ui_Dialog()

        #self.ui.target_usage(target_usage)

        self.ui.setupUi(self.window)
        self.window.show()
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(553, 443)
        self.diagnosticPushButton = QPushButton(Dialog, clicked = lambda:self.open_diagnostics_menu())
        self.diagnosticPushButton.setObjectName(u"diagnosticPushButton")
        self.diagnosticPushButton.setGeometry(QRect(10, 380, 171, 41))
        self.reportsPushButton = QPushButton(Dialog, clicked = lambda:self.open_reports_menu())
        self.reportsPushButton.setObjectName(u"reportsPushButton")
        self.reportsPushButton.setGeometry(QRect(380, 380, 161, 41))
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 191, 71))
        font = QFont()
        font.setPointSize(16)
        self.label.setFont(font)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.diagnosticPushButton.setText(QCoreApplication.translate("Dialog", u"\u0414\u0438\u0430\u0433\u043d\u043e\u0441\u0442\u0438\u043a\u0430", None))
        self.reportsPushButton.setText(QCoreApplication.translate("Dialog", u"\u041e\u0442\u0447\u0451\u0442\u044b", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u0413\u043b\u0430\u0432\u043d\u043e\u0435 \u043c\u0435\u043d\u044e", None))
    # retranslateUi

