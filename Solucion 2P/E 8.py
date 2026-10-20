'''
8.  Convertir una temperatura de grados Celsius a grados Farenheit, o a la inversa,
    conforme a lo que solicite el usuario.

Planteamiento:
    - Solicitar al usuario la temperatura a convertir.
    - Solicitar al usuario la unidad de medida de la temperatura a convertir (C o F).
    - Convertir la temperatura a la unidad de medida solicitada.
    - Mostrar la temperatura convertida.

formulas de conversión:
    C = (F - 32) * 5/9
    F = C * 9/5 + 32
'''

def convertir_temperatura(temperatura, unidad):
    if unidad.upper() == 'C':
        return (temperatura * 9/5) + 32
    elif unidad.upper() == 'F':
        return (temperatura - 32) * 5/9
    else:
        return "Unidad de medida no válida. Use 'C' para Celsius o 'F' para Farenheit."

temperatura = float(input("Ingrese la temperatura a convertir: "))
unidad = input("Ingrese la unidad de medida de la temperatura a convertir (C o F): ")

resultado = convertir_temperatura(temperatura, unidad)

if unidad.upper() == 'C':
    print(f"\n{temperatura} grados Celsius son {resultado} grados Farenheit.\n")
elif unidad.upper() == 'F':
    print(f"\n{temperatura} grados Farenheit son {resultado} grados Celsius.\n")
else:
    print(f"\n{resultado}\n")