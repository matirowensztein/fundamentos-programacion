
INCIO = 0

def main():
    # Abrir un archivo para lectura
    archivo = open("C:/Users/matia/Code/fundamentos-programacion/AR/archivos/dummy.txt", 'r')

    # Leer el archivo linea por linea
    linea = archivo.readline()
    while linea != '':
        print(linea, end='') 
        linea = archivo.readline()

    # Vuelvo al incio del archivo
    archivo.seek(1, INCIO)

    print('')
    print('')

    # Leer el archivo con todo el archivo en memoria <-- MAL
    for linea in archivo:
        print(linea, end='')

    # Cerrar el archivo <-- IMPORTANTE
    archivo.close()

main()
