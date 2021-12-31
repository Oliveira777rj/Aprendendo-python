distancia = float(input('Qual a distância da sua viagem? '))
print(f'Você está preste a percorrer uma viagem de {distancia}Km.')

if distancia <=200:
    preço = distancia*0.50

else:
    preço = distancia*0.45

print(f'Sua viagem terá o valor de R${preço:.2f}')
