def lista_valores():
    lista = []
    es_valido = True

    while es_valido:
        valor = int(input("Ingrese los valores que desee (ingrese 0 si desea dejar de ingresar valores): "))

        if valor == 0:
            es_valido = False
        else:
            lista.append(valor)
    
    return lista


def mostrar_valores(lista_obtenida):
    for i in lista_obtenida:
        print(i)

def mostrar_tercer_par(lista_obtenida):
    contador_pares = 0
    i = 0

    while contador_pares < 3 and i < len(lista_obtenida):
        if lista_obtenida[i] % 2 == 0:
            contador_pares += 1

        print(lista_obtenida[i])   

        i += 1     

def mostrar_pos_pares(lista_obtenida):
    for i in range(1, len(lista_obtenida), 2):
        print(lista_obtenida[i])

def mostrar_ordenado(lista_obtenida):
    lista_obtenida.sort()

    for i in lista_obtenida:
        print(i) 


def main():
    res = lista_valores()
    # mostrar_valores(res)
    # mostrar_tercer_par(res)
    # mostrar_pos_pares(res)
    # mostrar_ordenado(res)
    print(res[1::2])

main()