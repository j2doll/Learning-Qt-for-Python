# .py 

# Import required modules
import sys, time
from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *

# Our main window class
class MainWindow(QWidget):
    # Constructor function
    def __init__(self):
        super(MainWindow,self).__init__()
        self.initGUI()
    def initGUI(self):
        self.setWindowTitle("Grid Layout")
        self.setGeometry(300, 250, 400, 300)
        self.SetLayout()
        self.show()
    def SetLayout(self): # Add Buttons and set the layout
        gridLayout = QGridLayout(self)
        gButton1 = QPushButton('Button 1', self)
        gButton2 = QPushButton('Button 2', self)
        gButton3 = QPushButton('Button 3', self)
        gButton4 = QPushButton('Button 4', self)
        gButton5 = QPushButton('Button 5', self)

        gridLayout.addWidget(gButton1, 0, 0)
        gridLayout.addWidget(gButton2, 0, 1)
        gridLayout.addWidget(gButton3, 1, 0, 1, 2)
        gridLayout.addWidget(gButton4, 2, 0)
        gridLayout.addWidget(gButton5, 2, 1)
        
        self.setLayout(gridLayout)
        
        
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
