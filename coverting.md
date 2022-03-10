- for converting ui file to python3 file use that command

py -m PyQt5.uic.pyuic -x [ui file] -o [py file]

- for converting qrc file to python3 file use that command

pyrcc5 -o [py file] [qrc file]

- run the application in the main file

----------------
 
def main():
    app = QApplication(sys.argv)
    home = AccountPage()
    home.show()
    app.exec_()


if __name__ == '__main__':
    main()

----------------

- other py file in widget folder

class AccountPage(QtWidgets.QMainWindow, accueilInterface.Ui_Home):
    def __init__(self):
        super(AccountPage, self).__init__()
        self.setupUi(self)