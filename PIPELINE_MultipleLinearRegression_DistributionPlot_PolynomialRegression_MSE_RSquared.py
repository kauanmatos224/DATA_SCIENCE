import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

#IMPORTA BIBLIOTECA DE VISUALIZAÇAÕ SEABORN
import seaborn as sns
#IMPORTA BIBLIOTECA DE VISUALIZAÇAÕ SEABORN



# CRIAÇÃO DE REGREÇÃO POLINOMAL
import sklearn.preprocessing



#CONTRUÇÃO DE PIPELINE
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
#CONTRUÇÃO DE PIPELINE


from sklearn.preprocessing import PolynomialFeatures


#erro quadratico medio - MULTIPLE LINEAR REGRESSION
from sklearn.metrics import mean_squared_error



#R SQUARED E MSE PARA POLINOMIAL REGRESSION
from sklearn.metrics import r2_score
path = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/automobileEDA.csv'
df = pd.read_csv(path)
df.head()




#IMPORTAÇÕES------------------------------------------------------------------------












  

#PLOTA GRAFICO DE DISTRIBUIÇÃO, RESIDUO E REGESSÃO LINEAR
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
        sns.regplot(x=dataf[x1], y=dataf[y1], data=dataf)
        plt.ylim(0,)
        
     elif (plot_type == 'resid'):   #plota o gráfico de resíduo linear
         plt.figure(figsize=(width, height))
         sns.residplot(dataf[x1], df[y1])

    
     elif (plot_type == 'distribution'): #plota gráfico de distribuição em curvas
         
         lm = LinearRegression()
         lm.fit(df[x1], df[y1])
         y_prediction = lm.predict(df[x1])
         
         
         plt.figure(figsize=(width, height))

         ax1 = sns.kdeplot(df[y1], color="r", label="Actual Value")
         sns.kdeplot(y_prediction, color="b", label="Fitted Values" , ax=ax1)


         plt.title('Actual vs Fitted Values for '+ y1)
         plt.xlabel(y1)
        
         '''abaixo, cria um contador para extrair da variável de termos independentes
         os rótulos do eixo X do gráfico a partir de seus índices
         '''
         c=0   
         ylabel = ''
         while(c < len(x1)):
             ylabel = ylabel+" | "+x1[c] +"|"
             
             c+=1
             print(c)
                    
         plt.ylabel(ylabel) #insere a string de rótulos

         
         

     '''
     abaixo, verifica se na invocação do método foi pedidio para salvar a imagem
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

''' **O Termo independente poderá ser uma array de valores se for o caso do gráfico de 
distribuição, seguindo o seguinte formato ['valor1', 'valor2', 'valor3'....]
'''

#PLOTA GRAFICO DE DISTRIBUIÇÃO, RESIDUO E REGESSÃO LINEAR















#---------------------IMPLEMENTATION LINEAR REGRESSION--------------------------

#CRIAÇÃO DE OBJETO LINER REGRESSION
lm = LinearRegression()
#CRIAÇÃO DE OBJETO LINER REGRESSION





#PAGAR VALORES 'x' VARIAVEL PREDIDITAVA E 'Y' VARIAVEL PREDITA
X = df[['highway-mpg']]
Y = df['price']
#PAGAR VALORES 'x' VARIAVEL PREDIDITAVA E 'Y' VARIAVEL PREDITA





#MÉTODO "fit" - OBTEM PARAMETROS DOS METODOS B-1 e B-0 PARA CONTRUIR LINHA
lm.fit(X,Y)
#MÉTODO "fit" - OBTEM PARAMETROS DOS METODOS B-1 e B-0 PARA CONTRUIR LINHA






#REALIZA PREVISÕES POR MEIO DE REGRESSÃO LINEAR
Yhat=lm.predict(X)
a = Yhat[0:5]   
#REALIZA PREVISÕES POR MEIO DE REGRESSÃO LINEAR




#Yhat = a + b  X


#CAPTURA O VALOR DO COEFICIENTE B_0
B_ZERO = lm.intercept_
#CAPTURA O VALOR DO COEFICIENTE B_0




#CAPTURA O COEFICIENTE B_1
b_UM = lm.coef_
#CAPTURA O COEFICIENTE B_1




#PAGAR VALORES 'x' VARIAVEL PREDIDITAVA E 'Y' VARIAVEL PREDITA
lm1 = LinearRegression()

X = df[['engine-size']]
Y = df['price']

lm1.fit(X,Y)
#PAGAR VALORES 'x' VARIAVEL PREDIDITAVA E 'Y' VARIAVEL PREDITA
#Yhat=-7963.34 - 166.86*X


lm1_coef = lm1.coef_

lm1_intercept = lm1.intercept_

EQUATION =  -7963.34 + (166.86* X)





#---------------------IMPLEMENTATION LINEAR REGRESSION--------------------------














#---------------------IMPLEMENTATION MULTIPLE LINEAR REGRESSION--------------------------

#PEGA OS VALORES DAS VARIAVEIS PREDITORAS
Z = df[['horsepower', 'curb-weight', 'engine-size', 'highway-mpg']]
#PEGA OS VALORES DAS VARIAVEIS PREDITORAS






#CONSTRÓI OS PONTOS DA REGRAÇÃO LINEAR
lm.fit(Z, df['price'])
#CONTRÓI OS PONTOS DA REGRAÇÃO LINEAR







# QUESTION 2 - A
lm2 = LinearRegression()
x = df[['normalized-losses', 'highway-mpg']]
Y = df['price']
# QUESTION 2 - A
# QUESTION 2 - B
lm2.fit(x, Y)

# QUESTION 2 - A






#GRAFICO DISPERSÃO - RESIDUO -  ENTRE HIGWAY MPG E PRICE
width = 12
height = 10
plt.figure(figsize=(width, height))
sns.regplot(x="highway-mpg", y="price", data=df)
plt.ylim(0,)
plt.clf()
#GRAFICO DISPERSÃO - RESIDUO -  ENTRE HIGWAY MPG E PRICE







#CRIAR GRAFICO DE RESIDUO DE "highway-mpg", E "price"
create_plot(df, "highway-mpg", "price", "resid", "regplot1.png")
#CRIAR GRAFICO DE RESIDUO DE "highway-mpg", E "price"







#CONSTROI REGRESSAÕ LINAR MULTIPLA COM VARIAVEL Z QUE PREVE O PRICE
Y_hat = lm.predict(Z)
#CONSTROI REGRESSAÕ LINAR MULTIPLA COM VARIAVEL Z QUE PREVE O PRICE








#CONSTRUÇAÕ DE GRAFICO DE DISTRIBUIÇÃO
'''
plt.figure(figsize=(width, height))


