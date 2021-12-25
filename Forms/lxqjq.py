# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'lxqjq.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QButtonGroup, QComboBox,
    QFormLayout, QFrame, QGroupBox, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QRadioButton, QScrollArea, QSizePolicy, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(933, 574)
        self.horizontalLayout_3 = QHBoxLayout(MainWindow)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.widget = QWidget(MainWindow)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_8 = QVBoxLayout(self.widget)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.scrollArea_2 = QScrollArea(self.widget)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setMinimumSize(QSize(300, 0))
        self.scrollArea_2.setFrameShape(QFrame.NoFrame)
        self.scrollArea_2.setFrameShadow(QFrame.Plain)
        self.scrollArea_2.setLineWidth(0)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 642, 1033))
        self.verticalLayout_6 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.groupBox_5 = QGroupBox(self.scrollAreaWidgetContents_2)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setFlat(False)
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.materialTable = QTableWidget(self.groupBox_5)
        if (self.materialTable.columnCount() < 5):
            self.materialTable.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.materialTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.materialTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.materialTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.materialTable.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.materialTable.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.materialTable.setObjectName(u"materialTable")
        self.materialTable.setMinimumSize(QSize(0, 150))
        self.materialTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.materialTable.setAlternatingRowColors(False)
        self.materialTable.setSelectionMode(QAbstractItemView.SingleSelection)
        self.materialTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.materialTable.setShowGrid(True)
        self.materialTable.setGridStyle(Qt.SolidLine)
        self.materialTable.setSortingEnabled(True)
        self.materialTable.setWordWrap(True)
        self.materialTable.setCornerButtonEnabled(True)
        self.materialTable.setRowCount(0)
        self.materialTable.horizontalHeader().setVisible(True)
        self.materialTable.horizontalHeader().setCascadingSectionResizes(False)
        self.materialTable.horizontalHeader().setHighlightSections(True)
        self.materialTable.horizontalHeader().setProperty("showSortIndicator", False)
        self.materialTable.verticalHeader().setVisible(False)
        self.materialTable.verticalHeader().setProperty("showSortIndicator", False)

        self.verticalLayout_2.addWidget(self.materialTable)


        self.verticalLayout_6.addWidget(self.groupBox_5)

        self.groupBox_6 = QGroupBox(self.scrollAreaWidgetContents_2)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setFlat(False)
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_6)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pointTable = QTableWidget(self.groupBox_6)
        if (self.pointTable.columnCount() < 4):
            self.pointTable.setColumnCount(4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.pointTable.setHorizontalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.pointTable.setHorizontalHeaderItem(1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.pointTable.setHorizontalHeaderItem(2, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.pointTable.setHorizontalHeaderItem(3, __qtablewidgetitem8)
        self.pointTable.setObjectName(u"pointTable")
        self.pointTable.setMinimumSize(QSize(0, 150))
        self.pointTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.pointTable.setSelectionMode(QAbstractItemView.SingleSelection)
        self.pointTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.pointTable.horizontalHeader().setHighlightSections(True)
        self.pointTable.verticalHeader().setVisible(False)
        self.pointTable.verticalHeader().setProperty("showSortIndicator", False)

        self.verticalLayout_4.addWidget(self.pointTable)


        self.verticalLayout_6.addWidget(self.groupBox_6)

        self.groupBox_7 = QGroupBox(self.scrollAreaWidgetContents_2)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setFlat(False)
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_7)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.unitsTable = QTableWidget(self.groupBox_7)
        if (self.unitsTable.columnCount() < 4):
            self.unitsTable.setColumnCount(4)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.unitsTable.setHorizontalHeaderItem(0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.unitsTable.setHorizontalHeaderItem(1, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.unitsTable.setHorizontalHeaderItem(2, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.unitsTable.setHorizontalHeaderItem(3, __qtablewidgetitem12)
        self.unitsTable.setObjectName(u"unitsTable")
        self.unitsTable.setMinimumSize(QSize(0, 150))
        self.unitsTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.unitsTable.setSelectionMode(QAbstractItemView.SingleSelection)
        self.unitsTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.unitsTable.verticalHeader().setVisible(False)
        self.unitsTable.verticalHeader().setProperty("showSortIndicator", False)

        self.verticalLayout_5.addWidget(self.unitsTable)


        self.verticalLayout_6.addWidget(self.groupBox_7)

        self.groupBox_12 = QGroupBox(self.scrollAreaWidgetContents_2)
        self.groupBox_12.setObjectName(u"groupBox_12")
        self.groupBox_12.setFlat(False)
        self.verticalLayout_7 = QVBoxLayout(self.groupBox_12)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.displacementTable = QTableWidget(self.groupBox_12)
        if (self.displacementTable.columnCount() < 4):
            self.displacementTable.setColumnCount(4)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.displacementTable.setHorizontalHeaderItem(0, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.displacementTable.setHorizontalHeaderItem(1, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.displacementTable.setHorizontalHeaderItem(2, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.displacementTable.setHorizontalHeaderItem(3, __qtablewidgetitem16)
        self.displacementTable.setObjectName(u"displacementTable")
        self.displacementTable.setMinimumSize(QSize(0, 150))
        self.displacementTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.displacementTable.setSelectionMode(QAbstractItemView.SingleSelection)
        self.displacementTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.displacementTable.verticalHeader().setVisible(False)

        self.verticalLayout_7.addWidget(self.displacementTable)


        self.verticalLayout_6.addWidget(self.groupBox_12)

        self.groupBox_9 = QGroupBox(self.scrollAreaWidgetContents_2)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.groupBox_9.setFlat(False)
        self.groupBox_9.setCheckable(False)
        self.verticalLayout_9 = QVBoxLayout(self.groupBox_9)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.singleLoadsTable = QTableWidget(self.groupBox_9)
        if (self.singleLoadsTable.columnCount() < 4):
            self.singleLoadsTable.setColumnCount(4)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.singleLoadsTable.setHorizontalHeaderItem(0, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.singleLoadsTable.setHorizontalHeaderItem(1, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.singleLoadsTable.setHorizontalHeaderItem(2, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.singleLoadsTable.setHorizontalHeaderItem(3, __qtablewidgetitem20)
        self.singleLoadsTable.setObjectName(u"singleLoadsTable")
        self.singleLoadsTable.setMinimumSize(QSize(0, 150))
        self.singleLoadsTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.singleLoadsTable.setSelectionMode(QAbstractItemView.SingleSelection)
        self.singleLoadsTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.singleLoadsTable.verticalHeader().setVisible(False)

        self.verticalLayout_9.addWidget(self.singleLoadsTable)

        self.bothLoadsTable = QTableWidget(self.groupBox_9)
        if (self.bothLoadsTable.columnCount() < 5):
            self.bothLoadsTable.setColumnCount(5)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.bothLoadsTable.setHorizontalHeaderItem(0, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.bothLoadsTable.setHorizontalHeaderItem(1, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.bothLoadsTable.setHorizontalHeaderItem(2, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.bothLoadsTable.setHorizontalHeaderItem(3, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.bothLoadsTable.setHorizontalHeaderItem(4, __qtablewidgetitem25)
        self.bothLoadsTable.setObjectName(u"bothLoadsTable")
        self.bothLoadsTable.setMinimumSize(QSize(0, 150))
        self.bothLoadsTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.bothLoadsTable.setSelectionMode(QAbstractItemView.SingleSelection)
        self.bothLoadsTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.bothLoadsTable.verticalHeader().setVisible(False)

        self.verticalLayout_9.addWidget(self.bothLoadsTable)

        self.verticalLayout_9.setStretch(0, 4)
        self.verticalLayout_9.setStretch(1, 3)

        self.verticalLayout_6.addWidget(self.groupBox_9)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_8.addWidget(self.scrollArea_2)

        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.calcBtn = QPushButton(self.widget_2)
        self.calcBtn.setObjectName(u"calcBtn")

        self.horizontalLayout_2.addWidget(self.calcBtn)

        self.openBtn = QPushButton(self.widget_2)
        self.openBtn.setObjectName(u"openBtn")

        self.horizontalLayout_2.addWidget(self.openBtn)

        self.saveBtn = QPushButton(self.widget_2)
        self.saveBtn.setObjectName(u"saveBtn")

        self.horizontalLayout_2.addWidget(self.saveBtn)

        self.aboutBtn = QPushButton(self.widget_2)
        self.aboutBtn.setObjectName(u"aboutBtn")

        self.horizontalLayout_2.addWidget(self.aboutBtn)


        self.verticalLayout_8.addWidget(self.widget_2)


        self.horizontalLayout_3.addWidget(self.widget)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")

        self.horizontalLayout_3.addLayout(self.verticalLayout_3)

        self.scrollArea = QScrollArea(MainWindow)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMinimumSize(QSize(200, 0))
        self.scrollArea.setMaximumSize(QSize(16777215, 16777215))
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setFrameShadow(QFrame.Plain)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 207, 1531))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox.setObjectName(u"groupBox")
        self.formLayout = QFormLayout(self.groupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.materialType = QComboBox(self.groupBox)
        self.materialType.addItem("")
        self.materialType.setObjectName(u"materialType")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.materialType)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.mE = QLineEdit(self.groupBox)
        self.mE.setObjectName(u"mE")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.mE)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.mI = QLineEdit(self.groupBox)
        self.mI.setObjectName(u"mI")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.mI)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_4)

        self.mA = QLineEdit(self.groupBox)
        self.mA.setObjectName(u"mA")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.mA)

        self.addMaterialBtn = QPushButton(self.groupBox)
        self.addMaterialBtn.setObjectName(u"addMaterialBtn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.addMaterialBtn.sizePolicy().hasHeightForWidth())
        self.addMaterialBtn.setSizePolicy(sizePolicy1)
        self.addMaterialBtn.setMinimumSize(QSize(100, 0))
        self.addMaterialBtn.setFlat(False)

        self.formLayout.setWidget(4, QFormLayout.SpanningRole, self.addMaterialBtn)

        self.modifyMaterialBtn = QPushButton(self.groupBox)
        self.modifyMaterialBtn.setObjectName(u"modifyMaterialBtn")

        self.formLayout.setWidget(5, QFormLayout.SpanningRole, self.modifyMaterialBtn)

        self.removeMaterialBtn = QPushButton(self.groupBox)
        self.removeMaterialBtn.setObjectName(u"removeMaterialBtn")

        self.formLayout.setWidget(6, QFormLayout.SpanningRole, self.removeMaterialBtn)


        self.verticalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.formLayout_2 = QFormLayout(self.groupBox_2)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.xLabel = QLabel(self.groupBox_2)
        self.xLabel.setObjectName(u"xLabel")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.xLabel)

        self.pointX = QLineEdit(self.groupBox_2)
        self.pointX.setObjectName(u"pointX")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.pointX)

        self.yLabel = QLabel(self.groupBox_2)
        self.yLabel.setObjectName(u"yLabel")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.yLabel)

        self.pointY = QLineEdit(self.groupBox_2)
        self.pointY.setObjectName(u"pointY")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.pointY)

        self.Label = QLabel(self.groupBox_2)
        self.Label.setObjectName(u"Label")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.Label)

        self.pointType = QComboBox(self.groupBox_2)
        self.pointType.addItem("")
        self.pointType.addItem("")
        self.pointType.addItem("")
        self.pointType.addItem("")
        self.pointType.setObjectName(u"pointType")

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.pointType)

        self.addPointBtn = QPushButton(self.groupBox_2)
        self.addPointBtn.setObjectName(u"addPointBtn")

        self.formLayout_2.setWidget(3, QFormLayout.SpanningRole, self.addPointBtn)

        self.modifyPointBtn = QPushButton(self.groupBox_2)
        self.modifyPointBtn.setObjectName(u"modifyPointBtn")

        self.formLayout_2.setWidget(4, QFormLayout.SpanningRole, self.modifyPointBtn)

        self.removePointBtn = QPushButton(self.groupBox_2)
        self.removePointBtn.setObjectName(u"removePointBtn")

        self.formLayout_2.setWidget(5, QFormLayout.SpanningRole, self.removePointBtn)


        self.verticalLayout.addWidget(self.groupBox_2)

        self.groupBox_11 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_11.setObjectName(u"groupBox_11")
        self.formLayout_7 = QFormLayout(self.groupBox_11)
        self.formLayout_7.setObjectName(u"formLayout_7")
        self.Label_10 = QLabel(self.groupBox_11)
        self.Label_10.setObjectName(u"Label_10")

        self.formLayout_7.setWidget(0, QFormLayout.LabelRole, self.Label_10)

        self.point1 = QLineEdit(self.groupBox_11)
        self.point1.setObjectName(u"point1")

        self.formLayout_7.setWidget(0, QFormLayout.FieldRole, self.point1)

        self.Label_11 = QLabel(self.groupBox_11)
        self.Label_11.setObjectName(u"Label_11")

        self.formLayout_7.setWidget(1, QFormLayout.LabelRole, self.Label_11)

        self.point2 = QLineEdit(self.groupBox_11)
        self.point2.setObjectName(u"point2")

        self.formLayout_7.setWidget(1, QFormLayout.FieldRole, self.point2)

        self.groupBox_13 = QGroupBox(self.groupBox_11)
        self.groupBox_13.setObjectName(u"groupBox_13")
        self.horizontalLayout_4 = QHBoxLayout(self.groupBox_13)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.UXRbtn = QRadioButton(self.groupBox_13)
        self.buttonGroup = QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.addButton(self.UXRbtn)
        self.UXRbtn.setObjectName(u"UXRbtn")

        self.horizontalLayout_4.addWidget(self.UXRbtn)

        self.UYRBtn = QRadioButton(self.groupBox_13)
        self.buttonGroup.addButton(self.UYRBtn)
        self.UYRBtn.setObjectName(u"UYRBtn")

        self.horizontalLayout_4.addWidget(self.UYRBtn)

        self.phiRBtn = QRadioButton(self.groupBox_13)
        self.buttonGroup.addButton(self.phiRBtn)
        self.phiRBtn.setObjectName(u"phiRBtn")

        self.horizontalLayout_4.addWidget(self.phiRBtn)


        self.formLayout_7.setWidget(2, QFormLayout.SpanningRole, self.groupBox_13)

        self.pushButton = QPushButton(self.groupBox_11)
        self.pushButton.setObjectName(u"pushButton")

        self.formLayout_7.setWidget(4, QFormLayout.SpanningRole, self.pushButton)

        self.modifyButton = QPushButton(self.groupBox_11)
        self.modifyButton.setObjectName(u"modifyButton")

        self.formLayout_7.setWidget(5, QFormLayout.SpanningRole, self.modifyButton)

        self.removeButton = QPushButton(self.groupBox_11)
        self.removeButton.setObjectName(u"removeButton")

        self.formLayout_7.setWidget(6, QFormLayout.SpanningRole, self.removeButton)


        self.verticalLayout.addWidget(self.groupBox_11)

        self.groupBox_3 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.formLayout_3 = QFormLayout(self.groupBox_3)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.Label_12 = QLabel(self.groupBox_3)
        self.Label_12.setObjectName(u"Label_12")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.Label_12)

        self.Label_13 = QLabel(self.groupBox_3)
        self.Label_13.setObjectName(u"Label_13")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.Label_13)

        self.point2CBox = QComboBox(self.groupBox_3)
        self.point2CBox.setObjectName(u"point2CBox")

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.point2CBox)

        self.Label_2 = QLabel(self.groupBox_3)
        self.Label_2.setObjectName(u"Label_2")

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.Label_2)

        self.materialCBox = QComboBox(self.groupBox_3)
        self.materialCBox.setObjectName(u"materialCBox")

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.materialCBox)

        self.addUnitBtn = QPushButton(self.groupBox_3)
        self.addUnitBtn.setObjectName(u"addUnitBtn")

        self.formLayout_3.setWidget(3, QFormLayout.SpanningRole, self.addUnitBtn)

        self.modifyUnitBtn = QPushButton(self.groupBox_3)
        self.modifyUnitBtn.setObjectName(u"modifyUnitBtn")

        self.formLayout_3.setWidget(4, QFormLayout.SpanningRole, self.modifyUnitBtn)

        self.removeUnitBtn = QPushButton(self.groupBox_3)
        self.removeUnitBtn.setObjectName(u"removeUnitBtn")

        self.formLayout_3.setWidget(5, QFormLayout.SpanningRole, self.removeUnitBtn)

        self.point1CBox = QComboBox(self.groupBox_3)
        self.point1CBox.setObjectName(u"point1CBox")

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.point1CBox)


        self.verticalLayout.addWidget(self.groupBox_3)

        self.groupBox_4 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.formLayout_4 = QFormLayout(self.groupBox_4)
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.Label_3 = QLabel(self.groupBox_4)
        self.Label_3.setObjectName(u"Label_3")

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.Label_3)

        self.uxLabel = QLabel(self.groupBox_4)
        self.uxLabel.setObjectName(u"uxLabel")

        self.formLayout_4.setWidget(1, QFormLayout.LabelRole, self.uxLabel)

        self.UX = QLineEdit(self.groupBox_4)
        self.UX.setObjectName(u"UX")

        self.formLayout_4.setWidget(1, QFormLayout.FieldRole, self.UX)

        self.uYLabel = QLabel(self.groupBox_4)
        self.uYLabel.setObjectName(u"uYLabel")

        self.formLayout_4.setWidget(2, QFormLayout.LabelRole, self.uYLabel)

        self.UY = QLineEdit(self.groupBox_4)
        self.UY.setObjectName(u"UY")

        self.formLayout_4.setWidget(2, QFormLayout.FieldRole, self.UY)

        self.Label_4 = QLabel(self.groupBox_4)
        self.Label_4.setObjectName(u"Label_4")

        self.formLayout_4.setWidget(3, QFormLayout.LabelRole, self.Label_4)

        self.phi = QLineEdit(self.groupBox_4)
        self.phi.setObjectName(u"phi")

        self.formLayout_4.setWidget(3, QFormLayout.FieldRole, self.phi)

        self.acceptDisplacementBtn = QPushButton(self.groupBox_4)
        self.acceptDisplacementBtn.setObjectName(u"acceptDisplacementBtn")

        self.formLayout_4.setWidget(4, QFormLayout.SpanningRole, self.acceptDisplacementBtn)

        self.clearDisplacementBtn = QPushButton(self.groupBox_4)
        self.clearDisplacementBtn.setObjectName(u"clearDisplacementBtn")

        self.formLayout_4.setWidget(5, QFormLayout.SpanningRole, self.clearDisplacementBtn)

        self.displacementSelectPoint = QLineEdit(self.groupBox_4)
        self.displacementSelectPoint.setObjectName(u"displacementSelectPoint")
        self.displacementSelectPoint.setReadOnly(True)

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.displacementSelectPoint)


        self.verticalLayout.addWidget(self.groupBox_4)

        self.groupBox_8 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.formLayout_5 = QFormLayout(self.groupBox_8)
        self.formLayout_5.setObjectName(u"formLayout_5")
        self.Label_5 = QLabel(self.groupBox_8)
        self.Label_5.setObjectName(u"Label_5")

        self.formLayout_5.setWidget(0, QFormLayout.LabelRole, self.Label_5)

        self.bothLoadsSelectUnit = QComboBox(self.groupBox_8)
        self.bothLoadsSelectUnit.setObjectName(u"bothLoadsSelectUnit")

        self.formLayout_5.setWidget(0, QFormLayout.FieldRole, self.bothLoadsSelectUnit)

        self.Label_6 = QLabel(self.groupBox_8)
        self.Label_6.setObjectName(u"Label_6")

        self.formLayout_5.setWidget(1, QFormLayout.LabelRole, self.Label_6)

        self.bothLoadsType = QComboBox(self.groupBox_8)
        self.bothLoadsType.addItem("")
        self.bothLoadsType.setObjectName(u"bothLoadsType")

        self.formLayout_5.setWidget(1, QFormLayout.FieldRole, self.bothLoadsType)

        self.Label_14 = QLabel(self.groupBox_8)
        self.Label_14.setObjectName(u"Label_14")

        self.formLayout_5.setWidget(2, QFormLayout.LabelRole, self.Label_14)

        self.bothLoadsValue1 = QLineEdit(self.groupBox_8)
        self.bothLoadsValue1.setObjectName(u"bothLoadsValue1")

        self.formLayout_5.setWidget(2, QFormLayout.FieldRole, self.bothLoadsValue1)

        self.Label_15 = QLabel(self.groupBox_8)
        self.Label_15.setObjectName(u"Label_15")

        self.formLayout_5.setWidget(3, QFormLayout.LabelRole, self.Label_15)

        self.bothLoadsValue2 = QLineEdit(self.groupBox_8)
        self.bothLoadsValue2.setObjectName(u"bothLoadsValue2")

        self.formLayout_5.setWidget(3, QFormLayout.FieldRole, self.bothLoadsValue2)

        self.addBothLoadsBtn = QPushButton(self.groupBox_8)
        self.addBothLoadsBtn.setObjectName(u"addBothLoadsBtn")

        self.formLayout_5.setWidget(4, QFormLayout.SpanningRole, self.addBothLoadsBtn)

        self.removeBothLoadsBtn = QPushButton(self.groupBox_8)
        self.removeBothLoadsBtn.setObjectName(u"removeBothLoadsBtn")

        self.formLayout_5.setWidget(6, QFormLayout.SpanningRole, self.removeBothLoadsBtn)

        self.modifyBothLoadsBtn = QPushButton(self.groupBox_8)
        self.modifyBothLoadsBtn.setObjectName(u"modifyBothLoadsBtn")

        self.formLayout_5.setWidget(5, QFormLayout.SpanningRole, self.modifyBothLoadsBtn)


        self.verticalLayout.addWidget(self.groupBox_8)

        self.groupBox_10 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_10.setObjectName(u"groupBox_10")
        self.formLayout_6 = QFormLayout(self.groupBox_10)
        self.formLayout_6.setObjectName(u"formLayout_6")
        self.Label_7 = QLabel(self.groupBox_10)
        self.Label_7.setObjectName(u"Label_7")

        self.formLayout_6.setWidget(0, QFormLayout.LabelRole, self.Label_7)

        self.singleLoadSelectUnit = QComboBox(self.groupBox_10)
        self.singleLoadSelectUnit.setObjectName(u"singleLoadSelectUnit")

        self.formLayout_6.setWidget(0, QFormLayout.FieldRole, self.singleLoadSelectUnit)

        self.Label_8 = QLabel(self.groupBox_10)
        self.Label_8.setObjectName(u"Label_8")

        self.formLayout_6.setWidget(1, QFormLayout.LabelRole, self.Label_8)

        self.singleLoadType = QComboBox(self.groupBox_10)
        self.singleLoadType.addItem("")
        self.singleLoadType.addItem("")
        self.singleLoadType.addItem("")
        self.singleLoadType.setObjectName(u"singleLoadType")

        self.formLayout_6.setWidget(1, QFormLayout.FieldRole, self.singleLoadType)

        self.Label_9 = QLabel(self.groupBox_10)
        self.Label_9.setObjectName(u"Label_9")

        self.formLayout_6.setWidget(2, QFormLayout.LabelRole, self.Label_9)

        self.singleLoadValue = QLineEdit(self.groupBox_10)
        self.singleLoadValue.setObjectName(u"singleLoadValue")

        self.formLayout_6.setWidget(2, QFormLayout.FieldRole, self.singleLoadValue)

        self.addSingleLoadBtn = QPushButton(self.groupBox_10)
        self.addSingleLoadBtn.setObjectName(u"addSingleLoadBtn")

        self.formLayout_6.setWidget(3, QFormLayout.SpanningRole, self.addSingleLoadBtn)

        self.removeSingleLoadBtn = QPushButton(self.groupBox_10)
        self.removeSingleLoadBtn.setObjectName(u"removeSingleLoadBtn")

        self.formLayout_6.setWidget(5, QFormLayout.SpanningRole, self.removeSingleLoadBtn)

        self.modifySingleLoadBtn = QPushButton(self.groupBox_10)
        self.modifySingleLoadBtn.setObjectName(u"modifySingleLoadBtn")

        self.formLayout_6.setWidget(4, QFormLayout.SpanningRole, self.modifySingleLoadBtn)


        self.verticalLayout.addWidget(self.groupBox_10)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout_3.addWidget(self.scrollArea)

        QWidget.setTabOrder(self.materialTable, self.pointTable)
        QWidget.setTabOrder(self.pointTable, self.unitsTable)
        QWidget.setTabOrder(self.unitsTable, self.displacementTable)
        QWidget.setTabOrder(self.displacementTable, self.singleLoadsTable)
        QWidget.setTabOrder(self.singleLoadsTable, self.scrollArea)
        QWidget.setTabOrder(self.scrollArea, self.materialType)
        QWidget.setTabOrder(self.materialType, self.mE)
        QWidget.setTabOrder(self.mE, self.mI)
        QWidget.setTabOrder(self.mI, self.mA)
        QWidget.setTabOrder(self.mA, self.addMaterialBtn)
        QWidget.setTabOrder(self.addMaterialBtn, self.modifyMaterialBtn)
        QWidget.setTabOrder(self.modifyMaterialBtn, self.removeMaterialBtn)
        QWidget.setTabOrder(self.removeMaterialBtn, self.pointX)
        QWidget.setTabOrder(self.pointX, self.pointY)
        QWidget.setTabOrder(self.pointY, self.pointType)
        QWidget.setTabOrder(self.pointType, self.addPointBtn)
        QWidget.setTabOrder(self.addPointBtn, self.modifyPointBtn)
        QWidget.setTabOrder(self.modifyPointBtn, self.removePointBtn)
        QWidget.setTabOrder(self.removePointBtn, self.point1)
        QWidget.setTabOrder(self.point1, self.point2)
        QWidget.setTabOrder(self.point2, self.UYRBtn)
        QWidget.setTabOrder(self.UYRBtn, self.phiRBtn)
        QWidget.setTabOrder(self.phiRBtn, self.pushButton)
        QWidget.setTabOrder(self.pushButton, self.modifyButton)
        QWidget.setTabOrder(self.modifyButton, self.removeButton)
        QWidget.setTabOrder(self.removeButton, self.point2CBox)
        QWidget.setTabOrder(self.point2CBox, self.materialCBox)
        QWidget.setTabOrder(self.materialCBox, self.addUnitBtn)
        QWidget.setTabOrder(self.addUnitBtn, self.modifyUnitBtn)
        QWidget.setTabOrder(self.modifyUnitBtn, self.removeUnitBtn)
        QWidget.setTabOrder(self.removeUnitBtn, self.UX)
        QWidget.setTabOrder(self.UX, self.UY)
        QWidget.setTabOrder(self.UY, self.phi)
        QWidget.setTabOrder(self.phi, self.acceptDisplacementBtn)
        QWidget.setTabOrder(self.acceptDisplacementBtn, self.clearDisplacementBtn)
        QWidget.setTabOrder(self.clearDisplacementBtn, self.bothLoadsSelectUnit)
        QWidget.setTabOrder(self.bothLoadsSelectUnit, self.bothLoadsType)
        QWidget.setTabOrder(self.bothLoadsType, self.bothLoadsValue1)
        QWidget.setTabOrder(self.bothLoadsValue1, self.bothLoadsValue2)
        QWidget.setTabOrder(self.bothLoadsValue2, self.addBothLoadsBtn)
        QWidget.setTabOrder(self.addBothLoadsBtn, self.modifyBothLoadsBtn)
        QWidget.setTabOrder(self.modifyBothLoadsBtn, self.removeBothLoadsBtn)
        QWidget.setTabOrder(self.removeBothLoadsBtn, self.singleLoadSelectUnit)
        QWidget.setTabOrder(self.singleLoadSelectUnit, self.singleLoadType)
        QWidget.setTabOrder(self.singleLoadType, self.singleLoadValue)
        QWidget.setTabOrder(self.singleLoadValue, self.addSingleLoadBtn)
        QWidget.setTabOrder(self.addSingleLoadBtn, self.modifySingleLoadBtn)
        QWidget.setTabOrder(self.modifySingleLoadBtn, self.removeSingleLoadBtn)
        QWidget.setTabOrder(self.removeSingleLoadBtn, self.point1CBox)

        self.retranslateUi(MainWindow)

        self.addMaterialBtn.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u529b\u5b66\u6c42\u89e3\u5668", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"\u6750\u6599", None))
        ___qtablewidgetitem = self.materialTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u7f16\u53f7", None));
        ___qtablewidgetitem1 = self.materialTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u6750\u6599\u7c7b\u578b", None));
        ___qtablewidgetitem2 = self.materialTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u521a\u5ea6E", None));
        ___qtablewidgetitem3 = self.materialTable.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u9759\u77e9I", None));
        ___qtablewidgetitem4 = self.materialTable.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\u6a2a\u622a\u9762\u79efA", None));
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"\u7ed3\u70b9", None))
        ___qtablewidgetitem5 = self.pointTable.horizontalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"\u7f16\u53f7", None));
        ___qtablewidgetitem6 = self.pointTable.horizontalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"X", None));
        ___qtablewidgetitem7 = self.pointTable.horizontalHeaderItem(2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Y", None));
        ___qtablewidgetitem8 = self.pointTable.horizontalHeaderItem(3)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"\u7ea6\u675f\u7c7b\u578b", None));
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"\u5355\u5143", None))
        ___qtablewidgetitem9 = self.unitsTable.horizontalHeaderItem(0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"\u7f16\u53f7", None));
        ___qtablewidgetitem10 = self.unitsTable.horizontalHeaderItem(1)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"\u7ed3\u70b91", None));
        ___qtablewidgetitem11 = self.unitsTable.horizontalHeaderItem(2)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"\u7ed3\u70b92", None));
        ___qtablewidgetitem12 = self.unitsTable.horizontalHeaderItem(3)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"\u6750\u6599\u7f16\u53f7", None));
        self.groupBox_12.setTitle(QCoreApplication.translate("MainWindow", u"\u4f4d\u79fb", None))
        ___qtablewidgetitem13 = self.displacementTable.horizontalHeaderItem(0)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"\u7ed3\u70b9\u7f16\u53f7", None));
        ___qtablewidgetitem14 = self.displacementTable.horizontalHeaderItem(1)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"UX", None));
        ___qtablewidgetitem15 = self.displacementTable.horizontalHeaderItem(2)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"UY", None));
        ___qtablewidgetitem16 = self.displacementTable.horizontalHeaderItem(3)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"\u03a6", None));
        self.groupBox_9.setTitle(QCoreApplication.translate("MainWindow", u"\u8377\u8f7d", None))
        ___qtablewidgetitem17 = self.singleLoadsTable.horizontalHeaderItem(0)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"\u7f16\u53f7", None));
        ___qtablewidgetitem18 = self.singleLoadsTable.horizontalHeaderItem(1)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"\u7ed3\u70b9\u7f16\u53f7", None));
        ___qtablewidgetitem19 = self.singleLoadsTable.horizontalHeaderItem(2)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"\u7c7b\u578b", None));
        ___qtablewidgetitem20 = self.singleLoadsTable.horizontalHeaderItem(3)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"\u503c", None));
        ___qtablewidgetitem21 = self.bothLoadsTable.horizontalHeaderItem(0)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"\u7f16\u53f7", None));
        ___qtablewidgetitem22 = self.bothLoadsTable.horizontalHeaderItem(1)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"\u5355\u5143\u7f16\u53f7", None));
        ___qtablewidgetitem23 = self.bothLoadsTable.horizontalHeaderItem(2)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"\u7c7b\u578b", None));
        ___qtablewidgetitem24 = self.bothLoadsTable.horizontalHeaderItem(3)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"1\u503c", None));
        ___qtablewidgetitem25 = self.bothLoadsTable.horizontalHeaderItem(4)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"2\u503c", None));
        self.calcBtn.setText(QCoreApplication.translate("MainWindow", u"\u8ba1\u7b97", None))
        self.openBtn.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00", None))
        self.saveBtn.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58", None))
        self.aboutBtn.setText(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u5b9a\u4e49\u6750\u6599", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u6750\u6599\u7c7b\u578b", None))
        self.materialType.setItemText(0, QCoreApplication.translate("MainWindow", u"\u6881\u5355\u5143", None))

        self.label_2.setText(QCoreApplication.translate("MainWindow", u"E", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"I", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"A", None))
        self.addMaterialBtn.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0\u6750\u6599", None))
        self.modifyMaterialBtn.setText(QCoreApplication.translate("MainWindow", u"\u4fee\u6539\u6750\u6599", None))
        self.removeMaterialBtn.setText(QCoreApplication.translate("MainWindow", u"\u5220\u9664\u6750\u6599", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u5b9a\u4e49\u7ed3\u70b9", None))
        self.xLabel.setText(QCoreApplication.translate("MainWindow", u"X\u5750\u6807", None))
        self.yLabel.setText(QCoreApplication.translate("MainWindow", u"Y\u5750\u6807", None))
        self.Label.setText(QCoreApplication.translate("MainWindow", u"\u7ea6\u675f\u7c7b\u578b", None))
        self.pointType.setItemText(0, QCoreApplication.translate("MainWindow", u"\u56fa\u5b9a\u652f\u5ea7", None))
        self.pointType.setItemText(1, QCoreApplication.translate("MainWindow", u"\u94f0\u652f\u5ea7", None))
        self.pointType.setItemText(2, QCoreApplication.translate("MainWindow", u"\u521a\u63a5", None))
        self.pointType.setItemText(3, QCoreApplication.translate("MainWindow", u"\u94f0\u63a5", None))

        self.addPointBtn.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0\u7ed3\u70b9", None))
        self.modifyPointBtn.setText(QCoreApplication.translate("MainWindow", u"\u4fee\u6539\u7ed3\u70b9", None))
        self.removePointBtn.setText(QCoreApplication.translate("MainWindow", u"\u5220\u9664\u7ed3\u70b9", None))
        self.groupBox_11.setTitle(QCoreApplication.translate("MainWindow", u"\u7ed3\u70b9\u8026\u5408", None))
        self.Label_10.setText(QCoreApplication.translate("MainWindow", u"\u7ed3\u70b91", None))
        self.Label_11.setText(QCoreApplication.translate("MainWindow", u"\u7ed3\u70b92", None))
        self.groupBox_13.setTitle(QCoreApplication.translate("MainWindow", u"\u8026\u5408\u81ea\u7531\u5ea6", None))
        self.UXRbtn.setText(QCoreApplication.translate("MainWindow", u"UX", None))
        self.UYRBtn.setText(QCoreApplication.translate("MainWindow", u"UY", None))
        self.phiRBtn.setText(QCoreApplication.translate("MainWindow", u"\u03a6", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0", None))
        self.modifyButton.setText(QCoreApplication.translate("MainWindow", u"\u4fee\u6539", None))
        self.removeButton.setText(QCoreApplication.translate("MainWindow", u"\u5220\u9664", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"\u5b9a\u4e49\u5355\u5143", None))
        self.Label_12.setText(QCoreApplication.translate("MainWindow", u"\u7ed3\u70b91", None))
        self.Label_13.setText(QCoreApplication.translate("MainWindow", u"\u7ed3\u70b92", None))
        self.Label_2.setText(QCoreApplication.translate("MainWindow", u"\u6750\u6599", None))
        self.addUnitBtn.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0\u5355\u5143", None))
        self.modifyUnitBtn.setText(QCoreApplication.translate("MainWindow", u"\u4fee\u6539\u5355\u5143", None))
        self.removeUnitBtn.setText(QCoreApplication.translate("MainWindow", u"\u5220\u9664\u5355\u5143", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"\u7ed3\u70b9\u4f4d\u79fb", None))
        self.Label_3.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u7ed3\u70b9", None))
        self.uxLabel.setText(QCoreApplication.translate("MainWindow", u"UX", None))
        self.uYLabel.setText(QCoreApplication.translate("MainWindow", u"UY", None))
        self.Label_4.setText(QCoreApplication.translate("MainWindow", u"\u03a6", None))
        self.acceptDisplacementBtn.setText(QCoreApplication.translate("MainWindow", u"\u786e\u5b9a", None))
        self.clearDisplacementBtn.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u7a7a", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("MainWindow", u"\u5206\u5e03\u8377\u8f7d", None))
        self.Label_5.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u5355\u5143", None))
        self.Label_6.setText(QCoreApplication.translate("MainWindow", u"\u7c7b\u578b", None))
        self.bothLoadsType.setItemText(0, QCoreApplication.translate("MainWindow", u"\u5206\u5e03\u6a2a\u5411\u529b", None))

        self.Label_14.setText(QCoreApplication.translate("MainWindow", u"1\u503c", None))
        self.Label_15.setText(QCoreApplication.translate("MainWindow", u"2\u503c", None))
        self.addBothLoadsBtn.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0\u5206\u5e03\u8377\u8f7d", None))
        self.removeBothLoadsBtn.setText(QCoreApplication.translate("MainWindow", u"\u5220\u9664\u5206\u5e03\u8377\u8f7d", None))
        self.modifyBothLoadsBtn.setText(QCoreApplication.translate("MainWindow", u"\u4fee\u6539\u5206\u5e03\u8377\u8f7d", None))
        self.groupBox_10.setTitle(QCoreApplication.translate("MainWindow", u"\u96c6\u4e2d\u8377\u8f7d", None))
        self.Label_7.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u7ed3\u70b9", None))
        self.Label_8.setText(QCoreApplication.translate("MainWindow", u"\u7c7b\u578b", None))
        self.singleLoadType.setItemText(0, QCoreApplication.translate("MainWindow", u"\u6574\u4f53X\u65b9\u5411\u529b", None))
        self.singleLoadType.setItemText(1, QCoreApplication.translate("MainWindow", u"\u6574\u4f53Y\u65b9\u5411\u529b", None))
        self.singleLoadType.setItemText(2, QCoreApplication.translate("MainWindow", u"\u5f2f\u77e9", None))

        self.Label_9.setText(QCoreApplication.translate("MainWindow", u"\u503c", None))
        self.addSingleLoadBtn.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0\u96c6\u4e2d\u8377\u8f7d", None))
        self.removeSingleLoadBtn.setText(QCoreApplication.translate("MainWindow", u"\u5220\u9664\u96c6\u4e2d\u8377\u8f7d", None))
        self.modifySingleLoadBtn.setText(QCoreApplication.translate("MainWindow", u"\u4fee\u6539\u96c6\u4e2d\u8377\u8f7d", None))
    # retranslateUi

