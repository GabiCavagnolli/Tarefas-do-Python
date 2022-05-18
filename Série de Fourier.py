# -*- coding: utf-8 -*-
"""
Created on Wed May 18 10:58:46 2022

@author: GRCav
"""

#Calcular a aproximação de uma onda quadrada seguindo a seguinte expressão (a expressão abaixo é calculada utilizando uma teoria matemática conhecida como série de Fourier):
    #x(t) = 4/pi + x + sin[(2i+1)*t]/2i-1
    
#a) N = 10
import math
s = 0
t1 = 1
for i in range(1, 11):
    s1 = 4 / math.pi * s + math.sin((2*i-1)*t1)/2*i-1
print('x(t) =', s1)
    
#b)N = 100
import math
s = 0
t2 = 2
for i in range(1, 100):
    s2 = 4 / math.pi * s + math.sin((2*i-1)*t2)/2*i-1
print('x(t) =', s2)

#c) N = 1000
import math
s = 0
t3 = 3
for i in range(1, 1000):
    s3 = 4 / math.pi * s + math.sin((2*i-1)*t3)/2*i-1
print('x(t) =', s3)

#d) N = 10000
import math
s = 0
t4 = 4
for i in range(1, 10000):
    s4 = 4 / math.pi * s + math.sin((2*i-1)*t4)/2*i-1
print('x(t) =', s4)

#Coloque todas as aproximações em um único gráfico, com a aproximação de x(t) em função de t.
s = (s1, s2, s3, s4)
t = (t1, t2, t3, t3)
import matplotlib.pyplot as plt
plt.figure()
plt.plot(s, t, marker = 'o', linestyle ='--', color = 'black')
plt.xlabel('Aproximação de x(t)')
plt.ylabel('t')
plt.show()