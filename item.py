class item(object):
    def __init__(self, __cantidad, __tipo, __precio,  __nf):
        self.__cantidad = __cantidad
        self.__tipo = __tipo
        self.__precio = __precio
        self.__nf = __nf

    #Getters:
    def getCantidad(self):
        return self.__cantidad

    def getTipo(self):
        return self.__tipo

    def getPrecio(self):
        return self.__precio


    #Setters:
    def setCantidad(self, newcantidad):
        self.__cantidad = newname

    def setTipo(self, newtipo):
        self.__tipo = newtipo

    def setPrecio(self, newprecio):
        self.__precio = newprecio
