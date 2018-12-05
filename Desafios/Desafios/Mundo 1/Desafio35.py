r1 = int(input('1 seguimento: '))
r2 = int(input('2 seguimento: '))
r3 = int(input('3 seguimento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
    print('isso pode um triangulo')
else:
    print('Isso nao pode ser um triangulo')
