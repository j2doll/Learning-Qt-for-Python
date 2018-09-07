import sys
from PySide.QtGui import *
from PySide.QtCore import *
from PySide.QtSql import *

ID, FIRST_NAME, LAST_NAME, AGE, SEX, INCOME = range(6)


class EmployeeForm(QDialog):

    FIRST, PREV, NEXT, LAST = range(4)

    def __init__(self):
        QDialog.__init__(self)

        firstNameEdit = QLineEdit()
        firstNameLabel = QLabel("First Name:")
        firstNameLabel.setBuddy(firstNameEdit)

        lastNameEdit = QLineEdit()
        lastNameLabel = QLabel("Last Name:")
        lastNameLabel.setBuddy(lastNameEdit)

        ageEdit = QLineEdit()
        ageLabel = QLabel("Age:")
        ageLabel.setBuddy(ageEdit)

        genderEdit = QLineEdit()
        genderLabel = QLabel("Gender:")
        genderLabel.setBuddy(genderEdit)

        incomeEdit = QLineEdit()
        incomeLabel = QLabel("Income:")
        incomeLabel.setBuddy(incomeEdit)

        firstButton = QPushButton("<< First")
        previousButton = QPushButton("< Previous")
        nextButton = QPushButton("> Next")
        lastButton = QPushButton(">> Last")

        addButton = QPushButton("&Add")
        addButton.setIcon(QIcon("add.png"))
        deleteButton = QPushButton("&Delete")
        deleteButton.setIcon(QIcon("delete.png"))
        quitButton = QPushButton("&Quit")
        quitButton.setIcon(QIcon("quit.png"))

        fieldLayout = QGridLayout()
        fieldLayout.addWidget(firstNameLabel, 0, 0)
        fieldLayout.addWidget(firstNameEdit, 0, 1, 1, 3)
        fieldLayout.addWidget(lastNameLabel, 1, 0)
        fieldLayout.addWidget(lastNameEdit, 1, 1, 1, 3)        
        fieldLayout.addWidget(ageLabel, 2, 0)
        fieldLayout.addWidget(ageEdit, 2, 1)
        fieldLayout.addWidget(genderLabel, 2, 2)
        fieldLayout.addWidget(genderEdit, 2, 3)
        fieldLayout.addWidget(incomeLabel, 3, 0)
        fieldLayout.addWidget(incomeEdit, 3, 1, 1, 3)
        navigationLayout = QHBoxLayout()
        navigationLayout.addWidget(firstButton)
        navigationLayout.addWidget(previousButton)
        navigationLayout.addWidget(nextButton)
        navigationLayout.addWidget(lastButton)
        fieldLayout.addLayout(navigationLayout, 4, 0, 1, 2)
        buttonLayout = QVBoxLayout()
        buttonLayout.addWidget(addButton)
        buttonLayout.addWidget(deleteButton)
        buttonLayout.addStretch()
        buttonLayout.addWidget(quitButton)
        layout = QHBoxLayout()
        layout.addLayout(fieldLayout)
        layout.addLayout(buttonLayout)
        self.setLayout(layout)

        self.model = QSqlTableModel(self)
        self.model.setTable("employee")
        self.model.setSort(FIRST_NAME, Qt.AscendingOrder)
        self.model.select()

        self.mapper = QDataWidgetMapper(self)
        self.mapper.setSubmitPolicy(QDataWidgetMapper.ManualSubmit)
        self.mapper.setModel(self.model)
        self.mapper.addMapping(firstNameEdit, FIRST_NAME)
        self.mapper.addMapping(lastNameEdit, LAST_NAME)
        self.mapper.addMapping(ageEdit, AGE)
        self.mapper.addMapping(genderEdit, SEX)
        self.mapper.addMapping(incomeEdit, INCOME)
 
        self.mapper.toFirst()

        self.connect(firstButton, SIGNAL("clicked()"),
                     lambda: self.saveRecord(EmployeeForm.FIRST))
        self.connect(previousButton, SIGNAL("clicked()"),
                     lambda: self.saveRecord(EmployeeForm.PREV))
        self.connect(nextButton, SIGNAL("clicked()"),
                     lambda: self.saveRecord(EmployeeForm.NEXT))
        self.connect(lastButton, SIGNAL("clicked()"),
                     lambda: self.saveRecord(EmployeeForm.LAST))
        self.connect(addButton, SIGNAL("clicked()"), self.addRecord)
        self.connect(deleteButton, SIGNAL("clicked()"),
                     self.deleteRecord)
        self.connect(quitButton, SIGNAL("clicked()"), self.done)

        self.setWindowTitle("Employee Details")

    def done(self, result=None):
        self.mapper.submit()
        QDialog.done(self, True)

        
    def addRecord(self):
        row = self.model.rowCount()
        self.mapper.submit()
        self.model.insertRow(row)
        self.mapper.setCurrentIndex(row)


    def deleteRecord(self):
        row = self.mapper.currentIndex()
        self.model.removeRow(row)
        self.model.submitAll()
        if row + 1 >= self.model.rowCount():
            row = self.model.rowCount() - 1
        self.mapper.setCurrentIndex(row)


    def saveRecord(self, where):
        row = self.mapper.currentIndex()
        self.mapper.submit()
        if where == EmployeeForm.FIRST:
            row = 0
        elif where == EmployeeForm.PREV:
            row = 0 if row <= 1 else row - 1
        elif where == EmployeeForm.NEXT:
            row += 1
            if row >= self.model.rowCount():
                row = self.model.rowCount() - 1
        elif where == EmployeeForm.LAST:
            row = self.model.rowCount() - 1
        self.mapper.setCurrentIndex(row)

def createConnection():
    db = QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName('sample.db')

    ok = db.open()

    if not ok:
        return False
    
    return True
    

if __name__ =='__main__':
    try:
        myApp = QApplication(sys.argv)

        if not createConnection():
            print("Error Connecting to Database")
            sys.exit(1)

        myForm = EmployeeForm()
        myForm.show()
        myApp.exec_()
        sys.exit(0)
    except NameError:
        print("Name Error:", sys.exc_info()[1])
    except SystemExit:
        print("Closing Window...")
    except Exception:
        print(sys.exc_info()[1])
