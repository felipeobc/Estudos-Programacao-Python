ano = int(input('Digite um Ano: '))

if ano % 4 == 0 and ano != 100 == 0 or ano % 400 == 0:
    print('O ano {} é Bissexto'.format(ano))

else:
    print('Essa ano não é Bissexto')

