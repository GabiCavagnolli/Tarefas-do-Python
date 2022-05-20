# -*- coding: utf-8 -*-
"""
Created on Thu May 19 10:47:03 2022

@author: GRCav
"""

import random as rd

#Simule 1000 vezes o jogo.
n = 1000

#Modifique a simulação da ruína do jogador para dois participantes. 
for i in range(n):
        
#Um começa o jogo com 100 reais. 
    creditos_a = 100
    
#O outro começa com 1000 reais. 
    creditos_b = 1000

    aposta = 50

    rodada = 0
    
    perdeu = 0

while rodada < 1000:
       sorteio_a = rd.choice(['ganhou', 'perdeu'])
       if sorteio_a == 'ganhou':
          creditos_a = creditos_a + aposta
       else:
          creditos_a = creditos_a - aposta
          
       rodada = rodada + 1
       print(creditos_a)
       sorteio_b = rd.choice(['ganhou', 'perdeu'])
       if sorteio_b == 'ganhou':
          creditos_b = creditos_b + aposta
       else:
          creditos_b = creditos_b - aposta
          perdeu += 1
          
       rodada = rodada + 1
       print(creditos_b)
#Quantas vezes o jogador inicialmente com mais dinheiro perde o jogo?
print('O jogador inicialmente com mais dinheiro perdeu o jogo', perdeu, 'vezes')


