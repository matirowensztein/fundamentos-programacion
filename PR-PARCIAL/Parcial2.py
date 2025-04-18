def contar(cadena):
    cont = 0
    letras_usadas = ""
    VOCALES_ACENTUADAS = "áÁéÉíÍóÓúÚ"

    for char in cadena.lower():
        if char in VOCALES_ACENTUADAS:
            if char == "á":
                char = "a"
        
            if char == "é":
                char = "e"

            if char == "í":
                char = "i"

            if char == "ó":
                char = "o"

            if char == "ú":
                char = "u"
        
        if char.isalpha() and char not in letras_usadas:
            cont += 1
            letras_usadas += char

    return cont

def elegir(atracciones, actividades_deseadas, monto):
    MONTO_MAXIMO = 5000
    ACTIVIDADES_NECESARIAS = 3
    cont_act_deseadas = 0
    i = 0
    it_valido = False

    if monto <= MONTO_MAXIMO:
        while not it_valido and i < len(actividades_deseadas):
            if actividades_deseadas[i] in atracciones:
                cont_act_deseadas += 1

            if cont_act_deseadas == ACTIVIDADES_NECESARIAS:
                it_valido = True
            
            i += 1

    return it_valido

MAX_COSTO = 5000

# lista_1 = ["museos", "senderismo", "bares", "montañismo"]
# lista_2 = ["bares", "museos", "senderismo", "conciertos"]
# lista_3 = ["bares", "conciertos", "museos"]
# lista_4 = ["senderismo", "museos", "montañismo", "conciertos"]
# lista_5 = ["baile", "navegación", "compras"]

# print(elegir(lista_1, lista_2, 5000))  # True: 3 actividades deseadas (museos, senderismo, bares) y costo ≤ MAX_COSTO
# print(elegir(lista_1, lista_3, 1000))  # False: solo 2 actividades deseadas coinciden
# print(elegir(lista_1, lista_4, 4000))  # True: 3 deseadas (senderismo, museos, montañismo)
# print(elegir(lista_3, lista_2, 6000))  # False: costo supera MAX_COSTO
# print(elegir(lista_5, lista_1, 1000))  # False: no hay coincidencias suficientes
# print(elegir(lista_2, lista_1, 3000))  # True: 3 coincidencias (bares, museos, senderismo)
# print(elegir(lista_4, lista_4, 5000))  # True: todas coinciden

def ordenar_votaciones(votaciones_cargadas):
    lista_votaciones = []

    for participante, puntaje in votaciones_cargadas.items():
        lista_votaciones.append([puntaje[2], participante])

    lista_votaciones.sort(reverse=True)

    for votacion in lista_votaciones:
        print(f"{votacion[1]} - {votacion[0]}")

def camino_a_la_fama(votaciones):
    dicc_votaciones = {}

    for votacion in votaciones:
        sumatoria_puntaje = 0
        cantidad_puntajes = 0
        promedio_puntaje = 0

        if votacion[0] not in dicc_votaciones:
            dicc_votaciones[votacion[0]] = [votacion[1], 1, votacion[1]]
        else: 
            sumatoria_puntaje = dicc_votaciones[votacion[0]][0] + votacion[1]
            cantidad_puntajes = dicc_votaciones[votacion[0]][1] + 1
            promedio_puntaje = sumatoria_puntaje / cantidad_puntajes
            dicc_votaciones[votacion[0]] = [sumatoria_puntaje, cantidad_puntajes, promedio_puntaje]

    return dicc_votaciones

votaciones = [
    ["Luisa", 4],
    ["Mariano", 10],
    ["Luisa", 5],
    ["Ana", 8],
    ["Mariano", 9],
    ["Ana", 10],
    ["Pedro", 7],
    ["Pedro", 6],
    ["Mariano", 8],
    ["Luisa", 6]
]

votaciones_cargadas = camino_a_la_fama(votaciones)
ordenar_votaciones(votaciones_cargadas)