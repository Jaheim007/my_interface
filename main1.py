import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from Widget.hoverinterface import AccountPage_hover


 
def main():
    app = QApplication(sys.argv)
    home = AccountPage_hover()
    home.show()
    app.exec_()


if __name__ == '__main__':
    main()
