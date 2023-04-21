if __name__ == '__main__':
    valores = input('Informe 3 valores colocando espaço entre eles: ').split()
    a, b, c = float(valores[0]), float(valores[1]), float(valores[2])
    if a + b > c and a + c > b and b + c > a:
        perimetro = a + b + c
        print("Perimetro = {:.1f}".format(perimetro))
    else:
        area = ((a + b) * c) / 2
        print("Area = {:.1f}".format(area))