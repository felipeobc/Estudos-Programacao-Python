#Leia uma temperatura em graus Kelvin e apresente-a convertida em graus Celsius. A
#f ´ ormula de convers˜ao ´ e: C = K 􀀀 273:15, sendo C a temperatura em Celsius e K a
#temperatura em Kelvin.

K = float(input("Coloque a temperatura em Kelvin: "))

C = K - 273.15

print("A temperatura em Celsius: {:.2f}ºC".format(C))
