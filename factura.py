#from albaran import *
#from PyQt4.QtCore import SIGNAL
#from PyQt4.QtGui import *
#from interfaz import Ui_albaran
import shelve
from cliente import *
from item import *



class factura():
    
    def __init__(self, __nf,  __fecha,  __pago, __iva = 18):
        self.__nf = __nf
        self.__fecha = __fecha
        self.__pago = __pago
        self.__iva = __iva

    
    #Setters
    
    def setFecha(self, newfecha):
        self.__fecha = newfecha

    def setNf(self, newnf):
        self.__nf = newnf
    
    def setIva(self, newiva):
        self.__iva = __iva
        
    
        
    #Getters
    def getNf(self):
        return self.__nf

    def getFecha(self):
        return self.__fecha

    def getImporte(self):
        return self.__importe
        
    def getIva(self):
        return self.__iva
     

        
# Esto se deberia llamar desde el programa que maneja la interfaz aunque solo son pruebas aun
# Trabajar sobre el problema de darle otros valores al objeto Item y Cliente. Usar sus setters. Quiza util Sobrecarga
""""
f = factura("", 18 ,"", "")
aclientetst = f.agregarCliente("maria", "4", "bilbao", "arizona")
aclientetst = f.agregarCliente("jose",  "22", "madrid",  "cosa")
aclientetst = f.agregarCliente("pepillo",  "333", "lerida",  "lalala")
clienteA = aclientetst[0]
print clienteA.getNombre() + " " + clienteA.getNif() + " " + clienteA.getPoblacion() + " " + clienteA.getCalle()



aclientetst = f.agregarCliente("maria", "10", "valencia", "marquesina")
aitem = f.loadItem()
aitem = f.agregarItem(2,  "cosa2",  10)
importe = f.calculaImporte()
f.agregarCliente("alberto",  "5555",  "monchin",  "chingon")
aclientetst = f.agregarCliente("pepillo",  "333", "lerida",  "lalala")

iva = f.calculaIva()
addiva = f.agregaIva(importe,  iva)
#Prueba para anadir clientes
for i in aitem:
    print i.getTipo()
for i in aclientetst:
    print i.getNombre() + " " + i.getNif() + " " + i.getPoblacion() + " " + i.getCalle()

#f.loadItem("cosa2")
#f.guardaClientes()
print importe
print iva
print addiva

"""
   

