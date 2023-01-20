import pygame
from constantes import *
import random

def crear(path:str, x:int, y:int, ancho:int, alto:int)-> dict:
    '''
    Podria hacerlo como hice con el personaje o asi.
    Creo la imagen de la dona, la escalo y le creo su rectangulo, tambien el rectangulo del eje x e y
    creo un diccionario de donas, le agrego la clave superficie y como valor la imagen de la dona, le agrego la clave rectangulo
    y como valor el rectangulo de la dona, tambien la velocidad de la dona
    Retorna el diccioanrio
    '''
    imagen_dona = pygame.image.load(path)
    imagen_dona = pygame.transform.scale(imagen_dona,(ancho,alto))
    rec_dona = imagen_dona.get_rect() 
    rec_dona.x = x
    rec_dona.y = y
    dict_donas = {}
    dict_donas ["surface"] = imagen_dona
    dict_donas ["rect"] = rec_dona
    dict_donas["speed"] = 3

    return dict_donas

def crear_lista_donas(cantidad:int)->list:
    '''
    Creo una lista de donas, mediante un for recorremos el len de la lista que se le pasa por parametro(cantidad)
    a la lista de donas le apendeamos la funcion anterior "crear" y por parametro le pasamos el path de la imagen de la dona
    eje x, eje y, ancho y alto de la dona  
    Retorna la lista de donas
    '''
    lista_donas = [] 
    for i in range(cantidad):
        x = random.randrange(150,1500,80)
        y = random.randrange(-1000,0,80)
        lista_donas.append(crear(PATH_RECURSOS + "dona.png",x,y,70,70))
    return lista_donas

def restart_dona(dona)->None:
    '''
    Se le asigna a eje x y al eje y del rectangulo de la 2 la funcion ramndom esta funcion es para que la llame la funcion
    actualizar_pantalla
    NO retorna nada
    '''
    dona["rect"].x = random.randrange(150,1500,70)
    dona["rect"].y = random.randrange(-1000,0,70)

def actualizar_pantalla(lista_donas:list, personaje:dict, screen)->None:
    '''
    Recorremos mediante un for la lista de donas que recibimos por parametro y preguntamos si el rectangulo de la boca
    del perosnaje que recibimos por parametro coliciona con el rect de la dona, si esto pasa se suma 100 al score del personaje
    y se llama a la funcion resta_dona que recibe la dona por parametro, tambien se pregunta si el eje y de la dona se 
    fue de pantalla, si se fue de pantalla se llama a la funcion resta_dona. Entonces cada vez que se cumplan esas condiciones
    las donas van a volver a aparecer arriba de la pantalla entonces no hace falta crear muchas donas.
    Se actualiza la imagen de la dona y su rectangulo en la pantalla
    Ya fuera del for se le agrega un texto del puntaje
    '''

    
    for dona in lista_donas:
        
        if personaje["rect"].colliderect(dona["rect"]):
            personaje["score"] += 100
            restart_dona(dona)
            sonido_comida = pygame.mixer.Sound(PATH_RECURSOS + "comiendo.mp3")
            sonido_comida.play()
            
        if dona["rect"].y > 910:
            restart_dona(dona)

        screen.blit(dona["surface"],dona["rect"])

    fuente = pygame.font.SysFont("Purisa",50)
    texto = fuente.render("Score:{0}".format(personaje["score"]),True,AZUL)
    screen.blit(texto,(0,0))

def update(lista_donas, personaje):
    '''
    Recorremos mediante un for la lista de donas que recibimos por parametro, a la variable rect_dona le asignamos el rectangulo
    de la dona y a al eje y de la dona le sumamos el speed(velocidad) preguntamos si el score es 10000 le sumamos 1 a la velocidad
    y si es 15000 le sumamos otro 1 a la velocidad
    '''
    for dona in lista_donas:
        rect_dona = dona["rect"]
        rect_dona.y += dona["speed"]
        if personaje["score"] > 9999:
            rect_dona.y = rect_dona.y + dona["speed"] + 1
        if personaje["score"] > 14999:
            rect_dona.y = rect_dona.y + dona["speed"] + 1
        if personaje["score"] > 19999:
            rect_dona.y = rect_dona.y + dona["speed"] + 1


