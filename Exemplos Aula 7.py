# -*- coding: utf-8 -*-
"""
Created on Mon May 16 09:06:59 2022

@author: GRCav
"""

#Exemplo 1
#Na tabela contendo os dados do Campeonato Brasileiro de 2018, que está em https://raw.githubusercontent.com/rnwatanabe/BasesComputacionais2021/main/dados/tabelaBrasileirao2018.csv, crie uma nova coluna que contenha o número de gols feito no jogo.
import pandas as pd
jogo = pd.read_csv('https://raw.githubusercontent.com/rnwatanabe/BasesComputacionais2021/main/dados/tabelaBrasileirao2018.csv')
jogo
#nova coluna que contenha o número de gols feito no jogo
jogo['Gols'] = jogo['Placar do Mandante'] + jogo['Placar do Visitante']

#Exemplo 2
#Considere a tabela com as visualizações de um usuário de Netflix. Qual a série mais vista por esse usuário?
netflix = pd.read_csv("https://raw.githubusercontent.com/rnwatanabe/BasesComputacionais2021/main/dados/netflix.csv")
netflix['Programa'] = netflix['Title'].str.split(':', n = 1, expand = True)[0]
#Qual a série mais vista por esse usuário?
netflix['Programa'].mode()

#Exemplo 3
#Considere a tabela contendo os dados do Campeonato Brasileiro de 2018, que está em https://raw.githubusercontent.com/rnwatanabe/BasesComputacionais2021/main/dados/tabelaBrasileirao2018.csv.
import pandas as pd
jogo = pd.read_csv('https://raw.githubusercontent.com/rnwatanabe/BasesComputacionais2021/main/dados/tabelaBrasileirao2018.csv')
jogo
#1) Leia a tabela e receba o nome de um time que participou do campeonato.
time = input('Digite um time:')
#2) Receba uma opção: saldo, soma, tomados
if time in jogo['Mandante'].unique():
    opcao = input('Digite uma opção [Saldo, Soma ou Tomados]:')
    if opcao == 'Saldo':
        saldo_mandante = jogo.query('Mandante == "'+time+'"')['Placar do Mandante'] - jogo.query('Mandante == "'+time+'"')['Placar do Visitante']    
        saldo_visitante = jogo.query('Visitante == "'+time+'"')['Placar do Visitante'] - jogo.query('Visitante == "'+time+'"')['Placar do Mandante']
        saldo = saldo_mandante .sum() + saldo_visitante.sum()
        print('O time', time, 'teve um saldo de', saldo, 'gols')
    elif opcao == 'Soma':
        soma_mandante = jogo.query('Mandante == "'+time+'"')['Placar do Mandante']
        soma_visitante = jogo.query('Visitante == "'+time+'"')['Placar do Visitante']
        soma = soma_mandante.sum() + soma_visitante.sum()
        print('O time', time, 'teve um total de gols igual a', soma)
    elif opcao == 'Tomados':
        tomados_mandante = jogo.query('Mandante == "'+time+'"')['Placar do Visitante'] 
        tomados_visitante = jogo.query('Visitante == "'+time+'"')['Placar do Mandante']
        tomados = tomados_mandante.sum() + tomados_visitante.sum()
        print('O time', time, 'levou um total de', tomados, 'gols')
    else:
        print("Erro se entrada")
else:
    print("Erro de entrada")
    
#Exemplo 4
#Considere a tabela com diversas informações de sujeitos que participaram de um experimento de controle da postura, encontrada em https://raw.githubusercontent.com/rnwatanabe/BasesComputacionais2021/main/dados/BDSinfo.csv.  
import pandas as pd
experimento = pd.read_csv('https://raw.githubusercontent.com/rnwatanabe/BasesComputacionais2021/main/dados/BDSinfo.csv', sep = '\t')
experimento
#1) Ler o link da planilha e receber um número do sujeito (coluna Subject) a ser considerado.
sujeito = input('Digite um número:')
#2) Mostrar se a altura desse sujeito é maior, menor ou igual à média de altura dos sujeitos do mesmo Gênero.
genero = experimento.query('Subject == ' + sujeito)['Gender'].iloc[0]
altura = experimento.query('Subject ==' + sujeito)['Height'].iloc[0]
media_altura_genero = experimento.query('Gender == "'+genero+'"')['Height'].mean()
if altura > media_altura_genero:
    print('O sujeto', sujeito, 'tem a altura igual a', altura, 'cm, maior que a média de altura do gênero', genero)
