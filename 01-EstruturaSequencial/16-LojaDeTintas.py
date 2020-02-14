# -*- coding: utf-8 -*-

#  Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, 
# que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.



metros = float(input("Informe os metros quadrados: "))

litros = metros / 3.0
latas = int(litros / 18.0)

if (litros % 18 != 0):
	latas += 1

print("Deve ser comprado {} latas de tinta.\nValor: R${}".format(latas, latas * 80))