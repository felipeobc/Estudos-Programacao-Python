precoDoProduto = float(input('Qual é o valor do produto: '))

print('Valor do produto: {}'.format(precoDoProduto))

desconto = (precoDoProduto * 5) / 100
descontoProduto = precoDoProduto - desconto

print('O valor do produto com desconto R$:{:.2f} '.format(descontoProduto))