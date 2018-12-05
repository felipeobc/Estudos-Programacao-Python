Laboratorio = float(input("Digite a 1ª Laboratorio: "))
Semestral = float(input("Digite a 2ª Semestral: "))
Final = float(input("Digite a 3ª Final: "))

media =  2*Laboratorio + 3*Semestral + 5*Final / 2+3+5

print(media)
if media <=2.9:
    print("Aluno Reprovado!")
else:
    print("Aluno Aprovado!")

