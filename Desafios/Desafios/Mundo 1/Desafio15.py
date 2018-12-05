dias = float(input('Quantidade de dias de carro alugao: '))
km = float(input('Quantidade de km rodados'))

pagar = (dias * 60) + (km * 0.15)

print('valor total do aluguel do carro é R$: {:.2f}'.format(pagar))
