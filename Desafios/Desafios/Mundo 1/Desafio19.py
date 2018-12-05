import random

nome1 = input('Digite 1º nome: ')
nome2 = input('Digite 2º nome: ')
nome3 = input('Digite 3º nome: ')
nome4 = input('Digite 4º nome: ')

lista = [nome1, nome2, nome3, nome4]
escolha = random.choice(lista)

print('Aluno que vai apagar a a lousa é: {}'.format(escolha))

