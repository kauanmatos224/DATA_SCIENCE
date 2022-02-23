import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#IMPORTA AS BLIOTECAS NECESSARIAS PARA EXECUÇÃO DO CÓDIGO
#numpy, pandas, matploitlib


#----------IMPORTAÇÃO DA ESTRUTURA DE DADOS E CONFIGURAÇÃO DO CABEÇALHO----------------------------------------------------------------------------------------------------------------




#CRIA UMA VARÍAVEL QUE RECEBE A ESTRUTURA DE DADOS COM OS VALORES REFERENTES AOS CARROS
filename = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/auto.csv"
#CRIA UMA VARÍAVEL QUE RECEBE A ESTRUTURA DE DADOS COM OS VALORES REFERENTES AOS CARROS




#CRIA UM ARRAY COM VALORES REFERENTES AO CABEÇALHO/RÓTULO DO DATAFRAME
headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]
#CRIA UM ARRAY COM VALORES REFERENTES AO CABEÇALHO/RÓTULO DO DATAFRAME



#COLOCA O CABEÇALHO 
df = pd.read_csv(filename, names = headers)



#LE OS PRIMEIROS 5 VALORES
df.head()




#SUBSTIRUI OS VALORES DEMARCADOS COMO "NaN"
df.replace("?", np.nan, inplace = True)
#SUBSTIRUI OS VALORES DEMARCADOS COMO "NaN"


df.head(5)

#----------IMPORTAÇÃO DA ESTRUTURA DE DADOS E CONFIGURAÇÃO DO CABEÇALHO--------------------------------------------------------------------------------------------------------------



#-----------------------DETECÇÃO DE VALORES AUSENTES - MISSING-------------------------------------------------------------------



#CRIA ESTRUUTRA DE DADOS  COM OS VALORES REFERENTES AOS DADOS AUSENTES
missing_data = df.isnull()
#CRIA ESTRUUTRA DE DADOS  COM OS VALORES REFERENTES AOS DADOS AUSENTES



#EXIBE O VALOR DA ESTRUTURA DE DADOS
missing_data.head(5)



#LOOP - REALIZA A CONTAGEM DE QUANTOS VALORES SUSENTES EXISTEM EM CADA COLUNA - EXIBE O NOME DE CADA UMA -
for column in missing_data.columns.values.tolist():
    print(column)
    print (missing_data[column].value_counts())
    print("")    
#LOOP - REALIZA A CONTAGEM DE QUANTOS VALORES SUSENTES EXISTEM EM CADA COLUNA - EXIBE O NOME DE CADA UMA -


#!TRUE - VALOR AUSENTE
#!FALSE - VALOR PRESENTE
#!O NÚMERO SEGUIDO DO VALOR BOOLEANO REPRESENTA A QUANTIDADE





#CALCULAR MÉDIA DE UMA COLUNA 
#NORMALIZED-LOSSES
avg_norm_loss = df["normalized-losses"].astype("float").mean(axis=0)
print("Average of normalized-losses:", avg_norm_loss)


#SUBSTIRUIR O VALOR DA MÉDIA DA COLUNA "normalized-losses" DENTRO DA ESTRUTURA DE DADOS
df["normalized-losses"].replace(np.nan, avg_norm_loss, inplace=True)

#CALCULATE MEDIA COLUNA "stroke" E SUBSTIRUIR
avg_stroke = df["stroke"].astype("float").mean(axis=0)
df["stroke"].replace(np.nan, avg_stroke, inplace=True)
#----------------------------------------------------------



#MOSTRAR O TIPO DE DADOS MAIS COMUM "num-of-doors" E CONTAR QUANTOS VALORES HA DE CADA
df['num-of-doors'].value_counts()



#MOSTRAR O VALOR MAIS COMUM EM "num-of-doors"
df['num-of-doors'].value_counts().idxmax()


#SUBSTIRUIR O VALOR AUSENTE DE 'num-of-doors' PELO MAIS FREQUENTE
df["num-of-doors"].replace(np.nan, "four", inplace=True)
#-----------------------------------------------------------------


#RETIRAR AS LINHAS SEM VALORES EM PRICE
df.dropna(subset=["price"], axis=0, inplace=True)

