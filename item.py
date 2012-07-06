class item(object):
    def __init__(self, __tipo, __precio,  __cantidad = 1): 
        self.__tipo = __tipo
        self.__precio = __precio
        self.__cantidad = __cantidad

    #Getters:
    def getCantidad(self):
        return self.__cantidad

    def getTipo(self):
        return self.__tipo

    def getPrecio(self):
        return self.__precio
    
    def getCantidad(self):
        return self.__cantidad

    #Setters:
    def setCantidad(self, newcantidad):
        self.__cantidad = newname

    def setTipo(self, newtipo):
        self.__tipo = newtipo

    def setPrecio(self, newprecio):
        self.__precio = newprecio
        
    def setCantidad(self,  newcantidad):
        self.__cantidad = newcantidad
