import math

angulo = int(input('Digite um ângulo: '))

cosseno = math.cos(math.radians(angulo))
seno = math.sin(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print('Cosseno: {}\nSeno: {}\nTangente: {}'.format(cosseno, seno, tangente))
