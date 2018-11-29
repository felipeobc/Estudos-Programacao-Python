#Leia uma temperatura em graus Fahrenheit e apresente-a convertida em graus Celsius.
#A f ´ ormula de convers˜ao ´ e: C = 5:0  (F 􀀀 32:0)=9:0, sendo C a temperatura em Celsius
#e F a temperatura em Fahrenheit.

F = int(input("Digite a temperatura em Fahrenhait: "))

C = 5.0 *(F - 32.0)/9.0

print("A conversão em Celso: {}ºC".format(C))

