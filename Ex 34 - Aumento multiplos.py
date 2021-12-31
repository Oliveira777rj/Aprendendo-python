salario = float(input('Qual salario do funcionario: R$ ? '))



if salario <= 1250:
    novo = salario + ((salario * 15) /100)

else:
    novo = salario + ((salario * 10) / 100)

print(f'Quem recebia R${salario:.2f} passa a receber R${novo:.2f}.')