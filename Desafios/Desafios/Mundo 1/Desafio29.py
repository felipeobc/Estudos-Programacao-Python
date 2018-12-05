velocidade = int(input('Escreva a a sua velocidade em Km/h:'))

if velocidade > 80:
    print('Você foi multado !!')
    print('O valor da multa vai ser de R$: {}'.format(float((velocidade - 80) * 7)))

