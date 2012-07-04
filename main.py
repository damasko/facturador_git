import sys, shelve
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
        #self.connect(self.boxfacs, SIGNAL("activated(const QString&)"), self.loadItem)
        self.connect(self.boxclient, SIGNAL("activated(const QString&)"), self.loadCliente)
        self.connect(self.addclienteB, SIGNAL("clicked()"),self.agregarCliente)
    
        # # Actualizar nf desplegable:
        self.updateComboC("") # como no le pasamos nada y no lo guardamos ese "nada" en ninguna base de datos pues entonces no importa
        self.boxclient.setCurrentIndex(-1) #<-- poner el combobox por default en blanco            
        
    def updateComboC(self, nombrec):
        # # Actualizar desplegable Cliente:
        self.boxclient.clear() # limpiamos combobox clietnes
        clidb = shelve.open("clientes.db") # abrimos bases de datos en el caso de que exista
        self.boxclient.addItems(sorted(clidb.keys())) # rellenamos con todos los clientes
        index = self.boxclient.findText(str(nombrec))# busco el nf para obtener el index
        self.boxclient.setCurrentIndex(index) # seteo por index
        clidb.close() # cerramos

    def agregarItem(self,  cantidad,  precio,  nombre): #Esta funcion crea un objeto item, comprueba si esta en el array y si no esta lo anade y devuelve el array de items FUNCIONANDO
        item1 = item(cantidad,  precio,  nombre)
        if not self.total_items:
            self.total_items.append(item1)
        else:
            indice = 0
            existe = False
            while (not existe and indice < len(self.total_items)):
                if item1.getTipo() == self.total_items[indice].getTipo(): # si EXISTEN coincidencias es True
                    existe = True
                else:
                    existe = False  # si NO existe coincidencias es False
                
                indice += 1
            if existe: #Modificacion para que esta funcion actualice el item en caso de existir
                self.total_items[indice-1].setCantidad(cantidad) #Indice - 1 ya que aunque se ha cortado el bucle se ha incrementado indice por eso no coincide
                self.total_items[indice-1].setPrecio(precio)
            else:
                self.total_items.append(item1)
                
            #Podria ser interesante devolver el item si existe
            #else:
            #  cargarItem
             
        return self.total_items
    
    def agregarCliente(self): #FUNCIONANDO   #####MODIFICADAD PARA ABRIR ARCHIVO, ACTUALIZARLO O ANADIR CLIENTE
        ocliente = cliente(self.namec.text(), self.nif.text(), self.poblacion.text(), self.calle.text(),  self.nf.text())
        # w:
        clidb = shelve.open("clientes.db")
        clidb[str(ocliente.getNombre())] = ocliente
        
        # r:
        clidb = shelve.open("clientes.db")
        print clidb[str(ocliente.getNombre())]
        
        clidb.close()
        #actualizamos combobox cliente: 
        self.updateComboC(ocliente.getNombre())

    def loadItem(self): #Esta funcion comprueba si hay un item, si es asi lo carga NO FUNCIONANDO
        item1 = item()
        if not self.total_items:
             self.total_items.append(item1)
        else:
            indice = 0
            existe = False
            while (not existe and indice < len(self.total_items)):
                if item1.getTipo() == self.total_items[indice].getTipo(): # si EXISTEN coincidencias es True
                    existe = True
                else:
                    existe = False  # si NO existe coincidencias es False
                
                indice += 1
            if existe:
                return item1
            
                
        return False #Devuelvo algo por si no existe o ha habido un error


    #Carga de clientes sobrecargada con valores puestos por el usuario
    #No existe sobrecarga! D:
    
    def loadCliente(self): #NO FUNCIONANDO
        clidb = shelve.open("clientes.db") # abrimos bases de datos en el caso de que exista
        cn = str(self.boxclient.currentText()) # recuperamos el nombre del susodicho
        
        c = clidb[ str(cn) ]   # estamos creando un objetos llamado ocliente recuperado de la database
        print str(c.getNombre())
        # seteo desde el objeto recuperado de la base de datos:
        self.namec.setText(str(c.getNombre()))
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

