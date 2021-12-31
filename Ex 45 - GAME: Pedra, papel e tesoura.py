from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print(''' Suas Opções
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
jogador = int(input('Qual a sua jogada: '))
print ('JO')
sleep (1)
print ('KEN')
sleep (1)
print ('PÔ')
sleep (1)
print('-=' * 20)
print(f'Computador: {itens [computador] }')
print(f'Você: {itens[jogador]}')
print('-=' * 20)

if computador == 0:  # computador jogou PEDRA
    if jogador == 0:
        print('EMPATOU')
    elif jogador == 1:
        print('Jogador ganhou')
    elif jogador == 2:
        print('Computador ganhou')
    else:
        print('Jogada invalida.')
elif computador == 1:  # Computador jogou PAPEL
    if jogador == 1:
        print('EMPATOU')
    elif jogador == 0:
        print('Computador ganhou')
    elif jogador == 2:
        print('Você ganhou')
    else:
        print('Jogada invalida.')

elif computador == 2:  # Computador jogou TESOURA
    if jogador == 2:
        print('EMPATOU')
    elif jogador == 0:
        print('Você ganhou')
    elif jogador == 1:
        print('Computador ganhou')
    else:
         print('Jogada invalida.')  
