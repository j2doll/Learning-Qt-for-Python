import sys
from PySide.QtGui import *
from PySide.QtCore import *
from PySide.QtSql import *

def initializeModel(model):
    model.setTable("employee")

    model.setEditStrategy(QSqlTableModel.OnManualSubmit)
    
    model.setHeaderData(0, Qt.Horizontal, "ID")
    model.setHeaderData(1, Qt.Horizontal, "Name")
    model.setHeaderData(2, Qt.Horizontal, "Department")
    model.setHeaderData(3, Qt.Horizontal, "Branch")

    model.setRelation(2, QSqlRelation("department", "id", "name"));
    model.setRelation(3, QSqlRelation("branch", "id", "name"));

    model.select()

def createView(title, model):
    view = QTableView()
    view.setModel(model)
    view.setWindowTitle(title)
    return view

def createConnection():
    db = QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName('test.db')

    ok = db.open()

    if not ok:
        return False

    myQuery = QSqlQuery()

    return True
    

if __name__ =='__main__':
    try:
        myApp = QApplication(sys.argv)

        if not createConnection():
            print("Error Connecting to Database")
            sys.exit(1)

        model = QSqlRelationalTableModel()
        initializeModel(model)

        view1 = createView("Relational Table Model - Example", model)

        view1.setGeometry(100, 100, 500, 220)
        view1.show()
        myApp.exec_()
        sys.exit(0)
    except NameError:
        print("Name Error:", sys.exc_info()[1])
    except SystemExit:
        print("Closing Window...")
    except Exception:
        print(sys.exc_info()[1])
