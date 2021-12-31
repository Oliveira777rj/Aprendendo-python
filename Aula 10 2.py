n1 = float(input('Qual a primeira nota? '))
n2 = float(input('Qual a segunda nota? '))

media = (n1 + n2)/2

print(f'A sua nota foi {media}')

if media >= 7:
    print('Parabéns, você passou.')

else:
    print('Infelizmente você reprovou. ')

