'''
Martin Luque DIV H 

La división de alimentos está trabajando en un pequeño software para cargar las compras
de ingredientes para la cocina de Industrias Wayne. 
Realizar el algoritmo permita ingresar los datos de una compra de ingredientes para
preparar comida al por mayor, HASTA QUE EL CLIENTE QUIERA.

PESO: (entre 10 y 100 kilos)
PRECIO POR KILO: (mayor a 0 [cero]).
TIPO VALIDAD: ("v", "a", "m");(vegetal, animal, mezcla).
Además tener en cuenta que si compro más de 100 kilos en total tenes 15% de descuento sobre el precio bruto.
O si compro más de 300 kilos en total, tenes 25% de descuento sobre el precio bruto.

a-El importe total a pagar, BRUTO sin descuento.
b-El importe total a pagar con descuento (Solo si corresponde).
c-Informar el tipo de alimento más caro.
d-El promedio de precio por kilo en total.
'''

acumulador_precio_v = 0
acumulador_peso_v = 0
acumulador_precio_bruto_v = 0
contador_tipo_v = 0
acumulador_precio_a = 0
acumulador_peso_a = 0
acumulador_precio_bruto_a = 0
contador_tipo_a = 0
acumulador_precio_m = 0
acumulador_peso_m = 0
acumulador_precio_bruto_m = 0
contador_tipo_m = 0

precio_tipo_mas_caro = None

respuesta = 's'

while(respuesta == 's'):
    tipo = input("¿Que tipo de alimento es? 'V' para vegetal, 'A' para animal o 'M' para mezcla.")
    while(tipo.lower() != "v" and tipo.lower() != "a" and tipo.lower() != "m"):
        tipo = input("Error! Ingrese un tipo valido :'V' para vegetal, 'A' para animal o 'M' para mezcla.")
    
    while(True):
        peso = input("Ingrese el peso (Entre 10kg y 100kg)")
        if(not peso.isnumeric()):
            print("Error! Debe ingresar un numero.")
            continue
        peso = int(peso)
        if(peso >= 10 and peso <= 100):
            break
        print("Error! Ingrese un peso valido (Entre 10kg y 100kg)")

    while(True):
        precio_kilo = input("Precio por Kilo.")
        if(not precio_kilo.isnumeric()):
            print("Debe ingresar un numero.")
            continue
        precio_kilo = int(precio_kilo)
        if(precio_kilo > 0):
            break
        print("Erro! Ingrese un precio valido.")

    if(tipo == "V"):
        acumulador_peso_v += peso
        acumulador_precio_v += precio_kilo
        acumulador_precio_bruto_v += peso * precio_kilo
        contador_tipo_v += 1
    elif(tipo == "A"):
        acumulador_peso_a += peso
        acumulador_precio_a += precio_kilo
        acumulador_precio_bruto_a += peso * precio_kilo
        contador_tipo_a += 1
    else:
        acumulador_peso_m += peso
        acumulador_precio_m += precio_kilo
        acumulador_precio_bruto_m += peso * precio_kilo
        contador_tipo_m += 1

    if(precio_tipo_mas_caro == None or precio_kilo > precio_tipo_mas_caro):
        precio_tipo_mas_caro = precio_kilo
        tipo_mas_caro = tipo

    respuesta = input("¿Quiere seguir ingresando?")
    

precio_bruto_total = acumulador_precio_bruto_v + acumulador_precio_bruto_a + acumulador_precio_bruto_m
acumulador_peso_total = acumulador_peso_v + acumulador_peso_a + acumulador_peso_m
acumulador_precio_por_kilo_total = acumulador_precio_v + acumulador_precio_a + acumulador_precio_m
contador_tipo_total = contador_tipo_v + contador_tipo_a + contador_tipo_m

promedio_precio_kilo = acumulador_precio_por_kilo_total / contador_tipo_total

print("\nEl importe total a pagar, bruto sin descuento es $", precio_bruto_total,"\n")

if(acumulador_peso_total > 100 and acumulador_peso_total < 300):
    precio_con_descuento = precio_bruto_total - (precio_bruto_total * 15 / 100)
    print("Por haber comprado mas de 100Kg tiene un descuento del 15%, el importe a pagar queda en $", precio_con_descuento,"\n")
elif(acumulador_peso_total > 300):
    precio_con_descuento = precio_bruto_total - (precio_bruto_total * 25 / 100)
    print("Por haber comprado mas de 300Kg tiene un descuento del 25%, el importe a pagar queda en $", precio_con_descuento,"\n")

print("El tipo mas caro es:", tipo_mas_caro,"\n")
print("EL promedio de precio por Kilo es $",promedio_precio_kilo)