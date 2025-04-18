def validar_cadena(cadena):
    cadena_valida = True
    contiene_mayus = False
    contiene_minus = False
    contiene_num = False
    contiene_simb = False
    no_contiene_simb = False
    LARGO_CADENA = len(cadena)
    MINIMO_CADENA = 8
    MAXIMO_CADENA = 12
    SIMBOLOS = ["*", "-", "$", "@"]
    CHAR_ACENTUDADOS = "áÁéÉíÍóÓÚuÚ"

    if LARGO_CADENA < MINIMO_CADENA or LARGO_CADENA > MAXIMO_CADENA:
        cadena_valida = False

    for char in cadena:
        if char.isupper():
            contiene_mayus = True

        if char.islower():
            contiene_minus = True

        if char.isnumeric():
            contiene_num = True

        if char in SIMBOLOS:
            contiene_simb = True

        if (not char.isalnum() and char not in SIMBOLOS) or (char in CHAR_ACENTUDADOS):
            no_contiene_simb = True


    if not contiene_mayus or not contiene_minus or not contiene_num or not contiene_simb or no_contiene_simb:
        cadena_valida = False

    print(cadena_valida)


def mostrar_resultados_ordenados(votos_por_partido):
    """Muestra los partidos y sus votos totales ordenados de mayor a menor, sin usar key."""
    # Creamos una lista con (total_votos, partido)
    lista_aux = []

    for partido, total in votos_por_partido.items():
        lista_aux.append((total, partido))

    # Ordenamos por total de votos (ya están primero en la tupla)
    lista_aux.sort(reverse=True)

    print("Partido - Total de votos")
    for total, partido in lista_aux:
        print(f"{partido} - {total}")

def partidos(votacion):
    dicc_partidos = {}
    total_votos = 0

    for partido in votacion:
        total_votos = partido[1] + partido[2]

        if partido[0] not in dicc_partidos:
            dicc_partidos[partido[0]] = total_votos
        else:
            dicc_partidos[partido[0]] += total_votos

        total_votos = 0

    # for clave_partido,votos_partido in dicc_partidos.items():
    #     mayor_votos.append([clave_partido,votos_partido])

    # mayor_votos.sort(
    #     key=lambda item: item[1],
    #     reverse=True
    # )

    # print(mayor_votos)

    return dicc_partidos



part = partidos([ ["PSOE", 20, 30], ["VOX", 15, 15], ["PP", 0, 15], ["PP", 19, 35]])

mostrar_resultados_ordenados(part)