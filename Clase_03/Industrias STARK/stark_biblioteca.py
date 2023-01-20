def mostrar_nombre_altura_superheroes(lista:list)->dict:
    '''
    Muestra los nombres de los Superheroes y le agrega su altura formateada.
    Recibe la lista de heroes.
    Devuelve un diccionario con cada heroe y su altura.
    '''

    for personaje in lista:
        print("Nombre: {0} | Altura: {1} cm \n".format(personaje["nombre"], float(personaje["altura"])))
        
def calcular_maximo_minimo_altura_peso(lista:list, tipo:str, dato:str)->dict:

    maximo_minimo = lista[0]

    for personaje in lista:

        if tipo == "maximo" and float(personaje[dato]) > float(maximo_minimo[dato]):
            maximo_minimo = personaje

        elif tipo == "minimo" and float(personaje[dato]) < float(maximo_minimo[dato]):
            maximo_minimo = personaje

    if dato == "altura":
        print("Nombre: {0} | Altura: {1} cm".format(maximo_minimo["nombre"], float(maximo_minimo[dato])))
    elif dato == "peso":
        print("Nombre: {0} | Peso: {1} kg".format(maximo_minimo["nombre"], float(maximo_minimo[dato])))

def mostrar_superheroe_mas_alto(lista:list)->dict:
    '''
    Muestra en consola el superheroe mas alto.
    Recibe una lista de heroes.
    Retorna un diccionario.
    '''
    calcular_maximo_minimo_altura_peso(lista, "maximo", "altura")

def mostrar_superheroe_mas_bajo(lista:list)->dict:
    '''
    Muestra en consola el superheroe mas bajo.
    Recibe una lista de heroes.
    Retorna un diccionario.
    '''
    calcular_maximo_minimo_altura_peso(lista, "minimo", "altura")

def calcular_promedio_altura(lista:list)->float:
    '''
    Calcula el promedio de alturas de los heroes que estan en la lista de heroes.
    Recibe la lista de heroes.
    Devuelve un flotante que equivale a la suma de todas las alturas dividido la longitud de la lista.
    '''
    acumulador_altura = 0

    for personaje in lista:
        acumulador_altura += float(personaje["altura"])

    print("Promedio de altura de los Superheroes: {0:.2f} cm".format(acumulador_altura/len(lista)))

def mostrar_superheroe_mas_pesado(lista:list)->dict:
    '''
    Muestra en consola el superheroe mas pesado.
    Recibe una lista de heroes.
    Retorna un diccionario.
    '''
    calcular_maximo_minimo_altura_peso(lista, "maximo", "peso")

def mostrar_superheroe_menos_pesado(lista:list)->dict:
    '''
    Muestra en consola el superheroe memos pesado.
    Recibe una lista de heroes.
    Retorna un diccionario.
    '''
    calcular_maximo_minimo_altura_peso(lista, "minimo", "peso")
