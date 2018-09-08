# Import necessary modules
import sys
from PySide.QtGui import *
from PySide.QtCore import *

class MyInputDialog(QWidget):
    
    def __init__(self):        

        QWidget.__init__(self)
        self.myNameButton = QPushButton('Name', self)
        self.myNameButton.clicked.connect(self.showNameDialog)

        self.myAgeButton = QPushButton('Age', self)
        self.myAgeButton.clicked.connect(self.showAgeDialog)

        self.myChoiceButton = QPushButton('Choice', self)
        self.myChoiceButton.clicked.connect(self.showChoiceDialog)
        
        self.myNameLE = QLineEdit(self)
        self.myAgeLE = QLineEdit(self)
        self.myChoiceLE = QLineEdit(self)

        self.myLayout = QFormLayout()
        self.myLayout.addRow(self.myNameButton, self.myNameLE)
        self.myLayout.addRow(self.myAgeButton, self.myAgeLE)
        self.myLayout.addRow(self.myChoiceButton, self.myChoiceLE)
        
        self.setLayout(self.myLayout)    
        self.setGeometry(300, 300, 290, 100)
        self.setWindowTitle('Input Dialog Example')
        self.show()
        
    def showNameDialog(self):
        text, ok = QInputDialog.getText(self, 'Input Text Dialog', 
            'Enter your name:')
        
        if ok:
            self.myNameLE.setText(str(text))

    def showAgeDialog(self):
        text, ok = QInputDialog.getInteger(self, 'Input Number Dialog', 
            'Enter your age:')
        
        if ok:
            self.myAgeLE.setText(str(text))

    def showChoiceDialog(self):
        strList = ['Ice Cream', 'Choclates', 'Milk Shakes']
        text, ok = QInputDialog.getItem(self, 'Input Combo Dialog', 
            'Enter your choice:', strList)
        
        if ok:
            self.myChoiceLE.setText(str(text))
        
if __name__ =='__main__':
    # Exception Handling
    try:
        myApp = QApplication(sys.argv)
        myID = MyInputDialog()
        myID.show()
        myApp.exec_()
        sys.exit(0)
    except NameError:
        print("Name Error:", sys.exc_info()[1])
    except SystemExit:
        print("Closing Window...")
    except Exception:
        print(sys.exc_info()[1])
