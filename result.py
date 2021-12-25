import sys

from PySide6.QtCore import SIGNAL, QObject, Signal, Slot
from PySide6.QtGui import Qt
from PySide6.QtWidgets import QFileDialog, QWidget

from Forms.result_form import Ui_ResultForm


class EmittingStr(QObject):
    textWritten = Signal(str)

    def write(self, text):
        self.textWritten.emit(str(text))


class ResultWidget(QWidget, Ui_ResultForm):
    def __init__(self, parent=None):
        super().__init__(parent, Qt.Dialog)
        if parent is not None:
            self.setAttribute(Qt.WA_ShowModal, True)
        self.setupUi(self)

    def showEvent(self, event):
        self.stdout = sys.stdout
        sys.stdout = EmittingStr()
        self.calcMsg.connect(
            sys.stdout, SIGNAL("textWritten(QString)"), self.outputWritten
        )
        QWidget.showEvent(self, event)

    def closeEvent(self, event):
        sys.stdout = self.stdout
        QWidget.closeEvent(self, event)

    @Slot(str)
    def outputWritten(self, text: str):
        self.calcMsg.insertPlainText(text)
        self.calcMsg.ensureCursorVisible()

    @Slot()
    def on_closeBtn_clicked(self):
        self.calcMsg.clear()
        self.close()

    @Slot()
    def on_saveBtn_clicked(self):
        save_file_path, file_type = QFileDialog.getSaveFileName(
            self, "保存计算结果", filter="文本文件 (*.txt)"
        )
        if len(save_file_path) > 0:
            with open(save_file_path, "w", encoding="utf-8") as save_file:
                save_file.write(self.calcMsg.toPlainText())
