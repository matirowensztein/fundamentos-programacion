def es_identidad(matriz):
    es_iden = True
    i = 0
    j = 0

    while es_iden and i < len(matriz):
        if i == j and matriz[i][j] != 1:
            es_iden = False
        
        if i != j and matriz[i][j] != 0:
            es_iden = False

        j += 1

        if j == len(matriz):
            j = 0
            i += 1

    return es_iden

print(es_identidad([[1]]))  # True
print(es_identidad([[1, 0], [0, 1]]))  # True
print(es_identidad([[1, 0, 0], [0, 1, 0], [0, 0, 1]]))  # True
print(es_identidad([[2, 0], [0, 1]]))  # False - Diagonal incorrecta
print(es_identidad([[1, 1], [0, 1]]))  # False - Elemento fuera de la diagonal no es cero
print(es_identidad([[0, 0], [0, 0]]))  # False - Todo ceros
print(es_identidad([[0, 0], [0, 1]]))  # False - Diagonal con ceros
print(es_identidad([[1, 0, 0], [0, 0, 0], [0, 0, 1]]))  # False - Valor incorrecto en la diagonal
print(es_identidad([[1.0, 0.0], [0.0, 1.0]]))  # True (aunque puede depender de cómo se trate float vs int)
