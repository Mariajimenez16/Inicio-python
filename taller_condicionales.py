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