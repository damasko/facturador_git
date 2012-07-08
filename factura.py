
import shelve
from cliente import *
from item import *

class factura():
    
    def __init__(self, __nf,  __fecha,  __nombrec, __pago, __volcado_aitems, __importe = 0, __iva_apli = 0, __total = 0,  __iva=18):
        self.__nf = __nf
        self.__fecha = __fecha
        self.__nombrec = __nombrec
        self.__pago = __pago
        self.__volcado_aitems = __volcado_aitems
        self.__importe = __importe
        self.__iva_apli = __iva_apli
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
        self.__importe = newimporte
        
    def setIvaApli(self, newivaapli):
        self.__iva_apli = newivaapli
        
    def setTotal(self, newtotal):
        self.__total = newtotal
        
    def setIva(self, newiva):
        self.__iva = newiva

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
        
    def getIvaApli(self):
        return self.__iva_apli
     
    def getVolcado(self):
        return __volcado_aitems

    def getTotal(self):
        return self.__total

    def getIva(self):
        return self.__iva
        
        
     # Funcion calculo de importe, etc
        
    def calculaImporte(self,  __volcado_aitems): #Esto hace el calculo de todos los precios y cantidades de los objetos del array No devuelve nada, solo setea los atributos
        importeant = 0 #mirar si la 2 vez se ha convertido el iva en algo que no le mola 
        for i in self.__volcado_aitems:
            importeant = int(i.getCantidad())*float(i.getPrecio()) + importeant
        importeround = round(importeant,  3)
        self.setImporte(importeround)
        
        self.setIvaApli(float(self.__importe)*float(self.__iva)/100)
        self.setTotal(self.__importe + self.__iva_apli)

