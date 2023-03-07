# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 10:39:46 2022

@author: kauan
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats




path='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/automobileEDA.csv'
df = pd.read_csv(path)
df.head()


#IMPORT----------------------------------------------------------










#-----------------REG PLOT --- CALCULATION OF CORRELATION--------------------------------------------------------



#Import SEABORN LIBRARY for contruction of the PLOTS with the sintax below
#import seaborn as sns



# SEE THAT IN THE PLOT THE DOTs ARE FIT WITH THE LINE
#POSITIVE CORRELATION DETECTED WITH THE POINTS - THE POINTS INCREASE LIKE THE LINE
sns.regplot(x="engine-size", y="price", data=df)
plt.ylim(0,)
#plt.ylim(0,) <---- CONSTROI O GRAFICO COM O EIXO Y COMEÇADO EM ZERO



#PLOT GUIDE 
#MEAN -  MEAN OF DOTs
#DOTs -  VARIABLE VALUES COMPARED WITH "price"
#Y AXIS VALUES - VALUES OF VARIABLE "prices"
#X AXIS - VALUES OF THE COMPARED VARIABLE  




#CALCULATION OF THE CORRELATION RATE BETWEEN THE VARIABLES 
CORRELAO_1 = df[["engine-size", "price"]].corr()
#0,87 OR 87% CORRELATED 



#-----------------REG PLOT --- CALCULATION OF CORRELATION--------------------------------------------------------








#-----------------REG PLOT --- CALCULATION OF CORRELATION--------------------------------------------------------


#CORRELAÇAÕ ENTRE VARIAVEIS
sns.regplot(x="highway-mpg", y="price", data=df)

print(df[["highway-mpg", "price"]].corr())
#CALCULO DE CORRELAÇAÕ ENTRE VARIAVEIS



#-----------------REG PLOT --- CALCULATION OF CORRELATION--------------------------------------------------------







#-----------------REG PLOT --- CALCULATION OF CORRELATION--------------------------------------------------------


%matplotlib inline 
sns.regplot(x="peak-rpm", y="price", data=df)

#analaise de correlação
df[['peak-rpm','price']].corr()



#-----------------REG PLOT --- CALCULATION OF CORRELATION--------------------------------------------------------















#-------------------------BOX PLOT-------------------------------------------------------




#CRIAÇAÕ DE GRAFICO DE CAIXA - BOX PLOT---------------------------------------
#IMPORTAR BIBLIOTECA A SEGUIR PARA CONSTRUIR O GRAFICO
#import seaborn as sns
%matplotlib inline
sns.boxplot(x="body-style", y="price", data=df)
#CRIAÇAÕ DE GRAFICO DE CAIXA - BOX PLOT---------------------------------------





#CRIAÇAÕ DE GRAFICO DE CAIXA - BOX PLOT---------------------------------------
%matplotlib inline
sns.boxplot(x="engine-location", y="price", data=df)
#CRIAÇAÕ DE GRAFICO DE CAIXA - BOX PLOT---------------------------------------






#CRIAÇAÕ DE GRAFICO DE CAIXA - BOX PLOT---------------------------------------
%matplotlib inline
sns.boxplot(x="drive-wheels", y="price", data=df)
#CRIAÇAÕ DE GRAFICO DE CAIXA - BOX PLOT---------------------------------------




#-------------------------BOX PLOT-------------------------------------------------------











#----------------ESTATISTICAS DESCRITIVAS SOBRE OS DADOS-------------------------------------


#DATAFRAME - ESTATISTICAS DESCRITIVAS-------------------
print(df.describe())
'''
  symboling  normalized-losses  ...      diesel         gas
count  201.000000          201.00000  ...  201.000000  201.000000
mean     0.840796          122.00000  ...    0.099502    0.900498
std      1.254802           31.99625  ...    0.300083    0.300083
min     -2.000000           65.00000  ...    0.000000    0.000000
25%      0.000000          101.00000  ...    0.000000    1.000000
50%      1.000000          122.00000  ...    0.000000    1.000000
75%      2.000000          137.00000  ...    0.000000    1.000000
max      3.000000
'''
#COUNT - QUANTIDADE DE VALORES
#MEAN - MÉDIA DOS VALORES
#STD - DESVIO PADRÃO - INDICA O QUANTO DOS DADOS SÃO CONTINUOS/HOMOGENEOS
#*** QUANNDO O DESVIO PADRÃO É MAIS PRÓXIMO DE ZERO OS DADOS SÃO MAIS HOMOGENEOS
#25% - 25 PORCENTO DO TOTAL DE DADOS
#50% - 50 PORCENTO DA MÉDIA TOTAL DOS DADOS
#75 - 75 PORCENTO DA MÉDIA DO TOTAL DOS DADOS
#MAX -  VALOR MAXIMO DETECTADO OS DADOS 


