# -*- coding: utf-8 -*-

# Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58

altura = float(input("Informe a sua altura: "))

pideal = (72.7*altura) - 58

print("O seu peso ideal é de {:.4}kg.".format(pideal))