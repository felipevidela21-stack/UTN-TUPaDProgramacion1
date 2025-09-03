#1) Imprimir números del 0 al 100

for i in range(101):
    print(i)

#2) Contar dígitos de un número

numero = int(input("Ingresá un número entero: "))
cantidad_digitos = len(str(abs(numero)))
print("Cantidad de dígitos:", cantidad_digitos)


#3) Suma de números entre dos valores (excluidos)

a = int(input("Ingresá el primer número: "))
b = int(input("Ingresá el segundo número: "))

suma = 0
for i in range(min(a, b) + 1, max(a, b)):
    suma += i

print("La suma de los números entre", a, "y", b, "es:", suma)

if suma == 0:
 print("El resultado de la suma es" , suma, "ya que entre ellos no hay numeros")


#4) Suma de números hasta ingresar 0

suma = 0
while True:
    numero = int(input("Ingresá un número (0 para terminar): "))
    if numero == 0:
        break
    suma += numero

print("La suma acumulada es:", suma)


#5) Juego de adivinar un número

import random

numero_secreto = random.randint(0, 9)
intentos = 0
adivinado = False

while not adivinado:
    intento = int(input("Adiviná el número (entre 0 y 9): "))
    intentos += 1
    if intento == numero_secreto:
        adivinado = True

print("¡Correcto! El número era", numero_secreto, "y lo lograste en", intentos, "intentos.")


#6) Números pares de 0 a 100 en orden decreciente en Python:

for i in range(100, -1, -2):
    print(i)

#7) Suma de números de 0 hasta n



n = int(input("Ingresá un número entero positivo: "))
suma = 0

for i in range(n + 1):
    suma += i

print("La suma de los números de 0 hasta", n, "es:", suma)


#8) Clasificación de 100 números

cantidad = 100  # cambiar este valor si querés probar con menos
pares = impares = positivos = negativos = 0

for i in range(cantidad):
    numero = int(input(f"Ingresá el número {i+1}: "))
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
    if numero >= 0:
        positivos += 1
    else:
        negativos += 1

print("Pares:", pares)
print("Impares:", impares)
print("Positivos:", positivos)
print("Negativos:", negativos)
