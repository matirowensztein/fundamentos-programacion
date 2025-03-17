num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

if num1 > num2:
    print(f"El mayor número es: {num1}")
else:
    print(f"El mayor número es: {num2}")

num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

if num1 == num2:
    print("Los dos números son iguales.")
elif num1 > num2:
    print(f"El mayor número es: {num1}")
else:
    print(f"El mayor número es: {num2}")

numero = int(input("Ingresa un número entero: "))

if numero % 2 == 0:
    print(f"El número {numero} es par.")
else:
    print(f"El número {numero} es impar.")

numero = float(input("Ingresa un número: "))

if numero > 0:
    print(f"El número {numero} es positivo.")
elif numero < 0:
    print(f"El número {numero} es negativo.")
else:
    print("El número ingresado es neutro.")

palabra1 = input("Ingresa la primera palabra: ")
palabra2 = input("Ingresa la segunda palabra: ")
palabra3 = input("Ingresa la tercera palabra: ")

palabras = [palabra1, palabra2, palabra3]
palabras.sort()

print("Las palabras en orden alfabético son:", palabras)
