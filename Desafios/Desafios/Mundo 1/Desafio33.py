a = int(input('Numero 1: '))
b = int(input('Numero 2: '))
c = int(input('Numero 3: '))

menor = a

if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

maior = a

if b > a and b > c:
    maior = b
if c > b and c > a:
    maior = c

print("maior numero {}".format(maior))
print("menor numero {}".format(menor))
