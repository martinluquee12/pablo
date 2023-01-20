def mostrar_video(video:dict)->dict:
    '''
    Muestra los temas y su data.
    Recibe una diccionario.
    Devuelve un str
    '''

    mensaje = "\nNombre: {0} \nVistas: {1:.2f} M \nDuracion: {2} seg \nPortada: {3} \nLink: {4} \nFecha de pucblicacion: {5} "
    print(mensaje.format(   video["title"], 
                            video["views"]/1000000, 
                            video["length"], 
                            video["img_url"], 
                            video["url"], 
                            video["date"]))

def mostrar_lista_videos(lista:list)-> dict:
    '''
    Muestra la lista de los videos.
    Recibe una lista de video.
    Devuelve un diccionario.
    '''

    for video in lista:
        print(video["title"])

def cacula_maximo_minimo(lista:list, tipo:str, dato:str)->dict:
    '''
    Calcula el maximo/minimo segun el tipo que se pase por parametro y calcula el dato segun,
    el dato que se pase por parametro "views"/"length".
    Recibe la lista de videos, el tipo a calcular "maximo"/"minimo" y el dato a calcular.
    Retorna el diccionario que contiene al maximo o al minimo o "Error!".
    '''
    maximo_minimo = lista[0]

    retorno = "Error!"

    for personaje in lista:
        
        if tipo == "maximo" and float(personaje[dato]) > float(maximo_minimo[dato]):
            maximo_minimo = personaje

        elif tipo == "minimo" and float(personaje[dato]) < float(maximo_minimo[dato]):
            maximo_minimo = personaje

        retorno = maximo_minimo

    return retorno

def mostrar_maximo_vistas(lista:list)-> dict:
    '''
    Muestra el video con mayor cantidad de vistas.
    Devuelve un diccionario con el maximo.
    '''
    mostrar_video(cacula_maximo_minimo(lista, "maximo", "views"))

def mostrar_minimo_vista(lista:list)-> dict:
    '''
    Muestra el video con menor cantidad de vistas.
    Devuelve un diccionario con el minimo.
    '''
    mostrar_video(cacula_maximo_minimo(lista, "minimo", "views"))

def mostrar_maximo_duracion(lista:list)-> dict:
    '''
    Muestra el video con mayor duracion.
    Devuelve un diccionario con el maximo.
    '''
    mostrar_video(cacula_maximo_minimo(lista, "maximo", "length"))

def mostrar_minimo_duracion(lista:list)-> dict:
    '''
    Muestra el video con menor duracion.
    Devuelve un diccionario con el minimo.
    '''
    mostrar_video(cacula_maximo_minimo(lista, "minimo", "length"))

def calcular_promedio_vistas_duracion(lista: list, dato:str)->int:
    '''
    Calcula el promedio de vistas/duracion y lo muestra por consola.
    Recibe la lista de videos y el dato que se quiere calcular "views"/"length"

    '''
    if dato == "length":

        acumulador_duracion = 0

        for duracion in lista:
            acumulador_duracion += duracion[dato]
            
        print("Promedio de duracion de videos: {0:.2f} seg".format(acumulador_duracion/len(lista)))

    if dato == "views":

        acumulador_vistas = 0

        for vistas in lista:
            acumulador_vistas += vistas[dato]

        print("Promedio de vistas de videos: {0:.2f} M".format((acumulador_vistas//len(lista)/1000000)))

