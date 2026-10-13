'''
1.  Dados dos puntos A y B en el plano coordenado cartesiano XY, mostrar la ecuación de
    la recta que pasa por estos puntos en la forma y = mx + b, o bien x = a (recta vertical).
    Mostrar un mensaje si los puntos son coincidentes.

planteamiento:
    - Solicitar al usuario las coordenadas de los puntos A y B.
    - Calcular la pendiente m de la recta que pasa por los puntos A y B
    - Calcular la ordenada al origen b de la recta que pasa por los puntos A y B
    - Mostrar la ecuación de la recta en la forma y = mx + b, o bien x = a (recta vertical).
    - Mostrar un mensaje si los puntos son coincidentes.

formula de la recta:
    m = (y2 - y1) / (x2 - x1)
    b = y1 - m * x1
'''

def calcular_ecuacion_recta(x1, y1, x2, y2):
    if x1 == x2 and y1 == y2:
        return "Los puntos son coincidentes."
    elif x1 == x2:
        return f"La ecuación de la recta es: x = {x1} (recta vertical)."
    else:
        m = (y2 - y1) / (x2 - x1)
        b = y1 - m * x1
        return f"La ecuación de la recta es: y = {m}x + {b}."

x1 = float(input("Ingrese la coordenada x del punto A: "))
y1 = float(input("Ingrese la coordenada y del punto A: "))
x2 = float(input("Ingrese la coordenada x del punto B: "))
y2 = float(input("Ingrese la coordenada y del punto B: "))
print(calcular_ecuacion_recta(x1, y1, x2, y2))