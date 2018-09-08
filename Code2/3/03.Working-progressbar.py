# 03.Working-progressbar.py 
# main code from 'PySide GUI Application Development (2013)'

# Import required modules
import sys, time
from PySide2.QtWidgets import QMainWindow, QApplication, QStatusBar, QLabel, QProgressBar

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
    def CreateStatusBar(self): # Function to create the status bar
        self.myStatusBar = QStatusBar()
        #self.progressBar.setValue(0)
        self.myStatusBar.addWidget(self.statusLabel, 1)
        self.myStatusBar.addWidget(self.progressBar, 2)
        self.setStatusBar(self.myStatusBar)
    def ShowProgress(self,progress): # Function to show progress
        self.progressBar.setValue(progress)
        if progress == 100:
            self.statusLabel.setText('Ready')
            return
        
if __name__ == '__main__': # main function 
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
