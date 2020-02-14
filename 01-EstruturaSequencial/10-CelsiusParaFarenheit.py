# -*- coding: utf-8 -*-

# Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Farenheit.

c = int(input("Digite a temperatura em Celsius: "))

f = (c*9/5) + 32

print("A temperatura de {}° celsius é equivalente a {}° farenheit.".format(c, f))