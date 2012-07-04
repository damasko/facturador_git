class cliente(object):
    def __init__(self, __nombre, __nif, __poblacion, __calle ,  __facturas_suyas):
        self.__nombre = __nombre
        self.__nif = __nif
        self.__poblacion = __poblacion
        self.__calle = __calle
        self.__facturas_suyas = __facturas_suyas #Va a ser un array con las nfacturas del cliente

    #Getters:
    def getNombre(self):
        return self.__nombre

    def getNif(self):
        return self.__nif

    def getPoblacion(self):
        return self.__poblacion

    def getCalle(self):
        return self.__calle
        
    def getFacturas(self):
        return self.__facturas_suyas
        
    #Setters:
    def setNombre(self, newname):
        self.__nombre = newname

    def setNif(self, newnif):
        self.__nif = newnif

    def setPoblacion(self, newpob):
        self.__poblacion = newpob
    
    def setCalle(self, newstreet):
        self.__calle = newstreet
    
    def setFacturas(self,  newfactura):
        self.__facturas_suyas.append(newfactura)
