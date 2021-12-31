# A soma de dois numeros mais o dobro, triplo e a raiz do resultado da soma.


n = int(input('Digite um número: '))

d = n*2
t = n*3
r = n**(1/2)
print(f'Dado o valor: {n}')
print(f'O dobro é: {d}')
print(f'O triplo é: {t}')
print(f'E a raiz é: {r:.5f}')
