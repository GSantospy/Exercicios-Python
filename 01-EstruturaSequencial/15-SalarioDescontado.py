# -*- coding: utf-8 -*-
# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no 
# referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
# salário bruto.
# quanto pagou ao INSS.
# quanto pagou ao sindicato.
# o salário líquido.
# calcule os descontos e o salário líquido, conforme a tabela abaixo:
#  + Salário Bruto : R$
#  - IR (11%) : R$
#  - INSS (8%) : R$
#  - Sindicato ( 5%) : R$
#  = Salário Liquido : R$


ganho = float(input("Quanto você ganha a cada hora de trabalho: "))
h = int(input("Quantas horas você trabalha por mês: "))

salario = (ganho*h)
ir = (11*salario)/100
inss = (8*salario)/100
sindicato = (5*salario)/100
porct = ir + inss + sindicato
sliquido = salario - porct

print("Salário Bruto: R${}\nImposto de Renda: R${}\nINSS: R${}\nSindicato: R${}\nSalário Liquido: R${}".format(salario, ir, inss, sindicato, sliquido))