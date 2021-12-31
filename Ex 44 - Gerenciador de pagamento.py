print ('=============== Luci Comercios ===============')

preço =  float(input('Preço do produto: R$ '))

print('''Forma de pagamento
[ 1 ] A vista no dinheiro
[ 2 ] A vista no cartão 
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão ''')

opção = int(input('Qual a opção de pagamento? '))

if opção == 1:
    total = preço - (preço * 10 / 100)
elif opção == 2:
    total = preço - (preço * 5 / 100)
elif opção == 3:
    total = preço
    parcela = total / 2
    print(f'Sua compra de {total:.2f} será paga em 2 parcelas de {parcela:.2f}.')
elif opção >= 4:
    total = preço + (preço * 20 / 100)
    totparc = int(input('Quantas parcelas? '))
    parcela = preço / totparc
    print(f'Sua compra de R${total:.2f} será em {totparc}x parcelas de {parcela:.2f} de juros..')

print(f'Sua compra de R${preço:.2f} vai custar ao final R${total:.2f}.')


