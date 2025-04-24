from datetime import date

FIN_DE_ARCHIVO = ("", "", "")

def abrir_archivo(ruta, modo = 'r'):
    try:
        archivo = open(ruta, modo)
    except FileNotFoundError:
        archivo = open(ruta, "x")
        archivo.close()
        archivo = open(ruta, modo)

    return archivo

def obtener_linea_csv(archivo, fin_archivo = FIN_DE_ARCHIVO):
    linea = archivo.readline()
    
    if linea == "":
        resultado = fin_archivo
    else:
        resultado = linea.rstrip().split(',')

    return resultado

def vacunados_fuera_de_termino():
    fecha_actual = str(date.today())

    archivo = abrir_archivo('C:/Users/matia/Code/fundamentos-programacion/AR/vacunaciones.csv')

    archivoEscritura = abrir_archivo('AR/archivos/infraganti.txt', 'w')

    linea = obtener_linea_csv(archivo)

    while linea != FIN_DE_ARCHIVO:
        nombre, apellido, fecha_vacunacion = linea

        if fecha_vacunacion > fecha_actual:
            archivoEscritura.write(f"{nombre}\n")
        
        linea = obtener_linea_csv(archivo)

    # Cerraramos los archivos
    archivo.close()
    archivoEscritura.close()

vacunados_fuera_de_termino()

def vacunados_por_zona():
    vacunas_pais = 0
    vacunas_ciudad = 0
    vacunas_vacunatorio = 0

    archivo = abrir_archivo('C:/Users/matia/Code/fundamentos-programacion/AR/vacunas_otorgadas.csv')

    linea = obtener_linea_csv(archivo)

    ciudad, vacunatorio, vacunas = linea

    while linea != FIN_DE_ARCHIVO: 
        ciudad_actual = ciudad

        while linea != FIN_DE_ARCHIVO and ciudad_actual == ciudad:
            vacunatorio_actual = vacunatorio

            while linea != FIN_DE_ARCHIVO and ciudad_actual == ciudad and vacunatorio_actual == vacunatorio:
                vacunas_pais += int(vacunas)
                vacunas_ciudad += int(vacunas)
                vacunas_vacunatorio += int(vacunas)

                linea = obtener_linea_csv(archivo)
                ciudad, vacunatorio, vacunas = linea

            print(f"El vacunatorio: {vacunatorio_actual}, dio {vacunas_vacunatorio} vacunas")
            vacunas_vacunatorio = 0

        print(f"La ciudad de {ciudad_actual} dio {vacunas_ciudad} vacunas")
        vacunas_ciudad = 0
        

    print(f"El pais dio {vacunas_pais} vacunas")

    archivo.close()

vacunados_por_zona()