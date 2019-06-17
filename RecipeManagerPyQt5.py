import PyQt5.QtWidgets as wid
import PyQt5.QtCore as core
import PyQt5.QtGui as gui
import os

# Subclass QWidget - just an empty container - to serve as the container for the login page
class LoginPage(wid.QWidget):
    def __init__(self, *args, **kwargs):
        super(LoginPage, self).__init__(*args, **kwargs)
        
        # Set window title
        self.setWindowTitle('Login')

        # Set layout; this is a vertical box orientation
        layout = wid.QVBoxLayout()

        # Add widgets to allow returning users to login
        self.populateReturningUser(layout)

        # Add widgets to allow new users to create username/new recipe DB
        self.populateNewUser(layout)

        # Set layout
        self.setLayout(layout)

    def populateReturningUser(self, layout):
        # Create a label
        returningUserLabel = wid.QLabel('For returning users, enter username:')
        layout.addWidget(returningUserLabel)

        # Create a text entry line
        loginEntry = wid.QLineEdit('Enter Username...')
        layout.addWidget(loginEntry)

        # Create a push button, connect a signal, add to layout
        loginButton = wid.QPushButton('Login')
        loginButton.pressed.connect(self.loginButtonCallback)
        layout.addWidget(loginButton)

    def populateNewUser(self, layout):
        # Create a label
        newUserLabel = wid.QLabel('For new users, choose username:')
        layout.addWidget(newUserLabel)

        # Create a text entry line
        newUserEntry = wid.QLineEdit('Choose New Username...')
        layout.addWidget(newUserEntry)

        # Create a second push button, connect a signal, add to layout
        newUserButton = wid.QPushButton('Register New User')
        newUserButton.pressed.connect(self.newUserButtonCallback)
        layout.addWidget(newUserButton)

    def loginButtonCallback(self):
        print('login')
    
    def newUserButtonCallback(self):
        print('new user')

app = wid.QApplication([])
window = LoginPage()
window.show()
app.exec_()