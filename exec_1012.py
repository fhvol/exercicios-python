import math
A = float(input("Digite o valor de A: "))
B = float(input("Digite o valor de B: "))
C = float(input("Digite o valor de C: "))
area_triangulo = (A * C) / 2
area_circulo = math.pi * (C ** 2)
area_trapezio = ((A + B) * C) / 2
area_quadrado = B ** 2
area_retangulo = A * B
print("Área do triângulo retângulo: %.4f" % area_triangulo)
print("Área do círculo: %.4f" % area_circulo)
print("Área do trapézio: %.4f" % area_trapezio)
print("Área do quadrado: %.4f" % area_quadrado)
print("Área do retângulo: %.4f" % area_retangulo)