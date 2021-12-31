# Aluguel de carro

d = int(input('Quantos dias será alugado?: '))
km = float(input('Quantos kilometros será rodado?: '))

valor = d*60 + km*0.15
print(f'O valor total do aluguel será: R$ {valor:.2f}')