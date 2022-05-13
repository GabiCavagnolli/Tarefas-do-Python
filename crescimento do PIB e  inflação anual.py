# -*- coding: utf-8 -*-
"""
Created on Fri May 13 13:28:53 2022

@author: GRCav
"""

#Faça o gráfico de dispersão entre o crescimento do PIB e a inflação anual de 1961 a 2018. Calcule e mostre na tela a correlação entre as duas grandezas.

#importando as tabelas
import pandas as pd
inflaAnual = pd.read_csv('https://raw.githubusercontent.com/rnwatanabe/BasesComputacionais2021/main/dados/inflaAnual.csv')
pibAnual = pd.read_csv('https://raw.githubusercontent.com/rnwatanabe/BasesComputacionais2021/main/dados/pibAnual.csv')


#Faça o gráfico de dispersão entre o crescimento do PIB e a inflação anual de 1961 a 2018
#Apagando as linhas de 1945 a 1960
inflaAnual.drop(inflaAnual[inflaAnual['Ano']<1961].index, inplace = True)
#Apagando a coluna Unnamed: 0
pibAnual = pibAnual.drop(columns = ['Unnamed: 0'])

#Criando o gráfico
import matplotlib.pyplot as plt
plt.figure()
plt.plot(inflaAnual, pibAnual, marker = 'o', color = 'red', linestyle = '')
plt.xlabel('inflação Anual')
plt.ylabel('pib Anual')
plt.grid()
plt.show()

#Calcule e mostre na tela a correlação entre as duas grandezas
corr_inflapib = inflaAnual['Inflação'].corr(pibAnual['Variação anual do PIB real (%)'])
print(corr_inflapib)