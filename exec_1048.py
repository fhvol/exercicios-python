salario = float(input("Digite o salário do funcionário: "))
if salario <= 400.00:
    novo_salario = salario * 1.15
    reajuste = salario * 0.15
    indice = 15
elif salario <= 800.00:
    novo_salario = salario * 1.12
    reajuste = salario * 0.12
    indice = 12
elif salario <= 1200.00:
    novo_salario = salario * 1.10
    reajuste = salario * 0.10
    indice = 10
elif salario <= 2000.00:
    novo_salario = salario * 1.07
    reajuste = salario * 0.07
    indice = 7
else:
    novo_salario = salario * 1.04
    reajuste = salario * 0.04
    indice = 4
print("Novo salario: R$ %.2f" % novo_salario)
print("Reajuste ganho: R$ %.2f" % reajuste)
print("Em percentual: %d %%" % indice)