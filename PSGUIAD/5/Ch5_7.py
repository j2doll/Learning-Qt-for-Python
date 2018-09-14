# Import necessary modules
import sys
from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *

class MyMDIApp(QMainWindow):
    
    def __init__(self):
        QMainWindow.__init__(self)

        workspace = QWorkspace()
        workspace.setWindowTitle("Simple WorkSpace Example")

        for i in range(5):
            textEdit = QTextEdit()
            textEdit.setPlainText("Dummy Text " * 100)
            textEdit.setWindowTitle("Document %i" % i)
            workspace.addWindow(textEdit)

        workspace.tile()
        self.setCentralWidget(workspace)

        self.setGeometry(300, 300, 600, 350)
        self.show()

if __name__ =='__main__':
    # Exception Handling
    try:
        myApp = QApplication(sys.argv)
        myMDIApp = MyMDIApp()
        myMDIApp.show()
        myApp.exec_()
        sys.exit(0)
    except NameError:
        print("Name Error:", sys.exc_info()[1])
    except SystemExit:
        print("Closing Window...")
    except Exception:
        print(sys.exc_info()[1])
