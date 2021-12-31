from datetime import date
atual = date.today().year

nasc = int(input('Digite o ano de nascimento: '))
idade = atual - nasc

print(f'Quem nasceu em {nasc} tem {idade} em {atual}.')

if idade == 18:
    print('Você tem que se alistar imediatamente!')
elif idade < 18:
    saldo = idade - 18
    print(f'Você ainda não tem 18 anos, ainda faltam {saldo} para o alistamento.')

elif idade > 18:
    saldo = idade - 18
    print (f'Você já deveria ter se alistado a {saldo} anos.')
 


