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
        self.myLabel = QLabel("Press 'Esc' to close this App")
        self.infoLabel = QLabel()
        self.myLabel.setAlignment(Qt.AlignCenter)
        self.infoLabel.setAlignment(Qt.AlignCenter)
        self.myLayout.addWidget(self.myLabel)
        self.myLayout.addWidget(self.infoLabel)
        self.setLayout(self.myLayout)
        self.show()

    def keyPressEvent(self, event):
        # Function reimplementing Key Press, Mouse Click and Resize Events
        if event.key() == Qt.Key_Escape:
            self.close()

    def mouseDoubleClickEvent(self, event):
        self.close()

    def resizeEvent(self, event):
        self.infoLabel.setText("Window Resized to QSize(%d, %d)" % (event.size().width(), event.size().height()))
        
if __name__ =='__main__': # main function
    try: # Exception Handling
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
