# -*- coding: utf-8 -*-
"""
Created on Tue May 10 10:39:36 2022

@author: GRCav
"""

# Tabela dos resultados do campeonato Brasileiro de futebol de 2018
import pandas as pd
futebol = pd.read_csv('https://raw.githubusercontent.com/rnwatanabe/BasesComputacionais2021/main/dados/tabelaBrasileirao2018.csv')
futebol

#Escolha um time e faça o histograma da distribuição do público nos jogos em que este time foi o mandante.
import matplotlib.pyplot as plt
plt.figure() 
futebol['Público'][futebol['Mandante']=='Sport'].hist()
plt.show()

#Calcule qual foi o público médio nos jogos em que o time escolhido foi o mandante.
mediaPublicoSport = futebol[futebol['Mandante']=='Sport']['Público'].mean()
print(mediaPublicoSport)