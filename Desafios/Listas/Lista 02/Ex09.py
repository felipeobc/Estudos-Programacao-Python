salario = float(input("Salario  do Trabalhador R$: "))
emprestimo = float(input("Valor do Emprestimo R$: "))

prestacao = float(input("Digite o numero da prestação: "))


prestacao = emprestimo / prestacao

salario = (salario*20)/100

if prestacao > salario:
    print("Emprestimo Negado")
else:
    print("Emprestimo Aprovado")


