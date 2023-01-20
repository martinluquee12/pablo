import re
import json


def cargar_json(path:str)->list:
    '''
    Carga el archivo json para poder trabajarlo.

    Recibe el path (ruta del archivo json)

    Devuelve la lista que contiene el archivo.
    '''

    with open (path, "r") as file:
        dato = json.load(file)

    return dato["results"]

def mostrar_dato_crudo(lista:list):
    '''
    Muestra el dato sin formatear para poder guardarlo en una variable para luego exportarlo.
    Recibe la lista de personajes.
    ''' 
    mensaje = ""
    for personaje in lista:
        mensaje += "{0}, {1}, {2}, {3}\n".format(personaje["name"],
                                                personaje["height"],
                                                personaje["mass"],
                                                personaje["gender"])
    return mensaje

def mostrar_dato(lista:list):
    '''
    Muestra el dato formateado por consola.

    Recibe la lista de personajes.
    ''' 

    for personaje in lista:
        print("*--------------------*")
        print("Nombre: {0}\nAltura: {1}cm\nPeso: {2}kg\nGenero: {3}".format(personaje["name"],
                                                                            personaje["height"],
                                                                            personaje["mass"],
                                                                            personaje["gender"]))
                                        
def buscar_min_max(lista:list, key:str, order:str)->int:
    '''
    Busca el indice que contiene el valor min/max del dato que se pase por la key
    Recibe la lista de personajes, la key y el orden.
    Devuelve el indice que encontro.
    '''

    if type(lista) == type([]) and len(lista) > 0:

        index_min_max = 0
    
        for i in range(len(lista)):

            if order == "max" and float(lista[i][key]) > float(lista[index_min_max][key]):
                index_min_max = i   
            elif order == "min" and lista[i][key] < lista[index_min_max][key]:
                index_min_max = i 

        return index_min_max

def nahuel_sort_improve(lista:list, key:str, order:str)->list:
    '''
    Crea una copia de la lista original y segun el order y la key se le pase va ordernar la lista,
    va a comparar el indice 0 con toda la lista y va hacer un swap.
    Recibe la lista de personajes, la key para saber que dato va ordenar y el orden min/max.
    Devuelve la copia de la lista ordenada.
    '''

    lista_ordenada = lista.copy()

    for i in range(len(lista_ordenada)):
        index_min_max = buscar_min_max(lista_ordenada[i:], key, order) + i
        lista_ordenada[i], lista_ordenada[index_min_max] = lista_ordenada[index_min_max], lista_ordenada[i]
    
    return lista_ordenada

def mas_alto_genero(lista:list):
    '''
    '''
    lista_masc = []
    lista_fem = []
    lista_na = []

    for personaje in lista:
        if personaje["gender"] == "male":
            lista_masc.append(personaje)
        elif personaje["gender"] == "female":
            lista_fem.append(personaje)
            nahuel_sort_improve(lista_fem, "height", "max")
        elif personaje["gender"] == "n/a":
            lista_na.append(personaje)

    masculino_mayor_altura = lista_masc[0]
    for persona in lista_masc:
        if float(persona["height"]) > float(masculino_mayor_altura["height"]):
            masculino_mayor_altura = persona

    femenino_mayor_altura = lista_fem[0]
    for persona in lista_fem:
        if float(persona["height"]) > float(femenino_mayor_altura["height"]):
            femenino_mayor_altura = persona

    na_mayor_altura = lista_na[0]
    for persona in lista_na:
        if float(persona["height"]) > float(na_mayor_altura["height"]):
            na_mayor_altura = persona

    print("Personajes mas alto de acada genero:\n")
    print("Nombre: {0} | Altura: {1}cm".format(masculino_mayor_altura["name"], masculino_mayor_altura["height"]))
    print("*-------------------------*")
    print("Nombre: {0} | Altura: {1}cm".format(femenino_mayor_altura["name"], femenino_mayor_altura["height"]))
    print("*-------------------------*")
    print("Nombre: {0} | Altura: {1}cm".format(na_mayor_altura["name"], na_mayor_altura["height"]))

def buscador(lista:list, patron:str):
    '''
    Atravez de RegEx busca el aptron que ingresa el usuario y lo imprime.
    Recibe la lista y el patron que se le pide al usuario.
    '''
    for personaje in lista:
        if re.search(patron, personaje["name"], re.IGNORECASE):
            print("Nombre: {0}\nAltura: {1}cm\nPeso: {2}kg\nGenero: {3}".format(personaje["name"],
                                                                                personaje["height"],
                                                                                personaje["mass"],
                                                                                personaje["gender"]))

def exportar_csv(mensaje:str, nombre_archivo:str, lista:list):
    '''
    Exporta a csv la lista que extraimos del archivo json.
    Recibe la lista y el nombre del archivo que se lo pedimos al usuario. 
    '''
    nombre_final = nombre_archivo + ".csv"

    with open (nombre_final, "w") as file:
        for elemento in lista:
            encabezado = "Nombre, Altura, Peso, Genero\n"
            file.write(encabezado)
            linea = "{0}, {1}, {2}, {3}\n".format(  elemento["name"],
                                                    elemento["height"],
                                                    elemento["mass"],
                                                    elemento["gender"])
            file.write(linea)
                                                                                  
        encabezado = "Nombre, Altura, Peso, Genero\n"
        file.write(encabezado)
        file.write(mensaje)
                                                                                  


