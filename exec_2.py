"2) Desenvolver um algoritmo que leia a altura de 15 pessoas. Este programa deverá calcular e mostrar"
"a. A menor altura do grupo;"
"b. A maior altura do grupo;"
maiorAltura = 0
menorAltura = 1000
for c in range(1, 16):
    altura = float(input('Digite o valor da altura {}: '.format(c)))
    if altura > maiorAltura:
        maiorAltura = altura
    if altura < menorAltura:
        menorAltura = altura
print('Maior altura: {}'.format(maiorAltura))
print('Menor altura: {}'.format(menorAltura))

