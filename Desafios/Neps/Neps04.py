N = int(input())

V = input().split()

for i in range(len(V)):
    V[i] = int(V[i])

total = 0
for elemento in V:
    total = total + elemento

print(total)