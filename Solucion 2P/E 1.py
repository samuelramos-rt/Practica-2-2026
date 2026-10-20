'''
1.  Mostrar los n primeros términos de una progresión aritmética, dado el primer término
    y la diferencia.

Planteamiento:
    - Solicitar al usuario el primer término de la progresión aritmética.
    - Solicitar al usuario la diferencia de la progresión aritmética.
    - Solicitar al usuario el número de términos a mostrar.

formula de la progresión aritmética:
    a_n = a_1 + (n - 1) * d
'''

def mostrar_progresion_aritmetica(primer_termino, diferencia, n):
    for i in range(n):
        termino = primer_termino + i * diferencia
        print(termino)


primer_termino = int(input("primer término P.A.: "))
diferencia = int(input("diferencia de la P.A.: "))
n = int(input("número de términos a mostrar: "))

mostrar_progresion_aritmetica(primer_termino, diferencia, n)
