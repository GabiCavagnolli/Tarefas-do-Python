# -*- coding: utf-8 -*-
"""
Created on Fri May  6 09:37:10 2022

@author: GRCav
"""

import pandas as pd
campeonato = pd.read_csv('https://raw.githubusercontent.com/rnwatanabe/BasesComputacionais2021/main/dados/tabelaBrasileirao2018.csv')
campeonato
campeonato ['Vitorioso'] = campeonato ['Placar do Mandante'] > campeonato ['Placar do Visitante']
campeonato
campeonato ['Empate'] = campeonato ['Placar do Mandante'] == campeonato ['Placar do Visitante']
campeonato
campeonato['Vitorioso'].value_counts()
campeonato ['Empate'].value_counts()


x = 202*100/380
print('A porcentagem de jogos ganhos do time da casa é:', x, '%')

y = 110*100/380
print('A porcentagem de jogos empatados é: ', y, '%')
