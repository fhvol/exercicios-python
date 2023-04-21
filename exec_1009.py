if __name__ == '__main__':
    nome = str(input('Informe o nome do vendedor: '))
    salFixo = float(input('Salário fixo: '))
    totalVendas = float(input('Total de vendas: '))
    comissao = totalVendas * 0.15
    salFinal = salFixo + comissao
    print('O salário + comissão foi {:.2f}'.format(salFinal))