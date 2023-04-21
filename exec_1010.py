if __name__ == '__main__':
    valoresA = input("Digite o código da peça 1, o número de peças e o valor unitário: ").split()
    a1, b1, c1 = int(valoresA[0]), int(valoresA[1]), float(valoresA[2])
    valoresB = input("Digite o código da peça 2, o número de peças e o valor unitário: ").split()
    a2, b2, c2 = int(valoresB[0]), int(valoresB[1]), float(valoresB[2])
    total = (b1 * c1) + (b2 * c2)
    print('VALOR A PAGAR = R$ {:.2f}'.format(total))