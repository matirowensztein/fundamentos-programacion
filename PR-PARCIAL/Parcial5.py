def contar_vocales(cadena):
    a = 0
    e = 0
    i = 0
    o = 0
    u = 0

    VOCALES = "aeiou"

    for char in cadena.lower():
        if char in VOCALES:
            if char == "a":
                a += 1
            elif char == "e":
                e += 1
            elif char == "i":
                i += 1
            elif char == "o":
                o += 1
            else:
                u += 1

    return (a,e,i,o,u)

# print(contar_vocales("aeiou"))                  # ➤ (1, 1, 1, 1, 1)
# print(contar_vocales(""))                        # ➤ (0, 0, 0, 0, 0)
# print(contar_vocales("Yo los conozco, son ocho los monos!"))  # ➤ (0, 0, 0, 11, 0)
# print(contar_vocales("MURCIÉLAGO"))              # ➤ (1, 0, 1, 1, 1)
# print(contar_vocales("3004924024004232-1"))      # ➤ (0, 0, 0, 0, 0)
# print(contar_vocales("AaáEeiIOoUuÚ"))            # ➤ (2, 2, 2, 2, 2)


def aprobo_cursada(puntajes_maximos, puntajes_recibidos):
    aprobo = True
    i = 0

    while aprobo and i < len(puntajes_maximos):
        if puntajes_maximos[i] * 0.6 > puntajes_recibidos[i]:
            aprobo = False

        i += 1

    return aprobo

# print(aprobo_cursada([10, 20, 15], [6, 15, 12]))    # ➤ True (todos ≥ 60%)
# print(aprobo_cursada([10, 20, 15], [6, 8, 12]))     # ➤ False (8 < 12 en actividad 2)
# print(aprobo_cursada([10, 20, 15, 30], [6, 12, 9, 12]))  # ➤ False (12 < 18 en actividad 4)

# def promedio_mundial(sistema_previsional):
#     total_personas_mundial = 0
#     total_trabajando_mundial = 0
#     total_jubilado_mundial = 0
#     total_desempleado_mundial = 0

#     for pais in sistema_previsional:
#         total_trabajando_mundial += sistema_previsional[pais][0]
#         total_jubilado_mundial += sistema_previsional[pais][1]
#         total_desempleado_mundial += sistema_previsional[pais][2]
#         total_personas_mundial += sistema_previsional[pais][0] + sistema_previsional[pais][1] +sistema_previsional[pais][2]

#     print(f"El promedio de personas trabajando a nivel mundial es: {(total_trabajando_mundial / total_personas_mundial) * 100}")
#     print(f"El promedio de personas jubiladas a nivel mundial es: {(total_jubilado_mundial / total_personas_mundial) * 100}")
#     print(f"El promedio de personas desempleadas a nivel mundial es: {(total_desempleado_mundial / total_personas_mundial) * 100}")

def ordenar_tasa_desempleo(sistema_previsional):
    lista_pais_ordenada = []

    for pais in sistema_previsional:
        tasa_desempleo = (sistema_previsional[pais][2] / sistema_previsional[pais][0]) * 100
        jubilados_trabajadores = (sistema_previsional[pais][1] / sistema_previsional[pais][0]) * 100

        lista_pais_ordenada.append([tasa_desempleo, jubilados_trabajadores, pais])

    lista_pais_ordenada.sort(reverse=True)

    for pais in range(len(lista_pais_ordenada)):
        print(f"{lista_pais_ordenada[pais][2]} - {lista_pais_ordenada[pais][0]} - {lista_pais_ordenada[pais][1]}")


def generar_diccionario_grupo(sistema_provisional):
    dicc_grupo = {}

    for pais in sistema_previsional:
        if sistema_previsional[pais][3] not in dicc_grupo:
            dicc_grupo[sistema_previsional[pais][3]] = [sistema_previsional[pais][0], sistema_previsional[pais][1], sistema_previsional[pais][2]]
        else:
            dicc_grupo[sistema_previsional[pais][3]][0] += sistema_previsional[pais][0]
            dicc_grupo[sistema_previsional[pais][3]][1] += sistema_previsional[pais][1]
            dicc_grupo[sistema_previsional[pais][3]][2] += sistema_previsional[pais][2]

    return dicc_grupo

sistema_previsional = {
    "Argentina": [18000, 7000, 2000, "Mercosur"],
    "Alemania": [40000, 15000, 3000, "Unión Europea"],
    "Brasil": [30000, 10000, 4000, "Mercosur"]
}

# promedio_mundial(sistema_previsional)
# ordenar_tasa_desempleo(sistema_previsional)
print(generar_diccionario_grupo(sistema_previsional))