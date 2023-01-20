class Personaje:
    '''
    Documento la clase
    '''
    #no se usa mucho
    tipo = "X"
    #poner los atributos en init es una buena practica
    def __init__(self, nombre) -> None:
        self.__nombre = nombre

    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def mostrar(self):
        print("El personaje se llama {}".format(self._nombre))

        

perso = Personaje("Olga")
print(perso.nombre)

personaje_1 = Personaje("Pablo")
personaje_2 = Personaje("Hector")
personaje_1.mostrar()
personaje_2.mostrar()

print(personaje_1.tipo)#muestra x

personaje_2.tipo = "F"
print(personaje_2.tipo)#muestra f

print(Personaje.tipo)#muestra x