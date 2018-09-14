
import sys
from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *

class MyWidget(QWidget):
    def __init__(self):
        super(MyWidget,self).__init__()
        self.initGUI()

    def initGUI(self):
        self.myListWidget1 = MyListWidget(self,None)
        self.myListWidget2 = MyListWidget(self,'ICON')


        self.setGeometry(300, 350, 500, 150)

        self.myLayout = QHBoxLayout()
        self.myLayout.addWidget(self.myListWidget1)
        self.myLayout.addWidget(self.myListWidget2)

        self.myListWidget1.additem('blue_bird.png',"Angry Bird Blue")
        self.myListWidget1.additem('red_bird.png',"Angry Bird Red")
        self.myListWidget1.additem('green_bird.png',"Angry Bird Green")
        self.myListWidget1.additem('black_bird.png',"Angry Bird Black")
        self.myListWidget1.additem('white_bird.png',"Angry Bird White")

        self.myListWidget2.additem('gray_pig.png', "Grey Pig")
        self.myListWidget2.additem('brown_pig.png', "Brown Pig")
        self.myListWidget2.additem('green_pig.png', "Green Pig")
       
        self.setWindowTitle('Drag and Drop Example');

        self.setLayout(self.myLayout)
        self.show()

class MyListWidget(QListWidget):

    def __init__(self,parent=None,viewMode=None):
        super(MyListWidget,self).__init__(parent)
        self.initWidget(viewMode)

    def initWidget(self,viewMode=None):
        self.setAcceptDrops(True)
        self.setDragEnabled(True)
        if viewMode == 'ICON':
            self.setViewMode(QListWidget.IconMode)

    def additem(self,fileName, desc):
        QListWidgetItem(QIcon(fileName), desc, self)

    

if __name__ == '__main__':
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
