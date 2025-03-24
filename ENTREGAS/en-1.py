def calcular_mcm(num_1, num_2, param_1, param_2):
    mcm = 0

    if num_1 > num_2:
        mcm = num_1
        while mcm % num_2 != 0:
            mcm += num_1
    else:
        mcm = num_2
        while mcm % num_1 != 0:
            mcm += num_2
    
    if not (mcm >= param_1 and mcm <= param_2):
        mcm = 0
    
    return mcm

print(calcular_mcm(10,11,0,12))