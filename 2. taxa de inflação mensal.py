# -*- coding: utf-8 -*-
"""
Created on Wed May 11 11:11:29 2022

@author: GRCav
"""

#taxa de inflação mensal (IGP-DI) no Brasil de fevereiro de 1944 a junho de 2019
import pandas as pd
inflacao = pd.read_csv('https://raw.githubusercontent.com/rnwatanabe/BasesComputacionais2021/main/dados/inflacaoMensal.csv')
inflacao

#Mudando os meses de números para nomes em extenso
inflacao [ 'Data' ] =  pd . to_datetime ( inflacao [ 'Mês' ], format = '%m' )
inflacao['Mês'] = inflacao['Data'].dt.month_name()
inflacao = inflacao.drop(columns=['Data'])

#Calcule a mediana da inflação mensal nos meses de março.
medianaMarco = inflacao[inflacao['Mês']=='March']['Inflação'].median()
print(medianaMarco)

#Calcule a média da inflação mensal nos meses de março.
mediaMarco = inflacao[inflacao['Mês']=="March"]['Inflação'].mean()
print(mediaMarco)

#Calcule o desvio-padrão da inflação mensal nos meses de março.
DesvioPadrao = inflacao[inflacao['Mês']=='March']['Inflação'].std()
print(DesvioPadrao)

#Faça o histograma da inflação mensal nos meses de março.
import matplotlib.pyplot as plt
plt.figure()
plt.hist(inflacao[inflacao['Mês']=='March']['Inflação'])
plt.xlabel('Inflação nos meses de março')
plt.show()

