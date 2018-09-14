# hello-icon.py

# Import required modules
import sys
from PySide2.QtGui import *
from PySide2.QtWidgets import *

class SampleWindow(QWindow): # Our main window class 
	def __init__(self): # Constructor Function
		QWindow.__init__(self)
		self.setTitle("Icon Sample")
		self.setGeometry(300, 300, 200, 150)
	def setIconFile(self): # Function to set Icon
		appIcon = QIcon('xpm.xpm')
		self.setIcon(appIcon)

if __name__ == '__main__':
	# Exception Handling
	try:
		myApp = QApplication(sys.argv)
		myWindow = SampleWindow()
		myWindow.setIconFile()
		myWindow.show()
		myApp.exec_()
		sys.exit(0)
	except NameError:
		print("Name Error:", sys.exc_info()[1])
	except SystemExit:
		print("Closing Window...")
	except Exception:
		print(sys.exc_info()[1])

