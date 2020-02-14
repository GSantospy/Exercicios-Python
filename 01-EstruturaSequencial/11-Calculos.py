# -*- coding: utf-8 -*-

# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#  A. o produto do dobro do primeiro com metade do segundo .
#  B. a soma do triplo do primeiro com o terceiro.
#  C. o terceiro elevado ao cubo.

import math

n1 = int(input("Digite um número inteiro: "))
n2 = int(input("Digite um número inteiro: "))
n3 = float(input("Digite um número real: "))

c = math.pow(n3, 3)
b = (n1*3) + n3  
a = (n1*n1) / (n2/2)

print("O dobro do primeiro número com a metado do segundo é {}\nA soma do triplo do primeiro número com o terceiro número é {}\nO terceiro número elevado ao cudo é igual a {}".format(a,b,c))