# reset index, because we droped two rows
df.reset_index(drop=True, inplace=True)


#-----------------------DETECÇAÕ DE VALORES AUSENTES - MISSING--------------------------------------------------------------------





#-------------------------#PADRONIZAÇÃO DE DADOS data_standardization----------------------------------------------



#CONVERSÕES DE VALORES DAS COLUNAS PARA O TIPO RESPECTIVO DELAS

df[["bore", "stroke"]] = df[["bore", "stroke"]].astype("float")
df[["normalized-losses"]] = df[["normalized-losses"]].astype("int")
df[["price"]] = df[["price"]].astype("float")
df[["peak-rpm"]] = df[["peak-rpm"]].astype("float")

#CONVERSÕES DE VALORES DAS COLUNAS PARA O TIPO RESPECTIVO DELAS



#------------------------#PADRONIZAÇÃO DE DADOS data_standardization-----------------------------------------------------

#conversão: MILHAS POR GALÃO (mpg) para (L/100KM)
# RELAÇAÕ DE CONVERSÃO L/100km = 235 / mpg
df['city-L/100km'] = 235/df["city-mpg"]


#ANLISAR A MUDANÇA DE ESTADO DOS DADOS
df.head()



#------------------------#PADRONIZAÇÃO DE DADOS data_standardization----------------------------------------------------------------------
#REALIZAR CONVERSÃO POR MEIO DA RELAÇÃO MATEMATICA DE CONVERSÃO MPG - L/100KM
df["highway-mpg"] = 235/df["highway-mpg"]


#RENOMEAÇÃO DA COLUNA
df.rename(columns={'"highway-mpg"':'highway-L/100km'}, inplace=True)


# ANALISAR NOVO ESTADO DOS DADOS
df.head()
#-----------------------#PADRONIZAÇÃO DE DADOS data_standardization------------------------------------------------------------------------



#-----------------------#NORMALIZAÇÃO------------------------------------------------------------------------------------------

#RELAÇÃO MATEMATICA PARA TRANFORMAÇÃO DE VLOR PARA INTERVALO QUE VARIE DE 0 A 1
#(valor original)/(valor máximo)
df['length'] = df['length']/df['length'].max()
df['width'] = df['width']/df['width'].max()


#-----------------------#NORMALIZAÇÃO------------------------------------------------------------------------------------------



#-------------------------NORMALIZAÇÃO DA COLUNA ALTURA---------------------------------------------------------------------------------
df['height'] = df['height']/df['height'].max()
#-------------------------NORMALIZAÇÃO DA COLUNA ALTURA---------------------------------------------------------------------------------









#-------------------------BINNING------------------------------------------------------------------------------------------------------
#COMPARTIMENTAÇÃO DOS DADOS
#IMPORTAR A BIBLIOTECA MATPLOIT LIB PARA EXECUTAR O CÓDIGO COM A SINTAXE A SEGUIR:
    
#-------IMPORTAÇÃO------------ 
#%matplotlib inline
#import matplotlib as plt
#from matplotlib import pyplot
#-------IMPORTAÇÃO------------



#CONVERSAÕ DOS DADOS PARA O FORMATO CORRETO 
#!(NA IMPLEMENTAÇAÕ A COVERÇÃO ERA PARA VALOR "int", NO ENTANTO ERROS FORAM APRESENTADOS NESSE ESTADO)
df["horsepower"]=df["horsepower"].astype(float, copy=True)







def create_plot(dataf, x1, y1 , plot_type, savename):
     
     #limpa e fecha o gráfico atual (ultimo gráfico plotado)
     plt.clf()
     plt.close()
     
     #define as dimensões da figura / gráfico
     width = 12
     height = 10
     
     '''
     abaixo, verifica o parâmetro passado na invocação do método referente ao tipo de 
     gráfico a ser plotado
     '''
     if(plot_type == 'regression'): #plota o gráfico de regressão linear
        plt.figure(figsize=(width, height))
        sns.regplot(x=dataf[[x1]], y=dataf[y1], data=dataf)
        plt.ylim(0,)
        
     elif (plot_type == 'resid'):   #plota o gráfico de resíduo linear
         plt.figure(figsize=(width, height))
         sns.residplot(dataf[[x1]], df[y1])

     '''
     abaixo, verifica se na invocação do método foi pedidio para salvar a imagem
     respectiva var savename deverá conter caminho/nome_arquivo.extensao ou caminho\nome_arquivo.extensao
     se for S.O windows 
     '''
     if len(savename) > 0:
        plt.savefig(savename)    
        
        
     plt.show() #mostra o gráfico



