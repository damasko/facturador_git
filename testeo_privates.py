class objetito():
    # privatizamos el array por que va a ser un atrubuto nuevo....
    def __init__(self,__objetos = ["p","j","k"],literal=""): # <-- si no se le pasa nada en el campo objetos por default sera el array p,j,k
        self.__objetos = __objetos # <-- Atributo variable privado
        self.literal = literal

    """
    # funcion test no se usa ahora
    #def test(self,objetos): # <-- self recibe los atributos de el mismo por eso pilla objetos y no vale cualquier nombre
    def __test(self,__objetos): # <-- con __ delante de la funcion se hace privado y no es accesible
        for x in range(len(self.objetos)):
            print self.objetos[x]
    """

    # Setters:
    def setArray(self,literal): # <-- se recibe a el mismo y sus atributos por eso no tenemos por que decir que recibira __objetos 
       self.__objetos.append(literal)
    
    # Getters:
    def getArray(self):
        for x in range(len(self.__objetos)):
            print self.__objetos[x]

        


a = objetito()
#print a.__objetos
#a.__test(a.objetos) # no lo pilla por que es privado
#a.test(a.objetos) # de ninguna de las dos es accesible, pero de serlo seria __test
print "escribe un texto: "
#texto = raw_input() # <-- si solo se usa una vez no merece la pena crear una variable nueva

a.getArray()
a.setArray(raw_input())
a.getArray()
