import subprocess
import sys
import os

from PySide6.QtWidgets import QApplication

if not os.path.exists("./forms"):
    os.mkdir("forms")
for name in os.listdir("./ui"):
    if name.endswith(".ui") and not os.path.isdir(name):
        subprocess.getstatusoutput(
            f"pyside6-uic {os.path.join('./ui', name)} -o {os.path.join('./forms',name.rsplit('.')[0])}.py")

from mainwindow import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    lxqjq = MainWindow()
    lxqjq.show()
    sys.exit(app.exec())
