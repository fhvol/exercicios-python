"9) Escreva um algoritmo que leia um valor inicial A e uma razão R e imprima uma seqüência em P.G. contendo 10 valores."
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
pa = primeiro
for c in range(1, 11):
    print('{} -> '.format(pa), end='')
    pa *= razão
print('FIM')