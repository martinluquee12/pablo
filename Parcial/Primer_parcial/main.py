'''
1 - Listar los personajes ordenados por altura
2 - Mostrar el personaje mas alto de cada genero
3 - Ordenar los personajes por peso
4 - Armar un buscador de personajes 
5 - Exportar lista personajes a CSV
6 - Salir
'''
import funciones as f

def starwars_app():
    lista_personajes = f.cargar_json(r"Primer Cuatrimestre/Primer_parcial/data.json")
    while(True):
        print("\n1 - Listar los personajes ordenados por altura\n2 - Mostrar el personaje mas alto de cada genero\n3 - Ordenar los personajes por peso\n4 - Armar un buscador de personajes\n5 - Exportar lista personajes a CSV\n6 - Salir\n")
        respuesta = input()
        if(respuesta=="1"):
            lista_final = f.mostrar_dato_crudo(f.nahuel_sort_improve(lista_personajes, "height", "max"))
            f.mostrar_dato(f.nahuel_sort_improve(lista_personajes, "height", "max"))
        elif(respuesta=="2"):
            f.mas_alto_genero(lista_personajes)
        elif(respuesta=="3"):
            lista_final = f.mostrar_dato_crudo(f.nahuel_sort_improve(lista_personajes, "mass", "max"))
            f.mostrar_dato(f.nahuel_sort_improve(lista_personajes, "mass", "max"))
        elif(respuesta=="4"):
            patron = input("Buscar: ")
            f.buscador(lista_personajes, patron)
        elif(respuesta=="5"):
            nombre_archivo = input("Nombre para el archivo: ")
            f.exportar_csv(lista_final , nombre_archivo)
        elif(respuesta=="6"):
            break


starwars_app()