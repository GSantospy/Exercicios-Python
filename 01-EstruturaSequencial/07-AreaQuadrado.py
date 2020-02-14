# -*- coding: utf-8 -*-

# Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

area = int(input("Digite a área do quadrado: "))
areaq = (area*area)
areadbr = 2*(area*area)
print("A área do quadrado {} é {}.\nO dobro da área é {}.".format(area, areaq, areadbr))