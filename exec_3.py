"3) Desenvolver um algoritmo que leia um número não determinado de valores e calcule e escreva a média aritmética dos valores lidos, a quantidade de valores positivos, a quantidade de valores negativos e o percentual de valores negativos e positivos."
qtdPositivos = 0
qtdNegativos = 0
soma = 0
contador = 0
num = 0
while num != -100:
    num = int(input('Digite um valor(-100 p/ sair): '))
    if num != -100:
        contador += 1
        soma += num
        if num >= 0:
            qtdPositivos += 1
        else:
            qtdNegativos += 1
percentualTotal = qtdPositivos + qtdNegativos
percentualPositivos = qtdPositivos*100/percentualTotal
percentualNegativos = qtdNegativos*100/percentualTotal
media = soma / contador
print('\nMédia dos valores: {}'.format(media))
print('Quantidade de valores positivos: {}'.format(qtdPositivos))
print('Quantidade de valores negativos: {}'.format(qtdNegativos))
print('{:.0f}% dos valores são positivos e {:.0f}% são negativos'.format(percentualPositivos, percentualNegativos))