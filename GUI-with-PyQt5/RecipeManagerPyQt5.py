import PyQt5.QtWidgets as wid
import PyQt5.QtCore as core
import PyQt5.QtGui as gui
import recipe_database_interface as rdi
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

        # Create a text entry line, connect a signal (carriage return)
        loginEntry = wid.QLineEdit('Enter Username...')
        loginEntry.returnPressed.connect(self.loginCallback(loginEntry))
        layout.addWidget(loginEntry)

        # Create a push button, connect a signal (button press)
        loginButton = wid.QPushButton('Login')
        loginButton.pressed.connect(self.loginCallback(loginEntry))
        layout.addWidget(loginButton)

    def populateNewUser(self, layout):
        # Create a label
        newUserLabel = wid.QLabel('For new users, choose username:')
        layout.addWidget(newUserLabel)

        # Create a text entry line, connect a signal (carriage return)
        newUserEntry = wid.QLineEdit('Choose New Username...')
        newUserEntry.returnPressed.connect(self.newUserCallback)
        layout.addWidget(newUserEntry)

        # Create a second push button, connect a signal (button press)
        newUserButton = wid.QPushButton('Register New User')
        newUserButton.pressed.connect(self.newUserCallback)
        layout.addWidget(newUserButton)

    def loginCallback(self):
        print('login')
    
    def newUserCallback(self, lineEdit):
        # Get text from QLineEdit
        usernameNew = lineEdit.text()
    
        # Get current working directory, add 'RecipeManager' for folder to store all
        # related files
        thisFileDir = os.getcwd() + '\\' + 'RecipeManager'

        # If running on new computer, create recipe manager folder
        if(not(os.path.isdir(thisFileDir))):
            os.mkdir(thisFileDir)

        # If folder doesn't already exist, make it and make a new recipe text file
        recipePath = thisFileDir + '\\' + usernameNew
        if(not(os.path.isdir(recipePath))):
            # Create folder with username
            os.mkdir(recipePath)

            # Create new SQL database to hold recipes
            rdi.create_new_DB(recipePath)

############################################################################################################
            # Go to empty DB home page from login page
            # Need to actually implement this!!!
############################################################################################################

        # If directory exists, display 'username already exists'
        elif(os.path.isdir(recipePath)):
            lineEdit.setText("That username is already taken.")
            
        print('new user')
        print(usernameNew)
        print(thisFileDir)

app = wid.QApplication([])
window = LoginPage()
window.show()
app.exec_()