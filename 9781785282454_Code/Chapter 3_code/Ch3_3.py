# Import required modules
import sys, time
from PySide.QtGui import *
from PySide.QtCore import *

# Our main window class
class MainWindow(QMainWindow):
    # Constructor function
    def __init__(self):
        super(MainWindow,self).__init__()
        self.initGUI()


    def initGUI(self):
        self.setWindowTitle("Main Window")
        self.setGeometry(300, 250, 400, 300)
        self.statusLabel = QLabel('Showing Progress')
        self.CreateProgessBar()
        self.CreateStatusBar()
        self.show()

    def CreateProgessBar(self):
        self.progressBar = QProgressBar()
        self.progressBar.setMinimum(0)
        self.progressBar.setMaximum(100)

    # Function to create the status bar
    def CreateStatusBar(self):
        self.myStatusBar = QStatusBar()
        #self.progressBar.setValue(0)
        self.myStatusBar.addWidget(self.statusLabel, 1)
        self.myStatusBar.addWidget(self.progressBar, 2)
        self.setStatusBar(self.myStatusBar)

    # Function to show progress
    def ShowProgress(self,progress):
        self.progressBar.setValue(progress)
        if progress == 100:
            self.statusLabel.setText('Ready')
            return
        
        
        
if __name__ == '__main__':
    # Exception Handling
    try:
        myApp = QApplication(sys.argv)
        mainWindow = MainWindow()
        #Pretend that a file download is in Progress
        filedownload = 0
        while(filedownload <= 100):
             mainWindow.ShowProgress(filedownload)
             filedownload = filedownload + 20
             time.sleep(1)
        myApp.exec_()
        sys.exit(0)
    except NameError:
        print("Name Error:", sys.exc_info()[1])
    except SystemExit:
        print("Closing Window...")
    except Exception:
        print(sys.exc_info()[1])
