import pygame#importamos la biblioteca pygame
import colores#importo la biblioteca de colores que cree
pygame.init()#inicializamos la biblioteca

ANCHO_VENTANA = 800
ALTO_VENTANA = 800

ventana_principal = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA),pygame.FULLSCREEN)#creo una ventana y le paso por parametro alto y ancho, la ventana es de type superface
pygame.display.set_caption("PYGAME TEST")

running = True #para que el usuario pueda jugar en un loop infinito hasta que pase un evento quit

posicion_circulo = [60,30]#cordenadas del circulo

#creo un timer en milisegundos
timer_seg = pygame.USEREVENT
pygame.time.set_timer(timer_seg,100)

imagen_homero = pygame.image.load("Primer Cuatrimestre/Clase_15/homero.png")#creo una imagen 
imagen_homero = pygame.transform.scale(imagen_homero,(150,200))#escalo la imagen a el ancho y alto que quiero
rec_homero = pygame.Rect(700,700,150,200)#dibujamos un rectangulo en homero que lo dilimita 

imagen_dona = pygame.image.load("Primer Cuatrimestre/Clase_15/dona.png")#creo una imagen
imagen_dona = pygame.transform.scale(imagen_dona,(50,50))#escalo la imagen a el ancho y alto que quiero
rec_dona = imagen_dona.get_rect() 
rec_dona.x = 100
rec_dona.y = 100

fuente = pygame.font.SysFont("Arial",30)#creo una fuente de letras
texto = fuente.render("Score:",True,colores.NEGRO)#creo un texto

while running:

    lista_eventos = pygame.event.get()#guardo en una variable la lista de eventos de pygame
    for evento in lista_eventos:#recorro la lista de eventos
        if evento.type == pygame.QUIT:#pregunto si el evento es de tipo QUIT si es se cierra la ventana
            running = False
        if evento.type == pygame.MOUSEBUTTONDOWN:#pregunto si el evento es del tipo mause si lo es, se imprimen las cordenadas y se posiciona el circulo donde se haga click
            print(evento.pos)
            posicion_circulo = list(evento.pos)
        if evento.type == pygame.USEREVENT:#si es True el circulo se va a desplazar 10pixels hacia la derecha
            if evento.type == timer_seg:
                if posicion_circulo[0] < ANCHO_VENTANA + 80: 
                    posicion_circulo[0] = posicion_circulo[0] + 10#si se va de la ventana vuelve a su a salir por el otro
                else:
                    posicion_circulo[0] = -80
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_RIGHT:#si toco la flecha hacia la derecha baja 1 pixel
                posicion_circulo[1] = posicion_circulo[1] + 10
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                running = False                

    lista_teclas = pygame.key.get_pressed()
    if lista_teclas[pygame.K_LEFT]:
        posicion_circulo[1] = posicion_circulo[1] + 1

    ventana_principal.fill((colores.VERDE))#le digo que el color del fondo de la entana sea de un color, en esta caso rojo
    pygame.draw.circle(ventana_principal,colores.BLANCO,(posicion_circulo),80)#dibujo un circulo (cordenadas) radio
    pygame.draw.rect(ventana_principal,colores.NEGRO,(30,60,100,200))#dibujo un rectangulo (cordenadas, medidas)
    
    pygame.draw.rect(ventana_principal,colores.NEGRO,rec_homero)#dibujo un rectangulo (cordenadas, medidas)
    ventana_principal.blit(imagen_homero,rec_homero)#pongo la imagen en la ventana principal

    pygame.draw.rect(ventana_principal,colores.ROJO,rec_dona)#dibujo un rectangulo (cordenadas, medidas)
    ventana_principal.blit(imagen_dona,rec_dona)#pongo la imagen en la ventana principal

    ventana_principal.blit(texto,(0,0))


    pygame.display.flip()#le muestra los cambios al usuario

pygame.quit()#forma mas correcta de que se cierre el programa a nivel programacion

