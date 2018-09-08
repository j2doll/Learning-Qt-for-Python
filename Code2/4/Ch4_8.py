import sys

from PySide.QtCore import *
from PySide.QtGui import *

IdRole = Qt.UserRole

class PaintArea(QWidget):

    points = QPolygon([
        QPoint(10, 80),
        QPoint(20, 10),
        QPoint(80, 30),
        QPoint(90, 70)
    ])

    Line, Points, Polyline, Polygon, Rect, RoundRect, Ellipse, Arc, Chord, Pie, Path, Text, Pixmap = range(13)
    
    def __init__(self):
        QWidget.__init__(self)

    def minimumSizeHint(self):
        return QSize(50, 50)

    def sizeHint(self):
        return QSize(100, 100)

    def setShape(self, shape):
        self.shape = shape
        self.update()

    def setPen(self, pen):
        self.pen = pen
        self.update()

    def setBrush(self, brush):
        self.brush = brush
        self.update()

    def paintEvent(self, event):
        rect = QRect(10, 20, 80, 60)

        startAngle = 30 * 16
        arcLength = 120 * 16

        painter = QPainter()
        painter.begin(self)
        painter.setPen(self.pen)
        painter.setBrush(self.brush)
        if self.shape == PaintArea.Line:
            painter.drawLine(rect.bottomLeft(), rect.topRight())
        elif self.shape == PaintArea.Points:
            painter.drawPoints(PaintArea.points)
        elif self.shape == PaintArea.Polyline:
            painter.drawPolyline(PaintArea.points)
        elif self.shape == PaintArea.Polygon:
            painter.drawPolygon(PaintArea.points)
        elif self.shape == PaintArea.Rect:
            painter.drawRect(rect)
        elif self.shape == PaintArea.RoundRect:
            painter.drawRoundRect(rect)
        elif self.shape == PaintArea.Ellipse:
            painter.drawEllipse(rect)
        elif self.shape == PaintArea.Arc:
            painter.drawArc(rect, startAngle, arcLength)
        elif self.shape == PaintArea.Chord:
            painter.drawChord(rect, startAngle, arcLength)
        elif self.shape == PaintArea.Pie:
            painter.drawPie(rect, startAngle, arcLength)
        elif self.shape == PaintArea.Text:
            painter.drawText(rect, Qt.AlignCenter, "Basic Drawing Widget")
        painter.end()

