def contar_caracteres(cadena):
    mayusculas = 0
    minusculas = 0
    otros = 0

    for char in cadena:
        if char != " ":
            if char.isupper():
                mayusculas += 1
            elif char.islower():
                minusculas += 1
            else: 
                otros += 1

    return (mayusculas,minusculas,otros)

# print(contar_caracteres("Hola, ¿qué tal?"))        # ➤ (1, 9, 3)
# print(contar_caracteres("HoLaChAu"))               # ➤ (4, 4, 0)
# print(contar_caracteres(" "))                      # ➤ (0, 0, 0)
# print(contar_caracteres("42910%(@!"))              # ➤ (0, 0, 9)
# print(contar_caracteres("429A10E%(@!"))            # ➤ (2, 0, 9)
# print(contar_caracteres("90em28ú"))                # ➤ (0, 3, 4)
# print(contar_caracteres("A MÍ MI MAMÁ ME MIMA"))   # ➤ (15, 0, 0)

def prueba_covid(temperaturas_corporales, tos_seca, nivel_cansacio):
    sospechosos = []
    TEMPERATURA_COVID = 37
    NIVEL_CANSANCIO_MAX = 6

    for medicion in range(len(temperaturas_corporales)):
        if temperaturas_corporales[medicion] >= TEMPERATURA_COVID and tos_seca[medicion] and nivel_cansacio[medicion] > NIVEL_CANSANCIO_MAX:
            sospechosos.append(medicion)

    return sospechosos


def generar_diccionario(partidos):
    dicc_equipos = {}

    for partido in partidos:
        if partido[0] not in dicc_equipos:
            if partido[2] == 0:
                dicc_equipos[partido[0]] = [1,0,0]
            elif partido[2] == 1:
                dicc_equipos[partido[0]] = [0,1,0]
            else:
                dicc_equipos[partido[0]] = [0,0,1]
        else:
            if partido[2] == 0:
                dicc_equipos[partido[0]][0] += 1
            elif partido[2] == 1:
                dicc_equipos[partido[0]][1] += 1
            else:
                dicc_equipos[partido[0]][2] += 1

        if partido[1] not in dicc_equipos:
            if partido[2] == 0:
                dicc_equipos[partido[1]] = [0,1,0]
            elif partido[2] == 1:
                dicc_equipos[partido[1]] = [1,0,0]
            else:
                dicc_equipos[partido[1]] = [0,0,1]
        else:
            if partido[2] == 0:
                dicc_equipos[partido[1]][1] += 1
            elif partido[2] == 1:
                dicc_equipos[partido[1]][0] += 1
            else:
                dicc_equipos[partido[1]][2] += 1

    return dicc_equipos

def mas_partidos_jugados(dicc_equipos):
    equipos_partidos = []
    mas_partidos = 0

    for equipo,partidos in dicc_equipos.items():
        if sum(partidos) > mas_partidos:
            equipos_partidos = []
            mas_partidos = sum(partidos)
            equipos_partidos.append(equipo)
        
        if equipo not in equipos_partidos and sum(partidos) == mas_partidos:
            equipos_partidos.append(equipo )

    return equipos_partidos

def puntajes_equipo(dicc_equipos):
    equipos_partidos = []

    for equipo,partidos in dicc_equipos.items():
        equipos_partidos.append([partidos[0] * 3 + partidos[2],equipo])

    
    equipos_partidos.sort(reverse=True)

    for equipo in equipos_partidos:
        print(f"{equipo[1]} -> {equipo[0]}")


partidos = [
    ["Boca", "River", 0],  # Ganó Boca
    ["Boca", "San Lorenzo", 1],  # Ganó San Lorenzo
    ["River", "San Lorenzo", 2],  # Empate
    ["River", "Boca", 1],  # Ganó Boca
    ["San Lorenzo", "Boca", 2]  # Empate
]

dicc_equipos = generar_diccionario(partidos)
print(mas_partidos_jugados(dicc_equipos))
puntajes_equipo(dicc_equipos)