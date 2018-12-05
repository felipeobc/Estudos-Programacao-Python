import math
Numero = int(input("Digite  "))

if Numero % 2 == 0:
    print("Esse numero é PAR: {:.2f} ".format(math.sqrt(Numero)))
elif Numero < 0:
    print("Esse nurmeo é NEGATIVO")

