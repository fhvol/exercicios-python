a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))
maior = a
if b > maior:
    maior = b
if c > maior:
    maior = c
print("%.1f eh o maior" % maior)