if __name__ == '__main__':
    x = float(input('Valor de x: '))
    y = float(input('Valor de y: '))
    if x == y == 0:
        print('Origem!')
    elif x < y:
        print('Q2')
    elif x > y:
        print('Q4')
    elif x < 0 and y < 0:
        print('Q3')
    elif x > 0 and y > 0:
        print('Q1')