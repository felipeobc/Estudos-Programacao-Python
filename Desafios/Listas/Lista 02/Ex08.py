nota1 = float(input("Digite o valor da 1ªNota: "))

if nota1 > 10.0 or nota1 < 0.0:
    print("Valor invalido!")


nota2 = float(input("Digite o valor da 2ªNota: "))

if nota2 > 10.0 or nota2 < 0.0:
    print("Valor invalido!")


print("Media entre das notas: ", (nota1+nota2)/2)

