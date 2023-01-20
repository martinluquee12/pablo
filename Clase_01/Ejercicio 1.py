'''
Martin Luque DIV H

La división de higiene está trabajando en un control de stock para productos sanitarios. Debemos realizar la carga de 5 (cinco)
productos de prevención de contagio, de cada una debe obtener los siguientes datos:
El tipo (validar "barbijo", "jabón" o "alcohol")
El precio: (validar entre 100 y 300)
La cantidad de unidades ( no puede ser 0 ni negativo y no debe superar las 1000 unidades)
La marca y el Fabricante.
  
Se debe informar lo siguiente:
a-Del más caro de los barbijos, la cantidad de unidades y el fabricante.
b-Del ítem con más unidades, el fabricante.
c-Cuántas unidades de jabones hay en total.
'''
import re

def validar_str(patron:str, str_ingresado:str)->bool:
    '''
    Valida a traves de RegEx que el usuario haya ingresado una opcion correcta.
    
    Recibe el patron que queremos que se ingrese y lo que ingresa el usuario.

    Devuelve un True o un False en case de error.
    '''

    respuesta_validada = re.search(patron, str_ingresado, re.IGNORECASE)

    if respuesta_validada:
        return str_ingresado
    else:
        return False

def validar_int_3cifras(int_ingresado:str)->int:
    '''
    Valida a traves de RegEx que el usuario haya ingresado un numero correcto(De 3 cifras.).
    
    Recibe el unmero que ingreso el usuario que es str.

    Devuelve el numero casteado a int o un False en case de error.
    '''
    numero_validado = re.search("\d{3}", int_ingresado)

    if numero_validado != None:
        return int(int_ingresado)
    else:
        return False

def validar_int(int_ingresado:str)->int:
    '''
    Valida a traves de RegEx que el usuario haya ingresado un numero correcto(De 3 cifras.).
    
    Recibe el unmero que ingreso el usuario que es str.

    Devuelve el numero casteado a int o un False en case de error.
    '''
    numero_validado = re.search("^[0-9]+$", int_ingresado)

    if numero_validado != None:
        return int(int_ingresado)
    else:
        return False

precio_barbijo_mas_caro = None
item_con_mas_unidades = None

unidades_jabon = 0

for i in range(3):

    tipo = input('\nIngrese el tipo que desea cargar: "Alcohol", "Barbijo" o "Jabon". >')
    tipo = validar_str("(alcohol|barbijo|jabon)$", tipo)

    if tipo:
        pass
    else:
        print('\nError! Ingrese "Alcohol", "Barbijo" o "Jabon".')
        continue

    while True:

        precio = input("\nIngrese el precio de producto que ingreso. (Entre $100 y $300) >")
        precio = validar_int_3cifras(precio)

        if precio > 99 and precio < 301:
            break
        else:
            print("\nError! Debe ingresar un precio entre $100 y $300.")

    while True:

        cantidad = input("\nCantidad de unidades del producto: (No mayor a 1000 u) >")
        cantidad = validar_int(cantidad)

        if cantidad > 0 and cantidad < 1001:
            break
        else:
            print("\nError! Debe ingresar una cantidad valida no mayor a 1000 u.")
    
    marca = input("\nMarca del producto: >")

    fabricante = input("\nFabricante del producto: >")

    if tipo == "barbijo":
        if precio_barbijo_mas_caro == None or precio > precio_barbijo_mas_caro:
            precio_barbijo_mas_caro = precio
            unidades_barbijo_mas_caro = cantidad
            fabricante_barbijo_mas_caro = fabricante   
    if tipo == "jabon":
        unidades_jabon+= cantidad

    if item_con_mas_unidades == None or cantidad > item_con_mas_unidades:
        item_con_mas_unidades = cantidad
        tipo_item_con_mas_unidades = tipo
        fabricante_item_con_mas_unidades = fabricante

print("\nDel barbijo mas caro la cantidad de unidades es",unidades_barbijo_mas_caro,"su fabricante es",fabricante_barbijo_mas_caro)
print("\nEl item con mas unidades es del producto",tipo_item_con_mas_unidades,",las unidades son",
item_con_mas_unidades,"y su fabricante es",fabricante_item_con_mas_unidades)

if unidades_jabon > 0:

    print("\nHay",unidades_jabon,"unidades de jabon.")
else:
    print("\nNo se ingresaron jabones.")