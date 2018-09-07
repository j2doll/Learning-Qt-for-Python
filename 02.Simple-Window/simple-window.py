# simple-window.py

# Import required modules
import sys
import time
from PySide2.QtGui import QGuiApplication, QWindow

class SampleWindow(QWindow):
	def __init__(self): # Constructor function
		QWindow.__init__(self)
		self.setTitle("Sample Window")
		self.setGeometry(300, 300, 200, 150)
		self.setMinimumHeight(100)
		self.setMinimumWidth(250)
		self.setMaximumHeight(200)
		self.setMaximumWidth(800)

if __name__ == '__main__': # main function
	# Exception Handling
	try:
		myApp = QGuiApplication(sys.argv)
		myWindow = SampleWindow()
		myWindow.show()
		time.sleep(5) # wait a moment 
		myWindow.resize(300, 300)
		myWindow.setTitle("Sample Window Resized")
		myApp.exec_()
		sys.exit(0)
	except NameError:
		print("Name Error:", sys.exc_info()[1])
	except SystemExit:
		print("Closing Window...")
	except Exception:
		print (sys.exc_info()[1])
