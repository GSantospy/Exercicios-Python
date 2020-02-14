# -*- coding: utf-8 -*-

# Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), 
# calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

mb = float(input("Qual o tamanho do arquivo? (MB): "))
vel = float(input("Qual a velocidade da conexão (em MBPS): "))

tmnh = mb * 1024 * 1024 * 8
tmpsg = tmnh / (vel * 1024 * 1024)
tmpmn = tmpsg / 60

print("Tempo de download: {} minutos.".format(tmpmn))