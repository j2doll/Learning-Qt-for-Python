# 10.Widget.py

# Import required modules
import sys, time
from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *

# Our main window class
class MainWindow(QWidget):
    def __init__(self): # Constructor function
        super(MainWindow,self).__init__()
        self.initGUI()
    def initGUI(self):
        self.setWindowTitle("Form Layout")
        self.setGeometry(300, 250, 400, 300)
        self.SetLayout()
        self.show()
    def SetLayout(self): # Add Buttons and set the layout
        formLayout = QFormLayout(self)
        labelUsername = QLabel("Username")
        txtUsername = QLineEdit()
        labelPassword = QLabel("Password")
        txtPassword = QLineEdit()

        formLayout.addRow(labelUsername, txtUsername)
        formLayout.addRow(labelPassword, txtPassword)

        self.setLayout(formLayout)
       
if __name__ == '__main__':
    # Exception Handling
    try:
        myApp = QApplication(sys.argv)
        mainWindow = MainWindow()
        myApp.exec_()
        sys.exit(0)
    except NameError:
        print("Name Error:", sys.exc_info()[1])
    except SystemExit:
        print("Closing Window...")
    except Exception:
        print(sys.exc_info()[1])
