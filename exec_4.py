"4) Escrever um algoritmo que leia uma quantidade desconhecida de números e conte quantos deles estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100]. A entrada de dados deve terminar quando for lido um número negativo."
b26_50 = 0
c51_75 = 0
d76_100 = 0
while n >= 0:
    n = int(input('Digite um valor: '))
    if n >= 0 and n <= 25:
        a0_25 += 1
    elif n >= 26 and n <= 50:
        b26_50 += 1
    elif n >= 51 and n <= 75:
        c51_75 += 1
    elif n >= 76 and n <= 100:
        d76_100 += 1
print('')
print('-=' * 12)
print('Intervalo 0 até 25: {}'.format(a0_25))
print('Intervalo 26 até 50: {}'.format(b26_50))
print('Intervalo 51 até 75: {}'.format(c51_75))
print('Intervalo 76 até 100: {}'.format(d76_100))
print('-=' * 12)