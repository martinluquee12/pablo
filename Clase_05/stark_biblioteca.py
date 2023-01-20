from data import lista_personajes

def stark_normalizar_datos(lista_heroes:list)->str:
    '''
    Normaliza los datos, si tengo un dato que deberia ser de tipo int y es de tipo str, lo convierte a int.
    Recibe la lista de heroes de tipo list.
    Devuelve un str, 'Dato normalizado' si al menos un dato fue casteado, 'Error: Lista de héroes vacía'
     si la lista esta vacia.
    '''
    retorno = "Error: Lista de héroes vacía"
    
    if len(lista_heroes) > 0:
        for clave in lista_heroes:
            if type(clave["altura"]) != type(int) :
                clave["altura"] = float(clave["altura"])
                clave["peso"] = float(clave["peso"])
                clave["fuerza"] = float(clave["fuerza"])
        retorno = "Dato normalizado."

    return retorno

def mostrar_resultado(lista):

    print(stark_normalizar_datos(lista)) 

def obtener_nombre(dict_heroe:dict):

    for personaje in dict_heroe:
        print("Nombre: {0}".format(personaje["nombre"]))
   
def impirmir_dato(heroe:str):

    obtener_nombre(heroe)

def stark_imprimir_nombres_heroes(lista_heroes:list):

    retorno = -1

    if len(lista_heroes) > 0:
        impirmir_dato(lista_heroes)
    else:
        print(retorno)
        
def obtener_nombre_y_dato(lista_heroe :dict, key:str)->str:


    for personaje in lista_heroe:

        if personaje[key] == "identidad":
            heroe = ("Nombre: {0} | Identidad: {1}".format(personaje["nombre"],personaje["identidad"]))
        elif personaje[key] == "empresa":
            heroe = ("Nombre: {0} | Empresa: {1}".format(personaje["nombre"],personaje["empresa"]))
        elif personaje[key] == "altura":
            heroe = ("Nombre: {0} | Altura: {1} cm".format(personaje["nombre"],personaje["altura"]))
        elif personaje[key] == "peso":
            heroe = ("Nombre: {0} | Peso: {1} kg".format(personaje["nombre"],personaje["peso"]))
        elif personaje[key] == "genero":
            heroe = ("Nombre: {0} | Genero: {1}".format(personaje["nombre"],personaje["genero"]))
        elif personaje[key] == "color_ojos":
            heroe = ("Nombre: {0} | Color de ojos: {1}".format(personaje["nombre"],personaje["color_ojos"]))
        elif personaje[key] == "color_pelo":
            heroe = ("Nombre: {0} | Color de pelo: {1}".format(personaje["nombre"],personaje["color_pelo"]))
        elif personaje[key] == "fuerza":
            heroe = ("Nombre: {0} | Fuerza: {1}".format(personaje["nombre"],personaje["fuerza"]))
        elif personaje[key] == "inteligencia":
            heroe = ("Nombre: {0} | Inteligencia: {1}".format(personaje["nombre"],personaje["inteligencia"]))
        
    return heroe

def stark_impirmir_nombres_alturas(lista_heroes:list):

    if len(lista_heroes) > 0:
        obtener_nombre_y_dato(lista_heroes, "altura")
    else:
        print("-1")

def calcular_maximo(lista_heroe:list, key:str):

    maximo = lista_heroe[0]

    for personaje in lista_heroe:
        if float(personaje[key]) >= float(maximo[key]):
            maximo = personaje
    
    return(maximo["nombre"], maximo[key]) 

def calcular_minimo(lista_heroe:list, key:str):

    minimo = lista_heroe[0]

    for personaje in lista_heroe:
        if float(personaje[key]) <= float(minimo[key]):
            minimo = personaje

    return(minimo["nombre"], minimo[key])     
    
def calcular_max_min_dato(lista_heroes:list, tipo:str, key:str):

    if tipo == "maximo":
        print(calcular_maximo(lista_heroes, key ))
    

def stark_calcular_imprimir_heroe(lista_heroe:list, tipo:str, key:str):

   pass




def calcular_promedio_altura():

    acumulador_alturas = 0

    for superheroe in lista_personajes:
        superheroe["altura"] = float(superheroe["altura"])
        acumulador_alturas += superheroe["altura"]

    print("Promedio de altura:{0:.2f} cm\n".format(acumulador_alturas/len(lista_personajes)))

def calcular_superheroe_mas_pesado():

    superheroe_mas_pesado = lista_personajes[0]

    for superheroe in lista_personajes:
        superheroe["peso"] = float(superheroe["peso"])
        if(superheroe["peso"] > superheroe_mas_pesado["peso"]):
            superheroe_mas_pesado = superheroe

    print("Nombre: {0} \nPeso: {1:.2f} Kg\n".format(superheroe_mas_pesado["nombre"], superheroe_mas_pesado["peso"]))

def calcular_superheroe_menos_pesado():

    superheroe_menos_pesado = lista_personajes[0]

    for superheroe in lista_personajes:
        superheroe["peso"] = float(superheroe["peso"])
        if(superheroe["peso"] < superheroe_menos_pesado["peso"]):
            superheroe_menos_pesado = superheroe
    print("Nombre: {0} \nPeso: {1:.2f} kg\n".format(superheroe_menos_pesado["nombre"], superheroe_menos_pesado["peso"]))
