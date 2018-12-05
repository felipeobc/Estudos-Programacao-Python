horas_seg = 3600
tempo = int(input("Entre com o número de segundos: "))
horas = (tempo / horas_seg)
minutos = (tempo - (horas_seg * horas)) / 60
segundos = (tempo - (horas_seg * horas) - (minutos * 60))
print( horas, minutos, segundos)