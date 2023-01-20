
lista_palabras = [
    "goKU", "vEgETa", "FrIEzA", "CELl", "BeERuS", 'kriLLin'
]

# Refactorizar a la version clasica de la funcion
superficie_circulo = lambda x: pow(x, 2) * 3.1415
print(f'Superficie de circulo: {round(superficie_circulo(15), 2)}')


# Refactorizar a la version clasica
minisculizar = lambda x: str(x).lower()
print(f'Lista Minuscula: {minisculizar(lista_palabras)}')

# Refactorizar a la version clasica
capitalizar = lambda x: str(x).capitalize()
lista_mapeada = list(map(capitalizar, lista_palabras))
print(f'Lista Capitalizada: {lista_mapeada}')

heroes = [
    "goKU", "vEgETa", 'kriLLin'
]

villanos = [
    "FrIEzA", "CELl", "Majin Buu"
]

ataques = [
    "Kame hame ha", "Final flash", "Kienzan"
]

for heroe, ataque, villano in zip(heroes, ataques, villanos):
    print(f'{heroe.capitalize()} Lanza un {ataque.capitalize()} a {villano.capitalize()}')