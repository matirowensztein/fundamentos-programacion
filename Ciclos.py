numero = int(input("Ingresa un número para calcular su factorial: "))

factorial = 1
for i in range(1, numero + 1):
    factorial *= i

print(f"El factorial de {numero} es: {factorial}")

total = 0
contador = 0

while True:
    valor = float(input("Ingresa un número (ingresa 0 para terminar): "))
    if valor == 0:
        break
    total += valor
    contador += 1

print(f"Total acumulado: {total}")
print(f"Cantidad de valores ingresados: {contador}")

numero = int(input("Ingresa un número para verificar si es primo: "))

if numero < 2:
    print(f"El número {numero} no es primo.")
else:
    es_primo = True
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            es_primo = False
            break
    
    if es_primo:
        print(f"El número {numero} es primo.")
    else:
        print(f"El número {numero} no es primo.")

for i in range(100, -1, -1):
    if i % 2 == 0:
        print(i)

for i in range(100, -1, -2):
    print(i)
