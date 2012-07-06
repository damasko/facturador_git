import sys, shelve,  datetime
from PyQt4.QtCore import SIGNAL
from PyQt4.QtGui import *
from interfaz import Ui_albaran
from factura import *
from cliente import *
from item import  *

class programa(QMainWindow, Ui_albaran):
    total_facturas = []
    total_items = []
    total_clientes = []
    #aclientes = []
    
    def __init__(self, parent = None ):
        QWidget.__init__(self, parent)
        self.setupUi(self)
        self.setWindowTitle("Albaran v02")
        # linkando interfaz con funciones:
        self.connect(self.boxitems, SIGNAL("activated(const QString&)"), self.loadItem)
        self.connect(self.boxclient, SIGNAL("activated(const QString&)"), self.loadCliente)
        self.connect(self.addclienteB, SIGNAL("clicked()"),self.agregarCliente)
        self.connect(self.nuevoitem, SIGNAL("clicked()"),self.agregarItem)
    
        # # Actualizar nf desplegable clientes:
        self.updateComboC("") # como no le pasamos nada y no lo guardamos ese "nada" en ninguna base de datos pues entonces no importa
        self.boxclient.setCurrentIndex(-1) #<-- poner el combobox por default en blanco            
        #Desplegable items...
        self.updateComboI("") # como no le pasamos nada y no lo guardamos ese "nada" en ninguna base de datos pues entonces no importa
        self.boxitems.setCurrentIndex(-1) #<-- poner el combobox por default en blanco
        
        #Seteamos a la fecha actual, por defecto
        self.de3.setText(self.fechaActual())

    def fechaActual(self):
        fecha = datetime.date.today()
        fechaorden = fecha.strftime("%d/%m/%Y")
        return fechaorden
        
    def updateComboC(self, nombrec):
        # # Actualizar desplegable Cliente:
        self.boxclient.clear() # limpiamos combobox clietnes
        clidb = shelve.open("clientes.db") # abrimos bases de datos en el caso de que exista
        self.boxclient.addItems(sorted(clidb.keys())) # rellenamos con todos los clientes
        index = self.boxclient.findText(str(nombrec))# busco el nf para obtener el index
        self.boxclient.setCurrentIndex(index) # seteo por index
        clidb.close() # cerramos

    def updateComboI(self,  tipoi):
        self.boxitems.clear() # limpiamos combobox clietnes
        itdb = shelve.open("items.db") # abrimos bases de datos en el caso de que exista
        self.boxitems.addItems(sorted(itdb.keys())) # rellenamos con todos los clientes
        index = self.boxitems.findText(str(tipoi))# busco el nf para obtener el index
        self.boxitems.setCurrentIndex(index) # seteo por index
        itdb.close() # cerramos

    def agregarItem(self): #Esta funcion crea un objeto item, comprueba si esta en el array y si no esta lo anade y devuelve el array de items FUNCIONANDO
        item1 = item(self.newti.text(), self.npre.text())
        # w:
        itdb = shelve.open("items.db")
        itdb[str(item1.getTipo())] = item1
        
        itdb.close()
        #actualizamos combobox cliente: 
        self.updateComboI(item1.getTipo())
    
    def agregarCliente(self): #FUNCIONANDO   #####MODIFICADAD PARA ABRIR ARCHIVO, ACTUALIZARLO O ANADIR CLIENTE
        client1 = cliente(self.namec.text(), self.nif.text(), self.poblacion.text(), self.calle.text(),  self.nf.text())
        # w:
        clidb = shelve.open("clientes.db")
        clidb[str(client1.getNombre())] = client1
        

        
        clidb.close()
        #actualizamos combobox cliente: 
        self.updateComboC(client1.getNombre())

    def loadItem(self): #Esta funcion comprueba si hay un item, si es asi lo carga NO FUNCIONANDO
        
        itdb = shelve.open("items.db") # abrimos bases de datos en el caso de que exist
        it = itdb[str(self.boxitems.currentText()) ]
        self.precio.setText(it.getPrecio())
        
        itdb.close()

    
    def loadCliente(self): #NO FUNCIONANDO
        clidb = shelve.open("clientes.db") # abrimos bases de datos en el caso de que exist
        c = clidb[str(self.boxclient.currentText()) ]#  Falra 1 paso se ahorra una variable: estamos creando un objetos llamado client1 recuperado de la database Esto es lo  que contiene el combo cuando el user lo ha seleccionado: self.boxclient.currentText())# seteo desde el objeto recuperado de la base de datos:
        self.namec.setText(c.getNombre())
        self.nif.setText(c.getNif())
        self.poblacion.setText(c.getPoblacion())
        self.calle.setText(c.getCalle())
        
        clidb.close()
    
     ### Funciones de calculo de importe, etc
        
    def calculaImporte(self): #Esto hace el calculo de todos los precios y cantidades de los objetos del array FUNCIONANDO
        importe = 0
        for i in range(len(self.total_items)):
            importe = self.total_items[i].getCantidad()*self.total_items[i].getPrecio() + importe
        return importe
        
    def calculaIva(self): #No se puede llamar a calculaImporte D: por lo que no queda mas remedio que ir de uno en uno FUNCIONANDO
        return (self.calculaImporte()*self.__iva)/100
        
    def agregaIva(self,  importe,  iva): #FUNCIONANDO
        return self.calculaImporte() + self.calculaIva()
        


#MAIN
if __name__ == "__main__":
        app = QApplication(sys.argv)
        window = programa()
        window.show()
        sys.exit(app.exec_())

