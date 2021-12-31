nome = str(input('Qual o seu nome? '))

if nome == 'Michel':
    print('Que nome bonito')
elif nome == 'Lucas' or nome == 'Junior' or nome == 'Guilherme':
    print('Fala primo!')
elif nome in 'Adriano Augusto Caligulas':
    print('Você é Romano?')
else:
    print(f'Bom dia {nome}, seu nome é bem normal.')