#DATAFRAME -  ESTATISTICAS DESCRITIVAS-------------------





#DATAFRAME -  ESTATISTICAS DESCRITIVAS CONTENDO VARIAVEIS "object"-------------------


print(df.describe(include=['object']))
'''
          make aspiration  ... fuel-system horsepower-binned
count      201        201  ...         201               200
unique      22          2  ...           8                 3
top     toyota        std  ...        mpfi               Low
freq        32        165  
'''
#COUNT - QUANTIDADE DE VALORES
#UNIQUE - QUANTIDADE DE TIPOS DE VALORES QUE SE REPETEM ATÉ FORMAR O TOTAL(201)
#TOP - O VALOR QUE MAIS APARECE
#FREQ - A QAUNTDADE DE VEZES QUE O VALOR DO TOP APARECE NO CONJUNTO DE DADOS


#DATAFRAME -  ESTATISTICAS DESCRITIVAS CONTENDO VARIAVEIS "object"-------------------


#----------------ESTATISTICAS DESCRITIVAS SOBRE OS DADOS-------------------------------------













#------VALUE COUNTS--------------------------------------------------------------

#COMPREENDER MELHOR A VARIAVEL
#LISTA A QUANTIDADE DE VALORES DE CADA CATEGORIA
#LISTA O TIPO DE VARIAVEL QUE ARMAZENA OS DADOS
#***SÓ FUNCIONA COM COLUNAS UNICAS
#***NÃO FUNCINA COM DATA FRAMES COMPLETOS





#VALUE COUNTS EM "drive-wheels"--------------------------


#.to_frame() - CONVERTE A SERIE/COLUNA EM UM DATAFRAME
drive_wheels_counts = df['drive-wheels'].value_counts().to_frame()
#.to_frame() - CONVERTE A SERIE/COLUNA EM UM DATAFRAME




#RENOMEIA O DATAFRAME PARA "value-counts"
drive_wheels_counts.rename(columns={'drive-wheels': 'value_counts'}, inplace=True)
#RENOMEIA O DATAFRAME PARA "value-counts"
DWC_RENAME = drive_wheels_counts




#RENOMEIA O INDICE DO DATAFRAME
drive_wheels_counts.index.name = 'drive-wheels'
drive_wheels_counts
print(drive_wheels_counts)
'''     
VALOR DO INDICE
    |
    |
    |
   \/
----------------------------         
*drive-wheels* | value_counts  
----------------------------    
fwd          | 118
----------------------------
rwd          | 75
----------------------------
4wd          | 8
#---------------------------
'''
#RENOMEIA O INDICE DO DATAFRAME


#VALUE COUNTS EM "drive-wheels"--------------------------




#VALUE COUNTS EM "engine-location"--------------------------

engine_loc_counts = df['engine-location'].value_counts().to_frame()
engine_loc_counts.rename(columns={'engine-location': 'value_counts'}, inplace=True)
engine_loc_counts.index.name = 'engine-location'
print(engine_loc_counts)


#RESULTADO DO VALUE COUNTS
'''
engine-location   value_counts              
front             198
rear              3

'''
#NÃO É UM BOM PREDITOR PARA PREÇO POISE HÁ APENAS 3 VALORES DA CATERGORIA COM
#MOTOR ATRÁS, DE MODO QUE NÃO REPRESENTA QUANTIDADE SIGNIFICATIVA PARA A 
#CONSTUÇÃO DE UM MODELO PREDITIVO

#RESULTADO DO VALUE COUNTS

#VALUE COUNTS EM "engine-location"--------------------------

#------VALUE COUNTS--------------------------------------------------------------















#---------------------GROUP BY - AGRUPAMENTO--------------------------------------------------------------------------------------------
#VISUALIZAR DADOS EM GRUPOS EM FORMATO DE TABELA





#EXIBE QUAIS OS DADOS CATEGÓRICOS EXISTEM EM 'drive-wheels'
UNI_DRV_W = df['drive-wheels'].unique()





