frase = 'Curso em Video Python'
#Fatiamento
print(frase[9:13])
print(frase[9:21])
print(frase[9:21:2])#vai pular em dois em dois.
print(frase[:5])# vai até o char 4.
print(frase[15:])#começa do 15 e vai até o final
print(frase[9::3])#começa no até mo final pulando em 3 em 3.

len(frase)# mosta o numero de char dentro da string

frase.count('o') #ele vai contar quants vezes tem a letra (o)
frase.count('o', o, 13) #ele vai contar quants vezes tem a letra (o) entre os intervalo 0-13
frase.find('deo')# funçao  para encontrar  onde começa "deo" = 11
frase.find('androi')# caso ele nao encontra retorna = -1
'Curso' in frase # retorna = true

#Trasformação

frase.replace('Python', 'Androide')# ele substitui  a palavra Python por Androide
frase.upper()# trasnforma todos os char em maiuscula.
frase.lower()# trasnforma todos os char em minusculo.
frase.capitaliza() #joga todos os char em minusculo e so o primeiro pra maiuscula
frase.title() # coloca todas as primeiras letras em maiusculas.
frase.strip() # vai remover todos os espaços nas extremidade da string
frase.rstrip()
frase.ltrip()

#Divisão

frase.split() # ele vai separa cada frase em uma string tiferente. 
'-'.join(frase) #vai juntar todas as string com '-'.
