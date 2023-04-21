if __name__ == '__main__':
    fun = int(input('Informe o número de funcionários: '))
    horas = int(input('Informe as horas trabalhadas: '))
    valorHoras = float(input('Informe o valor das horas: '))
    salary = horas * valorHoras
    print('NUMBER = {} \nSALARY = US {:.2f}'.format(fun, salary))