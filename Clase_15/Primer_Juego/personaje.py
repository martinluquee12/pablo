import pygame
from constantes import *

def crear(x:int ,y:int ,ancho:int, alto:int)->dict:
    '''
    Creo un diccionario de personaje, le agrego la clave superficie y como valor le paso la imagen del 
    personaje, escalo la imagen del personaje para que quede bien las dimenciones, luego creo la clave
    posicion del rectangulo como valor el rectangulo del personaje para que no se valla de pantalla,
    luego agregp la clave rectangulo y se lo ajusto a la boca del personaje para que pueda colisionar
    con las donas, luego agrego la clave puntaje y la inicializo en 0 
    Retorno el diccionario
    '''
    dict_personaje = {}
    dict_personaje["surface"] = pygame.image.load(PATH_RECURSOS + "homero.png") 
    dict_personaje["surface"] = pygame.transform.scale(dict_personaje["surface"],(ancho, alto))
    dict_personaje["rect_pos"] = pygame.Rect(x,y, ancho, alto)
    dict_personaje["rect"] = pygame.Rect((x+ancho/2)-40,y+100, 50, 20)
    dict_personaje["score"] = 0

    return dict_personaje
    

def actualizar_pantalla(personaje, screen)->None:
    '''
    Dibujo la imagen del personaje y su rectangulo que en este caso es invisible en la pantalla de juego
    No retorna nada
    '''
    screen.blit(personaje["surface"],personaje["rect_pos"])

def update(personaje, incremento_x)->None:
    '''
    Creo la variable nueva_x y le asigno el rectangulo del personaje en su eje x mas el incremento de la x
    que se lo paso por parametro cuando llamo a esta funcion.
    pregunta si la nueva x es mayor a 0 y menor a 1400 (esto es para que no se valla de pantalla, 
    se le resto lo que mide el personaje)
    si eso pasa al eje x del rectangulo del personaje le sumo el incremento de x y tambien se lo sumo
    al rectangulo de la boca del personaje
    No retorna nada
    '''
    nueva_x = personaje["rect_pos"].x + incremento_x
    if nueva_x > 0 and nueva_x < 1400:
        personaje["rect_pos"].x = personaje["rect_pos"].x + incremento_x
        personaje["rect"].x = personaje["rect"].x + incremento_x
