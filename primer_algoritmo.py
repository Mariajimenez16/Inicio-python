#print("hola mundo")

#sumar dos numeros fijos
numero1 = 5
numero2 = 10
suma = numero1 + numero2
print("La suma de", numero1, "y", numero2, "es:", suma)

#multiplicar dos numeros fijos
numero3 = 7
numero4 = 5
multiplicacion = numero3 * numero4
print("la multiplicacion de", numero3, "y", numero4, "es:", multiplicacion)

#calcular mi edad
anioNacimiento = 2006
anioActual = 2026
edad = anioActual - anioNacimiento
print("Mi edad es:", edad)

#calcular el area de un rectangulo
base = 8
altura = 4
areaRectangulo = base * altura
print("El area del rectangulo es:", areaRectangulo)

#calcular promedio de tres notas
nota1= 4.3
nota2=3.8
nota3= 2.8
promedio = (nota1 + nota2 + nota3) / 3
print("El promedio de las notas es:", promedio)

#convertir grados Celsius a Fahrenheit
c= 25
f = (c * 9/5) + 32
print(c, "grados Celsius son", f, "grados Fahrenheit")  

#calcular el sueldo de un empleado 
horasTrabajadas = 160
valorHora = 15
sueldo = horasTrabajadas * valorHora
print("El sueldo del empleado es:", sueldo)

#calcular el sueldo de un empleado con datos ingresados por el usuario
nombre = input("Ingrese su nombre: ")
cantidadHoras = float(input("Ingrese la cantidad de horas trabajadas: "))
valorHora = float(input("Ingrese el valor por hora: "))
sueldo = cantidadHoras * valorHora
print("Hola", nombre + ", tu sueldo es:", sueldo)

#calcular el precio final con iva
precioSinIva = float(input("Ingrese el precio sin IVA: "))
iva= precioSinIva * 0.19
precioFinal = precioSinIva + iva
print("El precio final con IVA es:", precioFinal)
