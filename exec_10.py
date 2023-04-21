"10) Escreva um algoritmo que leia um valor inicial A e imprima a seqüência de valores do cálculo de A! e o seu resultado. Ex: 5! = 5 X 4 X 3 X 2 X 1 = 120"
num = int(input('Digite um número para\ncalcular seu fatorial: '))
print('{}! ='.format(num), end='')
resultado = 1
for c in range(num, 0, -1):
    resultado *= c
    print(' {} '.format(c), end='')
    print('x' if c > 1 else '=', end='')
print(' {}'.format(resultado))