import sys
from PyQt4.QtCore import Qt
from PyQt4.QtGui import QApplication, QLineEdit

class aplicacion(QLineEdit):

    completion_items = ["hello","world"]

    def __init__(self, parent = None):
    
        QLineEdit.__init__(self, parent)
    
    def keyPressEvent(self, event):
    
        if event.key() == Qt.Key_Tab:
            for item in self.completion_items:
                if item.startswith(self.text()):
                    self.setText(item)
                    break
            
            event.accept()
        else:
            QLineEdit.keyPressEvent(self, event)


if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = aplicacion()
    window.show()
    sys.exit(app.exec_())
