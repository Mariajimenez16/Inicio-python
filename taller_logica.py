#ejercicio 1: Mayor de 2 hermanos
nombre1 = input("Nombre del hermano 1: ")
edad1 = int(input(f"Edad de {nombre1}: "))

nombre2 = input("Nombre del hermano 2: ")
edad2 = int(input(f"Edad de {nombre2}: "))

if edad1 > edad2:
    print(f"El mayor es: {nombre1}")
else:
    print(f"El mayor es: {nombre2}")

#ejercicio 2: clasificación por edad
edad = int(input("Ingresa tu edad: "))

if edad < 10:
    categoria = "Niño"
elif edad <= 14:
    categoria = "Preadolescente"
elif edad <= 18:
    categoria = "Adolescente"
elif edad <= 50:
    categoria = "Adulto"
else:
    categoria = "Adulto mayor"

print(f"Categoría: {categoria}")

#ejerciio  3 : mayor salario
nombre_t1 = input("Nombre del trabajador 1: ")
bruto_t1 = float(input("Salario bruto: "))
deducciones_t1 = float(input("Deducciones: "))
bonificaciones_t1 = float(input("Bonificaciones: "))
neto_t1 = bruto_t1 - deducciones_t1 + bonificaciones_t1

nombre_t2 = input("\nNombre del trabajador 2: ")
bruto_t2 = float(input("Salario bruto: "))
deducciones_t2 = float(input("Deducciones: "))
bonificaciones_t2 = float(input("Bonificaciones: "))
neto_t2 = bruto_t2 - deducciones_t2 + bonificaciones_t2

if neto_t1 > neto_t2:
    print(f"\n{nombre_t1} tiene el mayor salario neto: ${neto_t1:,.2f}")
elif neto_t2 > neto_t1:
    print(f"\n{nombre_t2} tiene el mayor salario neto: ${neto_t2:,.2f}")
else:
    print("Ambos trabajadores tienen el mismo salario neto.")

#ejercicio 4
placa1 = input("Placa del bus 1: ")
pasajeros1 = int(input("Número de pasajeros: "))
valor_pasaje1 = float(input("Valor del pasaje: $"))
total1 = pasajeros1 * valor_pasaje1

placa2 = input("\nPlaca del bus 2: ")
pasajeros2 = int(input("Número de pasajeros: "))
valor_pasaje2 = float(input("Valor del pasaje: $"))
total2 = pasajeros2 * valor_pasaje2

if total1 > total2:
    print(f"\nEl bus {placa1} recogió más dinero: ${total1:,.2f}")
elif total2 > total1:
    print(f"\nEl bus {placa2} recogió más dinero: ${total2:,.2f}")
else:
    print("Ambos buses recogieron el mismo dinero.")
    
#ejercicio 5
TARIFA_A = 1200
TARIFA_B = 1000

placa = input("Placa del bus: ")
pasajeros = int(input("Número de pasajeros: "))
ruta = input("Ruta (A o B): ").upper()

if ruta == "A":
    dinero = pasajeros * TARIFA_A
    print(f"\nEl bus {placa} en la ruta A recaudó: ${dinero:,}")
elif ruta == "B":
    dinero = pasajeros * TARIFA_B
    print(f"\nEl bus {placa} en la ruta B recaudó: ${dinero:,}")
else:
    print("Ruta inválida. Solo se aceptan rutas A o B.")
    
    #ejercicio 6
    SALARIO_HORA_TEMPORAL = 6000

tipo = input("Tipo de trabajador (FIJO o TEMPORAL): ").upper()

if tipo == "FIJO":
    nombre = input("Nombre: ")
    horas = int(input("Horas trabajadas: "))
    salario_hora = float(input("Salario básico por hora: $"))
    deducciones = float(input("Total deducciones: $"))
    bonificaciones = float(input("Total bonificaciones: $"))
    salario_neto = (horas * salario_hora) - deducciones + bonificaciones
    print(f"\nNombre: {nombre}")
    print(f"Salario neto: ${salario_neto:,.2f}")

elif tipo == "TEMPORAL":
    nombre = input("Nombre: ")
    horas = int(input("Horas trabajadas: "))
    salario_neto = horas * SALARIO_HORA_TEMPORAL
    print(f"\nNombre: {nombre}")
    print(f"Salario neto: ${salario_neto:,}")

else:
    print("Tipo de trabajador inválido. Solo FIJO o TEMPORAL.")
    
#ejercicio 7
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))
num3 = float(input("Ingresa el tercer número: "))

# Verificar que sean diferentes
if num1 == num2 or num2 == num3 or num1 == num3:
    print("Los números deben ser todos diferentes entre sí")
else:
    if num1 > num2 and num1 > num3:
        mayor = num1
    elif num2 > num1 and num2 > num3:
        mayor = num2
    else:
        mayor = num3
    print(f"El mayor de los tres números es: {mayor}")

print("\n" + "="*50)
print("  ¡Taller completado!")
print("="*50)