#AGRUPA OS VALORES DAS COLUNAS 'drive-wheels','body-style' e 'price'
df_group_one = df[['drive-wheels','body-style','price']]
#AGRUPA OS VALORES DAS COLUNAS 'drive-wheels','body-style' e 'price'





#AGRUPA OS VALORES CATEGÓRICOS DE 'drive-wheels' COM A MÉDIA DO PREÇO DA 
#RESPECTIVA CATEGORIA
df_group_one = df_group_one.groupby(['drive-wheels'],as_index=False).mean()
#AGRUPA OS VALORES CATEGÓRICOS DE 'drive-wheels' COM A MÉDIA DO PREÇO DA 
#RESPECTIVA CATEGORIA





'''
AGRUPAR VALORES DA CATEGORIA "body-style" e "drive-wheels" COM A MÉDIA DE PREÇO
RESPECTIVA A CATEGORIA DELES
'''
df_gptest = df[['drive-wheels','body-style','price']]
grouped_test1 = df_gptest.groupby(['drive-wheels','body-style'],as_index=False).mean()
'''
AGRUPAR VALORES DA CATEGORIA "body-style" e "drive-wheels" COM A MÉDIA DE PREÇO
RESPECTIVA A CATEGORIA DELES
'''





#AGRUPAR OS VALORES DE 'grouped_test1' EM TABELAS DINAMICAS 
#(PARECIDO COM PLANILHAS EXCEL)
grouped_pivot = grouped_test1.pivot(index='drive-wheels',columns='body-style')
print(grouped_pivot)
#AGRUPAR OS VALORES DE 'grouped_test1' EM TABELAS DINAMICAS 
#(PARECIDO COM PLANILHAS EXCEL)





#PREENCHER DADOS AUSENTES DA TABELA PIVO COM ZERO 
grouped_pivot = grouped_pivot.fillna(0) #fill missing values with 0
#PREENCHER DADOS AUSENTES DA TABELA PIVO COM ZERO





#CRIAR GRAFICO DE CALOR COM BASE NO GROUPED.PIVOT
%matplotlib inline 
plt.pcolor(grouped_pivot, cmap='RdBu')
plt.colorbar()
plt.show()
#CRIAR GRAFICO DE CALOR COM BASE NO GROUPED.PIVOT






#DEFINIR PROPRIEDADES DO GRAFICO DE CALOR--------------------------------------------------------- 
fig, ax = plt.subplots()
im = ax.pcolor(grouped_pivot, cmap='PuRd')
#DEFINE OPADRÃO DE CORES "Red e Blues"

'''MELHORES CORES:
PuRd (ROSA)

Purples

OrRd

Blues

BuGn(VERDE, VERDE AGUA)

Greys (PRETO E BRANCO DO MAIOR PARA O MENOR)

Greys_r(PRETO E BRANCO DO MENOR PARA O MAIOR)

'''


#NOMES DOS EIXOS DO GRAFICO
row_labels = grouped_pivot.columns.levels[1]
col_labels = grouped_pivot.index
#NOMES DOS EIXOS DO GRAFICO



#MOVER RÓTUOLES PARA O CENTRO DA LATERAL DE CADA UNIDADE RETANGULAR
ax.set_xticks(np.arange(grouped_pivot.shape[1]) + 0.5, minor=False)
ax.set_yticks(np.arange(grouped_pivot.shape[0]) + 0.5, minor=False)
#MOVER RÓTUOLES PARA O CENTRO DA LATERAL DE CADA UNIDADE RETANGULAR



#DEFINIR POSIÇÃO DOS RÓTULOS
ax.set_xticklabels(row_labels, minor=False)
ax.set_yticklabels(col_labels, minor=False)
#DEFINIR POSIÇÃO DOS RÓTULOS



#FAZER ROTAÇÃO DE 90 GRAUS CASO NÃO HAJA ESPAÇO PARA OS RÓTULOS EM BAIXO
plt.xticks(rotation=90)
#FAZER ROTAÇÃO DE 90 GRAUS CASO NÃO HAJA ESPAÇO PARA OS RÓTULOS EM BAIXO



#DEFINIR FITA DE ESCALA DE CORES RELACIONADAS COM VALORES
fig.colorbar(im)
#DEFINIR FITA DE ESCALA DE CORES RELACIONADAS COM VALORES



#EXIBE O GRAFICO
plt.show()
#EXIBE O GRAFICO

