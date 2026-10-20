'''
20. Obtener el producto de dos números enteros, empleando únicamente sumas.

Planteamiento:
    - Solicitar al usuario dos números enteros.
    - Crear una función que reciba los dos números y calcule el producto mediante sumas.
    - Mostrar el resultado del producto.
'''
def multiplicar(a, b):
    resultado = 0
    for i in range(b):
        resultado += a
    return resultado

a = int(input("Ingrese el primer número entero: "))
b = int(input("Ingrese el segundo número entero: "))
producto = multiplicar(a, b)
print(f"El producto de {a} y {b} es: {producto}")