class MyDrawingWindow(QWidget):
    def __init__(self):
        super(MyDrawingWindow,self).__init__()
        self.initGUI()

    def initGUI(self):

        self.paintArea = PaintArea()

        self.shapeComboBox = QComboBox()
        self.shapeComboBox.addItem("Rectangle", PaintArea.Rect)
        self.shapeComboBox.addItem("Round Rectangle", PaintArea.RoundRect)
        self.shapeComboBox.addItem("Ellipse", PaintArea.Ellipse)
        self.shapeComboBox.addItem("Pie", PaintArea.Pie)
        self.shapeComboBox.addItem("Chord", PaintArea.Chord)
        self.shapeComboBox.addItem("Polygon", PaintArea.Polygon)
        self.shapeComboBox.addItem("Line", PaintArea.Line)
        self.shapeComboBox.addItem("Polyline", PaintArea.Polyline)
        self.shapeComboBox.addItem("Arc", PaintArea.Arc)
        self.shapeComboBox.addItem("Points", PaintArea.Points)
        self.shapeComboBox.addItem("Text", PaintArea.Text)


        self.shapeLabel = QLabel("Shape:")
        self.shapeLabel.setBuddy(self.shapeComboBox)

        self.penWidthSpinBox = QSpinBox()
        self.penWidthSpinBox.setRange(0, 20)

        self.penWidthLabel = QLabel("Pen Width:")
        self.penWidthLabel.setBuddy(self.penWidthSpinBox)

        self.penStyleComboBox = QComboBox()
        self.penStyleComboBox.addItem("Solid", Qt.SolidLine)
        self.penStyleComboBox.addItem("Dash", Qt.DashLine)
        self.penStyleComboBox.addItem("Dot", Qt.DotLine)
        self.penStyleComboBox.addItem("Dash Dot", Qt.DashDotLine)
        self.penStyleComboBox.addItem("Dash Dot Dot", Qt.DashDotDotLine)
        self.penStyleComboBox.addItem("None", Qt.NoPen)

        self.penStyleLabel = QLabel("Pen Style:")
        self.penStyleLabel.setBuddy(self.penStyleComboBox)

        self.penCapComboBox = QComboBox()
        self.penCapComboBox.addItem("Flat", Qt.FlatCap)
        self.penCapComboBox.addItem("Square", Qt.SquareCap)
        self.penCapComboBox.addItem("Round", Qt.RoundCap)

        self.penCapLabel = QLabel("Pen Cap:")
        self.penCapLabel.setBuddy(self.penCapComboBox)

        
        self.brushStyleComboBox = QComboBox()
        self.brushStyleComboBox.addItem("Linear Gradient", Qt.LinearGradientPattern)
        self.brushStyleComboBox.addItem("Radial Gradient", Qt.RadialGradientPattern)
        self.brushStyleComboBox.addItem("Conical Gradient", Qt.ConicalGradientPattern)
        self.brushStyleComboBox.addItem("Solid", Qt.SolidPattern)
        self.brushStyleComboBox.addItem("Horizontal", Qt.HorPattern)
        self.brushStyleComboBox.addItem("Vertical", Qt.VerPattern)
        self.brushStyleComboBox.addItem("Cross", Qt.CrossPattern)
        self.brushStyleComboBox.addItem("Backward Diagonal", Qt.BDiagPattern)
        self.brushStyleComboBox.addItem("Forward Diagonal", Qt.FDiagPattern)
        self.brushStyleComboBox.addItem("Diagonal Cross", Qt.DiagCrossPattern)
        self.brushStyleComboBox.addItem("Dense 1", Qt.Dense1Pattern)
        self.brushStyleComboBox.addItem("Dense 2", Qt.Dense2Pattern)
        self.brushStyleComboBox.addItem("Dense 3", Qt.Dense3Pattern)
        self.brushStyleComboBox.addItem("Dense 4", Qt.Dense4Pattern)
        self.brushStyleComboBox.addItem("Dense 5", Qt.Dense5Pattern)
        self.brushStyleComboBox.addItem("Dense 6", Qt.Dense6Pattern)
        self.brushStyleComboBox.addItem("Dense 7", Qt.Dense7Pattern)
        self.brushStyleComboBox.addItem("None", Qt.NoBrush)

        self.brushStyleLabel = QLabel("Brush Style:")
        self.brushStyleLabel.setBuddy(self.brushStyleComboBox)

        self.connect(self.shapeComboBox, SIGNAL("activated(int)"),
                     self.shapeChanged)
        self.connect(self.penWidthSpinBox, SIGNAL("valueChanged(int)"),
                     self.penChanged)
        self.connect(self.penStyleComboBox, SIGNAL("activated(int)"),
                     self.penChanged)
        self.connect(self.penCapComboBox, SIGNAL("activated(int)"),
                     self.penChanged)
        self.connect(self.brushStyleComboBox, SIGNAL("activated(int)"),
                     self.brushChanged)

        mainLayout = QGridLayout()
        mainLayout.addWidget(self.paintArea, 0, 1, 1, 2)
        mainLayout.addWidget(self.shapeLabel, 1, 0)
        mainLayout.addWidget(self.shapeComboBox, 1, 1)
        mainLayout.addWidget(self.penWidthLabel, 2, 0)
        mainLayout.addWidget(self.penWidthSpinBox, 2, 1)
        mainLayout.addWidget(self.penStyleLabel, 3, 0)
        mainLayout.addWidget(self.penStyleComboBox, 3, 1)
        mainLayout.addWidget(self.penCapLabel, 4, 0)
        mainLayout.addWidget(self.penCapComboBox, 4, 1)
        mainLayout.addWidget(self.brushStyleLabel, 6, 0)
        mainLayout.addWidget(self.brushStyleComboBox, 6, 1)

        self.setLayout(mainLayout)

        self.shapeChanged()
        self.penChanged()
        self.brushChanged()

        self.setWindowTitle("Basic Drawing")
        self.show()

    def shapeChanged(self):
        shape = int(self.shapeComboBox.itemData(
            self.shapeComboBox.currentIndex(), IdRole))
        self.paintArea.setShape(shape)

    def penChanged(self):
        width = self.penWidthSpinBox.value()
        style = Qt.PenStyle(int(self.penStyleComboBox.itemData(
            self.penStyleComboBox.currentIndex(), IdRole)))
        cap = Qt.PenCapStyle(int(self.penCapComboBox.itemData(
            self.penCapComboBox.currentIndex(), IdRole)))
    
        self.paintArea.setPen(QPen(Qt.blue, width, style, cap))

    def brushChanged(self):
        style = Qt.BrushStyle(int(self.brushStyleComboBox.itemData(
            self.brushStyleComboBox.currentIndex(), IdRole)))

        if style == Qt.LinearGradientPattern:
            linearGradient = QLinearGradient(0, 0, 100, 100)
            linearGradient.setColorAt(0.0, Qt.white)
            linearGradient.setColorAt(0.2, Qt.green)
            linearGradient.setColorAt(1.0, Qt.black)
            self.paintArea.setBrush(QBrush(linearGradient))
        elif style == Qt.RadialGradientPattern:
            radialGradient = QRadialGradient(50, 50, 50, 50, 50)
            radialGradient.setColorAt(0.0, Qt.white)
            radialGradient.setColorAt(0.2, Qt.green)
            radialGradient.setColorAt(1.0, Qt.black)
            self.paintArea.setBrush(QBrush(radialGradient))
        elif style == Qt.ConicalGradientPattern:
            conicalGradient = QConicalGradient(50, 50, 150)
            conicalGradient.setColorAt(0.0, Qt.white)
            conicalGradient.setColorAt(0.2, Qt.green)
            conicalGradient.setColorAt(1.0, Qt.black)
            self.paintArea.setBrush(QBrush(conicalGradient))
        else:
            self.paintArea.setBrush(QBrush(Qt.green, style))

if __name__ == "__main__":
    try:
        myApp = QApplication(sys.argv)
        myWindow = MyDrawingWindow()
        myApp.exec_()
        sys.exit(0)
    except NameError:
        print("Name Error:", sys.exc_info()[1])
    except SystemExit:
        print("Closing Window...")
    except Exception:
        print(sys.exc_info()[1])