'''chama a função passando os seguintes parâmetros:
    dataframe,
    termo independente,
    termo dependente,
    tipo de gráfico,
    nome de salvamento do gráfico + extensão
'''

create_plot(df, "highway-mpg", "price", "resid", "regplot1.png")









#-----CONSTRUÇÃO DE HISTOGRAMA COM OS DADOS DE "horsepower"



#-------IMPORTAÇÃO------------
%matplotlib inline
import matplotlib as plt
#import matplotlib.pyplot as plt

from matplotlib import pyplot

#CRIAÇÃO DO GRAFICO
plt.pyplot.hist(df["horsepower"]) 


#DEFINIÇÃO DOS ATRIBUTOS
plt.pyplot.xlabel("horsepower") #<------TITULO X DO GRAFICO
plt.pyplot.ylabel("count") #<-----TITULO Y DO GRAFICO
plt.pyplot.title("horsepower bins") # <------TITULO DO GRAFICO
plt.pyplot.show()


'''
plt.clf()
#limpar

plt.savefig("figura1.png")
#Salvar a figura

plt.show()
#Mostrar grafico
'''

#-----CONSTRUÇÃO DE HISTOGRAMA COM OS DADOS DE "horsepower"





#---------------LINSPACE 

# CONSTRUÇÃO DE COMPARTIMENTOS A PARTIR DE UM DATAFRAME

#SINTAXE DO MÉTODO:
#linspace(start_value, end_value, numbers_generated);



#ATRIBUTOS:
    
#PARAMETRO "start_value" SERÁ VALOR MINIMO DO DATAFRAME "Horse-power"
#PARAMETRO "and_value" SERÁ VALOR MINIMO DO DATAFRAME "Horse-power"
#PARAMETRO "numbers_generated" SERÁ A QUANTIDADE DE COMPARTIMENTOS OU "BINS" DE  "Horse-power"
#start_value = min(df["horsepower"])
#end_value = max(df["horsepower"])
#numbers_generated = 4
#PARA CONSTRUIR A QUANTIDADE DE COMPARTIMENTOS COLOCAR 
#A QUANTIDADE DE COMPARTIMENTOS + 1 NO VALOR DO ATRIBUTO numbers_generated




#CONTRUÇAÕ DOS COMPATIMENTOS "bins" DO DATAFRAME COM LINSPACE
bins = np.linspace(min(df["horsepower"]), max(df["horsepower"]), 4)
bins
#CONTRUÇAÕ DOS COMPATIMENTOS "bins" DO DATAFRAME COM LINSPACE


#---------------LINSPACE



#DEFINIÇAÕ DOS NOMES DOS COMPARTIMENTOS DE DADOS 
group_names = ['Low', 'Medium', 'High']
#DEFINIÇAÕ DOS NOMES DOS COMPARTIMENTOS DE DADOS




#SEGMENTAÇÃO DA COLUNA "horse_power" EM 3 COMPARTIMENTOS
df['horsepower-binned'] = pd.cut(df['horsepower'], bins, labels=group_names, include_lowest=True)
df[['horsepower','horsepower-binned']].head(20)
#SEGMENTAÇÃO DA COLUNA "horse_power" EM 3 COMPARTIMENTOS



#MOSTRAR O TIPO MAIS COMUM DENTRO DE "horsepower-binned"
df["horsepower-binned"].value_counts()
#MOSTRAR O TIPO MAIS COMUM DENTRO DE "horsepower-binned"




#----------CONSTRUIR HISTOGRAMA DOS COMPARTIMENTOS DE "horsepower-binned"



