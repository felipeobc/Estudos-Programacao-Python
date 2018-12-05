salario = float(input('Salario do funcionario R$: '))

print('Valor do produto: {:.2f}'.format(salario))

acrescimo = (salario * 15) / 100
novoSalario = salario + acrescimo

print('Salario novo com acrescimo de 15% R$:{:.2f} '.format(novoSalario))