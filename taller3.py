#Maria Alexandra Jiménez Suárez

#Taller 3

#EJ 1 Consumo de energía eléctrica
consumo_kwh = float(input("Ingrese el consumo de energía en kWh: "))
costo_por_kwh = float(input("Ingrese el costo por kWh: "))
total_a_pagar = consumo_kwh * costo_por_kwh
print("El total a pagar por el consumo de energía eléctrica es:", total_a_pagar)

#EJ 2 Precio final con IVA y descuento
precio_original = float(input("Ingrese el precio original del producto: "))
iva = precio_original * 0.19
descuento = float(input("Ingrese el descuento aplicado: "))
precio_final = precio_original + iva - descuento
print("El precio final del producto es:", precio_final)


#EJ 3 Ahorro anual
sueldo_mensual = float(input("Ingrese su sueldo mensual: "))

ahorro_semanal = sueldo_mensual * 0.15
ahorro_anual = ahorro_semanal * 4 * 12

print("El ahorro total al año es:", ahorro_anual)

#EJ 4 Monto de un cheque para viaje
dias = int(input("Ingrese el número de días del viaje: "))
valor_hotel = float(input("Ingrese el valor diario del hotel: "))
valor_comida = float(input("Ingrese el valor diario de la comida: "))

total_hotel = dias * valor_hotel
total_comida = dias * valor_comida
total_otros = dias * 200000

total_general = total_hotel + total_comida + total_otros

print("Total hotel:", total_hotel)
print("Total comida:", total_comida)
print("Total otros gastos:", total_otros)
print("Total general del cheque:", total_general)

#EJ 5 Promedio ponderado
examen1 = float(input("Ingrese la nota del primer examen: "))
examen2 = float(input("Ingrese la nota del segundo examen: "))
examen3 = float(input("Ingrese la nota del tercer examen: "))

promedio = (examen1 * 0.25) + (examen2 * 0.25) + (examen3 * 0.50)

print("El promedio final es:", promedio)

#EJ 6 Costo de estancia en hotel
dias = int(input("Ingrese la cantidad de días de hospedaje: "))
valor_noche = float(input("Ingrese el valor por noche: "))

total = dias * valor_noche

print("El total a pagar es:", total)