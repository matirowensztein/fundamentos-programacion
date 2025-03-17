def calcular_factorial(n):
    if n < 0:
        return None  
    
    factorial = 1
    
    for i in range(1, n + 1):
        factorial *= i
    return factorial

while True:
    numero = int(input("Ingresa un número para calcular su factorial: "))
    
    factorial = calcular_factorial(numero)
    
    if factorial is None:
        print("No se puede calcular el factorial de un número negativo.")
    else:
        print(f"El factorial de {numero} es: {factorial}")
    
    continuar = input("¿Quieres ingresar otro número? (si/no): ").lower()

    if continuar != 'si':
        break

def multiplicar_por_sumas(x, y):
    resultado = 0
    for i in range(abs(y)): 
        resultado += x

    if y < 0:
        resultado = -resultado  
    return resultado

x = int(input("Ingresa el primer número: "))
y = int(input("Ingresa el segundo número: "))

resultado = multiplicar_por_sumas(x, y)

print(f"El resultado de multiplicar {x} por {y} es: {resultado}")

def control_ascensor():
    peso_maximo = 400
    personas_maximas = 6
    peso_actual = 0
    cantidad_personas = 0
    
    while True:
        peso = float(input("Ingresa el peso de la persona (0 para terminar): "))
        
        if peso == 0:
            if cantidad_personas == 0:
                print("No hay personas en el ascensor.")
            else:
                print("Ascensor en movimiento.")
            break
        
        if peso_actual + peso > peso_maximo:
            print("¡Se ha excedido el peso máximo del ascensor!")
            break
        
        if cantidad_personas == personas_maximas:
            print("¡Se ha excedido el número máximo de personas en el ascensor!")
            break
        
        peso_actual += peso
        cantidad_personas += 1
        print(f"Persona subida. Peso total: {peso_actual} kg. Personas a bordo: {cantidad_personas}.")

control_ascensor()