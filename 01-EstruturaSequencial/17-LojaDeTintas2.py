# -*- coding: utf-8 -*-

# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a 
# cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões
# de 3,6 litros, que custam R$ 25,00.
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
#  comprar apenas latas de 18 litros;
#  comprar apenas galões de 3,6 litros;
#  misturar latas e galões, de forma que o preço seja o menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, 
#  considere latas cheias.

metros = float(input("Informe os metros quadrados: "))

litros = metros / 6.0
latas = litros / 18.0
galoes = litros / 3.6 

if (litros % 18 != 0):
	latas += 1

if (litros % 3.6 != 0):
	galoes += 1

latas1 = litros / 18
galoes2 = (litros * (latas1 * 18.0)) / 3.6

if ((litros - (latas1 * 18.0) % 3.6 != 0)):
	galoes2 +=1

print("Latas: {:.3}. Valor: R${:.4}\nGaloes: {:.3}. Valor: R${:.4}\nLatas {:.3} e {:.3}. Valor: R${:.4}".format(latas, latas * 80, galoes, galoes * 25, latas1, galoes2, (latas1 * 80)+(galoes2 * 25)))