#from albaran import *
#from PyQt4.QtCore import SIGNAL
#from PyQt4.QtGui import *
#from interfaz import Ui_albaran
import shelve
from cliente import *
from item import *

class factura():
    
    def __init__(self, __nf,  __fecha,  __nombrec, __pago, __volcado_aitems, __importe, __total,  __iva=18):
        self.__nf = __nf
        self.__fecha = self.fechaActual()
        self.__nombrec = __nombrec
        self.__pago = __pago
        self.__volcado_aitems = __volcado_aitems
        self.__importe = __importe
        self.__total = __total
        self.__iva = __iva

    
    # Setters ###############################
    
    def setFecha(self, newfecha):
        self.__fecha = newfecha

    def setNf(self, newnf):
        self.__nf = newnf
        
    def setNombrec(self, nombrec):
        self.__nombrec = nombrec
        
    def setPago(self, newpago):
        self.__pago = __pago
    
    def setVolcado(self,  array):
        self.__volcado_aitems = array
    
    def setImporte(self, newimporte):
        self.__importe = __importe
        
    def setItotal(self, newtotal):
        self.__total = __total
        
    def setIva(self, newiva):
        self.__iva = __iva

    # Getters ################################
    def getNf(self):
        return self.__nf

    def getFecha(self):
        return self.__fecha
        
    def getNombrec(self):
        return self.__nombrec
        
    def getPago(self):
        return self.__pago

    def getImporte(self):
        return self.__importe
     
    def getVolcado(self):
        return __volcado_aitems

    def getTotal(self):
        return self.__total

    def getIva(self):
        return self.__iva
        
        
    # Calculo de importe, iva y total
    
    def calculaImporte(self): #Esto hace el calculo de todos los precios y cantidades de los objetos del array FUNCIONANDO
        importe = 0
        for i in range(len(self.total_items)):
            importe = self.total_items[i].getCantidad()*self.total_items[i].getPrecio() + importe
        return importe
        
    def calculaIva(self): #No se puede llamar a calculaImporte D: por lo que no queda mas remedio que ir de uno en uno FUNCIONANDO
        return (self.calculaImporte()*self.__iva)/100
        
    def agregaIva(self,  importe,  iva): #FUNCIONANDO
        return self.calculaImporte() + self.calculaIva()
    
