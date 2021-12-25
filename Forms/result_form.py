# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'result_form.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QPushButton, QSizePolicy,
    QTextBrowser, QVBoxLayout, QWidget)

class Ui_ResultForm(object):
    def setupUi(self, ResultForm):
        if not ResultForm.objectName():
            ResultForm.setObjectName(u"ResultForm")
        ResultForm.resize(400, 600)
        self.verticalLayout = QVBoxLayout(ResultForm)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.calcMsg = QTextBrowser(ResultForm)
        self.calcMsg.setObjectName(u"calcMsg")
        self.calcMsg.setReadOnly(True)

        self.verticalLayout.addWidget(self.calcMsg)

        self.widget = QWidget(ResultForm)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.saveBtn = QPushButton(self.widget)
        self.saveBtn.setObjectName(u"saveBtn")

        self.horizontalLayout.addWidget(self.saveBtn)

        self.closeBtn = QPushButton(self.widget)
        self.closeBtn.setObjectName(u"closeBtn")

        self.horizontalLayout.addWidget(self.closeBtn)


        self.verticalLayout.addWidget(self.widget)


        self.retranslateUi(ResultForm)

        QMetaObject.connectSlotsByName(ResultForm)
    # setupUi

    def retranslateUi(self, ResultForm):
        ResultForm.setWindowTitle(QCoreApplication.translate("ResultForm", u"\u8ba1\u7b97\u7ed3\u679c", None))
        self.calcMsg.setPlaceholderText(QCoreApplication.translate("ResultForm", u"\u8fd9\u91cc\u663e\u793a\u8ba1\u7b97\u7ed3\u679c", None))
        self.saveBtn.setText(QCoreApplication.translate("ResultForm", u"\u4fdd\u5b58", None))
        self.closeBtn.setText(QCoreApplication.translate("ResultForm", u"\u5173\u95ed", None))
    # retranslateUi

