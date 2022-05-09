# -*- coding: utf-8 -*-
"""
Created on Fri May  6 10:07:52 2022

@author: GRCav
"""

"Tabela da taxa de inflação mensal durante os anos"
import pandas as pd
IM = pd.read_csv('https://raw.githubusercontent.com/rnwatanabe/BasesComputacionais2021/main/dados/inflacaoMensal.csv')
IM

"Criação de uma coluna Ano/Mês: ano adicionado da fração correspondente ao mês"
IM ['Ano/Mês'] = IM ['Ano'] + IM ['Mês'] / 12
IM
print(IM['Ano/Mês'].values)
print(IM['Inflação'].values)

"Gráfico da taxa de inflação mensal em função do tempo (Ano/Mês)"
import matplotlib.pyplot as plt
plt.figure(figsize=(15,5))
plt.plot(IM['Ano/Mês'], IM['Inflação'])
plt.xlabel('Tempo (Ano/Mês)')
plt.ylabel('Taxa de Inflação mensal')
plt.show()

"Mês e ano com a maior taxa de inflação mensal"
import numpy as np
x = np.max(IM['Ano/Mês'])
print('O ano+mês/12 com maior taxa de inflação mensal é:',x)