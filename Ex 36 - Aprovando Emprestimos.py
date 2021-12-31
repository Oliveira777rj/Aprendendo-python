casa = float(input('Qual o valor da casa: R$ '))
salario = float(input('Qual o valor do salario: R$ '))
ano = int(input('Quantos anos de financiamento? '))
prestação = casa / ( ano * 12)
minimo = salario * 30 / 100

print(f'Para pagar uma casa de R${casa:.2f} em {ano} anos, a prestação será de {prestação:.2f} ')

if prestação <= minimo:
    print('Emprestimo aprovado!')
else:
    print('Emprestimo negado!')
    