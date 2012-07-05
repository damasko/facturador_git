import sys, shelve
from PyQt4.QtCore import Qt
from PyQt4.QtGui import QApplication, QLineEdit


class miQLineEdit(QLineEdit):
	def __init__(self, parent = None):
		super(miQLineEdit, self).__init__(parent)
		#QLineEdit.__init__(self, parent)

	#completion_items = ["hello","world"]
	clientes_db = shelve.open("clientes.db")
	completion_items = [clientes_db.keys()]
	clientes_db.close()
	#print str(type(completion_items))
	#for i in completion_items:
	#	print i

	def keyPressEvent(self, event):
		# por alguna razon con qtdesigner el tab esta reservado para cambiar de posicion y no consigo 
		# asignarlo para completion en un entrytext:
		#if event.key() == Qt.Key_Tab:
		
		# combinacion de ctrl + space:
		if event.key() == Qt.Key_Space and event.modifiers() == Qt.ControlModifier:	
			for x in range(len(self.completion_items)):	#<-- he tenido que iterar por que startswith es un atributo de los literales no de las listas, y le esta llegando una lista...				
				for item in self.completion_items[x]:
					if item.startswith(self.text()):
						self.setText(item)
						break
				event.accept()
		else:
			QLineEdit.keyPressEvent(self, event)
