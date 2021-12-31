num = int(input('Digite um numero inteiro: '))
print('''Escolha uma das bases para conversão:
[ 1 ] Converter para BINARIO
[ 2 ] Converter para OCTAL
[ 3 ] Converter para HEXADECIMAL''')

opção = int(input('Sua opção: '))

if opção == 1:
    print(f'{num} convertido para BINARIO é igual a {bin(num) [2:]}')
elif opção == 2:
    print(f'{num} convertido para OCTAL é igual a {oct(num) [2:]}')
elif opção == 3:
    print(f'{num} convertido para HEXADECIMAL é igual a {hex(num)[2:]}')
else:
     print('Opção invalida, tente novamente.')