elif altura < media_altura_genero:
    print("O sujeito", sujeito, 'tem a altura igual a', altura, 'cm, menor que a média de altura do gênero', genero)
else:
    print('O sujeito', sujeito, 'tem a altura igual a', altura, 'cm, igual a média de altura do gênero', genero)
    
#Exemplo 5
#Considere a planilha que contém a porcetagem de analfabetismo nas Unidades da Federação do Brasil de 1981 a 2014, encontrada no link https://raw.githubusercontent.com/rnwatanabe/BasesComputacionais2021/main/dados/analfabetismo.csv .
import pandas as pd
analfabetismo = pd.read_csv('https://raw.githubusercontent.com/rnwatanabe/BasesComputacionais2021/main/dados/analfabetismo.csv')
analfabetismo
#1) receber do teclado uma Unidade da Federação.
unidade_federacao = input('Digite uma Unidade da Federação:')
#2) calcular a regressão linear entre os anos e a taxa de analfabetismo da Unidade da Federação escolhida.
#3) fazer o gráfico de dispersão da taxa de analfabetismo da Unidade da Federação. No mesmo gráfico, fazer a reta da regressão linear encontrada.
import numpy as np
import matplotlib.pyplot as plt
if unidade_federacao in analfabetismo.columns:
    m, b = np.polyfit(analfabetismo['Ano'], analfabetismo[unidade_federacao], deg = 1)
    print(m)
    print(b)
    plt.figure()
    plt.plot(analfabetismo['Ano'] , analfabetismo[unidade_federacao], marker='o', color='red', linestyle='')
    plt.grid()
    plt.show()
    #4) receber do teclado um ano maior do que 2014 e mostrar a previsão da taxa de analfabetismo para a Unidade da Federação escolhida.
    ano = int(input('Digite um ano:'))
    prev = m * ano + b
    if ano > 2014:
        print("No ano de", ano, 'a previsão é que a taxa de analfabetismo em', unidade_federacao, 'seja %.2f %%.' %prev)
    else:
        print( 'Erro de entrada')
else:
    print('Erro de entrada')
    
#Exemplo 6
#Considere a tabela com diversas informações de sujeitos que participaram de um experimento de controle da postura, encontrada em https://raw.githubusercontent.com/rnwatanabe/BasesComputacionais2021/main/dados/BDSinfo.csv.
import pandas as pd
BDSinfo = pd.read_csv('https://raw.githubusercontent.com/rnwatanabe/BasesComputacionais2021/main/dados/BDSinfo.csv', sep = '\t')
BDSinfo
#1) Ler a tabela e pedir para ser digitado duas colunas da tabela.
coluna_a = input("Digite o nome de uma coluna da tabela:")
coluna_b = input("Digite o nome de outra coluna da mesma tabela:")
#2) Se as duas colunas forem numéricas (tipo float64 ou int64), calcular o índice de correlação de cada uma das colunas com a coluna Falls12m. Essa coluna contém o número de quedas nos 12 meses que antecederam o experimento.
coluna_a_numerica = BDSinfo[coluna_a].dtype == 'float64' or BDSinfo[coluna_a].dtype == 'int64'
coluna_b_numerica = BDSinfo[coluna_b].dtype == 'float64' or BDSinfo[coluna_b].dtype == 'int64'
if coluna_a_numerica and coluna_b_numerica and coluna_a != coluna_b:
    correlacao_a = BDSinfo[coluna_a].corr(BDSinfo['Falls12m'])
    correlacao_b = BDSinfo[coluna_b].corr(BDSinfo['Falls12m'])
    #3) Mostrar na tela qual das colunas tem um módulo da correlação com a coluna Falls12m maior e as duas correlações.
    import numpy as np
    if np.abs(correlacao_a) > np.abs(correlacao_b):
        print(coluna_a, 'tem o módulo da correlação (%.3f' %correlacao_a,') com Falls12m maior do que', coluna_b, '(%.3f' %correlacao_b ,')')    
    elif np.abs(correlacao_a) < np.abs(correlacao_b):
        print(coluna_b, 'tem o módulo da correlação (%.3f' %correlacao_b,') com Falls12m maior do que', coluna_a, '(%.3f' %correlacao_a ,')')         
    else:
            print(coluna_a, 'tem o módulo da correlação (%.3f' %correlacao_a,') com Falls12m igual a', coluna_b, '(%.3f' %correlacao_b ,')')
else:
    print('Erro de entrada')