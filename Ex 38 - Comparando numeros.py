n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo numero: '))

if n1 > n2:
    print(f'O primeiro valor {n1} é maior que {n2}. ')

elif n2 > n1:
    print(f'O segundo valor {n2} é maior que o primeiro {n1}. ') 

elif n1 == n2:
    print(f'O primeiro numero ({n1}) e o segundo numero ({n2}) são iguais.')