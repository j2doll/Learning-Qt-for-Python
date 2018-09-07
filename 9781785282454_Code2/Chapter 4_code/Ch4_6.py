import sys
from PySide.QtCore import *
 
# define a new slot that receives and prints a string
def printText(text):
    print(text)
 
class CustomSignal(QObject):
    # create a new signal
    mySignal = Signal(str)

if __name__ == '__main__':
    try: 
        myObject = CustomSignal()
        # connect signal and slot
        myObject.mySignal.connect(printText)
        # emit signal
        myObject.mySignal.emit("Hello, Universe!")
    except Exception:
        print(sys.exc_info()[1])
