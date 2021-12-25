from Forms.about_dialog import Ui_aboutDialog
from PySide6.QtCore import Slot
from PySide6.QtGui import Qt
from PySide6.QtWidgets import QWidget


class AboutDialog(QWidget, Ui_aboutDialog):
    def __init__(self, parent=None):
        super().__init__(parent, Qt.Dialog)
        if parent is not None:
            self.setAttribute(Qt.WA_ShowModal, True)
        self.setupUi(self)
        with open("about.md", "r", encoding="utf-8") as f:
            self.textBrowser.setMarkdown(f.read())

    @Slot()
    def on_closeBtn_clicked(self):
        self.close()
