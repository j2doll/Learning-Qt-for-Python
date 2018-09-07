# Import required modules
import sys, time
from PySide.QtGui import *


# Our main window class
class MainWindow(QWidget):
    # Constructor function
    def __init__(self):
        super(MainWindow,self).__init__()
        self.initGUI()

    def initGUI(self):
        self.setWindowTitle("Horizontal Layout")
        self.setGeometry(300, 250, 400, 300)
        self.SetLayout()
        self.show()

    # Add Buttons and set the layout
    def SetLayout(self):
        horizontalLayout = QHBoxLayout(self)
        hButton1 = QPushButton('Button 1', self)
        hButton2 = QPushButton('Button 2', self)
        hButton3 = QPushButton('Button 3', self)
        hButton4 = QPushButton('Button 4', self)

        horizontalLayout.addWidget(hButton1)
        horizontalLayout.addWidget(hButton2)
        horizontalLayout.addStretch()
        horizontalLayout.addWidget(hButton3)
        horizontalLayout.addWidget(hButton4)
        
        self.setLayout(horizontalLayout)
        
        
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
