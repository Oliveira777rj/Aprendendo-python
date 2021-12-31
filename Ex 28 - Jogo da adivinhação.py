
from random import randint
from time import sleep

comp = randint (1, 5)  # computador "pensando"
print('-=-'*25)
print(f'Vou pensar em numero de 1 a 5 tente adivinhar...' )
print('-=-'*25)

jog = int(input('Qual numero entre 1 e 5 pensou? '))
print('PROCESSANDO ...')
sleep(3)

if comp==jog:
    print ('Você acertou, parabéns')
else: 
    print(f'Eu ganhei o numero escolhido foi {comp}, sinto muito.')












