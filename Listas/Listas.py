import random 
# Lista vacía
componentes = []
# 1. Agregar un elmento 
elemento = input("Ingrese un componente del avion:")
componentes.append(elemento)
print(componentes)

# Lista numerica
numero =[]
aleatorio = random.randint(0,100)
numero.append(aleatorio)
numero.append(10)
#Agregar aleatorios a la lista
for i in range(10):
    aleatorio = random.randint(0,100)
    numero.append(aleatorio)

print(numero)

# # Lista con elementos
# componentes = ["alas", "fuselaje", "motores", "tren de aterrizaje"]

# # Lista con diferentes tipos de datos
# datos_vuelo = [202, "Boeing 737", True, 10500.5]

# # Listas anidadas
# matriz_rotacion = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]