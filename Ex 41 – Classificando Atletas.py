from datetime import date
atual = date.today ().year
nascimento = int(input('Digite seu ano de nascimento: '))
idade = atual - nascimento

print(f'O atleta tem {idade} anos.')

if idade <=9:
    print('Classificação: MIRIM.')
elif idade <=14:
    print('Classificação: INFANTIL.')
elif idade <= 19:
    print('Classificação: JUNIOR.')
elif idade <= 25:
    print('Classificação: SENIOR.')
elif idade >= 25:
    print('Classificação: MASTER.')


