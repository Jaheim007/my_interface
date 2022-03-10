import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from Widget.signupformintterface import AccountPage_signup


 
def main():
    app = QApplication(sys.argv)
    home = AccountPage_signup()
    home.show()
    app.exec_()


if __name__ == '__main__':
    main()
