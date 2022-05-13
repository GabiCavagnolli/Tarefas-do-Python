# -*- coding: utf-8 -*-
"""
Created on Fri May 13 13:10:10 2022

@author: GRCav
"""

#Faça o gráfico de dispersão do tamanho do pé (FootLen) em função da altura da pessoa (Height). Calcule (e mostre na tela) a correlação e plote a reta de regressão entre esses dados.

#importando a tabela
import pandas as pd
BDSinfo = pd.read_csv('https://raw.githubusercontent.com/rnwatanabe/BasesComputacionais2021/main/dados/BDSinfo.csv', delimiter = '\t')


#criando o gráfico de dispersão
import matplotlib.pyplot as plt
plt.figure()
plt.plot(BDSinfo['FootLen'], BDSinfo['Height'], marker = "o", color = 'red', linestyle = '')
plt.xlabel('Tamanho do pé (FootLen)')
plt.ylabel('Altura da pessoa (Height)')
plt.grid()
plt.show()


#Calcule (e mostre na tela) a correlação
corr_BDSinfo = BDSinfo['FootLen'].corr(BDSinfo['Height'])
print(corr_BDSinfo)


#plote a reta de regressão entre esses dados
#Calculando a Regressão
import numpy as np
x = BDSinfo['FootLen']
y = BDSinfo['Height']
mediaX = np.mean(x)
mediaY = np.mean(y)
DesvioX = x - mediaX
DesvioY = y - mediaY
m = np.sum(DesvioX * DesvioY)/np.sum(DesvioX**2)
b = mediaY - m * mediaX
print(m)
print(b)

#Fazendo o gráfico da reta estimada pela regressão
import matplotlib.pyplot as plt
plt.figure()
plt.plot(BDSinfo['FootLen'], BDSinfo['Height'], marker = "o", color = 'red', linestyle = '')
plt.plot(x, m * x + b, color = 'blue', linestyle = '-')
plt.xlabel('Tamanho do pé (FootLen)')
plt.ylabel('Altura da pessoa (Height)')
plt.grid()
plt.show()