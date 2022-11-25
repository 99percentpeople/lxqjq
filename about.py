from Forms.about_dialog import Ui_aboutDialog
from PySide6.QtCore import Slot
from PySide6.QtGui import Qt, QShowEvent, QTextDocument
from PySide6.QtWidgets import QWidget


class AboutDialog(QWidget, Ui_aboutDialog):
    def __init__(self, parent=None):
        super().__init__(parent, Qt.Dialog)
        if parent is not None:
            self.setAttribute(Qt.WA_ShowModal, True)
        self.setupUi(self)

        with open("./assets/styles/markdown.css", "r") as sf:
                self.textBrowser.document().setDefaultStyleSheet(sf.read())

    def showEvent(self, event: QShowEvent) -> None:
        try:
            with open("README.md", "r", encoding="utf-8") as f:
                self.textBrowser.setMarkdown(
                    f.read())
                self.textBrowser.setHtml(self.textBrowser.toHtml())

        except:
            self.textBrowser.setHtml("<h1>can't find the file named README.md</h1>")
        return super().showEvent(event)

    @Slot()
    def on_closeBtn_clicked(self):
        self.close()
