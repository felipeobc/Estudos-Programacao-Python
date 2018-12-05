valor_Real = float(input("Digite o valor em reais R$:"))
contacao_dolar = float(input("Digite a cotação do Dolar do dia: US: "))

valor = contacao_dolar / valor_Real

print("Valor de conversão: US: {:.2f} ".format(valor))

