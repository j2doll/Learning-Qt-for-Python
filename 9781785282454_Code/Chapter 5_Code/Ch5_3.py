# Import necessary modules
import sys
from PySide.QtGui import *

class MyColorDialog(QWidget):
    
    def __init__(self):
        QWidget.__init__(self)
        myColor = QColor(0, 0, 0) 

        self.myButton = QPushButton('Press to Change Color', self)
        self.myButton.move(10, 50)

        self.myButton.clicked.connect(self.showColorDialog)

        self.myFrame = QFrame(self)
        self.myFrame.setStyleSheet("QWidget { background-color: %s }" 
            % myColor.name())
        self.myFrame.setGeometry(130, 22, 100, 100)            
        
        self.setGeometry(300, 300, 250, 180)
        self.setWindowTitle('Color Dialog - Example')
        self.show()
        
    def showColorDialog(self):
      
        color = QColorDialog.getColor()

        if color.isValid():
            self.myFrame.setStyleSheet("QWidget { background-color: %s }"
                % color.name())
            
if __name__ =='__main__':
    # Exception Handling
    try:
        myApp = QApplication(sys.argv)
        myCD = MyColorDialog()
        myCD.show()
        myApp.exec_()
        sys.exit(0)
    except NameError:
        print("Name Error:", sys.exc_info()[1])
    except SystemExit:
        print("Closing Window...")
    except Exception:
        print(sys.exc_info()[1])
