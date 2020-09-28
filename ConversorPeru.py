#primer programa de python

soles = input ("¿Cuántos soles tienes?: ")
soles = float (soles)
valor_dolar = 3.65
dolares = soles / valor_dolar
dolares = round(dolares,2)
dolares = str(dolares)
print("Tienes $"+dolares+" dolares")s