# -*- coding: utf-8 -*-
"""
Created on Wed May 11 12:23:42 2022

@author: GRCav
"""

#Use o comando 'np.random.rand(N)' para gerar N números aleatórios entre 0 e 1.
import numpy as np

#Faça o histograma e calcule (e mostre na tela) a média dos valores gerados.

#a) N = 100
#Gerando 100 números aleatórios
Na = np.random.rand(100)
#Fazendo o histograma
import matplotlib.pyplot as plt
plt.figure()
plt.hist('Na')
plt. ylabel('100 números aleatórios')
plt.show()
#calcule (e mostre na tela) a média dos valores gerados
mediaA = np.mean(Na)
print(mediaA)

#b) N = 1000
#Gerando 1000 números aleatórios
Nb = np.random.rand(1000)
#Fazendo o histograma
import matplotlib.pyplot as plt
plt.figure()
plt.hist('Nb')
plt. ylabel('1000 números aleatórios')
plt.show()
#calcule (e mostre na tela) a média dos valores gerados
mediaB = np.mean(Nb)
print(mediaB)

#c) N = 10000
#Gerando 10000 números aleatórios
Nc = np.random.rand(10000)
#Fazendo o histograma
import matplotlib.pyplot as plt
plt.figure()
plt.hist('Nc')
plt. ylabel('10000 números aleatórios')
plt.show()
#calcule (e mostre na tela) a média dos valores gerados
mediaC = np.mean(Nc)
print(mediaC)

#d) N = 100000
#Gerando 100000 números aleatórios
Nd = np.random.rand(100000)
#Fazendo o histograma
import matplotlib.pyplot as plt
plt.figure()
plt.hist('Nd')
plt. ylabel('100000 números aleatórios')
plt.show()
#calcule (e mostre na tela) a média dos valores gerados
mediaD = np.mean(Nd)
print(mediaD)