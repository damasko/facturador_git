from curses.ascii import isdigit
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
        self.setWindowTitle("Albaran v02 alpha")
        # linkando interfaz con funciones:
        self.connect(self.boxitems, SIGNAL("activated(const QString&)"), self.loadItem)
        self.connect(self.boxclient, SIGNAL("activated(const QString&)"), self.loadCliente)
        self.connect(self.itemfac, SIGNAL("activated(const QString&)"), self.loadPrecio)
        self.connect(self.boxfacs, SIGNAL("activated(const QString&)"), self.loadFactura)
        self.connect(self.addclienteB, SIGNAL("clicked()"),self.agregarCliente)
        self.connect(self.nuevoitem, SIGNAL("clicked()"),self.agregarItem)
        self.connect(self.rm_cliente, SIGNAL("clicked()"),self.eliminarCliente)
        self.connect(self.rm_item, SIGNAL("clicked()"),self.eliminarItem)
        self.connect(self.agregait, SIGNAL("clicked()"),self.volcarItems)
        self.connect(self.calculaImporteB, SIGNAL("clicked()"),self.calculo)
        self.connect(self.rmitemfacB, SIGNAL("clicked()"),self.rmitemfac)
        self.connect(self.guardartodoB, SIGNAL("clicked()"),self.guardarFactura)
        self.connect(self.rmallfac, SIGNAL("clicked()"),self.eliminarFactura )
        self.connect(self.newfacB, SIGNAL("clicked()"),self.nuevaFactura )
        

        # recopilamos listado de clientes del combobox en un array para el autocompletado por tabulador:
        #all_clientes_de_combo = [self.boxclient.itemText(x) for x in range(self.boxclient.count())]
 
        # # Actualizar nf desplegable clientes:
        self.updateComboC("") # como no le pasamos nada y no lo guardamos ese "nada" en ninguna base de datos pues entonces no importa
        self.boxclient.setCurrentIndex(-1) #<-- poner el combobox por default en blanco            
        #Desplegable items...
        self.updateComboI("") # como no le pasamos nada y no lo guardamos ese "nada" en ninguna base de datos pues entonces no importa
        self.boxitems.setCurrentIndex(-1) #<-- poner el combobox por default en blanco
        
        #Desplegable facturas
        self.updateComboF("")
        self.boxfacs.setCurrentIndex(-1)
        
        #Seteamos a la fecha actual, por defecto
        self.de3.setText(self.fechaActual())
        

    def fechaActual(self):
        fecha = datetime.date.today()
        fechaorden = fecha.strftime("%d/%m/%Y")
        return fechaorden
        
    def updateComboC(self, nombrec):
        # # Actualizar desplegable Cliente:
        self.boxclient.clear() # limpiamos combobox clietnes
        clientes_db = shelve.open("clientes.db") # abrimos bases de datos en el caso de que exista
        self.boxclient.addItems(sorted(clientes_db.keys())) # rellenamos con todos los clientes
        index = self.boxclient.findText(str(nombrec))# busco el nf para obtener el index
        self.boxclient.setCurrentIndex(index) # seteo por index
        clientes_db.close() # cerramos

    def updateComboI(self,  tipoi):
        self.boxitems.clear() # limpiamos combobox clietnes
        item_db = shelve.open("items.db") # abrimos bases de datos en el caso de que exista
        self.boxitems.addItems(sorted(item_db.keys())) # rellenamos con todos los clientes
        index = self.boxitems.findText(str(tipoi))# busco el nf para obtener el index
        self.boxitems.setCurrentIndex(index) # seteo por index
        item_db.close() # cerramos

    def agregarCliente(self): #FUNCIONANDO   #####MODIFICADAD PARA ABRIR ARCHIVO, ACTUALIZARLO O ANADIR CLIENTE
        ocliente = cliente(self.namec.text(), self.nif.text(), self.poblacion.text(), self.calle.text(),  self.nf.text())
        # w:
        clientes_db = shelve.open("clientes.db")
        clientes_db[str(ocliente.getNombre())] = ocliente
        

        
        clientes_db.close()
        #actualizamos combobox cliente: 
        self.updateComboC(ocliente.getNombre())

    def eliminarCliente(self):

        current = self.boxclient.currentText()
        clientes_db = shelve.open("clientes.db")
        
        try:
            del clientes_db[str(current)]
        except:
            print "No existe el Cliente a eliminar"
            
        self.boxclient.setCurrentIndex(-1)
        self.namec.setText("")
        self.nif.setText("")
        self.poblacion.setText("")
        self.calle.setText("")

        clientes_db.close()

        # # Actualizar combobox cliente:
        self.updateComboC("") # como no le pasamos nada y no lo guardamos ese "nada" en ninguna base de datos pues entonces no importa
        self.boxclient.setCurrentIndex(-1) #<-- poner el combobox por default en blanco
        
        

    def agregarItem(self): #Esta funcion crea un objeto item, comprueba si esta en el array y si no esta lo anade y devuelve el array de items FUNCIONANDO
        
        # esto comprobamos si tiene coma y la convertimos a punto:
        if  "," in str(self.precio_item.text()):
            nprec = str(self.precio_item.text())
            nprec = nprec.replace(",", ".")
            self.precio_item.setText(nprec)
        # comprobamos si el resultado es un int o un float, sino tiramos error:
        
        chequeo = self.precio_item.text()
        
        try:
            int(chequeo)
            valido = True
        except ValueError:
            try:
                float(chequeo)
                valido = True
            except ValueError:
                print "El numero no es un valor numerico"
                valido = False

        if valido: 

            item1 = item(self.newti.text(), self.precio_item.text())
           
            #w:
            item_db = shelve.open("items.db")
            item_db[str(item1.getTipo())] = item1
            
            item_db.close()
            #actualizamos combobox cliente: 
            self.updateComboI(item1.getTipo())
        

    def loadItem(self): 
        
        item_db = shelve.open("items.db") # abrimos bases de datos en el caso de que exist
        it = item_db[str(self.boxitems.currentText()) ]
        self.precio_item.setText(it.getPrecio())
        self.newti.setText(it.getTipo())
        item_db.close()

    def eliminarItem(self):

        current = self.boxitems.currentText()
        items_db = shelve.open("items.db")
        try:
            del items_db[str(current)]
        except: 
            print "No existe el Articulo a eliminar"

        self.boxitems.setCurrentIndex(-1)
        self.precio_item.setText("")
        self.newti.setText("")
        items_db.close()

        # # Actualizar combobox cliente:
        self.updateComboI("") # como no le pasamos nada y no lo guardamos ese "nada" en ninguna base de datos pues entonces no importa
        self.boxitems.setCurrentIndex(-1) #<-- poner el combobox por default en blanco
        
    def volcarItems(self):
        # dependiendo de si el item tiene cantidad o no
        if self.boxitems.currentIndex() != -1: # si no tiene cantidad pillamos la de por default del constructor
            if not self.cantidad.text():
                item1 = item( str(self.boxitems.currentText()),str(self.precio_item.text()))
            else: # sino creo el objeto con su cantidad dada por el user
                item1 = item( str(self.boxitems.currentText()),str(self.precio_item.text()),str(self.cantidad.text()) )
            
            # comprobacion para que no se repitan items:
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
                    
                if not existe:
                    self.total_items.append(item1)
                else:
                    if not self.cantidad.text():
                        self.cantidad.setText(str(item1.getCantidad()))
                    else:
                        self.total_items[indice-1].setCantidad(self.cantidad.text()) # aprovechamos el indice para usar y sacaar el id del ultimo elemento valido. El -1 es por que se ha iterado una vez de mas.
            
            self.cantidad_ro.setText(str(item1.getCantidad())) # actualizamos el read only de cantidad de abajo
            self.precio_fac.setText(str(item1.getPrecio()))
            self.cantidad.setText("") #Limpio el texto de la cantidad introducida, a ver si se ve mas limpio :D
    
            self.itemfac.clear()
            for i in self.total_items:
                self.itemfac.addItem(i.getTipo())
            index = self.itemfac.findText( str( self.boxitems.currentText() ))# busco el nf para obtener el index
            self.itemfac.setCurrentIndex(index) # seteo por index
            
            for pepe in self.total_items:
                print pepe.getPrecio()
                
                  
    def loadPrecio(self):
        indice = 0
        corto = False
        while not corto and indice < len(self.total_items):
            if self.total_items[indice].getTipo() == self.itemfac.currentText():
                it = self.total_items[indice]
                corto = True
            indice += 1
        
        self.cantidad_ro.setText(str(it.getCantidad()))
        self.precio_fac.setText(it.getPrecio())
        

    def loadCliente(self): 
        clientes_db = shelve.open("clientes.db") # abrimos bases de datos en el caso de que exist
        c = clientes_db[str(self.boxclient.currentText()) ]#  Falra 1 paso se ahorra una variable: estamos creando un objetos llamado ocliente recuperado de la database Esto es lo  que contiene el combo cuando el user lo ha seleccionado: self.boxclient.currentText())# seteo desde el objeto recuperado de la base de datos:
        self.namec.setText(c.getNombre())
        self.nif.setText(c.getNif())
        self.poblacion.setText(c.getPoblacion())
        self.calle.setText(c.getCalle())
        
        clientes_db.close()
        
    def rmitemfac(self):
        indice = 0
        corto = False
        while (not corto and indice < len(self.total_items)):
            if (self.total_items[indice].getTipo() == self.itemfac.currentText()):
                del self.total_items[indice]
                corto = True
            indice += 1
        self.cantidad_ro.setText("")
        self.precio_fac.setText("")
        
        
        self.itemfac.clear()
        for i in self.total_items:
            self.itemfac.addItem(i.getTipo())
        self.itemfac.setCurrentIndex(-1)
        
        
    def calculo(self):
        
        f = factura(str(self.nf.text()), str(self.de3.text()),  str(self.namec.text()), str(self.nif.text()), str(self.poblacion.text()),  str(self.calle.text()), str(self.pago.text()), self.total_items)
        
        if (not self.iva.text()): #Si esta vacio le decimos que coja el iva por defecto del constructor factura.
            self.iva.setText(str(f.getIva()))
        else:
            f.setIva(str(self.iva.text()))
            
        f.calculaImporte(self.total_items)
        
        #Seteo los campos...
        self.importe.setText(str(f.getImporte()))
        self.iva_a.setText(str(f.getIvaApli()))
        self.total.setText(str(f.getTotal()))
        
    def nuevaFactura(self):
        self.boxclient.setCurrentIndex(-1)
        self.namec.setText("")
        self.nif.setText("")
        self.poblacion.setText("")
        self.calle.setText("")
        self.nf.setText("")
        self.pago.setText("")
        self.cantidad_ro.setText("")
        self.precio_fac.setText("")
        self.total_items = []
        self.importe.setText("")
        self.iva.setText("")
        self.iva_a.setText("")
        self.total.setText("")
        self.boxfacs.setCurrentIndex(-1) #<-- poner el combobox por default en blanco
        self.boxclient.setCurrentIndex(-1) #<-- poner el combobox por default en blanco
        self.boxitems.setCurrentIndex(-1) #<-- poner el combobox por default en blanco
        self.itemfac.clear() # como no le pasamos nada y no lo guardamos ese "nada" en ninguna base de datos pues entonces no importa
        self.itemfac.setCurrentIndex(-1) #<-- poner el combobox por default en blanco
        self.de3.setText(self.fechaActual()) # seteamos la fecha actual
        
        
    def guardarFactura(self):
        ofactura = factura(str(self.nf.text()), str(self.de3.text()),  str(self.namec.text()), str(self.nif.text()), str(self.poblacion.text()), str(self.calle.text()), str(self.pago.text()), self.total_items, self.importe.text(), self.iva.text(), self.iva_a.text(),  self.total.text())
        # w:
        facturas_db = shelve.open("facturas.db")
        facturas_db[str(ofactura.getNf())] = ofactura        

        facturas_db.close()
        #actualizamos combobox facturas: 
        self.updateComboF(ofactura.getNf())
        self.agregarCliente()
        
    def updateComboF(self,  nf):
        self.boxfacs.clear() # limpiamos combobox clietnes
        facturas_db = shelve.open("facturas.db") # abrimos bases de datos en el caso de que exista
        self.boxfacs.addItems(sorted(facturas_db.keys())) # rellenamos con todos los clientes
        index = self.boxfacs.findText(str(nf))# busco el nf para obtener el index
        self.boxfacs.setCurrentIndex(index) # seteo por index
        facturas_db.close() # cerramos py
    
    def loadFactura(self):
        facturas_db = shelve.open("facturas.db") # abrimos bases de datos en el caso de que exist
        f = facturas_db[str(self.boxfacs.currentText()) ]#  Falra 1 paso se ahorra una variable: estamos creando un objetos llamado ocliente recuperado de la database Esto es lo  que contiene el combo cuando el user lo ha seleccionado: self.boxclient.currentText())# seteo desde el objeto recuperado de la base de datos:
        self.nf.setText(f.getNf())
        self.de3.setText(f.getFecha())
        self.namec.setText(f.getNombrec())
        self.nif.setText(f.getNifc())
        self.poblacion.setText(f.getPobc())
        self.calle.setText(f.getCallec())
        self.pago.setText(f.getPago())
        self.total_items = f.getVolcado()
        self.itemfac.setCurrentIndex(-1)
        self.importe.setText(f.getImporte())
        self.iva.setText(f.getIva())
        self.iva_a.setText(f.getIvaApli())
        self.total.setText(f.getTotal())
        
        self.itemfac.clear()
        for i in self.total_items:
            self.itemfac.addItem(i.getTipo())
        index = self.itemfac.findText( str( self.boxitems.currentText() ))# busco el nf para obtener el index
        self.itemfac.setCurrentIndex(index) # seteo por index
    
        facturas_db.close()
        
    def eliminarFactura(self):

        current = self.boxfacs.currentText()
        facturas_db = shelve.open("facturas.db")
        try:
            del facturas_db[str(current)]
        except: 
            print "No existe la Factura a eliminar"
        
        facturas_db.close()

        #Desplegable facturas
        self.updateComboF("")
        self.boxfacs.setCurrentIndex(-1)

        # # Actualizar combobox cliente:
        self.boxclient.setCurrentIndex(-1)
        
        self.itemfac.clear() # como no le pasamos nada y no lo guardamos ese "nada" en ninguna base de datos pues entonces no importa
        self.itemfac.setCurrentIndex(-1) #<-- poner el combobox por default en blanco
        
        self.nuevaFactura()
        

#MAIN

if __name__ == "__main__":
        app = QApplication(sys.argv)
        window = programa()
        window.show()
        sys.exit(app.exec_())