#CRIAR GRAFICO DE CALOR COM BASE NO GROUPED.PIVOT



#DEFINIR PROPRIEDADES DO GRAFICO DE CALOR--------------------------------------------------------- 




#---------------------GROUP BY - AGRUPAMENTO--------------------------------------------------------------------------------------------














#----------------------------CORRELAÇÃO E CAUSA------------------------------------------------------
#DETERMINAR A CORRELAÇÃO EXIGE O USO DE TESTE DE PEARSON E CALCULO DE P-VALUE

#DETERMINAR CAUSA EXIGE TESTES MAIS COMPLEXOS E EXPERIMENTAÇÃO INDEPENTE






#PEARSON CORRELATION-----------------------------------------------------------
#CALCULA A CORRELAÇÃO LINEAR ENTRE DUAS VARIAVEIS


#VALOR = 1 - CORRELAÇÃO LINEAR POSITIVA - 100% SIGNIFICANTE
#VALOR = 0 - CORRELAÇÃO LINEAR NULA     -   0% SIGNIFICANTE
#VALOR =-1 - CORRELAÇÃO LINEAR NEGATIVA - 100% SIGNIFICANTE




#MÉTODO CORR - CALCULA A CORRELAÇÃO DE PEARSON
df.corr()
#MÉTODO CORR - CALCULA A CORRELAÇÃO DE PEARSON
 




#PEARSON CORRELATION-----------------------------------------------------------
#CALCULA A CORRELAÇÃO ENTRE DUAS VARIAVEIS


#IMPORTAR A BIBLIOTECA A SEGUIR PARA FAZER ESSE CALCULO:
#from scipy import stats




#P - VALUE---------------------------------------------------------------------



#P - VALUE < 0,001 - CORRELAÇÃO FORTE
#P - VALUE < 0,05 - CORRELAÇÃO MODERADA
#P - VALUE < 0,1: - CORRELAÇÃO FRACA
#P - VALUE > 0,1: - CORRELAÇÃO NULA



#---CALCULAR O P-VALUE E CORRELAÇÃO DE PERSON EM TODAS AS VARIAVEIS---------------------------------------------------



#CALCULO DA CORRELAÇÃO DE PERSON E DO P-VALUE ENTRE Wheel-Base -  price
pearson_coef1, p_value1 = stats.pearsonr(df['wheel-base'], df['price'])
print("A CORRELAÇAO DE PEARSON: ", pearson_coef1, " P - VALUE:", p_value1)  
#CALCULO DA CORRELAÇÃO DE PERSON E DO P-VALUE ENTRE Wheel-Base -  price




#CALCULO DA CORRELAÇÃO DE PERSON E DO P-VALUE ENTRE horsepower -  price
pearson_coef2, p_value2 = stats.pearsonr(df['horsepower'], df['price'])
print("A CORRELAÇAO DE PEARSON: ", pearson_coef2, " P - VALUE: ", p_value2)
#CALCULO DA CORRELAÇÃO DE PERSON E DO P-VALUE ENTRE horsepower -  price




#CALCULO DA CORRELAÇÃO DE PERSON E DO P-VALUE ENTRE length - price
pearson_coef3, p_value3 = stats.pearsonr(df['length'], df['price'])
print("A CORRELAÇAO DE PEARSON: ", pearson_coef3, " P - VALUE: ", p_value3)  
#CALCULO DA CORRELAÇÃO DE PERSON E DO P-VALUE ENTRE length - price




#CALCULO DA CORRELAÇÃO DE PERSON E DO P-VALUE ENTRE width - price
pearson_coef4, p_value4 = stats.pearsonr(df['width'], df['price'])
print("A CORRELAÇAO DE PEARSON: ", pearson_coef4, " P - VALUE: ", p_value4) 
#CALCULO DA CORRELAÇÃO DE PERSON E DO P-VALUE ENTRE width - price




#CALCULO DA CORRELAÇÃO DE PERSON E DO P-VALUE ENTRE curb-weight - price
pearson_coef5, p_value5 = stats.pearsonr(df['curb-weight'], df['price'])
print("A CORRELAÇAO DE PEARSON: ", pearson_coef5, " P - VALUE: ", p_value5)  
#CALCULO DA CORRELAÇÃO DE PERSON E DO P-VALUE ENTRE curb-weight - price'''



