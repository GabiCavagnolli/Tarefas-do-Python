# -*- coding: utf-8 -*-
"""
Created on Thu May 19 12:48:05 2022

@author: GRCav
"""
#colocar uma probabilidade para mudar um caracter

import random as rd

frase = 'bases computacionais da ciencia'

frase_sorteada = [' ']*len(frase)


n = 0
frase_sorteada = list(frase_sorteada)
for i in range(len(frase)):
        frase_sorteada[i] = rd.choice(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                                       'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
                                       'w', 'x', 'y', 'z', ' '])
frase_sorteada = ''.join(frase_sorteada)
    
n = n + 1
print(frase_sorteada)
    
x = rd.uniform(1, 24)
if x == 'a':
    print('Existe uma probabilidade de 80 % para não mudar o caractere a')
else:
    print('Exte uma probabilidade de 80 % para o caracter a mudar')
    
    
   