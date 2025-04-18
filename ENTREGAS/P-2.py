def elegir(actividades, actividades_deseadas, valor_cuotas):
    MAX_CUOTA = 6000
    club_valido = True
    cont_actividades_deseadas = 0
    i = 0

    if valor_cuotas > MAX_CUOTA:
        club_valido = False
    else:
        while cont_actividades_deseadas < 2 and i < len(actividades_deseadas):
            if actividades_deseadas[i] in actividades:
                cont_actividades_deseadas += 1

            i += 1
        
        if cont_actividades_deseadas < 2:
            club_valido = False

    return club_valido

