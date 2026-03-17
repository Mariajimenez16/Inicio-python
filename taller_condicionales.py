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
        