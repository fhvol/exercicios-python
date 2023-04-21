if __name__ == '__main__':
    tabela = {1: 4.00, 2: 4.50, 3: 5.00, 4: 2.00, 5: 1.50}
    pedido = int(input('Informe o código do pedido: ' ))
    quantidade = int(input('Informe a quantidade: '))

    valor = tabela[pedido]
    total = quantidade * valor

    print('TOTAL = R$ {:.2f}'.format(total))