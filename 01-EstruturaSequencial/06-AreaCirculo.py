# -*- coding: utf-8 -*-

# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

import math

ra = int(input("Digite o raio de um circulo: "))
ar = 2*math.pi*ra
print("A área do círculo {} é {}".format(ra, ar))