#CONTRUIR HISTOGRAMA ATRAVÉS DA IMPORTAÇÃO COM A ESTRUTURA "inline"
%matplotlib inline
import matplotlib as plt
from matplotlib import pyplot
#CONTRUIR HISTOGRAMA ATRAVÉS DA IMPORTAÇÃO COM A ESTRUTURA "inline"



#CONSTROI GRAFICO
pyplot.bar(group_names, df["horsepower-binned"].value_counts())


#CONTRUÇÃO DO HISTOGRAMA/GRAFICO DO COMPARTIMENTO
plt.pyplot.xlabel("horsepower") #TITULO DO X
plt.pyplot.ylabel("count")#TITULO DO Y
plt.pyplot.title("horsepower bins")#TITULO
plt.pyplot.show()

#CONTRUÇÃO DO HISTOGRAMA/GRAFICO DO COMPARTIMENTO



#----------CONSTRUIR HISTOGRAMA DOS COMPARTIMENTOS DE "horsepower-binned"




#----------HISTOGRAMA - VALORES DE "horsepower" DIVIDIDOS EM 3 CLASSIFICAÇÕES
%matplotlib inline
import matplotlib as plt
from matplotlib import pyplot


#ATRIBUTOS DE HISTOGRAMA - VALORES DE "horsepower" E QUANTIDADE DE "bins" = 3
plt.pyplot.hist(df["horsepower"], bins = 3)


#ENVIAR RÓTULOS PARA O GRÁFICO
plt.pyplot.xlabel("horsepower")
plt.pyplot.ylabel("count")
plt.pyplot.title("horsepower bins")
plt.pyplot.show()


#-------------------------BINNING------------------------------------------------------------------------------------------------------




#-------------------------DUMMY VARIABLE-----------------------------------------------------
#SÃO VARIAVEIS USADAS PARA DIFERENCIAR CATEGORIAS
#TRANSFORMA UMA VARIAVEL (NESSE CASO UMA COLUNA DO CSV) QUE CONTEM PALAVRAS QUE 
#REPRESENTAM CATEGORIAS EM COLUNAS QUE CONTEM DADOS NÚMERICOS BOLEANOS
#ONDE CADA COLUNA/ VARIAVEL REPRESENTA UMA CATEGORIA 

#AS VARIAVEIS INDICADORAS, OU DUMMY VARIABLES SÃO UTILIZADAS PARA A IMPLEMENTAÇÃO
#DE REGRESSÕES LINEARES






#------------------------------DUMMY VARIABLE PARA "fuel-type"

#CRIA AS VARIAVEIS INDICADORES(dummy variable) E ATRIBUI AO DATA FRAME
dummy_variable_1 = pd.get_dummies(df["fuel-type"])
print(dummy_variable_1.head())



#ALTERAÇÃO DOS NOMES DAS VARIAVEIS INDICADORAS
dummy_variable_1.rename(columns={'gas':'fuel-type-gas', 'diesel':'fuel-type-diesel'}, inplace=True)
print(dummy_variable_1.head())





# merge data frame "df" and "dummy_variable_1"
#du
#ALOCAÇÃO DA DUMMY VARIABLE COM O DATAFRAME
df = pd.concat([df, dummy_variable_1], axis=1)

#EXCLUSÃO DA COLUNA "fuel-type" ORIGINAL DO DATAFRAME
df.drop("fuel-type", axis = 1, inplace=True)

#-----------------------------DUMMY VARIABLE PARA "fuel-type"





#-----------------------------DUMMY VARIABLE PARA "aspiration"
dummy_variable_aspiration = pd.get_dummies(df["aspiration"])
dummy_variable_1.rename(columns={'std':'aspiration-std', 'turbo':'aspiration-turbo'}, inplace=True)
dummy_variable_1.head()
df = pd.concat([df, dummy_variable_aspiration], axis=1)
df.drop("aspiration", axis = 1, inplace=True)
#-----------------------------DUMMY VARIABLE PARA "aspiration"





#-------------------------DUMMY VARIABLE-----------------------------------------------------

#SALVAMENTO DO DO NOVO DATAFRAME APÓS AS MODIFICAÇÕES
df.to_csv('clean_df.csv')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    



    