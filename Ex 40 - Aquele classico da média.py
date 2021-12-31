nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))

resultado = (nota1+nota2)/2

if 7 > resultado >=5:
    print(f'Sua média foi {resultado}, você está em RECUPERAÇÃO.')

elif resultado < 5:
    print(f'Sua média foi {resultado}, você está REPROVADO.')

elif resultado >= 7:
    print(f'Sua média foi {resultado}, você está APROVADO')