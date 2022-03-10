from PyQt5.QtWidgets import QMainWindow, QApplication
from Widget.hover import Ui_mainpage

class AccountPage_hover(QMainWindow, Ui_mainpage):
    def __init__(self):
        super().__init__()
        self.setupUi(self)