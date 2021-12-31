#Conversor de medidas
m = float(input('Digite uma distância em metro: '))

cm = m*100
mm = m*1000
km = m/1000

print(f'A conversão é: {cm:.0f} cm e {mm:.0f} mm.' )
print(f'E {km} km.')
