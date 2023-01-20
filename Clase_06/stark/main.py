from data import lista_personajes

def extraer_iniciales(nombre_heroe:str)->str:
    '''
    Extrae la inicial del/los nombre/s de cada personaje.

    Recibe una lista de tipo list, y una variable de tipo str.

    Devuelve un str con las iniciales de cada nombre de cada personaje y 'N/A' si no tiene nombre.
    '''
    
    if type(nombre_heroe) == type(str()) and len(nombre_heroe) > 0:
        nombre_heroe = nombre_heroe.upper()
        nombre_heroe = nombre_heroe.replace("THE ", "")
        nombre_heroe = nombre_heroe.replace("-", " ")
        nombre_heroe = nombre_heroe.strip()
        
        partes_nombres = nombre_heroe.split(" ")

        iniciales = " "

        for una_parte in partes_nombres:
            iniciales += una_parte[0] + "."
    
        return iniciales

    else:
        return "N/A"

    

for personaje in lista_personajes:
    print(extraer_iniciales(personaje["nombre"]))


def definir_iniciales_nombre(heroe:dict)-> dict:
    '''
    Agrega una nueva clave al diccionario recibido, la clave se llamara 'iniciales' y su valor sera obtindo al llamar
    a la funcion 'extraer_iniciales'.
 
    Recibe un diccionario.
    Retorna True y si hay algun error retorna False.
    '''
    retorno = False
    if type(heroe) == type(dict()) and len(heroe) > 0:
        for clave in heroe:
            if clave == "nombre":
                heroe["iniciales"] = extraer_iniciales(heroe["nombre"])
                retorno = True
                break

    print(heroe)
    return retorno

for personaje in lista_personajes:
    definir_iniciales_nombre(personaje)


def agregar_iniciales_nombre(lista_heroes:list):
    '''
    Recibe una lista.
    Devuelve True en caso de que salga todo bien y 'El origen de datos no contiene el formato correcto' en caso de error.
    '''

    retorno = False
    if type(lista_heroes) == type(list()) and len(lista_heroes) > 0:

        for heroe in lista_heroes:
            definir_iniciales_nombre(heroe)
            if definir_iniciales_nombre(heroe) == True :
                retorno = True
            else:
                retorno = False
                break
    if retorno == False:
        print("El origen de datos no contiene el formato correcto")
    return retorno
print(agregar_iniciales_nombre(lista_personajes))

'''
Crear la función ‘stark_imprimir_nombres_con_iniciales’  la cual recibirá como parámetro:
lista_heroes: la lista de personajes
La función deberá utilizar la función agregar_iniciales_nombre’ para añadirle las iniciales a los diccionarios contenidos en la lista_heroes
Luego deberá imprimir la lista completa de los nombres de los personajes seguido de las iniciales encerradas entre paréntesis () 
	Se deberá validar:
Que lista_heroes sea del tipo lista
Que la lista contenga al menos un elemento
Delante de cada nombre se deberá agregar un asterisco ‘*’ (de forma de viñeta) seguido de un espacio.
Ejemplo de salida:
* Howard the Duck (H.D.)
* Rocket Raccoon (R.R.)
…
La función no retorna nada

'''
def stark_imprimir_nombres_con_iniciales(lista_heroes:list):

    if type(lista_heroes) == type(list()) and len(lista_heroes) > 0:

        for personaje in lista_heroes:
            




#print(stark_imprimir_nombres_con_iniciales(lista_personajes))