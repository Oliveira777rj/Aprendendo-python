# Conversor de moedas

S = float(input('Digite o valor em reais para conversões: R$ '))
D = S / 5.25
E = S / 6.20
I = S / 0.048
B = S / 238.131
print(f'Com o valor de R$ {S} será em Dolar: US$ {D:.2f} ')
print(f'Com o valor de R$ {S} será em Euro: € {E:.2f}')
print(f'Com o valor de R$ {S} será em Iene: ¥ {I:.2f}')
print(f'Com o valor de R$ {S} será em Bitcoin: BTC {B:.4f}')
