S = input()

vogais =  ['a', 'e', 'i', 'o', 'u']

R = ''

for c in S:
    if c in vogais:
        R += c

if R == R[::-1]:
    print('S')
else:
    print('N')