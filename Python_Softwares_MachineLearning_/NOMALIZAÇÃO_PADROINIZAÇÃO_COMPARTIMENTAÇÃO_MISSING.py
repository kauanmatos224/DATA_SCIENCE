import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.pyplot as plt
#IMPORT THE NEEDED LIBRARY FOR THE RUNNING CODE
#numpy, pandas, matploitlib


#----------IMPORT OF DATA STRUCTURE AND HEAD LAYOUT----------------------------------------------------------------------------------------------------------------




#CREATE A THE VARIABLE THAT RECEIVE 
#THE DATA STRUCTURE WITH THE VALUES RELATED TO CARS
filename = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/auto.csv"
#CREATE A THE VARIABLE THAT RECEIVE 
#THE DATA STRUCTURE WITH THE VALUES RELATED TO CARS




#CREATE THE ARRAY WITH VALUES RELATED TO HEAD/LABEL FOR THE DATAFRAME
headers = ["symboling",
           "normalized-losses",
           "make","fuel-type",
           "aspiration", 
           "num-of-doors",
           "body-style",
           "drive-wheels",
           "engine-location",
           "wheel-base", 
           "length",
           "width",
           "height",
           "curb-weight",
           "engine-type",
           "num-of-cylinders", 
           "engine-size",
           "fuel-system",
           "bore",
           "stroke",
           "compression-ratio",
           "horsepower",
           "peak-rpm",
           "city-mpg",
           "highway-mpg",
           "price"]
#CREATE THE ARRAY WITH VALUES RELATED TO HEAD/LABEL FOR THE DATAFRAME



#INSERT THE HEAD IN THE DATAFRAME 
df = pd.read_csv(filename, names = headers)


#READ THE FIRSTs FIVE VALUES
print("FIRST VIFE VELUES OF THE DATAFRAME: ")
print(df.head())
print("-----------------------------")





#REPLACES THE VALUES EQUAL "NaN"
df.replace("?", np.nan, inplace = True)
#REPLACES THE VALUES EQUAL "NaN"




#READ THE FIRSTs 
df.head(5)
print("#REPLACES THE VALUES EQUAL NaN: ")
print(df.head(5))
print("-----------------------------")



#----------IMPORT THE DATA STRUCTURES AND HEAD LAYOUT---------------------------
#SUBSTIRUIR O VALOR AUSENTE DE 'num-of-doors' PELO MAIS FREQUENTE
df["num-of-doors"].replace(np.nan, "four", inplace=True)
#-----------------------------------------------------------------


#RETIRAR AS LINHAS SEM VALORES EM PRICE
df.dropna(subset=["price"], axis=0, inplace=True)



# reset index, because we droped two rows
df.reset_index(drop=True, inplace=True)


#-----------------------DETECT OF MISSING VALUE - MISSING-------------------------------------------------------------------





#-----------------------DETECT OF MISSING VALUE - MISSING-------------------------------------------------------------------


#CREATE DATA STRUCTURES WITH DATA MISSING
missing_data = df.isnull()
#CREATE DATA STRUCTURES WITH DATA MISSING



#PRINT THE NISSING VALUE OF DATA STRUCTURE
print("PRINT THE NISSINGVALUE OF DATA STRUCTURE")
print(missing_data.head(5))
print("-----------------------------")


#LOOP - COUNT MISSING VALUES IN THE COLUMNS - PRINT THE NAME OF COLUMNS TOO 
for column in missing_data.columns.values.tolist():
    print(column)
    print (missing_data[column].value_counts())
    print("")        
#LOOP - COUNT MISSING VALUES IN THE COLUMNS - PRINT THE NAME OF COLUMNS TOO

#-----LOOP GUIDE------
#!TRUE - MISSING VALUE
#!FALSE - PRESENT VALUE 
#!THE NUMBER AFTER THE BOOLEAN IS THE COUNT OF MISSING VALUES
#-----LOOP GUIDE------
    

    
    
    



#CALCULATATION MEAN OF COLUNM 
#NORMALIZED-LOSSES
avg_norm_loss = df["normalized-losses"].astype("float").mean(axis=0)
print("Average of normalized-losses:", avg_norm_loss)



#REPLACE THE MISSING VALUES OF THE MEAN OF COLUMN "normalized-losses" WHITIN DATA STRUCTURE
df["normalized-losses"].replace(np.nan, avg_norm_loss, inplace=True)



#CALCULATATION MEAN OF COLUNM  "stroke" AND REPLACE YOUR VALUE
avg_stroke = df["stroke"].astype("float").mean(axis=0)
df["stroke"].replace(np.nan, avg_stroke, inplace=True)
#----------------------------------------------------------



