# -*- coding: utf-8 -*-
"""
Created on Tue May 10 11:16:57 2022

@author: GRCav
"""

# Tabela dos dados de força e torque medidos no chão enquanto uma pessoa tenta ficar em pé o mais parada possível durante um minuto encontrado
import pandas as pd
ForcaeTorque = pd.read_csv('https://raw.githubusercontent.com/rnwatanabe/BasesComputacionais2021/main/dados/balance.csv')
ForcaeTorque

# Faça o gráfico do torque na direção y (My [Nm]) em função do tempo (Time [s]).
import matplotlib.pyplot as plt
plt.figure(figsize=(15,7))
plt.plot(ForcaeTorque['Time[s]'], ForcaeTorque['My[Nm]'])
plt.xlabel('Time [s]')
plt.ylabel('Torque na direção y (My [Nm]')
plt.grid()
plt.show()

# Média
mediaY = ForcaeTorque['My[Nm]'].mean()
print(mediaY)
# Desvio-padrão
desviopadraoY = ForcaeTorque['My[Nm]'].std()
print(desviopadraoY)
# Mostre na tela a média e o desvio-padrão do torque na direção y.
import numpy as np
plt.figure(figsize=(15,5))
plt.plot(np.arange(0,len(ForcaeTorque)), ForcaeTorque['My[Nm]'], marker = 'o', linestyle = '', label = 'Torque na direção Y', color = 'black')
plt.plot(np.arange(0,len(ForcaeTorque)), ForcaeTorque['My[Nm]'].mean()*np.ones(len(ForcaeTorque)), marker = '', linestyle = '-', color = 'red', label = 'Média')
plt.plot(np.arange(0,len(ForcaeTorque)), (ForcaeTorque['My[Nm]'].mean() + desviopadraoY)*np.ones(len(ForcaeTorque)), marker = '', linestyle = '--', color = 'blue', label = 'Desvio=padrão')
plt.plot(np.arange(0,len(ForcaeTorque)), (ForcaeTorque['My[Nm]'].mean() - desviopadraoY)*np.ones(len(ForcaeTorque)), marker = '', linestyle = '--', color = 'blue')
plt.legend()
plt.show()