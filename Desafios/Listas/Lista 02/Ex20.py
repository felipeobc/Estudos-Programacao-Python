Lado_A = int(input("Digite um valor do lado A: "))
Lado_B = int(input("Digite um valor do lado B: "))
Lado_C = int(input("Digite um valor do lado C: "))

if Lado_A == Lado_B == Lado_C:
    print("Triagulo Equilatero")
elif Lado_A == Lado_B or Lado_A == Lado_C or Lado_B == Lado_C:
    print("Triangulo Isosceles")
else:
    print("Triangulo Escaleno")


