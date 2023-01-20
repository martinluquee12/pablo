from data import lista_personajes
def guardar_superheroes_genero_m(lista:list)->list:
    '''
    Guarda en una nueva lista los nombres de los superheroes masculinos
    Recibe una lista de heroes.
    Retorna una nueva lista.
    '''
    lista_genero_m = []

    for personaje in lista:
        if personaje["genero"] == "M":
            lista_genero_m.append(personaje)

    return lista_genero_m

def guardar_superheroes_genero_f(lista:list)->list:
    '''
    Guarda en una nueva lista los nombres de los superheroes femeninos.
    Recibe una lista de heroes.
    Retorna una nueva lista.
    '''
    lista_genero_f = []

    for personaje in lista:
        if personaje["genero"] == "F":
            lista_genero_f.append(personaje)

    return lista_genero_f

def mostrar_superheroes_genero_m(lista_heroes:list):
    '''
    Muestra por consola los nombres de los superheroes genero masculino.
    Recibe la lista de heroes.
    '''
    lista_heroes = guardar_superheroes_genero_m(lista_heroes)

    for heroe in lista_heroes:
        print("Nombre: {0}".format(heroe["nombre"]))

def mostrar_superheroes_genero_f(lista_heroinas:list):
    '''
    Muestra por consola los nombres de los superheroes genero femenino.
    Recibe la lista de heroes.
    Devuelve una lista.
    '''

    lista_heroinas = guardar_superheroes_genero_f(lista_heroinas)

    for heroina in lista_heroinas:
        print("Nombre: {0}".format(heroina["nombre"]))
        
def calcular_maximo_minimo_m(lista_masculinos:list, tipo:str):
    '''
    Calcula el maximo/minimo de altura de masculino.
    Recibe la lista que se creo en la funcion: "guardar_superheroes_genero_m" y el tipo "maximo"/"minimo".
    '''
    lista_masculinos = guardar_superheroes_genero_m(lista_masculinos)
    altura_maxima_minima_m = lista_masculinos[0]

    for personaje in lista_masculinos:
        altura_maxima_minima_m["altura"] = float(altura_maxima_minima_m["altura"])
        personaje["altura"] = float(personaje["altura"])
        if tipo == "maximo" and personaje["altura"] > altura_maxima_minima_m["altura"]:
            altura_maxima_minima_m = personaje
        elif tipo == "minimo" and personaje["altura"] < altura_maxima_minima_m["altura"]:
            altura_maxima_minima_m = personaje
    
    print("Nombre: {0} | Altura: {1:.2f} cm".format(altura_maxima_minima_m["nombre"], altura_maxima_minima_m["altura"])) 

def calcular_maximo_minimo_f(lista_femenina:list, tipo:str):
    '''
    Calcula el maximo/minimo de altura de femenino.
    Recibe la lista que se creo en la funcion: "guardar_superheroes_genero_f" y el tipo "maximo"/"minimo".
    '''
    lista_femenina = guardar_superheroes_genero_f(lista_femenina)
    altura_maxima_minima_f = lista_femenina[0]

    for personaje in lista_femenina:
        altura_maxima_minima_f["altura"] = float(altura_maxima_minima_f["altura"])
        personaje["altura"] = float(personaje["altura"])
        if tipo == "maximo" and personaje["altura"] > altura_maxima_minima_f["altura"]:
            altura_maxima_minima_f = personaje
        elif tipo == "minimo" and personaje["altura"] < altura_maxima_minima_f["altura"]:
            altura_maxima_minima_f = personaje
    
   
    print("Nombre: {0} | Altura: {1:.2f} cm".format(altura_maxima_minima_f["nombre"], altura_maxima_minima_f["altura"]))

def calcular_promedio_altura_m_f(lista:list, tipo:str):
    '''
    Calcula el promedio de altura de los superheroes masculinos y femeninos.
    Recibe la lista de Superheroes y el tipo "M" o "F".
    '''

    if tipo == "M":
        lista_heroes = guardar_superheroes_genero_m(lista)

        acumulador_alturas_m = 0

        for personaje in lista_heroes:
            acumulador_alturas_m += float(personaje["altura"])

        print("Promedio altura Superheroes masculinos:\n{0:.2f} cm".format(acumulador_alturas_m/len(lista_heroes)))

    if tipo == "F":
        lista_heroinas = guardar_superheroes_genero_f(lista)

        acumulador_alturas_f = 0

        for personaje in lista_heroinas:
            acumulador_alturas_f += float(personaje["altura"])

        print("Promedio altura Superheroes femeninos:\n{0:.2f} cm".format(acumulador_alturas_f/len(lista_heroinas)))

