#1) Edad mayor de 18
edad = int(input("Ingresá tu edad: "))
if edad > 18:
 print("Es mayor de edad")
else:
 print("No es mayor de edad")
#2) Nota aprobada o desaprobada
nota = int(input("Ingresá tu nota: "))
if nota >= 6:
 print("Aprobado")
else:
 print("Desaprobado")
#3) Verificar número par
numero = int(input("Ingresá un número par: "))
if numero % 2 == 0:
 print("Ha ingresado un número par")
else:
 print("Por favor, ingrese un número par")
#4) Categorías de edad
edad = int(input("Ingresá tu edad: "))
if edad < 12:
 print("Niño/a")
elif edad < 18:
 print("Adolescente")
elif edad < 30:
 print("Adulto/a joven")
else:
 print("Adulto/a")
#5) Validar contraseña
contraseña = input("Ingresá tu contraseña: ")
if 8 <= len(contraseña) <= 14:
 print("Ha ingresado una contraseña correcta")
else:
 print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")
#6) Sesgo estadístico
import random
from statistics import mean, median, mode
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)
print("Media:", media)
print("Mediana:", mediana)
print("Moda:", moda)
if media > mediana > moda:
 print("Sesgo positivo")
elif media < mediana < moda:
 print("Sesgo negativo")
elif media == mediana == moda:
 print("Sin sesgo")
else:
 print("No cumple con ninguno de los criterios exactos")
#7) Agregar '!' si termina en vocal
texto = input("Ingresá una palabra o frase: ")
if texto[-1].lower() in "aeiou":
 print(texto + "!")
else:
 print(texto)
#8) Transformar nombre según opción
nombre = input("Ingresá tu nombre: ")
opcion = int(input("Ingresá 1 (MAYÚSCULAS), 2 (minúsculas) o 3 (Primera letra mayúscula): "))
if opcion == 1:
 print(nombre.upper())
elif opcion == 2:
 print(nombre.lower())
elif opcion == 3:
 print(nombre.title())
else:
 print("Opción inválida")
#9) Clasificación de magnitud (Escala de Richter)
magnitud = float(input("Ingresá la magnitud del terremoto: "))
if magnitud < 3:
 print("Muy leve")
elif magnitud < 4:
 print("Leve")
elif magnitud < 5:
 print("Moderado")
elif magnitud < 6:
 print("Fuerte")
elif magnitud < 7:
 print("Muy fuerte")
else:
 print("Extremo")
#10) Estaciones del año
hemisferio = input("Ingresá tu hemisferio (N/S): ").upper()
mes = int(input("Ingresá el número de mes (1-12): "))
dia = int(input("Ingresá el día del mes: "))
if (mes == 12 and dia >= 21) or mes in (1, 2) or (mes == 3 and dia <= 20):
 estacion_norte, estacion_sur = "Invierno", "Verano"
elif (mes == 3 and dia >= 21) or mes in (4, 5) or (mes == 6 and dia <= 20):
 estacion_norte, estacion_sur = "Primavera", "Otoño"
elif (mes == 6 and dia >= 21) or mes in (7, 8) or (mes == 9 and dia <= 20):
 estacion_norte, estacion_sur = "Verano", "Invierno"
else:
 estacion_norte, estacion_sur = "Otoño", "Primavera"
if hemisferio == "N":
 print("Estación:", estacion_norte)
elif hemisferio == "S":
 print("Estación:", estacion_sur)
else:
 print("Hemisferio inválido")