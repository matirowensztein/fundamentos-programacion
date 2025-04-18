def es_capicua(valor):
    return "Es capicúa" if valor == valor[::-1] else "No es capicúa"

def ingreso_capicuas():
    no_fin = True

    while no_fin:
        valor = input("Ingrese un número entero positivo o FIN para terminar la ejecución del programa: ")
        
        if valor == "FIN":
            no_fin = False
            print("Fin del programa")
        elif not valor.isdigit():
            print("Número Inválido")
        else:
            print(es_capicua(valor))

ingreso_capicuas()