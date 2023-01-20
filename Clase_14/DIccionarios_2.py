lista_precios = {
    
    "banana" : {
        "precio" : 120.10,
        "unidad_medida": "kg",
        "stock": 50
    },
    
    "pera": {
        "precio": 240.50,
        "unidad_medida": "kg",
        "stock": 40        
    },
    
    "frutilla": {
        "precio": 300,
        "unidad_medida": "kg",
        "stock": 100        
    }, 
    
    "mango" : {
        "precio": 300,
        "unidad_medida": "unidad",
        "stock": 100  
    }

}

# Punto 1: solicitar al usuario un producto y verificiar si existe en 'lista_precios' en caso de existir mostrar precio y el stock. En caso de no existir el 
# producto mostrar el mensaje 'el articulo no se encuentra en la lista'

# producto = input("Producto: ")
# producto = producto.lower
# producto_encontrado = lista_precios.get(producto)

# if producto_encontrado != None:
#     print("Nombre: {0} | Precio: ${1} | Stock: {2}u".format(producto.capitalize(),producto_encontrado["precio"], producto_encontrado["stock"]))
# else:
#     print("El articulo no se encuentra en la lista.")

# Punto 2: agregar al punto anterior que el usuario ingrese la cantidad y retornar el precio total (precio * cantidad)

# producto = input("Producto: ")
# producto = producto.lower()
# cantidad = float(input("Cantidad: "))
# producto_encontrado = lista_precios.get(producto)

# if producto_encontrado != None:
#     print("Nombre: {0} | Precio: ${1} | Stock: {2}u".format(producto.capitalize(),(producto_encontrado["precio"]*cantidad), producto_encontrado["stock"]))
# else:
#     print("El articulo no se encuentra en la lista.")

# Punto 3: solicitar al usuario que ingrese una nueva fruta junto con su precio, unidad de medida y stock. Agregar la nueva fruta a la lista de precios

fruta = input("Fruta: ")
fruta = fruta.lower()
precio = int(input("Precio: "))
unidad_medida = input("Unidad de medida: ")
unidad_medida = unidad_medida.lower()
stock = int(input("Stock: "))

lista_precios.update({fruta: {"precio": precio, "unidad_medida": unidad_medida, "stock": stock}})

print(lista_precios)
# Punto 4: imprimir el listado de frutas (solo su nombre)


# Punto 5: solicitarle al usuario el nombre de fruta y en caso de exisitir eliminarla. En caso de que el producto no exista mostrar 
# el mensaje 'el articulo no se encuentra en la lista'