# 08.Layout.py

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
        self.setWindowTitle("Vertical Layout")
        self.setGeometry(300, 250, 400, 300)
        self.SetLayout()
        self.show()
    def SetLayout(self): # Add Buttons and set the layout
        verticalLayout = QVBoxLayout(self)
        vButton1 = QPushButton('Button 1', self)
        vButton2 = QPushButton('Button 2', self)
        vButton3 = QPushButton('Button 3', self)
        vButton4 = QPushButton('Button 4', self)

        verticalLayout.addWidget(vButton1)
        verticalLayout.addWidget(vButton2)
        verticalLayout.addStretch()
        verticalLayout.addWidget(vButton3)
        verticalLayout.addWidget(vButton4)
        
        self.setLayout(verticalLayout)
        
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
