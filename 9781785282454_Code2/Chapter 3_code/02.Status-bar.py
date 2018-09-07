# 02.Status-bar.py
# main code from 'PySide GUI Application Development (2013)'

# Import required modules
import sys, time
from PySide2.QtWidgets import QMainWindow, QStatusBar, QApplication

# Our main window class
class MainWindow(QMainWindow):
    # Constructor function
    def __init__(self):
        super(MainWindow,self).__init__()
        self.initGUI()
    def initGUI(self):
        self.setWindowTitle("Main Window")
        self.setGeometry(300, 250, 400, 300)
        self.CreateStatusBar()
        self.show()
    def CreateStatusBar(self):
        self.myStatusBar = QStatusBar()
        self.myStatusBar.showMessage('Ready PySide2', 2000)
        self.setStatusBar(self.myStatusBar)
        
if __name__ == '__main__': # main function 
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

