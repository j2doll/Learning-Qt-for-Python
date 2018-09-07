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
        self.setWindowTitle("A Simple Text Editor")
        self.setWindowIcon(QIcon('appicon.png'))
        self.setGeometry(300, 250, 400, 300)
        self.SetupComponents()
        self.show()

    # Function to setup status bar, central widget, menu bar
    def SetupComponents(self):
        self.myStatusBar = QStatusBar()
        self.setStatusBar(self.myStatusBar)
        self.myStatusBar.showMessage('Ready', 10000)
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.CreateActions()
        self.CreateMenus()
        self.CreateToolBar()
        self.fileMenu.addAction(self.newAction)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.exitAction)
        self.editMenu.addAction(self.copyAction)
        self.fileMenu.addSeparator()
        self.editMenu.addAction(self.pasteAction)
        self.helpMenu.addAction(self.aboutAction)
        self.mainToolBar.addAction(self.newAction)
        self.mainToolBar.addSeparator()
        self.mainToolBar.addAction(self.copyAction)
        self.mainToolBar.addAction(self.pasteAction)
        

    # Slots called when the menu actions are triggered
    def newFile(self):
        self.textEdit.setText('')

    def exitFile(self):
        self.close()
    
    def aboutHelp(self):
        QMessageBox.about(self, "About Simple Text Editor",
                "This example demonstrates the use "
                "of Menu Bar")

    # Function to create actions for menus
    def CreateActions(self):
        self.newAction = QAction( QIcon('new.png'), '&New',
                                  self, shortcut=QKeySequence.New,
                                  statusTip="Create a New File",
                                  triggered=self.newFile)
        self.exitAction = QAction( QIcon('exit.png'), 'E&xit',
                                   self, shortcut="Ctrl+Q",
                                   statusTip="Exit the Application",
                                   triggered=self.exitFile)
        self.copyAction = QAction( QIcon('copy.png'), 'C&opy',
                                   self, shortcut="Ctrl+C",
                                   statusTip="Copy",
                                   triggered=self.textEdit.copy)
        self.pasteAction = QAction( QIcon('paste.png'), '&Paste',
                                    self, shortcut="Ctrl+V",
                                   statusTip="Paste",
                                   triggered=self.textEdit.paste)
        self.aboutAction = QAction( QIcon('about.png'), 'A&bout',
                                    self, statusTip="Displays info about text editor",
                                   triggered=self.aboutHelp)

    # Actual menu bar item creation
    def CreateMenus(self):
        self.fileMenu = self.menuBar().addMenu("&File")
        self.editMenu = self.menuBar().addMenu("&Edit")
        self.helpMenu = self.menuBar().addMenu("&Help")

    def CreateToolBar(self):
        self.mainToolBar = self.addToolBar('Main')
        
        
if __name__ == '__main__':
    # Exception Handling
    try:
        #QApplication.setStyle('plastique')
        myApp = QApplication(sys.argv)
        mainWindow = MainWindow()
        myApp.exec_()
        sys.exit(0)
    except NameError:
        print("Name Error:", sys.exc_info()[1])
    except SystemExit:
        print("Closing Window...")
    except Exception:
        print(sys.exc_info()[1])
