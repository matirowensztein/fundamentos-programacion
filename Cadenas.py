# def es_binario(cadena):
#     binario = True

#     for letra in cadena:
#         if letra != "0" and letra != "1":
#             binario = False

#     return binario

# 

# def validar_caracteres(cadena, caracteres_validos):
#     cadena_valida = True

#     for letra in cadena:
#         if letra not in caracteres_validos:
#             cadena_valida = False

#     return cadena_valida

# print(validar_caracteres("0101010f1", "01e"))

# def verif_mail(mail):
#     mail_valido = True
#     mail_partes = mail.split("@")

#     if mail.count(" ") != 0:
#         mail_valido = False

#     if mail.count("@") != 1:
#         mail_valido = False

#     if mail_partes[0].isalnum() == False:
#         mail_valido = False

#     if mail_partes[1] not in ["fi.uba.ar", "gmail.com"]:
#         mail_valido = False

#     return mail_valido

# print(verif_mail("matias@gmail.com"))

# def es_palindromo(cadena):
#     cadena = cadena.replace(" ", "")
#     return True if cadena == cadena[::-1] else False

# def verificar_palindromo():
#     on_programa = True 

#     while on_programa:
#         cadena = input("Ingrese una cadena (Finaliza cuando de enter, sin ingresar nada): ")

#         if cadena == "":
#             on_programa = False
#         elif not cadena.isalpha() and " " not in cadena:
#             print("Ingreso invalido")
#         else:
#             print(es_palindromo(cadena))

# print(verificar_palindromo())

def devolver_texto(cadena):
    nueva_cadena = ""

    siguiente_mayuscula = False

    for letra in cadena:
        if siguiente_mayuscula:
            nueva_cadena += letra.upper()
            siguiente_mayuscula = False
        else:
            if letra == ".":
                siguiente_mayuscula = True
                
            nueva_cadena += letra.lower()

    return nueva_cadena

cadena = "Escribir una función que reciba por parámetro un texto todo en mayúsculas.La función deberá devolver el texto pero respetando la regla que indica que luego de un punto la primer letra debe ser mayúscula, y el resto minúsculas. ".upper()
print(cadena)

print(devolver_texto(cadena))