def calcular_cantidad_tipo_ojos_pelo_inteligencia(lista:list, tipo:str):
    '''
    Calcula la cantidad de cada tipo de color de ojos, color de pelo e inteligencia que tienen los Superheroes.
    Recibe la lista de heroes.
    '''
    if tipo == "ojos":
        color_ojos = {}
        for superheroes in lista:
            color_ojos[superheroes["color_ojos"]] = 0

        for personaje in lista:
            color_ojos[personaje["color_ojos"]] += 1
        
        mensaje = "Hay {0} Superheroes con color de ojos 'Brown'. \nHay {1} Superheroes con color de ojos 'Blue'."
        mensaje += "\nHay {2} Superheroes con color de ojos 'Green'. \nHay {3} Superheroes con color de ojos 'Yellow (without irises)'."
        mensaje += "\nHay {4} Superheroes con color de ojos 'Hazel'. \nHay {5} Superheroes con color de ojos 'Yellow'."
        mensaje += "\nHay {6} Superheroes con color de ojos 'Silver'. \nHay {7} Superheroes con color de ojos 'Red'. "
        print(mensaje.format(   color_ojos["Brown"],
                                color_ojos["Blue"],
                                color_ojos["Green"],
                                color_ojos["Yellow (without irises)"],
                                color_ojos["Hazel"],
                                color_ojos["Yellow"],
                                color_ojos["Silver"],
                                color_ojos["Red"]))

    if tipo == "pelo":
        color_de_pelo = {} 
        for superheroes in lista:
            color_de_pelo[superheroes["color_pelo"]] = 0

        for personaje in lista: 
            color_de_pelo[personaje["color_pelo"]] += 1

        '''
        Si tuviera un valor "" en la clave "color_pelo"
        color_de_pelo = {}
        for superheroes in lista:
            if superheroes["color_pelo"] != "":
                color_de_pelo[superheroes["color_pelo"]] = 0

        for personaje in lista: 
            if personaje["color_pelo"] == "":
                color_de_pelo["No Hair"] += 1
            else: color_de_pelo[personaje["color_pelo"]] += 1
        '''
                
        mensaje = "Hay {0} Superheroes con el pelo de color 'Yellow'. \nHay {1} Superheroes con el pelo de color 'Brown'."
        mensaje += "\nHay {2} Superheroes con el pelo de color 'Black'. \nHay {3} Superheroes con el pelo de color 'Auburn'."
        mensaje += "\nHay {4} Superheroes con el pelo de color 'Red/Orange'. \nHay {5} Superheroes con el pelo de color 'White'."
        mensaje += "\nHay {6} Superheroes con el pelo de color 'Blond'. \nHay {7} Superheroes con el pelo de color 'Green'."
        mensaje += "\nHay {8} Superheroes con el pelo de color 'Red'. \nHay {9} Superheroes con el pelo de color 'Brown / White'."
        mensaje += "\nHay {10} Superheroes que no tienen pelo."
        print(mensaje.format(   color_de_pelo["Yellow"],
                                color_de_pelo["Brown"],
                                color_de_pelo["Black"],
                                color_de_pelo["Auburn"],
                                color_de_pelo["Red / Orange"],
                                color_de_pelo["White"],
                                color_de_pelo["Blond"],
                                color_de_pelo["Green"],
                                color_de_pelo["Red"],
                                color_de_pelo["Brown / White"],
                                color_de_pelo["No Hair"]))

    if tipo == "inteligencia":
        cantidad_iteligencia = {}
        for superheroes in lista:
            cantidad_iteligencia[superheroes["inteligencia"]] = 0

        for personaje in lista:
            cantidad_iteligencia[personaje["inteligencia"]] += 1
            
        cantidad_iteligencia["No tiene"] = cantidad_iteligencia.pop("")

        mensaje = "Hay {0} Superheroes con inteligencia 'Average'. \nHay {1} Superheroes con inteligencia 'Good'. "
        mensaje += "\nHay {2} Superheroes con inteligencia 'High'. \nHay {3} Superheroes sin inteligencia." 
        print(mensaje.format(   cantidad_iteligencia["average"],
                                cantidad_iteligencia["good"],
                                cantidad_iteligencia["high"],
                                cantidad_iteligencia["No tiene"]))

def agrupar_superheroes_por_ojos_pelo_inteligencia(lista: list, tipo:str):
    '''
    Agrupa los Superheroes por color de ojos, color de pelo e inteligencia y los muestra
    por consola agrupados.
    Recibe la lista de Superheroes y el tipo que puede ser "ojos", "pelo" e "inteligencia".
    '''
    if tipo == "ojos":
        diccionario_ojos = {}
        
        for personaje in lista:
            key = personaje["color_ojos"]
            if diccionario_ojos.get(key) == None:
                diccionario_ojos[key] = []

            diccionario_ojos[key].append(personaje)

        
        for key in diccionario_ojos:
            print("=========" + key + "=========")
            for personaje in diccionario_ojos[key]:
                print(personaje["nombre"])
            
    elif tipo == "pelo":
        diccionario_pelo = {}

        for personaje in lista:
            key = personaje["color_pelo"]
            if diccionario_pelo.get(key) == None:
                diccionario_pelo[key] = []

            diccionario_pelo[key].append(personaje)

        for key in diccionario_pelo:
            print("=========" + key + "=========")
            for personaje in diccionario_pelo[key]:
                print(personaje["nombre"])

    elif tipo == "inteligencia":
        diccionario_inteligencia = {}

        for personaje in lista:
            key = personaje["inteligencia"]
            if diccionario_inteligencia.get(key) == None:
                diccionario_inteligencia[key] = []
                

            diccionario_inteligencia[key].append(personaje)

        for key in diccionario_inteligencia:
            if key == "":
                print("=========No Tiene=========")
            else: print("=========" + key + "=========")
            for personaje in diccionario_inteligencia[key]:
                print(personaje["nombre"])
