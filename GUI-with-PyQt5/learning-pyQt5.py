import sys
import PyQt5.QtWidgets as wid
import PyQt5.QtCore as core
import PyQt5.QtGui as gui

# Subclass QMainWindow to customise your application's main window
class MainWindow(wid.QMainWindow):
    customSignal = core.pyqtSignal(str) # Can tell it what to listen for; if using object, it can pass anything

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle('Test App')

        # Use built-in signal for button press
        button = wid.QPushButton('button example')
        button.pressed.connect(self.buttonPushCallback)

        # Add in custom signal that emits a string upon button press;
        # main window handles callback
        self.customSignal.connect(self.buttonPushSlot)

        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(button)
    
    def buttonPushCallback(self):
        print('Pressed')
        self.customSignal.emit('signal sent')

    def buttonPushSlot(self, s):
        print(s)
    
    def contextMenuEvent(self, ev):
        print('Overriding context menu callback.')
        super(MainWindow, self).contextMenuEvent(ev)



app = wid.QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()