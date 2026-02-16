#Maria Alexandra Jiménez Suárez


#Ejercicio 1 Área de un rectángulo

base = float(input("Ingrese la base del rectángulo: "))
altura = float(input("Ingrese la altura del rectángulo: "))

area = base * altura

print("El área del rectángulo es:", area)

#EJ 2  Área de una circunferencia

radio = float(input("Ingrese el radio del círculo: "))

PI = 3.1416

area = PI * radio * radio

print("El área de la circunferencia es:", area)

#EJ 3  Área de un triángulo

base = float(input("Ingrese la base del triángulo: "))
altura = float(input("Ingrese la altura del triángulo: "))

resultado = base * altura
area = resultado / 2

print("El área del triángulo es:", area)

#EJ 4  Convertir metros a pulgadas

metros = float(input("Ingrese la cantidad de metros: "))

pulgadas = metros / 0.0254

print("La cantidad en pulgadas es:", pulgadas)

#EJ 5 Cobro de estacionamiento

horas = float(input("Ingrese las horas usadas: "))
valor_por_hora = float(input("Ingrese el valor por cada hora: "))

total = horas * valor_por_hora

print("El total a pagar es:", total)

#EJ 6 

#EJ 7  Conversión de litros a galones

litros = float(input("Ingrese los litros producidos: "))
precio_por_galon = float(input("Ingrese el precio por galón: "))

galones = litros / 3.785
total = galones * precio_por_galon

print("Total a recibir:", total)

#EJ 8 Costo de boleto

kilometros = float(input("Ingrese los kilómetros a recorrer: "))
costo_por_km = float(input("Ingrese el costo por kilómetro: "))

total = kilometros * costo_por_km

print("El valor total del boleto es:", total)

# EJ 9 Tiempo de viaje en bicicleta

distancia = float(input("Ingrese los kilómetros a recorrer: "))
velocidad = float(input("Ingrese la velocidad en km/h: "))

tiempo = distancia / velocidad

print("El tiempo de viaje en horas es:", tiempo)

#EJ 10 Costo de llamada telefónica

minutos = float(input("Ingrese los minutos de la llamada: "))
costo_por_minuto = float(input("Ingrese el costo por minuto: "))

total = minutos * costo_por_minuto

print("El total a pagar es:", total)