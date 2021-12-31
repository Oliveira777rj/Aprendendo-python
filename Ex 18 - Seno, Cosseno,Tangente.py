# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import radians, sin, cos, tan
ang =float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(ang))
cos = cos(radians(ang))
tan = tan(radians(ang))

print(f'O ângulo {ang} tem o seno de {seno:.2f}')
print(f'O cosseno de {cos:.2f}')
print(f'E a tangente de {tan:.2f}')
