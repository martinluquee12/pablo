import json
import re

def parse_json(nombre_archivo:str)-> list:

    dic_json = {}

    with open(nombre_archivo, "r") as archivo:
      dic_json = json.load(archivo)
    return dic_json["heroes"]

lista_heroes = parse_json('/home/martinluque/Escritorio/Laboratorio y Programacion 1/Primer Cuatrimestre/Clase_08/data_stark.json')

def imprimir_dato(mensaje:str):
    
    print(mensaje)
    
def impirmir_menu_desafio_5():

    imprimir_dato("\nA-Lista de superheroes masculinos. \nB-Lista de superheroes femeninos. \nC-Superheroe masculino mas alto.\nD-Superheroe femenino mas alto. \nE-Superheroe masculino mas bajo. \nF-Superheroe femenino mas bajo.\nG-Promedio alturas superheroes genero masculinos. \nH-Promedio alturas superheroes genero femeninos.")
        
def stark_menu_principal_desafio_5():

    impirmir_menu_desafio_5()

    respuesta = input("\n>")
    resultado = ""
    if re.search("[a-ozA-OZ]", respuesta) == None:
        resultado = -1
    else:
        resultado = respuesta

    return resultado

def stark_marvel_app_5(lista_personajes:list):

    

    while True:
        respuesta = stark_menu_principal_desafio_5()

        if respuesta != -1:
            imprimir_dato("Error!")
            respuesta.lower()
        else:
            continue

        if respuesta == "A":
            print(respuesta)
        elif respuesta == "B":
            pass
        elif respuesta == "C":
            pass
        elif respuesta == "D":
            pass
        elif respuesta == "E":
            pass
        elif respuesta == "F":
            pass
        elif respuesta == "G":
            pass
        elif respuesta == "H":
            pass
        elif respuesta == "I":
            pass
        elif respuesta == "J":
            pass
        elif respuesta == "K":
            pass
        elif respuesta == "L":
            pass
        elif respuesta == "M":
            pass
        elif respuesta == "N":
            pass
        elif respuesta == "O":
            pass





stark_marvel_app_5(lista_heroes)