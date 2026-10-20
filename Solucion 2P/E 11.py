'''
11. Dadas la masa, la altura y la velocidad de un cuerpo, calcular su energía mecánica
    como suma de su energía potencial y su energía cinética.

Planteamiento:
    - Solicitar al usuario la masa del cuerpo.
    - Solicitar al usuario la altura del cuerpo.
    - Solicitar al usuario la velocidad del cuerpo.
    - Calcular la energía potencial del cuerpo.
    - Calcular la energía cinética del cuerpo.
    - Calcular la energía mecánica del cuerpo como suma de su energía potencial y su energía cinética.
    - Mostrar la energía mecánica del cuerpo.
    
formulas de energía:
    E_p = m * g * h
    E_c = 1/2 * m * v^2
    E_m = E_p + E_c
'''
def calcular_energia_mecanica(masa, altura, velocidad):
    g = 9.8  # aceleración debida a la gravedad en m/s^2
    E_p = masa * g * altura
    E_c = 0.5 * masa * (velocidad ** 2)
    E_m = E_p + E_c
    return E_m

masa = float(input("Ingrese la masa del cuerpo (en kg): "))
altura = float(input("Ingrese la altura del cuerpo (en metros): "))
velocidad = float(input("Ingrese la velocidad del cuerpo (en m/s): "))
energia_mecanica = calcular_energia_mecanica(masa, altura, velocidad)
print(f"\nLa energía mecánica del cuerpo es: {energia_mecanica} Joules.\n")
