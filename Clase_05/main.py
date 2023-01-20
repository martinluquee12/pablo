from data import lista_personajes
#from stark_biblioteca import calcular_superheroe_mas_alto
#from stark_biblioteca import calcular_superheroe_mas_bajo
from stark_biblioteca import calcular_promedio_altura
from stark_biblioteca import calcular_superheroe_mas_pesado
from stark_biblioteca import calcular_superheroe_menos_pesado
from stark_biblioteca import mostrar_resultado
from stark_biblioteca import stark_imprimir_nombres_heroes
from stark_biblioteca import stark_impirmir_nombres_alturas
from stark_biblioteca import stark_calcular_imprimir_heroe

'''
    Recorrer la lista imprimiendo por consola el nombre de cada superhéroe
    Recorrer la lista imprimiendo por consola nombre de cada superhéroe junto a la altura del mismo
    Recorrer la lista y determinar cuál es el superhéroe más alto (MÁXIMO)
    Recorrer la lista y determinar cuál es el superhéroe más bajo (MÍNIMO)
    Recorrer la lista y determinar la altura promedio de los  superhéroes (PROMEDIO)
    Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (MÁXIMO, MÍNIMO)
    Calcular e informar cual es el superhéroe más y menos pesado.
    
'''
def app_stark(lista:list):

    while(True):
        mensaje = "\n1-Normalizar datos. \n2-Lista de superheroes. \n3-Lista de superheroes y su altura."
        mensaje += "\n4-Superheroe mas alto. \n5-Superheroe mas bajo. \n6-Promedio de altura. \n7-Superheroe mas pesado."
        mensaje += "\n8-Superheroe menos pesado.\n0-Salir.\n\n"
        respuesta = input(mensaje)

        if respuesta == "1":
            mostrar_resultado(lista)
        elif(respuesta == "2"):
            stark_imprimir_nombres_heroes(lista)
        elif(respuesta == "3"):
            stark_impirmir_nombres_alturas(lista)
        elif(respuesta == "4"):
            stark_calcular_imprimir_heroe(lista, "maximo", "fuerza")
        elif(respuesta == "5"):
            calcular_promedio_altura()
        elif(respuesta == "6"):
            calcular_superheroe_mas_pesado()
        elif(respuesta == "7"):
            calcular_superheroe_menos_pesado()
        elif respuesta == "8":
            break

app_stark(lista_personajes)