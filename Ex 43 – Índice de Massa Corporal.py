# Calculando IMC 

peso = float(input('Qual o seu peso? '))
altura = float(input('Qual a sua altura? '))

imc = peso / altura**2
print(f'Seu IMC é de {imc:.2f}')

if imc < 18.5:
    print('Sua classificação é MAGREZA.')
elif imc >= 18.5 and imc < 24.9:
    print('Sua classificação é NORMAL.')
elif imc > 25 and imc < 29.9:
    print('SUa classificação é SOBREPESO.')
elif imc > 30 and imc < 39.9:
    print('Sua classificação é OBESIDADE.')
elif imc > 40:
    print('Sua classificação é OBESIDADE GRAVE.')
