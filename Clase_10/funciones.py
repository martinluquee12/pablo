import csv
import json
import re

def cargar_json(path:str)->list:
    '''
    Carga el achivo json.
    Recibe el path (ruta del archivo .json)
    Devuelve la lista de diccionarios que contiene el json.
    '''

    with open(path, "r") as file:
        dato = json.load(file)
    return dato["heroes"]

def validar_entero(int_ingresado:str)->int:
    '''
    Valida con RegEx que lo que el usuario ingresa sea un numero y lo castea.
    Recibe el numero que el usuario ingreso.
    Devuelve el numero casteado o False en caso de que no se alla ingresado un numero.
    '''

    numero_validado = re.match("^[0-9]+$", int_ingresado)

    if numero_validado != None:
        
        return int(int_ingresado)
    else:
        return False

def validar_str(respuesta:str, patron:str)->str|bool:
    '''
    Valida con RegEx que el usuario alla ingresado el patron correcto.
    Recibe lo que el usuario ingresa por consola y el patron a validar.
    Devuelve el str que el usuario ingreso validado o False.
    '''

    respuesa_validada = re.search(patron, respuesta, re.IGNORECASE)

    if respuesa_validada != None:
        return respuesta
    else:
        return False

def mostrar_dato_crudo(lista:list, key:str)->list:
    '''
    Imprime los datos crudo para guardarlos en una variable.
    Recibe la lista de heroes y la key que indica que dato va a guardar.
    Devulve una nueva lista.
    '''
    mensaje = ""
    for heroe in lista:
        if key == "nombre":
            mensaje += "{0}\n".format(heroe["nombre"])
        elif key == "altura":
            mensaje += "{0}, {1}\n".format(heroe["nombre"], heroe["altura"])
        elif key == "fuerza":
            mensaje += "{0}, {1}\n".format(heroe["nombre"], heroe["fuerza"])
    return mensaje

def mostrar_dato_formateado(lista:list, key:str):
    '''
    Imprime los datos por pantalla.
    Recibe la lista de heroes y la key que indica que mensaje se muestra.
    '''
    for heroe in lista:
        print("*--------------------*")
        if key == "nombre":
            print("Nombre: {0}\n".format(heroe["nombre"]))
        elif key == "altura":
            print("Nombre: {0} | Altura: {1}cm\n".format(heroe["nombre"], heroe["altura"]))
        elif key == "fuerza":
            print("Nombre: {0} | Fuerza: {1}\n".format(heroe["nombre"], heroe["fuerza"]))
    
def buscar_min_max(lista:list, key:str, order:str)->int:
    '''
    Busca el maximo/minimo, segun el roder que se pase, de una lista del dato que se pase por la key.
    Recibe la lista de heroes, la key de tipo int y el order "asc"/"desc"
    Devuelve el indice donde se encuentra el dato encontrado o -1 en caso de error.
    '''

    if len(lista) > 0:

        index_min_max = 0

        for i in range(len(lista)):
            if order == "asc" and lista[i][key] < lista[index_min_max][key]:
                index_min_max = i
            elif order == "desc" and lista[i][key] > lista[index_min_max][key]:
                index_min_max = i
            
        return index_min_max
    else:
        return -1

def nahuel_sort_improve(lista:list, key:str, order:str)->list:
    '''
    Se crea una copia de la lista original y a partir de la funcion "buscar_min_max" 
    al encontrar el minimo/maximo lo compara, en la primer vuelta con el primer indice de la lista copiada,
    al encontrar el indice minimo/maximo lo swapea y va ordenando a medida que el for itere el indice + 1
    Recibe la lista, la key para saber que dato calcular y el orden en que lo quiere ordenar.
    Devuelve iuna nueva lista pordenada.
    '''
    lista_ordenada = lista.copy()
    if len(lista_ordenada) > 0:

        for i in range(len(lista_ordenada)):
            index_min_max = buscar_min_max(lista_ordenada[i:],key,order) + i
            lista_ordenada[i], lista_ordenada[index_min_max] = lista_ordenada[index_min_max], lista_ordenada[i]
    return lista_ordenada

def calcular_promedio(lista:list, key:str)->float:
    '''
    Calcula el promedio de cualquier key numerica.
    Recibe la lista de heroes y la key para calcular.
    Devuelve un flotante.
    '''
    
    if len(lista) > 0:
        acumulador_key = 0

        for heroe in lista:
            acumulador_key += heroe[key]
        promedio = acumulador_key / len(lista)
    
        if key == "altura":
            print("Promedio altura: {0:.2f}cm".format(promedio))
        if key == "peso":
            print("Promedio pesos: {0:.2f}kg".format(promedio))
        if key == "fuerza":
            print("Promedio fuerza: {0:.2f}".format(promedio))

    return promedio

def mayor_menor_promedio(lista:list, key:str, orden:str)->list:
    '''
     lista_promedio = []

        if orden == "mayor":
            for heroe in lista:
                if heroe[key] > promedio:
                    lista_promedio.append(heroe["nombre"])
                    print("*--------------------------*")
                    if key == "altura":
                        print("Nombre: {0} | Altura: {1}cm".format(heroe["nombre"], heroe["altura"]))
                    elif key == "peso":
                        print("Nombre: {0} | Altura: {1}kg".format(heroe["nombre"], heroe["peso"]))
                    elif key == "fuerza":
                        print("Nombre: {0} | Altura: {1}".format(heroe["nombre"], heroe["fuerza"]))

        elif orden == "menor":
            for heroe in lista:
                if heroe[key] < promedio:
                    lista_promedio.append(heroe["nombre"])
                    print("*--------------------------*")
                    if key == "altura":
                        print("Nombre: {0} | Altura: {1}cm".format(heroe["nombre"], heroe["altura"]))
                    elif key == "peso":
                        print("Nombre: {0} | Peso: {1}kg".format(heroe["nombre"], heroe["peso"]))
                    elif key == "fuerza":
                        print("Nombre: {0} | Fuerza: {1}".format(heroe["nombre"], heroe["fuerza"]))
    ''' 
    retorno = -1

    if orden == "mayor":
        promedio = calcular_promedio(lista, key)
        for heroe in lista:
            if heroe[key] > promedio:
                if key == "altura":
                    retorno = mostrar_dato_crudo(lista, "altura")
                elif key == "peso":
                    retorno = mostrar_dato_crudo(lista, "peso")
                elif key == "fuerza":
                    retorno = mostrar_dato_crudo(lista, "fuerza")

    elif orden == "menor":
        for heroe in lista:
            if heroe[key] < promedio:
                if key == "altura":
                    retorno = mostrar_dato_formateado(lista, "altura")
                elif key == "peso":
                    retorno = mostrar_dato_formateado(lista, "peso")
                elif key == "fuerza":
                    retorno = mostrar_dato_formateado(lista, "fuerza")
    return retorno



def exportar_csv(lista:list, nombre_archivo:str)->csv:
    '''
    Exporta la lista que se le pase por parametro a un archivo .csv
    Recibe la lista y el nombre del archivo.
    Devuelve un archivo csv.
    '''
    nombre_final = nombre_archivo + ".csv"
    with open(nombre_final, "w") as file:
        
        file.write(lista)
    