
import sys
from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *

class MyView(QGraphicsView):
    def __init__(self):
        QGraphicsView.__init__(self)

        self.myScene = QGraphicsScene(self)
        self.myItem = QGraphicsEllipseItem(-20, -10, 50, 20)

        self.effect = QGraphicsDropShadowEffect(self)
        self.effect.setBlurRadius(8)
        self.myItem.setGraphicsEffect(self.effect)
        self.myItem.setZValue(1)
        
        self.myScene.addItem(self.myItem)
        self.setScene(self.myScene)

        self.timeLine = QTimeLine(1000)
        self.timeLine.setFrameRange(0, 100)
        self.animate = QGraphicsItemAnimation()
        self.animate.setItem(self.myItem)
        self.animate.setTimeLine(self.timeLine)

        self.animate.setPosAt(0, QPointF(0, -10))
        self.animate.setRotationAt(1, 360)

        self.setWindowTitle("A Simple Animation")
        self.timeLine.start()
        

if __name__ == '__main__':
    try:
        myApp = QApplication(sys.argv)
        myView = MyView()
        myView.show()
        myApp.exec_()
        sys.exit(0)
    except NameError:
        print("Name Error:", sys.exc_info()[1])
    except SystemExit:
        print("Closing Window...")
    except Exception:
        print(sys.exc_info()[1])
