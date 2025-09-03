# 1) Hola Mundo

print("Hola Mundo!")

# 2) Saludo personalizado

nombre = input("¿Como te llamas? ")
print(f"Hola {nombre}!")

# 3) Datos personales

nombre = input("Nombre: ")
apellido = input("Apellido: ")
edad = input("Edad: ")
residencia = input("Lugar de residencia: ")
print(f"Nombre: {nombre} {apellido} | Edad: {edad} años | Vive en: {residencia}")

# 4) Área y perímetro de un círculo

pi = 3.1416
radio = float(input("Ingresá el radio del círculo: "))
area = pi * radio**2
perimetro = 2 * pi * radio
print(f"Área: {area}")
print(f"Perímetro: {perimetro}")

# 5) Segundos a horas

segundos = int(input("Ingresá una cantidad de segundos: "))
horas = segundos / 3600
print(f"{segundos} segundos equivalen a {horas} horas.")

# 6) Tabla de multiplicar

numero = int(input("Ingresá un número: "))
for i in range(1, 11):
 print(f"{numero} x {i} = {numero * i}")

# 7) Operaciones básicas

num1 = int(input("Primer número (distinto de 0): "))
num2 = int(input("Segundo número (distinto de 0): "))
print(f"Suma: {num1 + num2}")
print(f"Resta: {num1 - num2}")
print(f"Multiplicación: {num1 * num2}")
print(f"División: {num1 / num2}")

# 8) Índice de masa corporal

peso = float(input("Ingresá tu peso en kg: "))
altura = float(input("Ingresá tu altura en metros: "))
imc = peso / (altura ** 2)
print(f"Tu índice de masa corporal es: {round(imc, 2)}")

# 9) Celsius a Fahrenheit

celsius = float(input("Temperatura en Celsius: "))
fahrenheit = (9 / 5) * celsius + 32
print(f"{celsius}°C equivale a {fahrenheit}°F")

# 10) Promedio de tres números

n1 = float(input("Primer número: "))
n2 = float(input("Segundo número: "))
n3 = float(input("Tercer número: "))
promedio = (n1 + n2 + n3) / 3
print(f"El promedio es: {promedio}")