ax1 = sns.distplot(df['price'], hist=False, color="r", label="Actual Value")
sns.distplot(Y_hat, hist=False, color="b", label="Fitted Values" , ax=ax1)


plt.title('Actual vs Fitted Values for Price')
plt.xlabel('Price (in dollars)')
plt.ylabel('Proportion of Cars')

plt.show()
plt.close()
'''
#CONSTRUÇAÕ DE GRAFICO DE DISTRIBUIÇÃO






#FUNÇAÕ - CONSTRUÇÃO DE GRAFICO DE DISTRIBUIÇÃO DA REGRESSAÕ LINEAR MULTIPLA 
create_plot(df, ['horsepower', 'curb-weight', 'engine-size', 'highway-mpg'], "price", "distribution", "Dispplot2.png")
#FUNÇAÕ - CONSTRUÇÃO DE GRAFICO DE DISTRIBUIÇÃO DA REGRESSAÕ LINEAR MULTIPLA 






#---------------------IMPLEMENTATION MULTIPLE LINEAR REGRESSION--------------------------













#---------------------IMPLEMENTATION POLINOMIAL REGRESSION--------------------------------


#FUNÇÃO - CRIA FUNÇÃO PARA EXIBIR GRAFICO DE REGRESSÃO POLINOMIAL
def PlotPolly(model, independent_variable, dependent_variabble, Name):
    x_new = np.linspace(15, 55, 100)
    y_new = model(x_new)

    plt.plot(independent_variable, dependent_variabble, '.', x_new, y_new, '-')
    plt.title('Polynomial Fit with Matplotlib for Price ~ Length')
    ax = plt.gca()
    ax.set_facecolor((0.898, 0.898, 0.898))
    fig = plt.gcf()
    plt.xlabel(Name)
    plt.ylabel('Price of Cars')

    plt.show()
    plt.close()
    
#FUNÇÃO - CRIA FUNÇÃO PARA EXIBIR GRAFICO DE REGRESSÃO POLINOMIAL







# RECEBE OS VALORES DO ARRAY
x = df['highway-mpg']
y = df['price']
# RECEBE OS VALORES DO ARRAY






#CRIAÇÃO DA REGRESSÃO POLINOMIAL
f = np.polyfit(x, y, 3)
p = np.poly1d(f)
print(p)
#CRIAÇÃO DA REGRESSÃO POLINOMIAL







#CRIAR GRAFICO DA REGRESSÃO POLINOMIAL - CHAMA FUNÇÃO
PlotPolly(p, x, y, 'highway-mpg')
#CRIAR GRAFICO DA REGRESSÃO POLINOMIAL - CHAMA FUNÇÃO







#Z = df[['horsepower', 'curb-weight', 'engine-size', 'highway-mpg']]
#SELECIONA O GRAU DAS OPERAÇÕES PARA CRIAÇÃO DE FEATURES
pr=sklearn.preprocessing.PolynomialFeatures(degree=2)
#SELECIONA O GRAU DAS OPERAÇÕES PARA CRIAÇÃO DE FEATURES







#CRIA AS FEATURES
Z_pr=pr.fit_transform(Z)
#CRIA AS FEATURES







#LISTA QUNATIDADE - RIGISTROS - FEATURES/COLUNAS/VARIAVEIS - TRANSFORMA EM TUPLA
Z.shape
#LISTA QUNATIDADE - RIGISTROS - FEATURES/COLUNAS/VARIAVEIS - TRANSFORMA EM TUPLA







#LISTA QUNATIDADE - RIGISTROS - FEATURES/COLUNAS/VARIAVEIS - TRANSFORMA EM TUPLA
Z_pr.shape
#LISTA QUNATIDADE - RIGISTROS - FEATURES/COLUNAS/VARIAVEIS - TRANSFORMA EM TUPLA.







#LISTA DE TUPLAS - OBJETO LINER REGRESSION - POLINOMIALFEATURES -  STANDARDSCALER
Input=[('scale',StandardScaler()), ('polynomial', PolynomialFeatures(include_bias=False)), ('model',LinearRegression())]
#LISTA DE TUPLAS - OBJETO LINER REGRESSION - POLINOMIALFEATURES -  STANDARDSCALER






#CRIA PIPELINE - RECEBE COMO PARAMETRO LISTA DE TUPLAS COM OBJETOS 
pipe=Pipeline(Input)
#CRIA PIPELINE - RECEBE COMO PARAMETRO LISTA DE TUPLAS COM OBJETOS







#CONVERTE O VALOR DO Z PARA FLOAT PARA NAÕ DAR ERRO AO APLICAR O PIPELINE
Z = Z.astype(float)
#CONVERTE O VALOR DO Z PARA FLOAT PARA NAÕ DAR ERRO AO APLICAR O PIPELINE







#EXECUTA O FIT DENTRO DO PIPELINE PARA EXECUTAR TRABSFORMAÇÕES PRÉDETERMINDADAS
#DENTRO DO PIPELINE NA ESTRUTURA DE DADOS 'Z' E 'y' 
#----ALINHA MODELO DE REGRESSÃO LINEAR
pipe.fit(Z,y)
#----ALINHA MODELO DE REGRESSÃO LINEAR
#EXECUTA O FIT DENTRO DO PIPELINE PARA EXECUTAR TRABSFORMAÇÕES PRÉDETERMINDADAS
#DENTRO DO PIPELINE NA ESTRUTURA DE DADOS 'Z' E 'y'






#REALIZA PREDIÇÃO COM OS VALORES DE Z NO PIPELINE
ypipe=pipe.predict(Z)
ypipe[0:4]
#REALIZA PREDIÇÃO COM OS VALORES DE Z NO PIPELINE






#CONTROI INPUT - CIBTEM AS OPERAÇÕES DO PIPELINE
#OPERAÇÕES - PADRONIZAÇÃO DE ESCALA - REGREÇÃO LINEAR
Input=[('scale',StandardScaler()), ('model',LinearRegression())]
#CONTROI INPUT - CIBTEM AS OPERAÇÕES DO PIPELINE
#OPERAÇÕES - PADRONIZAÇÃO DE ESCALA - REGREÇÃO LINEAR







#CRIA O PIEPELINE
pipe = Pipeline(Input)
#CRIA O PIEPELINE







#CONTRÓI GRAFICO DE DISTRIBUIÇÃO COM KDEPLOT -  MULTIPLE LINEAR REGRESION PIPELINE
width = 12
height = 10
plt.figure(figsize=(width, height))
ax1 = sns.kdeplot(df['price'], color="r", label="Actual Value")
sns.kdeplot(ypipe, color="b", label="Fitted Values" , ax=ax1)
plt.title('Actual vs Fitted Values for price')
plt.xlabel('price')
plt.show()
#CONTRÓI GRAFICO DE DISTRIBUIÇÃO COM KDEPLOT -  MULTIPLE LINEAR REGRESION PIPELINE
















#MSE E R^ - MEDIDAS PARA AVALIAÇÃO In-Sample-----------------------------------------


#MSE - ERRO QUADRATICO MÉDIO - DETERMINA A PROXIMIDADE DA MÉDIA DOS VALORES 
#DOS VALORES REAIS DO MODELO COM OS VALORES PREVISTOS


#R-SQUARED - DETERMINA SE A VARIACIA DOS VALORES REAIS É EQUIVALENTE A DOS 
#VALORES PREVISTOS. O RESULTADO DO CALCULO VARIA DE 0 A 1.
# QUANTO MAIS PROXIMO DE 1 MAIOR A EQUIVALENCIA DA VARIANCIA.




#FIT - ALINHAR MODELO
lm.fit(X, Y)
#FIT - ALINHAR MODELO






#CALCUOLO DO R^ SQUARED
print('The R-square is: ', lm.score(X, Y))
#CALCUOLO DO R^ SQUARED








#CALCULO MSE - MEAN SQUARED ERROR
Yhat=lm.predict(X)
print('The output of the first four predicted value is: ', Yhat[0:4])
#CALCULO MSE - MEAN SQUARED ERROR






#BIBLOTECA ABAICXO NECESSARIA PARA A EXECUÇÃO
#from sklearn.metrics import mean_squared_error






# R^2 - R SQUARED - MULTIPLE LINEAR REGRESSION 
# fit the model 
lm.fit(Z, df['price'])
# Find the R^2
print('The R-square is: ', lm.score(Z, df['price']))
# R^2 - R SQUARED - MULTIPLE LINEAR REGRESSION







#REALIZA PREDIÇÕES PARA CALCULO DO MSE
Y_predict_multifit = lm.predict(Z)
#REALIZA PREDIÇÕES PARA CALCULO DO MSE

#CALCULA MSE DE MUTIPLE LINEAER REGRESSION
print('The mean square error of price and predicted value using multifit is: ', \
      mean_squared_error(df['price'], Y_predict_multifit))
#CALCULA MSE DE MUTIPLE LINEAER REGRESSION







#IMPORTAR - CALCULO DO R^ QUADRADO PARA POLINOMIAL FIT
#from sklearn.metrics import r2_score






# R^2 - R SQUARED - POLINOMIAL FIT
r_squared = r2_score(y, p(x))
print('The R-square value is: ', r_squared)
# R^2 - R SQUARED - POLINOMIAL FIT







#MSE - POLINOMIAL REGRESSION
print(mean_squared_error(df['price'], p(x)))
#MSE - POLINOMIAL REGRESSION



#MSE E R^ - MEDIDAS PARA AVALIAÇÃO In-Sample-----------------------------------------














#PRODUZINDO PREDIÇAÕ USANDO MÉTODO PREDICT-------------------------------------






#CRIA OBJETO NEW INPUT COM VALORES DE ZERO A 100 OBTIDOS PELO NP.ARANGE
new_input=np.arange(1, 100, 1).reshape(-1, 1)
#CRIA OBJETO NEW INPUT COM VALORES DE ZERO A 100 OBTIDOS PELO NP.ARANGE






#ALINHAR MODELO COM VALORES DE X E Y
lm.fit(X, Y)
#ALINHAR MODELO COM VALORES DE X E Y






#REALIZAR PREDIÇÃO USANDO O MÉTODO PREDICT
yhat=lm.predict(new_input)
print(yhat[0:5])
#REALIZAR PREDIÇÃO USANDO O MÉTODO PREDICT






#CRIA GRAFICO DA PREDIÇÃO
plt.plot(new_input, yhat)
plt.show()
#CRIA GRAFICO DA PREDIÇÃO





#PRODUZINDO PREDIÇAÕ USANDO MÉTODO PREDICT-------------------------------------





