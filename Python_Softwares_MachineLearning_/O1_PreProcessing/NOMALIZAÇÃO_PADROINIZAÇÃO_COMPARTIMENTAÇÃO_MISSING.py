
# THIS CLASS WAS WROTE WITH COMMENTS IN EN-US AND PT-BR  


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#IMPORT THE NEEDED LIBRARY FOR THE RUNNING CODE
#numpy, pandas, matploitlib


#----------IMPORT OF DATA STRUCTURE AND HEAD THE LAYOUT----------------------------------------------------------------------------------------------------------------




#CREATE A THE VARIABLE THAT RECEIVE 
#THE DATA STRUCTURE WITH THE VALUES RELATED TO CARS
filename = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/auto.csv"
#CREATE A THE VARIABLE THAT RECEIVE 
#THE DATA STRUCTURE WITH THE VALUES RELATED TO CARS




#CREATE THE ARRAY WITH VALUES RELATED TO HEAD/LABEL FOR THE DATAFRAME
headers = ["symboling",
           "normalized-losses",
           "make",
           "fuel-type",
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
print("FIRST FIVE VALUES OF THE DATAFRAME: ")
print(df.head())
print("-----------------------------")



#----------IMPORT THE DATA STRUCTURE AND HEAD THE LAYOUT-----------------------------------------------------------------------------



#REPLACES THE VALUES EQUAL "NaN"
df.replace("?", np.nan, inplace = True)
#REPLACES THE VALUES EQUAL "NaN"




#READ THE FIRSTs 
df.head(5)
print("#REPLACES THE VALUES EQUAL NaN: ")
print(df.head(5))
print("-----------------------------")



#SUBSTIRUIR O VALOR AUSENTE DE 'num-of-doors' PELO MAIS FREQUENTE
#REPLACE THE MISSING VALUE OF 'num-of-doors' WITH THE MOST FREQUENT
df["num-of-doors"].replace(np.nan, "four", inplace=True)
#-----------------------------------------------------------------


#RETIRAR AS LINHAS SEM VALORES EM PRICE
#REMOVE LINES WITHOUT VALUES IN PRICE
df.dropna(subset=["price"], axis=0, inplace=True)



# reset index, because we droped two rows
df.reset_index(drop=True, inplace=True)


#-----------------------DETECT OF MISSING VALUE - MISSING-------------------------------------------------------------------





#CREATE DATA STRUCTURES WITH DATA MISSING
missing_data = df.isnull()
#CREATE DATA STRUCTURES WITH DATA MISSING



#PRINT THE NISSING VALUE OF DATA STRUCTURE
print("PRINT THE firsth five NISSING-VALUE OF DATA STRUCTURE")
missing_value_df = missing_data.head(5)
print(missing_value_df)
print("-----------------------------")


#LOOP - COUNT MISSING VALUES IN THE COLUMNS - PRINT THE NAME OF COLUMNS TOO 
for column in missing_data.columns.values.tolist():
    print(column)
    print (missing_data[column].value_counts())
    print(" ")
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
#SHOW THE MOST COMMON DATA in  "num-of-doors" AND COUNT HOW MANY VALUES THERE ARE OF EACH
print("More often Value type in _num-of-doors_ and count values")
print(df['num-of-doors'].value_counts())


#MOSTRAR O VALOR MAIS COMUM EM "num-of-doors"
# SHOW THE MOST COMMON VALUE IN "num-of-doors"
df['num-of-doors'].value_counts().idxmax()
print("SHOW THE MOST COMMON VALUE IN num-of-doors")
print(df['num-of-doors'].value_counts().idxmax())

#SUBSTIRUIR O VALOR AUSENTE DE 'num-of-doors' PELO MAIS FREQUENTE
#REPLACE THE MISSING VALUE OF 'num-of-doors' WITH THE MOST FREQUENT
df["num-of-doors"].replace(np.nan, "four", inplace=True)
#-----------------------------------------------------------------


#RETIRAR AS LINHAS SEM VALORES EM PRICE
#REMOVE LINES WITHOUT VALUES IN PRICE
df.dropna(subset=["price"], axis=0, inplace=True)

# reset index, because we droped two rows
df.reset_index(drop=True, inplace=True)


#-----------------------DETECT OF MISSING VALUE - MISSING-------------------------------------------------------------------





#-------------------------#PADRONIZAÇÃO DE DADOS data_standardization----------------------------------------------



#CONVERSÕES DE VALORES DAS COLUNAS PARA O TIPO RESPECTIVO DELAS
# CONVERSIONS OF COLUMN VALUES TO THEIR RESPECTIVE TYPE

df[["bore", "stroke"]] = df[["bore", "stroke"]].astype("float")
df[["normalized-losses"]] = df[["normalized-losses"]].astype("int")
df[["price"]] = df[["price"]].astype("float")
df[["peak-rpm"]] = df[["peak-rpm"]].astype("float")

#CONVERSÕES DE VALORES DAS COLUNAS PARA O TIPO RESPECTIVO DELAS
# CONVERSIONS OF COLUMN VALUES TO THEIR RESPECTIVE TYPE



#------------------------#PADRONIZAÇÃO DE DADOS data_standardization-----------------------------------------------------

#conversão: MILHAS POR GALÃO (mpg) para (L/100KM)
# RELAÇAÕ DE CONVERSÃO L/100km = 235 / 
#---------------------------------------
#conversion: MILES PER GALLON (mpg) to (L/100KM)
# CONVERSION RATIO L/100km = 235 / mpg

df['city-L/100km'] = 235/df["city-mpg"]

# COLUMN RENAME
df.rename(columns={'"city-mpg"':'city-L/100km'}, inplace=True)


#ANLISAR A MUDANÇA  DOS DADOS
# ANALYZE DATA CHANGED
df.head()



#------------------------#PADRONIZAÇÃO DE DADOS data_standardization----------------------------------------------------------------------
#REALIZAR CONVERSÃO POR MEIO DA RELAÇÃO MATEMATICA DE CONVERSÃO MPG - L/100KM
#PERFORM CONVERSION THROUGH THE MATHEMATICAL RELATION OF MPG CONVERSION - L/100KM
df["highway-mpg"] = 235/df["highway-mpg"]


#RENOMEAÇÃO DA COLUNA
# COLUMN RENAME
df.rename(columns={'"highway-mpg"':'highway-L/100km'}, inplace=True)


# ANALISAR NOVO ESTADO DOS DADOS
# ANALYZE NEW DATA STATE
df.head()
#-----------------------#PADRONIZAÇÃO DE DADOS data_standardization------------------------------------------------------------------------



#-----------------------#NORMALIZAÇÃO/NORMALIZATION------------------------------------------------------------------------------------------

#RELAÇÃO MATEMATICA PARA TRANFORMAÇÃO DE VALOR PARA INTERVALO QUE VARIE DE 0 A 1
#(valor original)/(valor máximo)
#------------------------------
# MATHEMATICAL RELATION FOR TRANSFORMATION OF VALUE TO INTERVAL THAT VARIES FROM 0 TO 1
#(original value)/(maximum value)
df['length'] = df['length']/df['length'].max()
df['width'] = df['width']/df['width'].max()


#-----------------------#NORMALIZAÇÃO/NORMALIZATION------------------------------------------------------------------------------------------



#-------------------------NORMALIZATION OF COLUMN HEIGHT---------------------------------------------------------------------- -----------
df['height'] = df['height']/df['height'].max()
#-------------------------NORMALIZATION OF COLUMN HEIGHT---------------------------------------------------------------------- -----------








#-------------------------BINNING------------------------------------------------------------------------------------------------------
# DATA BINNING
#IMPORT THE MATPLOIT LIB LIBRARY TO RUN THE CODE WITH THE FOLLOWING SYNTAX:
    
#-------IMPORT------------
#%matplotlib inline
#import matplotlib as plt
#from matplotlib import pyplot
#-------IMPORT------------


#CONVERSAÕ DOS DADOS PARA O FORMATO CORRETO 
#!(NA IMPLEMENTAÇAÕ A COVERÇÃO ERA PARA VALOR "int", NO ENTANTO ERROS FORAM APRESENTADOS NESSE ESTADO)
#--------------------------------------
# CONVERTING THE DATA TO THE CORRECT FORMAT
#!(IN THE IMPLEMENTATION THE COVERAGE WAS FOR "int" VALUE, HOWEVER ERRORS WERE DISPLAYED IN THIS STATE)
df["horsepower"] = df["horsepower"].astype(float, copy=True)






#FUNCTION FOR CREATE PLOTS 
def create_plot(dataf, x1, y1 , plot_type, savename):
     
     #limpa e fecha o gráfico atual (ultimo gráfico plotado)
     #clears and closes the current graph (last graph plotted)
     plt.clf()
     plt.clf()
     plt.close()
     
     #define as dimensões da figura / gráfico
     #DEFINE PLOT FIGURE DIMENSIONS 
     width = 12
     height = 10
     
     
     # below, check the parameter passed in the method invocation 
     # referring to the type of graph to be plotted
     if(plot_type == 'regression'): #plota o gráfico de regressão linear
        plt.figure(figsize=(width, height))
        sns.regplot(x=dataf[[x1]], y=dataf[y1], data=dataf)
        plt.ylim(0,)
        
     elif (plot_type == 'resid'):   #plota o gráfico de resíduo linear
         plt.figure(figsize=(width, height))
         sns.residplot(dataf[[x1]], df[y1])
         
     
     # abaixo, verifica se na invocação do método foi pedidio para salvar a imagem
     # respectiva var savename deverá conter caminho/nome_arquivo.extensao ou 
     # caminho\nome_arquivo.extensao se for S.O windows 
         #---------------------------
     # below, check if the method invocation asked to save the image
     # respective var savename must contain path/file_name.extension or
     # path\filename.extension if OS windows
     
     if len(savename) > 0:
        plt.savefig(savename)    
        

     plt.show() # show the graph




#-----------------------------------------------
# chama a função passando os seguintes parâmetros:
#     dataframe,
#     termo independente,
#     termo dependente,
#     tipo de gráfico,
#     nome de salvamento do gráfico + extensão
# 
#------------------------------------------------
# call the function passing the following parameters:
# dataframe,
# independent term,
# dependent term,
# chart type,
# chart save name + extension
#
create_plot(df, "highway-mpg", "price", "resid", "regplot1.png")
#-------------------------------------------------------------







#-----CONSTRUCTION OF HISTOGRAM WITH DATA FROM "horsepower"------------------------------------------------------------




#import matplotlib.pyplot as plt

# CREATE THE GRAPHIC
def histogram_plot(dataframe_df, x_label, y_label, title):
    
    plt.clf()
    # #limpar
    
    #DEFINIÇÃO DOS ATRIBUTOS
    plt.hist(dataframe_df)
    plt.xlabel(x_label) #<------TITLE X 
    plt.ylabel(y_label) #<-----TITLE Y 
    plt.title(title) # <------TITLE OF THE PLOT
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


#-----CONSTRUCTION OF HISTOGRAM WITH DATA FROM "horsepower"










#---------------LINSPACE - #ENGLISH-US

# CONSTRUCTION OF COMPARTMENTS FROM A DATAFRAME

# METHOD SYNTAX:
#linspace(start_value, end_value, numbers_generated);



#ATTRIBUTES:
    
#PARAMETER "start_value" WILL BE MINIMUM VALUE OF DATAFRAME "Horse-power"
#PARAMETER "and_value" WILL BE MINIMUM VALUE OF DATAFRAME "Horse-power"
#PARAMETER "numbers_generated" WILL BE THE QUANTITY OF COMPARTMENTS OR "BINS" OF "Horse-power"
#start_value = min(df["horsepower"])
#end_value = max(df["horsepower"])
#numbers_generated = 4
#TO BUILD THE QUANTITY OF COMPARTMENTS TO PLACE
# THE NUMBER OF COMPARTMENTS + 1 IN THE ATTRIBUTE VALUE numbers_generated

#---------------LINSPACE - #ENGLISH-US 




#---------------LINSPACE pT-BR

# CONSTRUÇÃO DE COMPARTIMENTOS A PARTIR DE UM DATAFRAME

#SINTAXE DO MÉTODO:
#linspace(start_value, end_value, numbers_generated);



#ATRIBUTOS:
    
#PARAMETRO "start_value" SERÁ VALOR MINIMO DO DATAFRAME "Horse-power"
#PARAMETRO "end_value" SERÁ VALOR MAXIMO DO DATAFRAME "Horse-power"
#PARAMETRO "numbers_generated" SERÁ A QUANTIDADE DE COMPARTIMENTOS OU "BINS" DE  "Horse-power"
#start_value = min(df["horsepower"])
#end_value = max(df["horsepower"])
#numbers_generated = 4
#PARA CONSTRUIR A QUANTIDADE DE COMPARTIMENTOS COLOCAR 
#A QUANTIDADE DE COMPARTIMENTOS + 1 NO VALOR DO ATRIBUTO numbers_generated




#CONTRUÇAÕ DOS COMPATIMENTOS "bins" DO DATAFRAME COM LINSPACE
bins = np.linspace(min(df["horsepower"]), max(df["horsepower"]), 4)
print(bins)
#CONTRUÇAÕ DOS COMPATIMENTOS "bins" DO DATAFRAME COM LINSPACE


#---------------LINSPACE pT-BR


# DEFINITION OF DATA COMPARTMENT NAMES
group_names = ['Low', 'Medium', 'High']
# DEFINITION OF DATA COMPARTMENT NAMES



#SEGMENTATION OF THE COLUMN "horse_power" INTO 3 COMPARTMENTS
df['horsepower-binned'] = pd.cut(df['horsepower'], bins, labels=group_names, include_lowest=True)
df[['horsepower','horsepower-binned']].head(20)
#SEGMENTATION OF THE COLUMN "horse_power" INTO 3 COMPARTMENTS



#SHOW THE MOST COMMON TYPE INSIDE "horsepower-binned"
df["horsepower-binned"].value_counts()
#SHOW THE MOST COMMON TYPE INSIDE "horsepower-binned"




#----------CONSTRUCT HISTOGRAM OF "horsepower-binned" COMPARTMENTS




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



#----------CONSTRUCT HISTOGRAM OF "horsepower-binned" COMPARTMENTS





#----------HISTOGRAM - "horsepower" VALUES DIVIDED INTO 3 CLASSIFICATIONS

#HISTOGRAM ATTRIBUTES - VALUES OF "horsepower" AND QUANTITY OF "bins" = 3
plt.clf()
# #clean

plt.hist(df["horsepower"], bins = 3)


#SEND LABELS TO THE CHART
plt.xlabel("horsepower")
plt.ylabel("count")
plt.title("horsepower bins")
plt.show()


#----------HISTOGRAM - "horsepower" VALUES DIVIDED INTO 3 CLASSIFICATIONS

#-------------------------BINNING------------------------------------------------------------------------------------------------------




#READ THE FIRSTs
#-------------------------DUMMY VARIABLE---------------------- -------------------------------
# THESE ARE VARIABLES USED TO DIFFERENTIATE CATEGORIES
#TRANSFORM A VARIABLE (IN THIS CASE A CSV COLUMN) THAT CONTAINS WORDS THAT
#REPRESENT CATEGORIES IN COLUMNS THAT CONTAIN BOOLEAN NUMERIC DATA
#WHERE EACH COLUMN/VARIABLE REPRESENTS A CATEGORY

# THE INDICATOR VARIABLES, OR DUMMY VARIABLES ARE USED FOR THE IMPLEMENTATION
# OF LINEAR REGRESSIONS




#-----------------------------DUMMY VARIABLE FOR "fuel-type"

#CREATES THE INDICATOR VARIABLES (dummy variable) AND ASSIGNS TO THE DATA FRAME
dummy_variable_1 = pd.get_dummies(df["fuel-type"])
print(dummy_variable_1.head())



#CHANGE OF INDICATOR VARIABLE NAMES
dummy_variable_1.rename(columns={'gas':'fuel-type-gas', 'diesel':'fuel-type-diesel'}, inplace=True)
print(dummy_variable_1.head())





# merge data frame "df" and "dummy_variable_1"
#du
#ALLOCATION OF THE DUMMY VARIABLE WITH THE DATAFRAME
df = pd.concat([df, dummy_variable_1], axis=1)

#EXCLUSION OF THE ORIGINAL "fuel-type" COLUMN FROM THE DATAFRAME
df.drop("fuel-type", axis = 1, inplace=True)

#-----------------------------DUMMY VARIABLE FOR "fuel-type"






#-----------------------------DUMMY VARIABLE FOR "aspiration"
dummy_variable_aspiration = pd.get_dummies(df["aspiration"])
dummy_variable_1.rename(columns={'std':'aspiration-std', 'turbo':'aspiration-turbo'}, inplace=True)
dummy_variable_1.head()
df = pd.concat([df, dummy_variable_aspiration], axis=1)
df.drop("aspiration", axis = 1, inplace=True)
#-----------------------------DUMMY VARIABLE FOR "aspiration"





#-------------------------DUMMY VARIABLE-----------------------------------------------------

#SAVING THE NEW DATAFRAME AFTER MODIFICATIONS
df.to_csv('data/clean_df.csv')
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    


    