import random
numero = random.randint(0, 5)
escolha = int(input('Escolha uma nuemero de 0 a 5: '))

if escolha == numero:
    print('Parabens voce acertou o numero escolhido {}'.format(numero))
else:
    print('Que pena vc errou !\n\n Tente novamente')