#MOSTRAR O TIPO DE DADOS MAIS COMUM "num-of-doors" E CONTAR QUANTOS VALORES HA DE CADA
print("MOSTRAR O TIPO DE DADOS MAIS COMUM _num-of-doors_ E CONTAR QUANTOS VALORES HÁ DE CADA")
print(df['num-of-doors'].value_counts())


#MOSTRAR O VALOR MAIS COMUM EM "num-of-doors"
df['num-of-doors'].value_counts().idxmax()


#SUBSTIRUIR O VALOR AUSENTE DE 'num-of-doors' PELO MAIS FREQUENTE
df["num-of-doors"].replace(np.nan, "four", inplace=True)
#-----------------------------------------------------------------


#RETIRAR AS LINHAS SEM VALORES EM PRICE
df.dropna(subset=["price"], axis=0, inplace=True)

# reset index, because we droped two rows
df.reset_index(drop=True, inplace=True)


#-----------------------DETECT OF MISSING VALUE - MISSING-------------------------------------------------------------------





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

#RELAÇÃO MATEMATICA PARA TRANFORMAÇÃO DE VALOR PARA INTERVALO QUE VARIE DE 0 A 1
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






#FUNCTION FOR CREATE PLOTS 
def create_plot(dataf, x1, y1 , plot_type, savename):
     
     #limpa e fecha o gráfico atual (ultimo gráfico plotado)
     plt.clf()
     plt.close()
     
     #define as dimensões da figura / gráfico
     width = 12
     height = 10
     
     
     # abaixo, verifica o parâmetro passado na invocação do método referente ao tipo de 
     # gráfico a ser plotado
     
     if(plot_type == 'regression'): #plota o gráfico de regressão linear
        plt.figure(figsize=(width, height))
        sns.regplot(x=dataf[[x1]], y=dataf[y1], data=dataf)
        plt.ylim(0,)
        
     elif (plot_type == 'resid'):   #plota o gráfico de resíduo linear
         plt.figure(figsize=(width, height))
         sns.residplot(dataf[[x1]], df[y1])
         
     
     # abaixo, verifica se na invocação do método foi pedidio para salvar a imagem
     # respectiva var savename deverá conter caminho/nome_arquivo.extensao ou caminho\nome_arquivo.extensao
     # se for S.O windows 
     
     if len(savename) > 0:
        plt.savefig(savename)    
        

     plt.show() #mostra o gráfico



# chama a função passando os seguintes parâmetros:
#     dataframe,
#     termo independente,
#     termo dependente,
#     tipo de gráfico,
#     nome de salvamento do gráfico + extensão
# 

create_plot(df, "highway-mpg", "price", "resid", "regplot1.png")









#-----CONSTRUÇÃO DE HISTOGRAMA COM OS DADOS DE "horsepower"




#import matplotlib.pyplot as plt

#CRIAÇÃO DO GRAFICO
def histogram_plot(dataframe_df, x_label, y_label, title):
    
    plt.clf()
    # #limpar
    
    #DEFINIÇÃO DOS ATRIBUTOS
    plt.hist(dataframe_df)
    plt.xlabel(x_label) #<------TITULO X DO GRAFICO
    plt.ylabel(y_label) #<-----TITULO Y DO GRAFICO
    plt.title(title) # <------TITULO DO GRAFICO
    plt.show()


histogram_plot(df["horsepower"], "horsepower", "count", "horsepower bins")

#MANEGE PLOTS GUIDE---------------------
# plt.clf()
# #limpar

# plt.savefig("figura1.png")
# #Salvar a figura

# plt.show()
# #Mostrar grafico

#MANEGE PLOTS GUIDE---------------------

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





#CONSTROI GRAFICO
plt.clf()
# #limpar

plt.bar(group_names, df["horsepower-binned"].value_counts())

#CONTRUÇÃO DO HISTOGRAMA/GRAFICO DO COMPARTIMENTO
plt.xlabel("horsepower") #TITULO DO X
#READ THE FIRSTs 
plt.ylabel("count")#TITULO DO Y
plt.title("horsepower bins")#TITULO
plt.show()

#CONTRUÇÃO DO HISTOGRAMA/GRAFICO DO COMPARTIMENTO



#----------CONSTRUIR HISTOGRAMA DOS COMPARTIMENTOS DE "horsepower-binned"




#----------HISTOGRAMA - VALORES DE "horsepower" DIVIDIDOS EM 3 CLASSIFICAÇÕES


#ATRIBUTOS DE HISTOGRAMA - VALORES DE "horsepower" E QUANTIDADE DE "bins" = 3

plt.clf()
# #limpar

plt.hist(df["horsepower"], bins = 3)


#ENVIAR RÓTULOS PARA O GRÁFICO
plt.xlabel("horsepower")
plt.ylabel("count")
plt.title("horsepower bins")
plt.show()

#-------------------------BINNING------------------------------------------------------------------------------------------------------




#READ THE FIRSTs 
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
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    


    