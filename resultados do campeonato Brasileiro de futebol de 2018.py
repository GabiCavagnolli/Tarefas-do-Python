# -*- coding: utf-8 -*-
"""
Created on Fri May  6 09:37:10 2022

@author: GRCav
"""

"Tabela dos resultados do campeonato Brasileiro de futebol de 2018"
import pandas as pd
campeonato = pd.read_csv('https://raw.githubusercontent.com/rnwatanabe/BasesComputacionais2021/main/dados/tabelaBrasileirao2018.csv')
campeonato

"Criação de uma coluna mostrando se o time da casa ganhou o jogo"
campeonato ['Vitorioso'] = campeonato ['Placar do Mandante'] > campeonato ['Placar do Visitante']
campeonato

"Criação de uma coluna mostrando se o jogo deu empate"
campeonato ['Empate'] = campeonato ['Placar do Mandante'] == campeonato ['Placar do Visitante']
campeonato

"Contagem da quantidade de vezes que o time da casa ganhou (True)"
campeonato['Vitorioso'].value_counts()

"Contagem de vezes que deu empate (True)"
campeonato ['Empate'].value_counts()

"Calculo da porcentagem de jogos ganhos e empatados"
x = 202*100/380
print('A porcentagem de jogos ganhos do time da casa é:', x, '%')
y = 110*100/380
print('A porcentagem de jogos empatados é: ', y, '%')
