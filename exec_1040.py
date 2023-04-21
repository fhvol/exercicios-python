if __name__ == '__main__':
    n1 = float(input('Escreva a nota n1 do aluno: '))
    n2 = float(input('Escreva a nota n2 do aluno: '))
    n3 = float(input('Escreva a nota n3 do aluno: '))
    n4 = float(input('Escreva a nota n4 do aluno: '))
    p1 = 2 * n1
    p2 = 3 * n2
    p3 = 4 * n3
    p4 = 1 * n4
    media = (p1 + p2 + p3 + p4)/10
    if media >= 7.0:
        print('Aluno aprovado!')
    elif media < 5.0:
        print('Aluno Reprovado!')
    elif media >= 5 and media <= 6.9:
        print('Aluno em exame!')
        notaexame = float(input('Nota do exame: '))
        mediageral = (media + notaexame) / 2
        if mediageral >= 5:
            print('Aluno Aprovado!')
        else:
            print('Aluno Reprovado!')
        print('Media Final: {}'.format(mediageral))