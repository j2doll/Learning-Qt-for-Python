# Import necessary modules
import sys
from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *

class FindDialog(QDialog):
    
    def __init__(self):
        QDialog.__init__(self)
        self.findLabel = QLabel("Find &What:")
        self.lineEdit = QLineEdit()
        self.findLabel.setBuddy(self.lineEdit)

        self.caseCheckBox = QCheckBox("Match &Case")
        self.backwardCheckBox = QCheckBox("Search &Backward")

        self.findButton = QPushButton("&Find")
        self.findButton.setDefault(True)
        self.closeButton = QPushButton("Close")

        self.topLeftLayout = QHBoxLayout()
        self.topLeftLayout.addWidget(self.findLabel)
        self.topLeftLayout.addWidget(self.lineEdit)

        self.leftLayout = QVBoxLayout()
        self.leftLayout.addLayout(self.topLeftLayout)
        self.leftLayout.addWidget(self.caseCheckBox)
        self.leftLayout.addWidget(self.backwardCheckBox)

        self.rightLayout = QVBoxLayout()
        self.rightLayout.addWidget(self.findButton)
        self.rightLayout.addWidget(self.closeButton)
        self.rightLayout.addStretch()

        self.mainLayout = QHBoxLayout()
        self.mainLayout.addLayout(self.leftLayout)
        self.mainLayout.addLayout(self.rightLayout)

        self.findButton.clicked.connect(self.findText)
        self.setWindowTitle("Find")
        self.setLayout(self.mainLayout)
        self.show()

    def findText(self):
        mySearchText = self.lineEdit.text()
        if self.caseCheckBox.isChecked():
            caseSensitivity = Qt.CaseSensitive
        else:
            caseSensitivity = Qt.CaseInsensitive
        if self.backwardCheckBox.isChecked():
            print("Backward Find ")
        else:
            print("Forward Find")

class MyFileDialog(QMainWindow):
    
    def __init__(self):
        QMainWindow.__init__(self)
        
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.statusBar()

        findFile = QAction(QIcon('find.png'), 'Find', self)
        findFile.setShortcut('Ctrl+F')
        findFile.setStatusTip('Finds a text in the file')
        findFile.triggered.connect(self.findDialog)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(findFile)       
        
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Example - Find Dialog')
        
    def findDialog(self):
         myFindDialog = FindDialog()
         myFindDialog.exec_()


           
if __name__ =='__main__':
    # Exception Handling
    try:
        myApp = QApplication(sys.argv)
        myfileDialog = MyFileDialog()
        myfileDialog.show()
        myApp.exec_()
        sys.exit(0)
    except NameError:
        print("Name Error:", sys.exc_info()[1])
    except SystemExit:
        print("Closing Window...")
    except Exception:
        print(sys.exc_info()[1])
