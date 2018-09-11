# hello-exception.py
# base code from PySide GUI App. Dev. 2013

# Import the necessary modules required
import sys
from PySide2.QtCore import *
from PySide2.QtGui import *

if __name__ == '__main__': # Main Function
	# Create the main application
	myApp = QCoreApplication(sys.argv)
	# Create a Label and set its properties
	try:
		# appLabel = QLabel()
		appLabel.setText("Hello, World!!!\n Look at my first app using PySide")
		appLabel.setAlignment(Qt.AlignCenter)
		appLabel.setWindowTitle("My First Application")
		appLabel.setGeometry(300, 300, 250, 175)
		# Show the Label
		appLabel.show()
		# Execute the Application and Exit
		myApp.exec_()
		sys.exit()
	except NameError:
		print("[Exception] Name Error:", sys.exc_info()[1])
		pass
