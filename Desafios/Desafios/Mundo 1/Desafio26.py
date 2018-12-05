nome = str(input('Digite uma frase: ')).upper()

print('Essa frase tem {} letras ''A'' '.format(nome.count('A')))
print('A primeira letra ''A'' aparece na posição: {} '.format(nome.find('A')))
print('A ultima letra ''A'' aparece na posição: {} '.format(nome.rfind('A')))