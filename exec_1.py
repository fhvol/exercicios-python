"1) Desenvolver um algoritmo que efetue a soma de todos os números ímpares que são múltiplos de três e que se encontram no conjunto dos números de 1 até 500:"
soma = 0
for c in range(3, 501, 3):
    if c % 2 != 0:
        soma += c
print('Soma de todos os múltiplos de 3 ímpares entre 1 e 500: {}'.format(soma))