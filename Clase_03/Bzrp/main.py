from data import lista_bzrp
from bzrp_biblioteca import mostrar_lista_videos
from bzrp_biblioteca import mostrar_maximo_vistas
from bzrp_biblioteca import mostrar_minimo_vista
from bzrp_biblioteca import mostrar_maximo_duracion
from bzrp_biblioteca import mostrar_minimo_duracion
from bzrp_biblioteca import calcular_promedio_vistas_duracion

'''
1-Lista de videos.
2-Video mas vistio.
3-Video menos visto.
4-Video mayor duracion.
5-Video menor duracion.
6-Promedio de duracion de los videos.
7-Promedio de vistas.
'''
def mostrar_menu():
    '''
    Muestra el mensaje del menu de la aplicacion.
    '''

    mensaje = "\n1-Mostrar lista de videos. \n2-Video mas visto. \n3-Video menos visto."
    mensaje += "\n4-Video mas largo. \n5-Video mas corto. \n6-Promedio de duracion de videos."
    mensaje += "\n7-Promedio de vistas. \n0-Salir.\n\n>"   

    respuesta = input(mensaje)

    return respuesta

def app_bzrp(lista:list):

    while True:
        respuesta = mostrar_menu()

        if respuesta == "1":
            mostrar_lista_videos(lista)
        elif respuesta == "2":  
            mostrar_maximo_vistas(lista)
        elif respuesta == "3":  
            mostrar_minimo_vista(lista)
        elif respuesta == "4":  
            mostrar_maximo_duracion(lista)
        elif respuesta == "5":  
            mostrar_minimo_duracion(lista)
        elif respuesta == "6":  
            calcular_promedio_vistas_duracion(lista, "length")
        elif respuesta == "7":  
            calcular_promedio_vistas_duracion(lista, "views")
        elif respuesta == "0":
            break

app_bzrp(lista_bzrp)