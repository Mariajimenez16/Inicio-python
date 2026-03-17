#1 Ejercicio 1: usuario y contraseña
codigo = ""
contrasena = ""

while codigo != "1" or contrasena != "1234":
    codigo = input("Ingrese su código: ")
    contrasena = input("Ingrese su contraseña: ")
    
    if codigo != "1" or contrasena != "1234":
        print("Datos incorrectos, intente de nuevo")

print("Acceso aceptado")

#ejercicio 2: factorial 
numero = int(input("Ingrese un número positivo: "))
resultado = 1

for i in range(1, numero + 1):
    resultado = resultado * i

print("El factorial es:", resultado)

#ejercicio 3: continuar ? 
opcion = ""

while opcion != "N":
    opcion = input("¿Desea continuar S/N?: ")
    
    if opcion == "S":
        print("Continuando...")
    elif opcion == "N":
        print("Programa finalizado")
    else:
        print("Opción inválida")
        
#ejercicio 4: promedio de notas
suma = 0
contador = 0
opcion = "S"

while opcion == "S":
    nota = float(input("Ingrese una nota: "))
    suma = suma + nota
    contador = contador + 1
    
    opcion = input("¿Desea ingresar otra nota? S/N: ")

promedio = suma / contador
print("El promedio es:", promedio)        
        
#ejercicio 5: número hasta -1
suma = 0
contador = 0

numero = int(input("Ingrese un número (-1 para salir): "))

while numero != -1:
    suma = suma + numero
    contador = contador + 1
    numero = int(input("Ingrese otro número (-1 para salir): "))

if contador > 0:
    promedio = suma / contador
    print("Cantidad:", contador)
    print("Suma:", suma)
    print("Promedio:", promedio)
else:
    print("No se ingresaron números")
    
    
#ej 6: notas de 20 estudiantes 
suma = 0
mayor = 0
menor = 5

for i in range(20):
    nota = float(input("Ingrese nota: "))
    suma = suma + nota
    
    if nota > mayor:
        mayor = nota
    if nota < menor:
        menor = nota

promedio = suma / 20

print("Promedio:", promedio)
print("Mayor:", mayor)
print("Menor:", menor)

#ejercicio 7: suma de 1 hasta n
numero = int(input("Ingrese un número: "))
suma = 0

for i in range(1, numero + 1):
    suma = suma + i

print("La suma es:", suma)

#ejercicio 8 : suma de negativos 
suma_negativos = 0

for i in range(10):
    numero = int(input("Ingrese un número: "))
    
    if numero < 0:
        suma_negativos = suma_negativos + numero

print("Suma de negativos:", suma_negativos)

#ejercicio 9: numeros del 1 al 100
numero = 100

while numero >= 1:
    print(numero)
    numero = numero - 1
    
#ejercicio 10: focos de colores
N = int(input("¿Cuántos focos hay?: "))

verde = 0
blanco = 0
rojo = 0

for i in range(N):
    color = input("Ingrese color (verde/blanco/rojo): ")
    
    if color == "verde":
        verde = verde + 1
    elif color == "blanco":
        blanco = blanco + 1
    elif color == "rojo":
        rojo = rojo + 1

print("Verdes:", verde)
print("Blancos:", blanco)
print("Rojos:", rojo)