def menor_venta_sucursal(sucursal, total_sucursal, menor_venta): 
    if sucursal == 0:
            menor_venta[1] = total_sucursal
    else:
        if total_sucursal < menor_venta[1]:
            menor_venta[0] = sucursal
            menor_venta[1] = total_sucursal

    return menor_venta

def mayor_venta_semana(semana):
    dia_venta = [0,0]

    for dia in range(len(semana)):
        if semana[dia] > dia_venta[1]:
            dia_venta[0] = dia
            dia_venta[1] = semana[dia]

    return dia_venta

def gestion_comercio(sucursales):
    total_ventas = 0
    total_sucursal = 0
    menor_venta = [0,0]
    semana = [0,0,0,0,0]

    for sucursal in range(len(sucursales)):
        for dia in range(len(sucursales[sucursal])):
            total_ventas += sucursales[sucursal][dia]
            total_sucursal += sucursales[sucursal][dia]
            semana[dia] += sucursales[sucursal][dia]

        menor_venta = menor_venta_sucursal(sucursal, total_sucursal, menor_venta)
        
        total_sucursal = 0

    print(f"El total semanal de ventas es {total_ventas}")
    
    print(f"La sucursal que vendió menos fue la sucursal {menor_venta[0] + 1} con un total de ventas de {menor_venta[1]}.")
    
    print(f"El día que se vendió más fue el día {mayor_venta_semana(semana)[0] + 1} con un total de ventas de {mayor_venta_semana(semana)[1]}.") 

def main():
    ventas = [
    [100, 150, 130, 120, 160],
    [80, 140, 110, 90, 100],
    [200, 220, 210, 230, 250]
    ]
    gestion_comercio(ventas)

if __name__ == "__main__":
    main()