#CALCULO DA CORRELAÇÃO DE PERSON E DO P-VALUE ENTRE engine-size - price
pearson_coef6, p_value6 = stats.pearsonr(df['engine-size'], df['price'])
print("A CORRELAÇAO DE PEARSON: ", pearson_coef6, " P - VALUE: ", p_value6)
#CALCULO DA CORRELAÇÃO DE PERSON E DO P-VALUE ENTRE engine-size - price




#CALCULO DA CORRELAÇÃO DE PERSON E DO P-VALUE ENTRE bore - price
pearson_coef7, p_value7 = stats.pearsonr(df['bore'], df['price'])
print("A CORRELAÇAO DE PEARSON: ", pearson_coef7, "P - VALUE: ", p_value7 )  
#CALCULO DA CORRELAÇÃO DE PERSON E DO P-VALUE ENTRE bore - price




#CALCULO DA CORRELAÇÃO DE PERSON E DO P-VALUE ENTRE city-mpg - price
pearson_coef8, p_value8 = stats.pearsonr(df['city-mpg'], df['price'])
print("A CORRELAÇAO DE PEARSON: ", pearson_coef8, "P - VALUE: ", p_value8)  
#CALCULO DA CORRELAÇÃO DE PERSON E DO P-VALUE ENTRE city-mpg - price




#CALCULO DA CORRELAÇÃO DE PERSON E DO P-VALUE ENTRE highway-mpg - price
pearson_coef9, p_value9 = stats.pearsonr(df['highway-mpg'], df['price'])
print("A CORRELAÇAO DE PEARSON: ", pearson_coef9, "P - VALUE: ", p_value9)
#CALCULO DA CORRELAÇÃO DE PERSON E DO P-VALUE ENTRE highway-mpg - price

#---CALCULAR O P-VALUE E CORRELAÇÃO DE PERSON EM TODAS AS VARICAVEIS---------------------------------------------------




#P - VALUE---------------------------------------------------------------------


#----------------------------CORRELAÇÃO E CAUSA------------------------------------------------------













#--------------ANOVA---------------------------------------------------------------------------
#AGRUPA VALORES E TIRA SUAS MÉDIA E COMPARA COM OUTOS GRUPOS
#ESSE RESULTADO É A VARIAÇÃO ENTRE GRUPOS DE VALORES
#QUANTO MAIOR A VARIAÇÃO MAIOR A CHANCE DE A VARIAVEL SER PREDITORA
#QUANTO MENOR A CHANCE É PEQUENA


#F - test score - VALOR QUE INDICA A VARIAÇÃO DA MÉDIA
#P - value - VALOR QUE INDICA SE O RESULTA ESTATISTICAMENTE VALIDO





#CRIAÇÃO DE GRUPO COM OS A VARIAVEL "drive-wheels" E "price"
grouped_test2=df_gptest[['drive-wheels', 'price']].groupby(['drive-wheels'])
grouped_test2.head(2)
#CRIAÇÃO DE GRUPO COM OS A VARIAVEL "drive-wheels" E "price"





#MÉTODO get.group - RECEBE OS DADOS DO GRUPO
grouped_test2.get_group('4wd')['price']
#MÉTODO get.group - RECEBE OS DADOS DO GRUPO





#MÉTODO stats.f_oneway - CALCULA O TESTE ANOVA ENTRE OS GRUPOS PARAMETRIZADOS 
f_val, p_val = stats.f_oneway(grouped_test2.get_group('4wd')['price'], grouped_test2.get_group('rwd')['price'])  
#MÉTODO stats.f_oneway - CALCULA O TESTE ANOVA ENTRE OS GRUPOS PARAMETRIZADOS
print( "ANOVA - RESULTADOS F=", f_val, ", P =", p_val)   
#ANOVA results: F= 8.580681368924756 , P = 0.004411492211225333





#MÉTODO stats.f_oneway - CALCULA O TESTE ANOVA ENTRE OS GRUPOS PARAMETRIZADOS
f_val, p_val = stats.f_oneway(grouped_test2.get_group('4wd')['price'], grouped_test2.get_group('fwd')['price'])  
#MÉTODO stats.f_oneway - CALCULA O TESTE ANOVA ENTRE OS GRUPOS PARAMETRIZADOS



print("ANOVA results: F=", f_val, ", P =", p_val)
#ANOVA - RESULTADOS : F= 0.665465750252303 , P = 0.41620116697845666   
#--------------ANOVA---------------------------------------------------------------------------

