import sys, shelve
from PyQt4.QtCore import Qt
from PyQt4.QtGui import QApplication, QLineEdit
from update_db_completion import *

class miQLineEdit(QLineEdit):
    def __init__(self, parent = None):
        super(miQLineEdit, self).__init__(parent)
        #QLineEdit.__init__(self, parent)

    def keyPressEvent(self, event):
        # cada vez que queremos consultar actualizamos el listado:
        self.completion_items = completion_items()
        
        # por alguna razon con qtdesigner el tab esta reservado para cambiar de posicion y no consigo
        # asignarlo para completion en un entrytext:
        #if event.key() == Qt.Key_Tab:

        # combinacion de ctrl + space:
        if event.key() == Qt.Key_Space and event.modifiers() == Qt.ControlModifier:
            fin_bucle = False
            iterador = 0
            while not fin_bucle or iterador < len(self.completion_items):
                if self.completion_items[iterador].startswith(self.text()):
                    self.setText(self.completion_items[iterador])
                    fin_bucle = True
                iterador += 1
            event.accept()
        else:
            QLineEdit.keyPressEvent(self, event)
