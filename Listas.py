import random

# def orden_tupla(tupla):
#     creciente = False
#     decreciente = False
#     desordenado = False
#     res = 0

#     for elem in range(0, len(tupla)-1):
#             if tupla[elem] <= tupla[elem + 1]:
#                 creciente = True

#             if tupla[elem] >= tupla[elem + 1]:
#                 decreciente = True

#     if creciente and decreciente:
#         res = 0
#     elif creciente:
#         res = 1
#     else:
#         res = -1

#     return res

# print(orden_tupla((4,4,3)))

# def es_primo(valor):
#     primo = True
#     i = 1

#     if valor == 1:
#         primo = True
#     else:
#         while primo and i < valor ** 0.5:
#             if valor % i == 0 and i != 1:
#                 primo = False
            
#             i += 1
    
#     return primo
            

# def primos_aleatorios():
#     suma_acumulada = 0

#     valores_aleatorios = tuple(random.randint(0, 10000) for _ in range(100))

#     for num in valores_aleatorios:
#         if es_primo(num):
#             print(num)
#             suma_acumulada += num

#     return f"La suma acumulada es de: {suma_acumulada}"
    
# print(primos_aleatorios())

# def fibonacci(posicion):
#     lista_nums = [0,1]

#     for _ in range(posicion):
#         lista_nums.append(lista_nums[-1] + lista_nums[-2])
    
#     return lista_nums[: posicion + 1]

# print(fibonacci(12))


