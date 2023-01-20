import biblioteca as b

lista_paulina = b.cargar_json(r"Primer Cuatrimestre/Practica_parcial/data_paulina.json")

def menu_paulina(lista:list):
    '''
    Funcion principal donde se encuentra el menu para que el usuario elija diferentes opciones.
    Recibe la lista que se obtuvo de la carga del archivo json.
    '''

    menu = "\nElija una opción:\n\n1 - Listar TOP N videos.\n2 - Ordenar videos por duracion (UP/DOWN).\n"
    menu += "3 - Ordenar videos por cantidad de views (UP/DOWN).\n4 - Buscar videos por título.\n"
    menu += "5 - Exportar lista de videos a CSV.\n0 - Salir\n\n>"

    while True:

        respuesta = input(menu)

        match respuesta:

            case "1":
                top = input("\nCantidad de videos a mostrar: >")
                top = b.validar_int(top)

                if top != None:
                    if top < len(lista):
                        b.mostrar_dato(lista[:top])
                    elif top > len(lista):
                        print("\nEl numero ingresado supera la cantidad de videos. (Se mostraran todos los videos)")
                        top = len(lista)
                        b.mostrar_dato(lista[:top])
                else: 
                    print("Error! Debe ingresar un numero.")

            case "2":
                orden = input('¿En que orden quiere ordenar la lista? "UP" o "DOWN" >')
                orden_validado = b.validar_string("up|down", orden)

                if orden_validado != False:
                    if orden == "up":
                        b.mostrar_dato(b.nahuel_sort_improve(lista, "length", "up")) 
                    elif orden == "down":
                        b.mostrar_dato(b.nahuel_sort_improve(lista, "length", "down")) 
                else:
                    print('Error! Debe ingresar "UP" o "DOWN"')

            case "3":
                orden = input('¿En que orden quiere ordenar la lista? "UP" o "DOWN" >')
                orden_validado = b.validar_string("up|down", orden)

                if orden_validado != False:
                    if orden == "up":
                        b.mostrar_dato(b.nahuel_sort_improve(lista, "views", "up")) 
                    elif orden == "down":
                        b.mostrar_dato(b.nahuel_sort_improve(lista, "views", "down")) 
                else:
                    print('Error! Debe ingresar "UP" o "DOWN"')

            case "4":
                patron = input("Buscar: >")
                b.buscar(lista, patron)
            case "5":
                nombre_archivo = input("Nombre del archivo: >")
                b.exportar_csv(lista, nombre_archivo)

            case "0":
                break

            case _:
                print("Error! Opción no valida.")

menu_paulina(lista_paulina)
