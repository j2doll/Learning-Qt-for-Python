# 04.Simple-text-editor.py
# main code from 'PySide GUI Application Development (2013)'


# Import required modules
import sys, time
from PySide2.QtWidgets import *
from PySide2.QtGui import *

# Our main window class
class MainWindow(QMainWindow):
    textEdit = None
    textDocument = None
    def __init__(self): # Constructor function
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
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.textDocument = QTextDocument()
        self.textEdit.setDocument(self.textDocument)
        self.textDocument.setHtml("<b>H</b>ello <font color='red'>W</font>orld")
        
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
