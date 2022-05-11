# -*- coding: utf-8 -*-
"""
Created on Wed May 11 11:42:10 2022

@author: GRCav
"""

#taxa de inflação mensal (IGP-DI) no Brasil de fevereiro de 1944 a junho de 2019
import pandas as pd
inflacao = pd.read_csv('https://raw.githubusercontent.com/rnwatanabe/BasesComputacionais2021/main/dados/inflacaoMensal.csv')
inflacao

#Mudando os meses de números para nome em extenso
inflacao [ 'Data' ] =  pd . to_datetime ( inflacao [ 'Mês' ], format = '%m' )
inflacao['Mês'] = inflacao['Data'].dt.month_name()
inflacao = inflacao.drop(columns=['Data'])

#Excluindo todas as linhas que aparecem de 1944 até 1994
inflacaoAntes = inflacao['Ano']>=1995
inflacaoDepois = inflacao[inflacaoAntes]
print(inflacaoDepois)

#Calcule a mediana da inflação mensal nos meses de março a partir de 1995.
medianaMarco = inflacaoDepois[inflacaoDepois['Mês']=='March']['Inflação'].median()
print(medianaMarco)

#Calcule a média da inflação mensal nos meses de março a partir de 1995.
mediaMarco = inflacaoDepois[inflacaoDepois['Mês']=='March']['Inflação'].mean()
print(mediaMarco)

#Calcule o desvio-padrão da inflação mensal nos meses de março a partir de 1995.
DesvioPadrao = inflacaoDepois[inflacaoDepois['Mês']=='March']['Inflação'].std()
print(DesvioPadrao)

#Faça o histograma da inflação mensal nos meses de março a partir de 1995.
import matplotlib.pyplot as plt
plt.figure()
plt.hist(inflacaoDepois[inflacaoDepois['Mês']=='March']['Inflação'])
plt.xlabel('Inflação nos meses de março a partir de 1995')
plt.show()

#A razão da diferença entre a média e a mediana de março ser maior quando se 
#compara todos os anos e menos quando compara somente a partir de 1995 é que, 
#até 1994 a taxa de inflação era exorbitante, conluindo para que a media seja 
#muito maior do que a mediana. Ja a partir de 1995, a taxa de inflação diminui
#consideravelmente, fazendo com que a media e a mediana tenham números próximos
#e, consequentemente, a diferença entre os dois seja muito pequena.


