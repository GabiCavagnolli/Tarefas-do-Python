# -*- coding: utf-8 -*-
"""
Created on Fri May  6 08:02:29 2022

@author: GRCav
"""

import pandas as pd
analfabetismo = pd.read_csv('https://raw.githubusercontent.com/rnwatanabe/BasesComputacionais2021/main/dados/analfabetismo.csv')
analfabetismo
print (analfabetismo['Ano'].values)
print (analfabetismo['São Paulo'].values)
import matplotlib.pyplot as plt
plt.figure()
plt.plot(analfabetismo['Ano'], analfabetismo['São Paulo'])
plt.xlabel('Tempo (Ano)')
plt.ylabel('Taxa de Analfabetismo em São Paulo')
plt.grid()
plt.show()

