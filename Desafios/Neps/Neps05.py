N = int(input())

visualizacao = []


for i in range(N):
    A = int(input())
    visualizacao.append(A)


total = 0
resposta = -1

for i, v in enumerate(visualizacao):
    dia = i + 1
    total = total + v
    if total >= 1000000 and resposta == -1:
        resposta = dia



print(resposta)
