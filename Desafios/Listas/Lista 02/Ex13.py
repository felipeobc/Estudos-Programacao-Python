nota1 = float(input("Digite a 1ª Nota: "))
nota2 = float(input("Digite a 2ª Nota: "))
nota3 = float(input("Digite a 3ª Nota: "))

media = 1*(nota1+nota2) + 2*nota3 / nota1+nota2+nota3

if media >= 60.0:
    print("Aluno aprovado!")
else:
    print("Aluno Reprovado!")

