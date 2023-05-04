from PyQt5 import  QtWidgets
# from data import UserManager
from sql_data import UserManager

# app = QtWidgets.QApplication([])
# w = QtWidgets.QWidget()
# w.show()
# # make sure the window will not close
# app.exec_()


from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog
from PyQt5.uic import loadUi
import sys
from PyQt5.QtGui import QPixmap


class WelcomeScreen(QDialog):
    def __init__(self):
        super(WelcomeScreen, self).__init__()
        loadUi(r'DesignerScreens\main_window.ui',self)
        self.login.clicked.connect(self.gotologin)
        self.create_new_account.clicked.connect(self.gotocreate)

    def gotologin(self):
        print('login')
        login = LoginScreen()
        widget.addWidget(login)
        widget.setCurrentWidget(login)

    def gotocreate(self):
        print('create')
        create = CreateScreen()
        widget.addWidget(create)
        widget.setCurrentWidget(create)

class LoginScreen(QDialog):
    def __init__(self):
        super(LoginScreen, self).__init__()
        loadUi(r'DesignerScreens\login_window.ui', self)
        self.login.clicked.connect(self.login_user)

    def login_user(self):
        user_name = self.username.text()
        password = self.password.text()
        try:
            um = UserManager()
            um.user_exists(user_name, password)
        except Exception as E:
            self.label_error.setText(E.args[0])
        else:
            self.label_green.setText(f'user {user_name} logged successfully')
        print(f'user {user_name} logged in successfully')

class CreateScreen(QDialog):
    def __init__(self):
        super(CreateScreen, self).__init__()
        loadUi(r'DesignerScreens\create_new_user_window.ui', self)
        self.signup.clicked.connect(self.create_user)



    def create_user(self):
        print('create')
        user_name = self.username.text()
        password = self.password.text()
        confirm_password = self.confirm_password.text()

        if user_name == '' or password == '' or confirm_password == '':
            self.label_error.setText("must fill all inputs")
        elif password != confirm_password:
            self.label_error.setText("passwords does not match")
        else:
            try:
                um = UserManager()
                um.add_user(user_name, password)
            except Exception as E:
                self.label_error.setText(E.args[0])
            else:
                self.label_error.setText(f'user {user_name} created successfully')
                fill = FillProfileScreen(user_name)
                widget.addWidget(fill)
                widget.setCurrentWidget(fill)

        print(f'user {user_name} created successfully')

class FillProfileScreen(QDialog):
    def __init__(self, user_name):
        self.user_name = user_name
        super(FillProfileScreen, self).__init__()
        loadUi(r'DesignerScreens\fill_profile_window.ui', self)
        self.label_username.setText(user_name)
        self.continue_btn.clicked.connect(self.fill)
        self.upload_btn.clicked.connect(self.upload_image)
    def fill(self):
        fisrt_name = self.firstname.text()
        last_name = self.lastname.text()
        birthday = self.birthday.text()
        gender = self.gender.text()
        #todo

    def upload_image(self):
        # p = QPixmap('photos/curry.jpg')

        app = QApplication(sys.argv)
        # Set the type of file dialog box to photo file selection
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.ExistingFile)
        dialog.setNameFilter("Image Files (*.jpg *.png)")
        # Show the file dialog and get the selected photo file path
        if dialog.exec_() == QFileDialog.Accepted:
            file_path = dialog.selectedFiles()[0]
        # Load the image into a QPixmap object
        pixmap = QPixmap(file_path)
        # Set the pixmap as the label's image
        self.photo.setPixmap(pixmap)


app = QApplication([])

# for one window
welcome = WelcomeScreen()
# welcome.show()


widget = QtWidgets.QStackedWidget()
widget.setFixedWidth(1000)
widget.setFixedHeight(800)
widget.addWidget(welcome)
widget.show()

app.exec_()



