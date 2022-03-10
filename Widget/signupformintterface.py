from PyQt5.QtWidgets import QMainWindow, QApplication
from Widget.signupform import Ui_signupform
from Widget.hoverinterface import AccountPage_hover

class AccountPage_signup(QMainWindow, Ui_signupform):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.send_to_hover.clicked.connect(self.hover)

    def hover(self):

        self.win = AccountPage_hover()
        self.win.show()

