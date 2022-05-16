# -*- coding: utf-8 -*-
"""
Created on Mon May 16 11:02:51 2022

@author: GRCav
"""

#Três séries,  e  seguem as seguintes regras:
v[i] = v[i - 1] + 0.01 * (-9.81)
y[i] = y[i -1] + 0.01 * v[i - 1]
t[i] = t[i - 1] + 0.01
v = 10
y = 0
t = 0

import numpy as np
#Começando com v[0] = 10 m/s, y[0] = 0 m e t[0] = 0 s, calcule os 250 primeiros valores das três séries.
v = [0] * 250
y = [0] * 250
t = [0] * 250
v[0] = 10
y[0] = 0
t[0] = 0
for i in range(len(v)):
    v[i] = v[i - 1] + 0.01 * (-9.81)
for i in range(len(y)):
    y[i] = y[i -1] + 0.01 * v[i - 1]
for i in range(len(t)):
    t[i] = t[i - 1] + 0.01
print('v[i] =', v)
print('y[0] =', y)
print('t[0] =', t)
      
#Faça os gráficos com os valores encontrados de y em função de t e dos valores encontrados de v em função de t
# y em função de t
import matplotlib.pyplot as plt
plt.figure()
plt.plot(y, t)
plt.xlabel('y (posição em m)')
plt.ylabel('t (tempo em s)')
plt.show()
#v em função de t
plt.figure()
plt.plot(v, t)
plt.xlabel('v (velocidade em m/s)')
plt.ylabel('t (tempo em s)')
plt.show()
    