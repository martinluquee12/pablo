from data import lista_personajes
import func 

'''
M-Listar todos los superhéroes agrupados por color de ojos.
N-Listar todos los superhéroes agrupados por color de pelo.f
O-Listar todos los superhéroes agrupados por tipo de inteligencia

'''
def mostrar_menu_app()->str:
    '''
    Muestra el mensaje del menu de la app.
    Devuelve un str.
    '''

    mensaje = """\nElija una opción: \n\n
    1-Nombres de Superheroes masculinos.
    2-Nombres de Superheroes femeninos.
    3-Superheroe masculino mas alto.
    4-Superheroe femenino mas alto.
    5-Superheroe masculino mas bajo.
    6-Superheroe femenino mas bajo.
    7-Promedio altura Superheroes genero masculino.
    8-Promedio altura Superheroes genero femenino.
    9-Cantidad de tipos de color de ojos.
    10-Cantidad de tipos de color de pelo
    11-Cantidad de tipos de inteligencias.
    12-Nombre de los heroes por color de ojos.
    13-Nombre de los heroes por color de pelo.
    14-Nombre de los heroes por inteligencia.
    0-Salir.\n\n    >"""
    respuesta = input(mensaje)

    return respuesta

def app_stark(lista:list):

    while True:

        respuesta = mostrar_menu_app()

        if respuesta == "1":
            func.mostrar_superheroes_genero_m(lista)
        elif respuesta == "2":
            func.mostrar_superheroes_genero_f(lista)
        elif respuesta == "3":
            func.calcular_maximo_minimo_m(lista, "maximo")
        elif respuesta == "4":
            func.calcular_maximo_minimo_f(lista, "maximo")
        elif respuesta == "5":
            func.calcular_maximo_minimo_m(lista, "minimo")
        elif respuesta == "6":
            func.calcular_maximo_minimo_f(lista, "minimo")
        elif respuesta == "7":
            func.calcular_promedio_altura_m_f(lista, "M")
        elif respuesta == "8":
            func.calcular_promedio_altura_m_f(lista, "F")
        elif respuesta == "9":
            func.calcular_cantidad_tipo_ojos_pelo_inteligencia(lista, "ojos")
        elif respuesta == "10":
            func.calcular_cantidad_tipo_ojos_pelo_inteligencia(lista, "pelo")
        elif respuesta == "11":
            func.calcular_cantidad_tipo_ojos_pelo_inteligencia(lista, "inteligencia")
        elif respuesta == "12":
            func.agrupar_superheroes_por_ojos_pelo_inteligencia(lista, "ojos")
        elif respuesta == "13":
            func.agrupar_superheroes_por_ojos_pelo_inteligencia(lista, "pelo")
        elif respuesta == "14":
            func.agrupar_superheroes_por_ojos_pelo_inteligencia(lista, "inteligencia")
        elif respuesta == "0":
            break

app_stark(lista_personajes)