import math
co = float(input('Cumprimento do cateto oposto:'))
ca = float(input('Cumprimento do cateto adjacente:'))
hi = math.hypot(co,ca)

print(f'A hipotenusa ira medir {hi:.2f}')