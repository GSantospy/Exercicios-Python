# -*- coding: utf-8 -*-

# Faça um Programa que peça as 4 notas bimestrais e mostre a média.

n1 = float(input("Primeira nota: "))
n2 = float(input("Segunda nota: "))
n3 = float(input("Terceira nota: "))
n4 = float(input("Quarta nota: "))

m = (n1+n2+n3+n4)/4

print("A média é {:.1f}".format(m))