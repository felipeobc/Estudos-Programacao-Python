distancia = int(input('Digite o valor em Km: '))

if distancia <= 200:
    print('O valor da viagem vai custar R$: {}'.format(float(distancia * 0.5)))
else:
    print('O valor da viagem vai custar R$: {}'.format(float(distancia * 0.45)))
