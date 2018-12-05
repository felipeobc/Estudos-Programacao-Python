genero = input("m - Masculino\nf - Feminino\nDigite uma Lertra:")
altura = float(input("Digite o valor da altura: "))

if genero == 'm':
    print("Masculino")
    print("Peso ideal: ", (72.7*altura)-58)

if genero == 'f':
    print("Feminino")
    print("Peso ideal: ", (62.1*altura)-44.7)


