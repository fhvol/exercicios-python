import math

if __name__ == '__main__':
    p1 = input('Informe os pontos x e y para p1: ').split()
    x1, y1 = float(p1[0]), float(p1[1])
    p2 = input('Informe x e y para p2: ').split()
    x2, y2 = float(p2[0]), float(p2[1])
    distacia = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    print('{:.4f}'.format(distacia))