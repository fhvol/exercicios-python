"7) Escrever um algoritmo que leia um valor para uma variável N de 1 a 10 e calcule a tabuada de N. Mostre a tabuada na forma: 0 x N = 0, 1 x N = 1N, 2 x N = 2N, ..., 10 x N = 10N."
resultado = 0
num = int(input('Digite um valor para\ncalcular sua tabuada: '))
for c in range(1, 11):
    resultado = num * c
    print('{} x {} = {}'.format(num, c, resultado))