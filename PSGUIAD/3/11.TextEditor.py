# 11.TextEditor.py

# Import required modules
import sys, time
from PySide2.QtGui import *
from PySide2.QtWidgets import *

# Our main window class
class MainWindow(QMainWindow):
    def __init__(self, fileName=None): # Constructor function
        super(MainWindow,self).__init__()
        self.initGUI()
    def initGUI(self):
        self.setWindowTitle("A Simple Text Editor")
        self.setWindowIcon(QIcon('appicon.png'))
        self.setGeometry(100, 100, 800, 600)

        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.fileName = None

        self.filters = "Text files (*.txt)"
        self.SetupComponents()
        self.show()
    def SetupComponents(self):
    	# Function to setup status bar, central widget, menu bar, tool bar
        self.myStatusBar = QStatusBar()
        self.setStatusBar(self.myStatusBar)
        self.myStatusBar.showMessage('Ready', 10000)
        
        self.CreateActions()
        self.CreateMenus()
        self.CreateToolBar()
        self.fileMenu.addAction(self.newAction)
        self.fileMenu.addAction(self.openAction)
        self.fileMenu.addAction(self.saveAction)        
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.exitAction)
        self.editMenu.addAction(self.cutAction)
        self.editMenu.addAction(self.copyAction)
        self.editMenu.addAction(self.pasteAction)
        self.editMenu.addSeparator()
        self.editMenu.addAction(self.undoAction)
        self.editMenu.addAction(self.redoAction)
        self.editMenu.addSeparator()
        self.editMenu.addAction(self.selectAllAction)
        self.formatMenu.addAction(self.fontAction)
        self.helpMenu.addAction(self.aboutAction)
        self.helpMenu.addSeparator()
        self.helpMenu.addAction(self.aboutQtAction)
        self.mainToolBar.addAction(self.newAction)
        self.mainToolBar.addAction(self.openAction)
        self.mainToolBar.addAction(self.saveAction)
        self.mainToolBar.addSeparator()
        self.mainToolBar.addAction(self.cutAction)
        self.mainToolBar.addAction(self.copyAction)
        self.mainToolBar.addAction(self.pasteAction)
        self.mainToolBar.addSeparator()
        self.mainToolBar.addAction(self.undoAction)
        self.mainToolBar.addAction(self.redoAction)
        
        
    # Slots called when the menu actions are triggered
    def newFile(self):
        response = self.msgApp("Confirmation","Do you like to save the current file?")        
        if response == "Y":
            self.saveFile()
        
        self.textEdit.setText('')
        self.fileName = None

    def openFile(self):
        response = self.msgApp("Confirmation","Do you like to save the current file?")        
        if response == "Y":
            self.saveFile()
        
        self.fileName, self.filterName = QFileDialog.getOpenFileName(self)
        self.textEdit.setText(open(self.fileName).read())
            
    def saveFile(self):
        if self.fileName == None or self.fileName == '':
            self.fileName, self.filterName = QFileDialog.getSaveFileName(self, filter=self.filters)
        if(self.fileName != ''):
            file = open(self.fileName, 'w')        
            file.write(self.textEdit.toPlainText())
            self.statusBar().showMessage("File saved", 2000)

    def exitFile(self):
        response = self.msgApp("Confirmation","This will quit the application. Do you want to Continue?")        
        if response == "Y":
            myApp.quit()
        else:
            pass

    # Function to show Diaglog box with provided Title and Message
    def msgApp(self,title,msg):
        userInfo = QMessageBox.question(self,title,msg,
                                        QMessageBox.Yes | QMessageBox.No)
        if userInfo == QMessageBox.Yes:
            return "Y"
        if userInfo == QMessageBox.No:
            return "N"
        self.close()

    def fontChange(self):
        (font, ok) = QFontDialog.getFont(QFont("Helvetica [Cronyx]", 10), self)
        if ok:
            self.textEdit.setCurrentFont(font)
    
    def aboutHelp(self):
        QMessageBox.about(self, "About Simple Text Editor",
                "A Simple Text Editor where you can edit and save files")

    # Function to create actions for menus
    def CreateActions(self):
        self.newAction = QAction( QIcon('new.png'), '&New',
                                  self, shortcut=QKeySequence.New,
                                  statusTip="Create a New File",
                                  triggered=self.newFile)
        self.openAction = QAction( QIcon('open.png'), 'O&pen',
                                  self, shortcut=QKeySequence.Open,
                                  statusTip="Open an existing file",
                                  triggered=self.openFile)
        self.saveAction = QAction( QIcon('save.png'), '&Save',
                                  self, shortcut=QKeySequence.Save,
                                  statusTip="Save the current file to disk",
                                  triggered=self.saveFile)
        self.exitAction = QAction( QIcon('exit.png'), 'E&xit',
                                   self, shortcut="Ctrl+Q",
                                   statusTip="Exit the Application",
                                   triggered=self.exitFile)
        self.cutAction = QAction( QIcon('cut.png'), 'C&ut',
                                   self, shortcut=QKeySequence.Cut,
                                   statusTip="Cut the current selection to clipboard",
                                   triggered=self.textEdit.cut)
        self.copyAction = QAction( QIcon('copy.png'), 'C&opy',
                                   self, shortcut=QKeySequence.Copy,
                                   statusTip="Copy the current selection to clipboard",
                                   triggered=self.textEdit.copy)
        self.pasteAction = QAction( QIcon('paste.png'), '&Paste',
                                    self, shortcut=QKeySequence.Paste,
                                   statusTip="Paste the clipboard's content in current location",
                                   triggered=self.textEdit.paste)
        self.selectAllAction = QAction( QIcon('selectAll.png'), 'Select All',
                                    self, statusTip="Select All",
                                   triggered=self.textEdit.selectAll)
        self.redoAction = QAction( QIcon('redo.png'),'Redo', self,
                                   shortcut=QKeySequence.Redo,
                                   statusTip="Redo previous action",
                                   triggered=self.textEdit.redo)
        self.undoAction = QAction( QIcon('undo.png'),'Undo', self,
                                   shortcut=QKeySequence.Undo,
                                   statusTip="Undo previous action",
                                   triggered=self.textEdit.undo)
        self.fontAction = QAction( 'F&ont', self,
                                   statusTip = "Modify font properties",
                                   triggered = self.fontChange)
        self.aboutAction = QAction( QIcon('about.png'), 'A&bout',
                                    self, statusTip="Displays info about text editor",
                                   triggered=self.aboutHelp)
        self.aboutQtAction = QAction("About &Qt", self,
                                statusTip="Show the Qt library's About box",
                                triggered=qApp.aboutQt)



    # Actual menu bar item creation
    def CreateMenus(self):
        self.fileMenu = self.menuBar().addMenu("&File")
        self.editMenu = self.menuBar().addMenu("&Edit")
        self.formatMenu = self.menuBar().addMenu("F&ormat")
        self.helpMenu = self.menuBar().addMenu("&Help")
        
    def CreateToolBar(self):
        self.mainToolBar = self.addToolBar('Main')
        
        
if __name__ == '__main__':
    # Exception Handling
    try:
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
