# Import necessary modules
import sys
from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *

# Our main widget class
class MyWidget(QWidget):
    # Constructor function
    def __init__(self):
        super(MyWidget,self).__init__()
        self.initGUI()

    def initGUI(self):
        self.setWindowTitle("Reimplementing Events")
        self.setGeometry(300, 250, 300, 100)
        self.myLayout = QVBoxLayout()
        self.myLabel1 = QLabel("Text 1")
        self.myLineEdit1 = QLineEdit()
        self.myLabel2 = QLabel("Text 2")
        self.myLineEdit2 = QLineEdit()
        self.myLabel3 = QLabel("Text 3")
        self.myLineEdit3 = QLineEdit()
        self.myLayout.addWidget(self.myLabel1)
        self.myLayout.addWidget(self.myLineEdit1)
        self.myLayout.addWidget(self.myLabel2)
        self.myLayout.addWidget(self.myLineEdit2)
        self.myLayout.addWidget(self.myLabel3)
        self.myLayout.addWidget(self.myLineEdit3)
        self.setLayout(self.myLayout)
        self.show()

    # Function reimplementing event() function
    def event(self, event):
        if event.type()== QEvent.KeyRelease and event.key()== Qt.Key_Tab:
            self.myLineEdit3.setFocus()
            return True
        return QWidget.event(self,event)
        
if __name__ =='__main__':
    # Exception Handling
    try:
        myApp = QApplication(sys.argv)
        myWidget = MyWidget()
        myApp.exec_()
        sys.exit(0)
    except NameError:
        print("Name Error:", sys.exc_info()[1])
    except SystemExit:
        print("Closing Window...")
    except Exception:
        print(sys.exc_info()[1])
