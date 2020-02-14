# -*- coding: utf-8 -*-

# João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. 
#Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) 
#deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) 
#e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que 
#João deverá pagar. Imprima os dados do programa com as mensagens adequadas.

peso = float(input("Informe o peso dos peixes: "))

multa = 4
pesomax = 50

if peso > pesomax:
	lmt = peso - pesomax
	mlt = lmt * multa
	print("Foi ultrapassado o limite de 50kg. {}\nValor da multa: R${}".format(peso, mlt))
else:
	print("Não foi ultrapassado o limite de 50kg. {}kg".format(peso))