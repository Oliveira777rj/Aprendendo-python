#if simples, sem o uso do else.

vel = float(input('QUal a sua velocidade? '))

if vel > 80:
    print('Você excedeu o limite de velocidade de 80 KM/H.')
    multa = (vel-80)*7
    print(f'Você devera pagar uma multa de R${multa:.2f}!')

print('Boa viagem, dirija com cuidado.')