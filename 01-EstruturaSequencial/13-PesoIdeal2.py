# -*- coding: utf-8 -*-

# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#  Para homens: (72.7*h) - 58
#  Para mulheres: (62.1*h) - 44.7

hm = str(input("Informe se você é homem ou mulher (H/M): "))
altura = float(input("Informe a sua altura: "))
peso = float(input("Informe seu peso: "))

if hm == "H":
	pideal = (72.7*altura) - 58

else:
	pideal = (62.1*altura) - 44.7

if (peso > pideal):
	print("Você está acima do seu peso ideal. {:.4}kg.".format(pideal))

elif (peso < pideal):
	print("Você está abaixo do seu peso ideal. {:.4}kg.".format(pideal))

else:
	print("Você está no seu peso ideal. {}kg.".format(pideal))