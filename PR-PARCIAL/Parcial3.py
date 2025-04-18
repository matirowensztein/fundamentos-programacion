def es_cuadrada(matriz):
    es_cuadrada = True
    i = 1

    while es_cuadrada and i < len(matriz):
        if len(matriz[i]) != len(matriz[i - 1]) or len(matriz[i]) != len(matriz):
            es_cuadrada = False

        i += 1

    return es_cuadrada

# # Casos de test para es_cuadrada
# print(es_cuadrada([[1, 2], [3, 4]]))             # True (2x2)
# print(es_cuadrada([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))  # True (3x3)
# print(es_cuadrada([[1, 2, 3], [4, 5, 6]]))        # False (2x3)
# print(es_cuadrada([[1], [2], [3]]))              # False (3x1)
# print(es_cuadrada([]))                           # True (0x0, se puede considerar cuadrada)

def es_simetrica(matriz):
    es_simetrica = True
    i = 0
    j = 0

    while es_simetrica and i < len(matriz):
        if matriz[i][j] != matriz[j][i]:
            es_simetrica = False

        j += 1

        if j == len(matriz[i]):
            j = 0
            i += 1

    return es_simetrica

# # Casos de test para es_simetrica
# print(es_simetrica([[1, 2], [2, 1]]))            # True
# print(es_simetrica([[1, 0, 3], 
#                     [0, 5, 6], 
#                     [3, 6, 9]]))  # True
# print(es_simetrica([[1, 2], [3, 4]]))            # False (2 != 3)
# print(es_simetrica([[1]]))                      # True (matriz 1x1)
# print(es_simetrica([[1, 2, 3], [2, 5, 6], [7, 6, 9]]))  # False (3 != 7)

def ordernar_puestos(salarios):
    lista_ordeanada = []

    for salario in salarios:
        lista_ordeanada.append([salarios[salario][2], salario])

    lista_ordeanada.sort(reverse=True)

    for salario in lista_ordeanada:
        print(f"{salario[1]} -> {salario[0]}")

def programadores(salarios):
    dicc_programadores = {}
    total_salarios = 0
    cantidad = 0
    promedio = 0

    for programador in salarios:
        if programador[0] not in dicc_programadores:
            dicc_programadores[programador[0]] = [programador[1], 1, programador[1]]
        else:
            total_salarios = dicc_programadores[programador[0]][0] + programador[1]
            cantidad = dicc_programadores[programador[0]][1] + 1
            promedio = total_salarios / cantidad
            dicc_programadores[programador[0]] = [total_salarios, cantidad, promedio]

    print(dicc_programadores)
    ordernar_puestos(dicc_programadores)

salarios = [
    ["Desarrollador", 1000],
    ["Tester", 800],
    ["Desarrollador", 920],
    ["Analista", 950],
    ["Tester", 1000],
    ["Desarrollador", 1100]
]

programadores(salarios)
    