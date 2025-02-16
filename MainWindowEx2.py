import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from MainWindow2 import Ui_MainWindow2
from handler1 import AccountHandler
from MainWindowEx3 import MainWindowEx3

class MainWindowEx2(QMainWindow, Ui_MainWindow2):
    pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindowEx2()
    window.show()
    sys.exit(app.exec())
