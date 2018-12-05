#Leia uma temperatura em graus Celsius e apresente-a convertida em graus Kelvin. A
#f ´ ormula de convers˜ao ´ e: K = C + 273:15, sendo C a temperatura em Celsius e K a
#temperatura em Kelvin.

C = float(input("Digite o valor em Celsius: "))

K = C + 273.15

print("A conversão em Kelvin: {:.2f}".format(K))


