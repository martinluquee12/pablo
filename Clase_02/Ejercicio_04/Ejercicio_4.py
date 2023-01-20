'''
Martin Luque Ejercicio 04
Preparando todo para reclutar héroes y heroínas para la liga de la justicia, 
el departamento de HR dispone de una larga lista de justicieros pero solo tiene información detallada de algunos de ellos.
Es por eso que te piden que desarrolles un pequeño programa el cual basado en la lista 'heroes_para_reclutar' 
busque en el diccionario 'heroes_info' los que coincidan y los guarde en un nuevo diccionario para luego imprimir por consola
todos sus datos. (id, origen, etc)
TIP: Las habilidades están repetidas, busca la manera de que en el resultado final no existan duplicados,
que usarías para eso?
'''
from data import heroes_para_reclutar
from data import heroes_info

heroes_reclutados = {}

for heroes_para_reclutar in heroes_para_reclutar:
    for heroes in heroes_info:
        if heroes_para_reclutar == heroes:
            heroes_reclutados[heroes] = heroes_info[heroes]


for heroe in heroes_reclutados:
    habilidades_filtradas = set(heroes_reclutados[heroe]["Habilidades"])
    
    texto = ""
    for habilidades in habilidades_filtradas:
        texto += habilidades + " | "

    print("\nID: {0}, Codename: {1} \n".format(heroes_reclutados[heroe]["ID"],heroe))
    print("Identidad: {0}, Origen: {1}\n".format(heroes_reclutados[heroe]["Identidad"],heroes_reclutados[heroe]["Origen"]))
    print("Habilidades: {0}".format(texto))
    print("------------------------------------------------------------")

