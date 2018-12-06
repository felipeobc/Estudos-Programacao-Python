N = input()

L = input().split()

A = 0
B = 0

for acao in L:
    if(acao == '1'):
        if A == 1:
            A=0
        else:
            A=1
    elif acao == '2':
        if A == 1:
            A = 0
        else:
            A = 1
        if B == 1:
            B = 0
        else:
            B = 1

print(A)
print(B)
