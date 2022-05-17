# -*- coding: utf-8 -*-
"""
Created on Tue May 17 10:55:43 2022

@author: GRCav
"""

#Faça a aproximação de  usando a fórmula de Leibniz:
pi = 4 - 4/3 + 4/5 - 4/7 + 4/9 +...

#a) 50 termos
k = 1
s = 0
for i in range(50):
    if i % 2 == 0:
        s += 4/k
    else:
        s += 4/k
    k += 2

print('pi ~=', s)

#b) 500 termos
k = 1
s = 0
for i in range(500):
    if i % 2 == 0:
        s += 4/k
    else:
        s += 4/k
    k += 2

print('pi ~=', s)

#c)1000 termos
k = 1
s = 0
for i in range(1000):
    if i % 2 == 0:
        s += 4/k
    else:
        s += 4/k
    k += 2

print('pi ~=', s)

#d)10000 termos
k = 1
s = 0
for i in range(10000):
    if i % 2 == 0:
        s += 4/k
    else:
        s += 4/k
    k += 2

print('pi ~=', s)