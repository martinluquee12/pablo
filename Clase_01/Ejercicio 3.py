'''
Martin Luque DIV H

La división de alimentos de industrias Wayne está trabajando en un pequeño software
para cargar datos de heroínas y héroes, para para tener un control de las condiciones de heroes existentes, nos solicitan:
Nombre de Heroína/Héroe
EDAD (mayores a 18 años)
Sexo ("m", "f" o "nb")
Habilidad ("fuerza", "magia", "inteligencia").
A su vez, el programa deberá mostrar por consola lo siguiente:
a-Dar el nombre de Héroe | Heroína de 'fuerza' más joven.
b-El sexo y nombre de Heroe | Heroína de mayor edad.
c-La cantidad de Heroinas que tienen habilidades de 'fuerza' o 'magia'.
d-El promedio de edad entre Heroinas.
e-El promedio de edad entre Heroes de fuerza.
'''

contador_heroina_por_habilidad = 0
contador_heroinas = 0
acumulador_edades_heroinas = 0
contador_heroes_fuerza = 0
acumulador_edad_heroes_fuerza = 0

heroe_menor_edad = None
heroe_mayor_edad = None

respuesta = "s"

while(respuesta == "s"):
    nombre_heroe = input("Ingrese su nombre de Heroe/Heroina")

    while(True):
        edad = input("Ingrese su edad.")
        if(not edad.isnumeric()):
            print("Debe ingresar un numero.")
            continue
        edad = int(edad)
        if(edad > 18):
            break
        print("Debes tener mas de 18 años.")
    
    genero = input("Ingrese su enero: 'M' para masculino, 'F' para femenino o 'NB' para no binario.")
    while(genero.lower() != "m" and genero.lower() != "f" and genero.lower() != "nb"):
        genero = input("Error! Ingrese un genero valido: 'M' para masculino, 'F' para femenino o 'NB' para no binario.")
    
    habilidad = input("¿Que habilidad tiene: Fuerza, Magia o Inteligencia?")
    while(habilidad.lower() != "fuerza" and habilidad.lower() != "magia" and habilidad.lower() != "inteligencia"):
        habilidad = input("Error! Ingrese una habildiad valida: Fuerza, Magia o Inteligencia?")

    if(habilidad == "Fuerza"):
        if(genero == "M"):
            acumulador_edad_heroes_fuerza += edad
            contador_heroes_fuerza += 1

        if(heroe_menor_edad == None or edad < heroe_menor_edad):
            heroe_menor_edad = edad
            nombre_heroe_menor_edad = nombre_heroe
    
    if(heroe_mayor_edad == None or edad > heroe_mayor_edad):
        heroe_mayor_edad = edad
        genero_heroe_mayor_edad = genero
        nombre_heroe_mayor_edad = nombre_heroe
    
    if(genero == "F"):
        acumulador_edades_heroinas += edad
        contador_heroinas += 1
        if(habilidad == "Fuerza" or habilidad == "Magia"):
            contador_heroina_por_habilidad += 1

    
    respuesta = input("¿Quiere seguir Ingresando Heroes?")

promedio_edad_heroinas = acumulador_edades_heroinas / contador_heroinas
promedio_edad_heroes_fuerza = acumulador_edad_heroes_fuerza / contador_heroes_fuerza

print("\nEl Heroe/Heroina mas joven con la habilidad 'Fuerza' es", nombre_heroe_menor_edad,"\n")
print("El Heroe/Heroina de mayor edad es", nombre_heroe_mayor_edad, "y su genero es",genero_heroe_mayor_edad,"\n")
print("Hay", contador_heroina_por_habilidad," Heroinas con la habilidad 'Fuerza' y/o 'Magia'","\n")
if(contador_heroinas > 0):
    print("El promedio de edad entre las Heroinas es", promedio_edad_heroinas,"\n")
if(contador_heroes_fuerza > 0):
    print("EL promedio de edad entre los Heroes con la habilidad 'Fuerza es'", promedio_edad_heroes_fuerza)

