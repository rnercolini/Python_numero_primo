# Verifica se um número é primo
n = int(input('Digite um número inteiro: '))
cont = 0
for c in range(1, n + 1):
    if n % c == 0:
        cont += 1
if cont == 2:
    print('O número {} é um número primo.'.format(n))
else:
    print('O número {} não é um número primo.'.format(n))
