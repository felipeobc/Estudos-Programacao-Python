meses = ('Janeiro', 'Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro')

Dia = int(input("Digite o dia do seu nascimento: "))
mes = int(input("Digite o mes do Nascimento: "))
Ano = int(input("Digite o Ano de Nasciemnto:"))

print('Você Nasceu do{}'.format(meses[mes-1]))