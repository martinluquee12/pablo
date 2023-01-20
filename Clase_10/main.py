import funciones as f
'''
4  Calcular promedio de cualquier key numérica, filtrar los que cumplan con la condición de superar o no el promedio
(preguntar al usuario la condición: ‘menor’ o ‘mayor’) se deberá listar en consola aquellos que cumplan con ser mayores o menores según corresponda.

5   Buscar héroes por inteligencia [good, average, high] y listar en consola los que cumplan dicha búsqueda. (Usando RegEx)

6  Exportar a CSV la lista de héroes ordenada según opción elegida anteriormente [1-4]

Aclaraciones:
Los puntos deben ser accedidos mediante un menú. Para todas las opciones, validar lo ingresado por consola con RegEx
El set de datos proviene de un json
Realizar las validaciones que crea pertinentes
En todos los casos se deberá trabajar con una copia de la lista original

'''

lista_heroes = f.cargar_json(r"Primer Cuatrimestre/Clase_10/data_stark.json")

def menu_stark(lista:list):
    '''
    Muestra el menu al usuario.
    Recibe la lista de heroes.
    '''
    menu = "\nElija una opción: \n\n"
    menu += "1 - Listar un TOP N del menu. \n2 - Lista ordenada por altura. \n3 - Lita ordenada por fuerza. \n"
    menu += "4 - Calcular promedio. \n5 - Buscar Heroes por inteligencia. \n6 - Exportar a CSV. \n0 - Salir \n>"
    
    

    while True:
        respuesta = input(menu)
        match respuesta:
            case "1":
                top = input("Cantidad de Heroes a mostrar: >")
                top = f.validar_entero(top)
                if top:
                    if top < len(lista):
                        lista_final = f.mostrar_dato_crudo(lista[:top], "nombre")
                        f.mostrar_dato_formateado(lista[:top], "nombre")
                    else:
                        print("\nEl numero ingresado supera la cantidad de Heroes.\nSe muestran todos los heroes.\n")
                        top = len(lista)
                        lista_final = f.mostrar_dato_crudo(lista[:top], "nombre")
                        f.mostrar_dato_formateado(lista[:top], "nombre")
                else:
                    print("Error! Debe ingresar un numero.")
            case "2":
                orden = input('¿En que orden quiere ordenar la lista? "asc" para ascendeten o "desc" para descendente >' )
                f.validar_str("asc|desc", orden)
                if orden == "asc":
                    f.mostrar_dato_formateado(f.nahuel_sort_improve(lista, "altura" , "asc"), "altura")
                    lista_final = f.mostrar_dato_crudo(f.nahuel_sort_improve(lista, "altura" , "asc"), "altura")
                elif orden == "desc":
                    lista_final = f.mostrar_dato_crudo(f.nahuel_sort_improve(lista, "altura" , "desc"), "altura")
                    f.mostrar_dato_formateado(f.nahuel_sort_improve(lista, "altura" , "desc"), "altura")
                else:
                    print('Error! Ingrese "asc" o "desc"')
            case "3":
                orden = input('¿En que orden quiere ordenar la lista? "asc" para ascendeten o "desc" para descendente >' )
                f.validar_str("asc|desc", orden)
                if orden == "asc":
                    f.mostrar_dato_formateado(f.nahuel_sort_improve(lista, "fuerza" , "asc"), "fuerza")
                    lista_final = f.mostrar_dato_crudo(f.nahuel_sort_improve(lista, "fuerza" , "asc"), "fuerza")
                elif orden == "desc":
                    lista_final = f.mostrar_dato_crudo(f.nahuel_sort_improve(lista, "fuerza" , "desc"), "fuerza")
                    f.mostrar_dato_formateado(f.nahuel_sort_improve(lista, "fuerza" , "desc"), "fuerza")
                else:
                    print('Error! Ingrese "asc" o "desc"')
            case "4":
                promedio = input('¿Que promedio quiere calcular? "Altura", "Peso" o "Fuerza". >')
                f.validar_str("altura|peso|fuerza", promedio)
                orden = input('¿Quiere ver los heroes que superan el promedio o los que no lo superan? "Mayor" o "Menor" >')
                f.validar_str("mayor|menor", orden)

                if promedio == "altura":
                    f.calcular_promedio(lista, "altura")
                    if orden == "mayor":
                        f.mayor_menor_promedio(lista, "altura", "mayor")
                    elif orden == "menor":
                        f.mayor_menor_promedio(lista, "altura", "menor")
                elif promedio == "peso":
                    f.calcular_promedio(lista, "peso")
                    if orden == "mayor":
                        f.mayor_menor_promedio(lista, "altura", "mayor")
                    elif orden == "menor":
                        f.mayor_menor_promedio(lista, "altura", "menor")
                elif promedio == "fuerza":
                    f.calcular_promedio(lista, "fuerza")
                    if orden == "mayor":
                        f.mayor_menor_promedio(lista, "altura", "mayor")
                    elif orden == "menor":
                        f.mayor_menor_promedio(lista, "altura", "menor")
                else:
                    print('Error! Ingrese: Altura", "Peso" o "Fuerza".')

            case "5":
                pass
            case "6":
                nombre_archivo = input("¿Como quiere que se llame el archivo? >")
                f.exportar_csv(lista_final, nombre_archivo)
            case "0":
                break
            case _:
                print("Error!") 

                

menu_stark(lista_heroes)