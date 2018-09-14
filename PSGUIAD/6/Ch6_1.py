import sys
from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *

def initializeModel(model):
    model.setTable("employee")

    model.setEditStrategy(QSqlTableModel.OnManualSubmit)
    model.select()

    model.setHeaderData(0, Qt.Horizontal, "ID")
    model.setHeaderData(1, Qt.Horizontal, "First Name")
    model.setHeaderData(2, Qt.Horizontal, "Last Name")
    model.setHeaderData(3, Qt.Horizontal, "Age")
    model.setHeaderData(4, Qt.Horizontal, "Gender")
    model.setHeaderData(5, Qt.Horizontal, "Income")

def createView(title, model):
    view = QTableView()
    view.setModel(model)
    view.setWindowTitle(title)
    return view

def createConnection():
    db = QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName('sample.db')

    ok = db.open()

    if not ok:
        return False

    myQuery = QSqlQuery()

    myQuery.exec_("""CREATE TABLE employee (id INTEGER PRIMARY KEY
                  AUTOINCREMENT UNIQUE NOT NULL, first_name CHAR(20) NOT NULL, 
                  last_name CHAR(20), age INT, sex CHAR(1), income FLOAT)""")
    myQuery.exec_("""INSERT INTO employee (first_name, last_name, age, sex, income)
                  VALUES ('Alice', 'A', 30, 'F', 5000.00)""")
    myQuery.exec_("""INSERT INTO employee (first_name, last_name, age, sex, income)
                  VALUES ('Bob', 'B', 31, 'M', 5100.00)""")
    myQuery.exec_("""INSERT INTO employee (first_name, last_name, age, sex, income)
                  VALUES ('Caesar', 'C', 32, 'F', 5200.00)""")
    myQuery.exec_("""INSERT INTO employee (first_name, last_name, age, sex, income)
                  VALUES ('Danny', 'D', 34, 'M', 5300.00)""")
    myQuery.exec_("""INSERT INTO employee (first_name, last_name, age, sex, income)
                  VALUES ('Eziekel', 'E', 35, 'F', 5400.00)""")
    return True
    

if __name__ =='__main__':
    try:
        myApp = QApplication(sys.argv)

        if not createConnection():
            print("Error Connecting to Database")
            sys.exit(1)

        model = QSqlTableModel()
        initializeModel(model)

        view1 = createView("Table Model - Example1", model)
        view2 = createView("Table Model - Example2", model)

        view1.setGeometry(100, 100, 500, 220)
        view2.setGeometry(100, 100, 500, 220)
        view1.show()
        view2.move(view1.x() + view1.width() + 20, view1.y())
        view2.show()
        myApp.exec_()
        sys.exit(0)
    except NameError:
        print("Name Error:", sys.exc_info()[1])
    except SystemExit:
        print("Closing Window...")
    except Exception:
        print(sys.exc_info()[1])
