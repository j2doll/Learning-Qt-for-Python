# Import necessary modules
import sys
from PySide.QtGui import *
from PySide.QtCore import *

class MyFileDialog(QMainWindow):
    
    def __init__(self):
        QMainWindow.__init__(self)
        
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.statusBar()

        printFile = QAction(QIcon('print.png'), 'Print', self)
        printFile.setShortcut('Ctrl+P')
        printFile.setStatusTip('Prints a file')
        printFile.triggered.connect(self.printDialog)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(printFile)       
        
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Example - File Dialog')
        self.show()
        
    def printDialog(self):
         printer = QPrinter() 
         dialog = QPrintDialog(printer, self) 
         if(dialog.exec_() != QDialog.Accepted): 
             return
         self.textEdit.print_(printer)
                                
        
if __name__ =='__main__':
    # Exception Handling
    try:
        myApp = QApplication(sys.argv)
        myFD = MyFileDialog()
        myFD.show()
        myApp.exec_()
        sys.exit(0)
    except NameError:
        print("Name Error:", sys.exc_info()[1])
    except SystemExit:
        print("Closing Window...")
    except Exception:
        print(sys.exc_info()[1])
