# -*- coding: utf-8 -*-

"1-"
import numpy as np
"O volume de uma esfera com raio contida em uma variável R"
"a)"
R1 = 0.32
"raio da esfera é 0.32 metros"
V1 = 4*np.pi*R1**3/3
print('V1=',V1,'cm3')

import numpy as np
"O volume de uma esfera com raio contida em uma variável R"
"b)"
R2 = 1
"raio da esfera é 1 metro"
V2 = 4*np.pi*R2**3/3
print('V2=',V2,'CM3')

import numpy as np
"O volume de uma esfera com raio contida em uma variável R"
"C)"
R3 = 1.9
"raio da esfera é 1.9 metros"
V3 = 4*np.pi*R3**3/3
print('V3=',V3,'CM3')




"2-"
"Temperatura em Fahrenheit dada a temperatura em Celsius contida em uma variavel Tc"
"a)"
Tc1 = -10
"Temperatura: -10ºC"
Tf1 = Tc1*1.8+32
print('Tf1=',Tf1,'ºF')

"Temperatura em Fahrenheit dada a temperatura em Celsius contida em uma variavel Tc"
"b)"
Tc2 = 30
"Temperaruta: 30ºC"
Tf2 = Tc2*1.8+32
print('Tf2=',Tf2,'ºF')

"Temperatura em Fahrenheit dada a temperatura em Celsius contida em uma variavel Tc"
"C)"
Tc3 = 5
"Temperatura: 5ºC"
Tf3 = Tc3*1.8+32
print('Tf3=',Tf3,'ºF')




"3-"
import math
import numpy as np
"O tamanho do lado c de um triângulo com lados a, b e ângulo teta entre os lados a e b conhecidos. a, b e teta devem estar gravadas em variáveis. A expressão para isso é conhecida como lei dos cossenos:"
"a)"
a1=1
b1=2
teta1=30
"Lado a tem mendida 1, lado b tem medida 2 e teta tem medida 30º (pi/6 radianos)"
c1=math.sqrt(a1**2+b1**2-2*a1*b1*np.cos(np.pi/6))
print('c1=',c1,)

import math
import numpy as np
"O tamanho do lado c de um triângulo com lados a, b e ângulo teta entre os lados a e b conhecidos. a, b e teta devem estar gravadas em variáveis. A expressão para isso é conhecida como lei dos cossenos:"
"b)"
a2=3
b2=1
teta2=45
"Lado a tem medida 3, lado b tem medida 1 e teta tem medida 45º (pi/4 radianos)"
c2=math.sqrt(a2**2+b2**2-2*a2*b2*np.cos(np.pi/4))
print('c2=',c2)

import math
import numpy as np
"O tamanho do lado c de um triângulo com lados a, b e ângulo teta entre os lados a e b conhecidos. a, b e teta devem estar gravadas em variáveis. A expressão para isso é conhecida como lei dos cossenos:"
"c)"
a3=10
b3=11
teta3=15
"Lado a tem medida 10, lado b tem medida 11 e teta tem medida 15º (pi/12 radianos)"
c3=math.sqrt(a3**2+b3**2-2*a3*b3*np.cos(np.pi/12))
print('c3=',c3)




"4-"
import math
"A série de Fibonacci é uma sequência de números inteiros em que cada número da série é a soma dos dois números anteriores"
"a)"
i1=30
Fi1=(((1+math.sqrt(5))/2)**i1-((1-math.sqrt(5))/2)**i1)/math.sqrt(5)
print('Fi1=',Fi1)

import math
"A série de Fibonacci é uma sequência de números inteiros em que cada número da série é a soma dos dois números anteriores"
"b)"
i2=31
Fi2=(((1+math.sqrt(5))/2)**i2-((1-math.sqrt(5))/2)**i2)/math.sqrt(5)
print('Fi2=',Fi2)

import math
"A série de Fibonacci é uma sequência de números inteiros em que cada número da série é a soma dos dois números anteriores"
"c)"
i3=32
Fi3=(((1+math.sqrt(5))/2)**i3-((1-math.sqrt(5))/2)**i3)/math.sqrt(5)
print('Fi3=',Fi3)