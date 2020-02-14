# -*- coding: utf-8 -*-

# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

ganho = int(input("Quanto você ganha a cada hora de trabalho: "))
h = int(input("Quantas horas você trabalha por mês: "))

salario = (ganho*h)

print("Seu salário é de R${} por mês.".format(salario))