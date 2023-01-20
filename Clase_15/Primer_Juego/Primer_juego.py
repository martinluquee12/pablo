import pygame
from constantes import *
import donas
import personaje

pygame.init()

#Creo ventana 
screen = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA),pygame.FULLSCREEN)

#Titulo
pygame.display.set_caption("Homero")

#Icono
icon = pygame.image.load(PATH_RECURSOS + "icono.png")
pygame.display.set_icon(icon)

#creo fondo
fondo = pygame.image.load(PATH_RECURSOS + "fondo.jpg").convert_alpha()
fondo = pygame.transform.scale(fondo,(1600,900))

#Musica de fondo
musica = pygame.mixer.music.load(PATH_RECURSOS + "musica.mp3")
musica = pygame.mixer.music.set_volume(0.6)
musica = pygame.mixer.music.play(-1)


#Time para control de fps
time = pygame.time.Clock() 

#creo timer
timer = pygame.USEREVENT + 0
pygame.time.set_timer(timer,10)

#Personaje
player = personaje.crear(700, 700, 200, 200)
#Donas
lista_donas = donas.crear_lista_donas(20)

running = True


while running:
    lista_eventos = pygame.event.get()
    lista_teclas = pygame.key.get_pressed()

    for evento in lista_eventos:
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                pygame.quit()
                running = False
        if evento.type == pygame.USEREVENT:
            if evento.type == timer:
                donas.update(lista_donas, player)
    if lista_teclas[pygame.K_LEFT]:
        personaje.update(player,-7)
    elif lista_teclas[pygame.K_RIGHT]:
        personaje.update(player,7)

    time.tick(FPS)
    screen.blit(fondo, (0,0))
    personaje.actualizar_pantalla(player,screen)
    donas.actualizar_pantalla(lista_donas,player, screen)
    
    
    
    pygame.display.flip()
    
