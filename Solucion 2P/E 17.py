'''
17. Dado un número natural N de varios dígitos, mostrar cada uno de sus dígitos no primos
    de izquierda a derecha.
Planteamiento:
    - Solicitar al usuario un número natural N.
    - Crear una función que determine si un dígito es primo o no.
    - Crear una función que recorra cada dígito del número N y concatene los dígitos no primos en una cadena.
    - Mostrar la cadena resultante con los dígitos no primos.
'''

def es_primo(digito):
    if digito < 2:
        return False
    contador = 0
    for i in range(2, digito + 1):
        if digito % i == 0:
            contador += 1
    if contador == 1:
        return True
    else:
        return False

def obtener_digitos_no_primos(numero):
    digitos_no_primos = 0
    while numero > 0:
        digito = numero % 10
        numero = numero // 10

        if es_primo(digito):
            digitos_no_primos = digitos_no_primos * 10 + digito
    return digitos_no_primos

def invertir_digitos(numero):
    nuevo_numero = 0
    while numero > 0:
        digito = numero % 10
        numero = numero // 10
        nuevo_numero = nuevo_numero * 10 + digito
    return nuevo_numero

numero = obtener_digitos_no_primos(32450634)    #retorna de derecha a izquierda
nuevo_numero = invertir_digitos(numero)         #retorna de izquierda a derecha 
print(nuevo_numero)                             #salida esperada por el ejercicio
