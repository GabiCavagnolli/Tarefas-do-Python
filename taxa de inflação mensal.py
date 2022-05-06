# -*- coding: utf-8 -*-
"""
Created on Fri May  6 10:07:52 2022

@author: GRCav
"""

import pandas as pd
IM = pd.read_csv('https://raw.githubusercontent.com/rnwatanabe/BasesComputacionais2021/main/dados/inflacaoMensal.csv')
IM
IM ['Ano/Mês'] = IM ['Ano'] + IM ['Mês'] / 12
IM
print(IM['Ano/Mês'].values)
print(IM['Inflação'].values)
import matplotlib.pyplot as plt
plt.figure(figsize=(15,5))
plt.plot(IM['Ano/Mês'], IM['Inflação'])
plt.xlabel('Tempo (Ano/Mês)')
plt.ylabel('Taxa de Inflação mensal')
plt.show()

import numpy as np
x = np.max(IM['Ano/Mês'])
print('O ano, mês com maior taxa de inflação mensal é:',x)