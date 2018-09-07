# Import required modules
import sys, time
from PySide.QtGui import *
from PySide.QtCore import *

# Our main window class
class MainWindow(QMainWindow):
    # Constructor function
    def __init__(self):
        super(MainWindow,self).__init__()
        self.initGUI()


    def initGUI(self):
        self.setWindowTitle("A Simple Text Editor")
        self.setGeometry(300, 250, 400, 300)
        self.myStatusBar = QStatusBar()
        self.setStatusBar(self.myStatusBar)
        self.myStatusBar.showMessage('Ready', 10000)
        self.SetupComponents()
        self.show()

    def SetupComponents(self):
        textEdit = QTextEdit()
        self.setCentralWidget(textEdit)
        
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
