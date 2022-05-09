# -*- coding: utf-8 -*-
"""
Created on Fri May  6 11:04:50 2022

@author: GRCav
"""

"Tabela de histórico de visualização da Netflix"
import pandas as pd
data = pd.read_csv('https://raw.githubusercontent.com/rnwatanabe/BasesComputacionais2021/main/dados/netflix.csv')
data
data['Categoria'] = 'Filme'  
data['Categoria'][data['Title'].str.contains(": Temporada|: Stranger|: Parte")] = 'Série'  
data['Programa'] = data['Title']  
data[['Programa','Episódio']] = data[data['Categoria']=='Série']['Title'].str.split(pat = ': Temporada|: Stranger Things|: Parte', expand = True, n = 1)   
data.loc[data['Categoria']=='Filme', 'Programa'] = data.loc[data['Categoria']=='Filme', 'Title']  
data = data.drop(columns = 'Title')
data['Date'] = pd.to_datetime(data['Date'], format='%d/%m/%Y')
data

"OS 10 programas mais assistidos durante o intervalo de tempo da tabela"
data ['Programa'].value_counts().head (10)

"Criação de coluna Ano/Mês: ano adicionado da fração correspondente ao mês"
print(data['Date'].dt.year)
print(data['Date'].dt.month)
data['Year'] = data ['Date'].dt.year
data['Month'] = data['Date'].dt.month
data['Year/Month'] = data['Year'] + data['Month'] / 12 

"O mês do ano com mais histórico de visualização"
data['Year/Month'].value_counts().head(1)
print('O ano+mês/12 mais assistido foi:',data['Year/Month'].value_counts().head(1))

    