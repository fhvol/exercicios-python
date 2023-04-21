if __name__ == '__main__':
    dist = int(input('Qual a distância percorrida? '))
    combustivel = float(input('Qual o total de combustível gasto? '))
    consumo = dist / combustivel
    print('{:.3f} km/l'.format(consumo))