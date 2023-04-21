"5) Faça um algoritmo estruturado que leia uma quantidade não determinada de números positivos. Calcule a quantidade de números pares e ímpares, a média de valores pares e a média geral dos números lidos. O número que encerrará a leitura será zero."
soma = 0
somaPares = 0
qtdPares = 0
qtdImpares = 0
num = 1
while num > 0:
    num = int(input('Digite um valor: '))
    soma += num
    if num > 0:
        if num % 2 == 0:
            qtdPares += 1
            somaPares += num
        else:
            qtdImpares += 1
    elif num < 0:
        print('Número inválido')
        num = int(input('Digite um valor válido: '))
        soma += num
print('Números pares: {}'.format(qtdPares))
print(('Números ímpares: {}'.format(qtdImpares)))
print('Média dos pares: {}'.format(somaPares/qtdPares))
print('Média total: {}'.format(soma/qtdPares+qtdImpares))