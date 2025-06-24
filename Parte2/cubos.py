# Lista de los primeros 10 cubos
cubos = []

# Genera los cubos y los agrega a la lista
for numero in range(1, 11):
    cubo = numero ** 3
    cubos.append(cubo)

# Imprime cada cubo
for cubo in cubos:
    print(cubo)