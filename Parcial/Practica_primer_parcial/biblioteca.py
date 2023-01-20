import json
import re

def cargar_json(path:str)->list:
    '''
    Carga un archivo json para poder trabajar con el.
    Recibe el path del archivo json (Ruta del archivo).
    Devuelve la lista de diccionarios que contiene el archivo json.
    '''

    with open (path, "r") as file:
        dato = json.load(file)

    return dato["paulina"]

def validar_int(numero_ingresado:str)->int|bool:
    '''
    Valida mediante RegEx que el usuario halla ingresado un numero.
    Recibe el numero ingresado.
    Devuelve el numero casetado a int, o False.
    '''

    resultado = re.match("^[0-9]+$", numero_ingresado)

    if resultado != None:
        return int(numero_ingresado)
        
    else: False

def validar_string(str_ingresado:str, patron:str)->str|bool:
    '''
    Valida mediante RegEx que el usuario halla ingresado la pabra correcta.
    Recibe el str ingresado.
    Devuelve el str validado, o False.
    '''

    resultado = re.search(patron, str_ingresado, re.IGNORECASE)

    if resultado != None:
        return str_ingresado
    else: False

def mostrar_dato(lista:list):
    '''
    Imprime los datos de los videos formateados.
    Recibe la lista de videos.
    '''
    if type(lista) == type ([]) and len(lista) > 0:

        for video in lista:
            print("\nTitulo: {0}\nVistas: {1}\nDuracion: {2} seg".format(   video["title"],
                                                                            video["views"],
                                                                            video["length"]))
    
def buscar_min_max(lista:list, key:str, order:str)->int:
    '''
    Busca el indice que contiene el numero minimo/maximo segun el order que se le pase "UP"/"DOWN", del dato
    que se le pase en la key.
    Recibe la lista de videos, la key del dato a calcular y el order.
    Devuelve el indice minimo/maximo o -1 en caso de error.
    '''

    if type(lista) == type ([]) and len(lista) > 0:

        indice_min_max = 0

        for i in range(len(lista)):
            if order == "up" and lista[i][key] > lista[indice_min_max][key]:
                indice_min_max = i
            elif order == "down" and lista[i][key] < lista[indice_min_max][key]:
                indice_min_max = i

        return indice_min_max
    else: 
        return -1

def nahuel_sort_improve(lista:list, key:str, order:str)->list:
    '''
    Ordena una copia de la lista de videos segun el order que se le pase "UP"/"DOWN" del dato que se pase en la key.
    Recibe la lista de videos, la key del dato a calcular y el order en que quiero ordenar la lista.
    Devuelve la lista copiada en el orden que se quiere o -1 en caso de error.
    '''

    lista_ordenada = lista.copy()

    for i in range(len(lista_ordenada)):
        indice_min_max = buscar_min_max(lista_ordenada[i:],key, order) + i
        lista_ordenada[i], lista_ordenada[indice_min_max] = lista_ordenada[indice_min_max], lista_ordenada[i]

    return lista_ordenada

def buscar(lista:list, patron:str):
    '''
    Busca un patron mediante RegEx en el titulo.
    Recibe la lista de videos y el patron a buscar.
    '''

    if type(lista) == type ([]) and len(lista) > 0:

        for elemento in lista:
            match = re.search(patron, elemento["title"], re.IGNORECASE)
            if match :
                titulo = elemento["title"]
                palabra = "\033[0;31m" + match.group(0) + "\033[0;m"
                titulo = titulo.replace(match.group(0), palabra)
                print("\nTitulo: {0}\nVistas: {1}\nDuracion: {2} seg".format(   titulo,
                                                                                elemento["views"],
                                                                                elemento["length"]))
            
def exportar_csv(lista:list, nombre_archivo:str):
    '''
    Exporta la lista de video a un archivo csv.
    Recibe la lista de videos y el nombre del archivo que elija el usuario. 
    '''
    nombre_final = nombre_archivo + ".csv"

    with open (nombre_final, "w") as file:
        encabezado = "Titulo, Vistas, Duracion, Portada, Link, Fecha\n"
        file.write(encabezado)
        for elemento in lista:
            linea = "{0}, {1}, {2}, {3}, {4}, {5}\n".format(elemento["title"],
                                                            elemento["views"],
                                                            elemento["length"],
                                                            elemento["img_url"],
                                                            elemento["url"],
                                                            elemento["date"])
            file.write(linea)