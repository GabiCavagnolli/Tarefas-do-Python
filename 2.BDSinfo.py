# -*- coding: utf-8 -*-
"""
Created on Fri May 13 13:58:40 2022

@author: GRCav
"""

#Faça o gráfico de dispersão do número de medicamentos que a pessoa toma (Nmedication) em função da idade da pessoa (Age). Calcule (e mostre na tela) a correlação e plote a reta de regressão entre esses dados.

#importando a tabela
import pandas as pd
BDSinfo = pd.read_csv('https://raw.githubusercontent.com/rnwatanabe/BasesComputacionais2021/main/dados/BDSinfo.csv', delimiter = '\t')


#Faça o gráfico de dispersão do número de medicamentos que a pessoa toma (Nmedication) em função da idade da pessoa (Age)
import matplotlib.pyplot as plt
plt.figure()
plt.plot(BDSinfo['Nmedication'], BDSinfo['Age'], marker = 'o', color  = 'red', linestyle = '')
plt.grid()
plt.show()


#Calcule (e mostre na tela) a correlação
corr_BDSinfo = BDSinfo['Nmedication'].corr(BDSinfo['Age'])
print(corr_BDSinfo)


#plote a reta de regressão entre esses dados
#Calculando a regressão
import numpy as np
x = BDSinfo['Nmedication']
y = BDSinfo['Age']
mediaX = np.mean(x)
mediaY = np.mean(y)
DesvioX = x - mediaX
DesvioY = y - mediaY
m = np.sum(DesvioX * DesvioY)/np.sum(DesvioX**2)
b = mediaY - x * mediaX
print(m)
print(b)

#Fazendo o gráfico da reta estimada pela regressão
import matplotlib.pyplot as plt
plt.figure()
plt.plot(BDSinfo['Nmedication'], BDSinfo['Age'], marker = 'o', color  = 'red', linestyle = '')
plt.plot(x, m * x + b, linestyle = '-', color = 'blue')
plt.grid()
plt.show()