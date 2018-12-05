import math

catetoOposto = float(input('Digite o valor do cateto oposto: '))
catetoAdjcente = float(input('Digite o valor do cateto adjcente: '))

hipotenuza = math.sqrt(pow(catetoOposto,2) + pow(catetoAdjcente,2))

print('O valor da hipotenusa: {}' .format(hipotenuza))