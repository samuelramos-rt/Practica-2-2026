'''
14. Obtener el factorial de un número, utilizando operaciones de suma y/o resta
    únicamente.

Planteamiento:
    - Solicitar al usuario un número entero positivo.
    - Crear una funcion que calcule la multiplicación de dos números utilizando únicamente sumas.
    - Crear una funcion que calcule el factorial del número ingresado utilizando la funcion de multiplicación.
    - Mostrar el resultado del factorial.
'''

def multiplicar(a, b):
    resultado = 0
    for i in range(b):
        resultado += a
    return resultado

def factorial(n):
    if n >= 0 and n == 1:
        return 1
    elif n < 0:
        return "El factorial no está definido para números negativos."
    else:
        resultado = 1
        for i in range(2, n + 1):
            resultado = multiplicar(resultado, i)
        return resultado

numero = int(input("Ingrese un numero para calcular su factorial "))
resultado = factorial(numero)

print(resultado)

