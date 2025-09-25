#1).
lista_range = list(range(4,101,4))

print(lista_range)
#2).
lista_5= [1,2,3,4,5]
pelultimo=lista_5[3]
print("el pultimo numero es:",pelultimo)
#3).
lista_vacia = []

lista_vacia.append("sol")
lista_vacia.append("mar")
lista_vacia.append("montaña")

print(lista_vacia)
#4).
animales = ["perro", "gato", "conejo", "pez"]

animales[1] = "loro"
animales[3] = "oso"

print(animales)
#5).

#numeros= [8,15,3,22,7]
# Se crea una lista de 5 elementos, luego con //numeros.remove(max(numeros))//
#lo que se hace se hace es elimar el elemto un la ultima posicion, para que luego se imprima por pantalla de la siguiente manera
#//8,15,3,22//

#6).
numeros = list(range(10, 31, 5)) 
print(numeros[:2])  
#7).
autos = ["sedan", "polo", "suran", "gol"]

autos[1] = "camioneta"
autos[2] = "jeep"

print(autos)
#8).
dobles = []

dobles.append(5*2)
dobles.append(10*2)
dobles.append(15*2)

print(dobles)
#9).
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

compras[2].append("jugo")
compras[1][1] = "tallarines"
compras[0].remove("pan")

print(compras)
#10).
lista_anidada = [
    15,
    True,
    [25.5, 57.9, 30.6],
    False
]

print(lista_anidada)


