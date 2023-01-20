from functools import reduce
import random

lista_palabras = [
    "Goku", "Vegeta", "Freezer", "Cell", "Beerus", 'Krillin'
]

# Refactoprizar la funcion clasica usando lambda
def sup_triangulo(base: int, altura: int) -> float:
    return (base*altura)/2

#LA FUNCION "sup_triangulo" ES EQUIVALENTE A ESTA LINEA DE CODIGO
superficie = lambda base, altura : (base*altura)/2
print(superficie (5,10))


# Refactorizar la funcion clasica usando lambda y map
def aplicar_mayusculas(lista_palabras: list) -> list:
    for i in range(len(lista_palabras)):
        lista_palabras[i] = lista_palabras[i].upper()
    return lista_palabras

#LA FUNCION "aplicar_mayusculas" es equivalente a esta linea de codigo
mayusculas = list(map(str.upper, lista_palabras))
print(mayusculas)


# Refactorizar la funcion usando lambda y reduce
def obtener_mas_letras(lista: list) -> str:
    seleccionado = ''
    for palabra in lista:
        if len(palabra) > len(seleccionado):
            seleccionado = palabra
    return seleccionado

#LA FUNCION "obtener_mas_letras" es equivalente a estas lineas de codigo
comparar_palabra_mas_larga = lambda palabra1, palabra2 : palabra1 if len(palabra1) > len(palabra2) else palabra2
palabra_mas_larga = reduce(comparar_palabra_mas_larga, lista_palabras)
print(palabra_mas_larga)


# refactorizar la funcion usando lambda y filter
def obtener_nombres_cantidad_letras(lista: list, cantidad: int) -> list:
    seleccionados = list()
    for palabra in lista:
        if len(palabra) == cantidad:
            seleccionados.insert(0, palabra)
    return seleccionados

#LA FUNCION "obtener_nombres_cantidad_letras" es equivalente a estas lineas de codigo
def cantidad_letras(lista:list, cantidad:int):
    palabra = lambda letras: len(letras) == cantidad 
    lista_filtrada = list(filter(palabra, lista))
    return lista_filtrada

cantidad_le = input("Cantidad: ")
print(cantidad_letras(lista_palabras, int(cantidad_le)))


# refactorizar usando shuffle
def ordenar_random_lista(lista: list) -> list:
    maximo = len(lista)
    desordenada = list()
    while len(desordenada) < len(lista):
        indice = random.randint(0, maximo)
        for elemento in lista:
            desordenada.insert(indice, elemento)
    return desordenada

#LA FUNCION "ordenar_random_lista" es equivalente a esta linea de codigo
random.shuffle(lista_palabras)
print(lista_palabras)


# Refactorizar usando sort y lamda
def ordenar_burbujeo(lista: list) -> list:
    lista_copia = lista.copy()
    for i in range(len(lista_copia)-1):
        for j in range(i+1, len(lista_copia)):
            if lista_copia[i] > lista_copia[j]:
                lista_copia[i], lista_copia[j] = lista_copia[j], lista_copia[i]
    return lista_copia

#LA FUNCION "ordenar_burbujeo" es equivalente a esta linea de codigo
lista_palabras.sort()
print(lista_palabras)


heroes = [
    "goKU", "vEgETa", 'kriLLin'
]

villanos = [
    "FreEzeR", "CELl", "Majin Buu"
]

ataques = [
    "Kame hame ha", "Final flash", "Kienzan"
]

# Refactorizar usando zip
for ind_h in range(len(heroes)):
    for ind_a in range(ind_h, len(ataques)):
        for ind_v in range(ind_h, len(villanos)):
            mensaje =\
                f"""
                {heroes[ind_h].capitalize()}
                Lanza un {ataques[ind_a].capitalize()}
                a {villanos[ind_v].capitalize()}
                """
            print(mensaje)
            break
        break

#LAS LINEAS DE CODIGO 102 A 113 es equivalente a estas lineas de codigo
for heroe, ataque, villano in zip(heroes, ataques, villanos):
    print(heroe.capitalize(),"\nLanza un", ataque.capitalize(),"\na",villano.capitalize(),"\n")
    