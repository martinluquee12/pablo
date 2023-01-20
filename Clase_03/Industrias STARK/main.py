from data import lista_personajes
from stark_biblioteca import mostrar_nombre_altura_superheroes
from stark_biblioteca import mostrar_superheroe_mas_alto
from stark_biblioteca import mostrar_superheroe_mas_bajo
from stark_biblioteca import mostrar_superheroe_mas_pesado
from stark_biblioteca import mostrar_superheroe_menos_pesado
from stark_biblioteca import calcular_promedio_altura

def mostrar_menu():
    '''
    Muestra el mensaje del menu de la app.
    '''
    mensaje = "\nIngrese un numero: \n"
    mensaje += "\n1-Lista de Superheroes y su altura. \n2-Superheroe mas alto. \n3-Superheroe mas bajo."
    mensaje += "\n4-Promedio de altura de los Superheroes. \n5-Superheroe mas pesado. \n6-Superheroe menos pesado. \n0-Salir.\n\n> "

    respuesta = input(mensaje)

    return respuesta

def app_stark(lista:list):

    while True:
        respuesta = mostrar_menu()

        if respuesta == "1":
           mostrar_nombre_altura_superheroes(lista)
        elif respuesta == "2":
            mostrar_superheroe_mas_alto(lista)
        elif respuesta == "3":
            mostrar_superheroe_mas_bajo(lista)
        elif respuesta == "4":
            calcular_promedio_altura(lista)
        elif respuesta == "5":
            mostrar_superheroe_mas_pesado(lista)
        elif respuesta == "6":
            mostrar_superheroe_menos_pesado(lista)
        elif respuesta == "0":
            break
        
app_stark(lista_personajes)