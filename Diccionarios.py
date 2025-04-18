# def reponer_stock(id_stock):
#     for prod in id_stock:
#         if id_stock[prod][0] > id_stock[prod][1]:
#             print(f"Del producto con id: {prod}, se deben reponer {id_stock[prod][0] - id_stock[prod][1]} productos.")

# reponer_stock({
#     "A101": [10, 4],   # stock mínimo 10, actual 5 → falta 5
#     "B202": [8, 12],   # stock mínimo 8, actual 12 → ok
#     "C303": [15, 15],  # stock justo → ok
#     "D404": [20, 10]   # falta 10
# }
# )

# def repeticiones_palabra(texto):
#     cont_palabras = {}
#     palabra = ""

#     for letra in texto.lower():
#         if letra != " ":
#             palabra += letra
#         else:
#             if palabra not in cont_palabras:
#                 cont_palabras[palabra] = 1
#             else:
#                 cont_palabras[palabra] += 1

#             palabra = ""

#     return cont_palabras

# print(repeticiones_palabra("El sol brilla en el cielo y el sol sopla sobre el mar"))

def promedio_alumno(alumnos):
    lista_promedios = []

    for alumno in alumnos:
        lista_promedios.append(sum(alumnos[alumno]) / len(alumnos[alumno])) 

    return lista_promedios

def gestionar_datos_alumnos():
    alumnos = {}
    fin_programa = False

    while not fin_programa:
        padron = int(input("Ingrese su numero de padron: "))

        while padron < 0 or padron > 10000:
            padron = int(input("Ingreso un padron incorrecto, ingrese nuevamente su numero de padron: "))
        
        if padron == 0:
            fin_programa = True
        else:
            nota = int(input("Ingrese su nota: "))

            while nota < 0 or nota > 10:
                nota = int(input("Ingreso una nota incorrecta, ingrese nuevamente su nota: "))

            if padron not in alumnos:
                alumnos[padron] = [nota]
            else:
                alumnos[padron].append(nota)


    print(alumnos)
    print(promedio_alumno(alumnos))

gestionar_datos_alumnos()