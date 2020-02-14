# -*- coding: utf-8 -*-

# Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius

frnh = int(input("Digite a temperatura em Farenheit: "))
fpc = (5 * (frnh-32) / 9) 

print("A temperatura de {}° farenheit é equivalente a {}° celsius.".format(frnh, fpc))