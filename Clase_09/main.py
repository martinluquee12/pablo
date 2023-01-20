lista = [6,2,4,1,0,8,9,7,3,5]

def buscar_indice_minimo(lista:list)->int:
    '''
    Busca un minimo de una lista a travez del indice.
    Recibe una litsa.
    Devuelve un entero.
    '''
    minimo = 0

    for i in range(len(lista)):
        if lista[i] < lista[minimo]:
            minimo = i
    return minimo
            
def nahuel_sort(lista_desordenada:list)->list:
    '''

    '''
    copia_lista = lista_desordenada.copy()
    lista_ordenada = []

    while len(copia_lista) > 0:
        minimo_indice = buscar_indice_minimo(copia_lista)
        minimo = copia_lista.pop(minimo_indice)#pop te pide el indice pero te devuelve el valor de ese indice. lo saca de una lista y lo agrega a la otra
        lista_ordenada.append(minimo)

    return lista_ordenada


print(nahuel_sort(lista))


def ivan_sort(lista_desordenada:list)->list:
    copia_lista = lista_desordenada.copy()
    flag = True
    limite = 1

    while flag == True:
        flag = False
        for i in range(len(copia_lista) - limite):
            if copia_lista[i] > copia_lista[i + 1]:
                copia_lista[i], copia_lista[i + 1] = copia_lista[i + 1], copia_lista[i]
                flag == True
        limite += 1
    return copia_lista
            

print(ivan_sort(lista))



