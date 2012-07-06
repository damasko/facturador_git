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
        self.__fecha = self.fechaActual()
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
     

   

