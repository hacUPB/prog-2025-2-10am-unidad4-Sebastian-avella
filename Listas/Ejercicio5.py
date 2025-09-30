# Generar una lista con 100 numeros aleatorios entre 100 y 1000
# calcular el promedio de los valores de la lista
# calcular el mayor y menor de los numeros

import random
# Lista numerica
numero =[]
for i in range(100):
    aleatorio = random.randint(100,1000)
    numero.append(aleatorio)

suma = 0
# #Forma 1
# for i in numero:
#     suma += i

#Forma 2
for i in range (len(numero)):
     suma += numero[i]

prom = suma /len(numero)

prom = sum(numero) / len(numero)
print(f"promedio _ {prom}")

Mayor = max(numero)
menor = min(numero)
