from PyQt5 import  QtWidgets
from PyQt5.QtWidgets import QDialog,QApplication
from PyQt5.uic import loadUi


class WelcomeScreen(QDialog):
    def __init__(self):
        super(WelcomeScreen, self).__init__()
        loadUi(r'DesignerScreens\login.ui',self)

app = QApplication([])
welcome = WelcomeScreen()
welcome.show()
app.exec_()



# app = QtWidgets.QApplication([])
# w = QtWidgets.QWidget()
# w.show()
# # make sure the window will not close
# app.exec_()