import sys, shelve
from PyQt4.QtCore import SIGNAL
from PyQt4.QtGui import *
from interfaz import Ui_albaran
from factura import *

class miMain(QMainWindow, Ui_albaran):
    #factura1 = factura()
    def __init__(self, parent = None):
        QWidget.__init__(self, parent)
        self.setupUi(self)
        self.setWindowTitle("Albaran v01")
        f = factura()
        
        
        #links:
        # self.connect(self.addb, SIGNAL("clicked()"),self.crearf)

        

########## MAIN ##########
if __name__ == "__main__":
        app = QApplication(sys.argv)
        window = miMain()
        window.show()
        sys.exit(app.exec_())

    
    




