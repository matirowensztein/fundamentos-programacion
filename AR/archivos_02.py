
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
    linea = archivo.readline() # Todo lo que se lee del archivo es una string
    
    if linea == "":
        resultado = fin_archivo
    else:
        resultado = linea.rstrip().split(',')

    return resultado

def main():
    # Abrir el archivo para lectura
    archivo = abrir_archivo('C:/Users/matia/Code/fundamentos-programacion/AR/dummy_csv.csv')
    # Abrir el archivo para escritura
    archivoEscritura = abrir_archivo('temp.csv', 'w')

    linea = obtener_linea_csv(archivo)
    while linea != FIN_DE_ARCHIVO:
        nombre, edad, dni = linea

        # Muestro por pantalla el contenido del archivo
        print(f"Nombre: {nombre}, Edad: {edad}, DNI: {dni}")

        # Escribo en el archivo de salida los datos originales con 1 mas de edad
        archivoEscritura.write(f"{nombre},{int(edad) + 1},{dni}\n")
        
        linea = obtener_linea_csv(archivo)

    # Cerraramos los archivos
    archivo.close()
    archivoEscritura.close()

main()