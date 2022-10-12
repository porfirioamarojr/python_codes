import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model as lm

#loading data
df_raw = pd.read_csv('/home/amaroj/Downloads/data_akbilgic2.csv')

#preparação dos dados    *
#features
x_train = df_raw.drop(columns=['BOVESPA', 'date'])

for i in x_train:
  x_train[i] = x_train[i].apply(lambda x: str(x).replace(",","."))

#for i in x_train:
#  x_train[i] = x_train[i].astype('float64')

#response data variable 
y_train = df_raw.drop(columns=['date', 'ISE', 'ISE.1', 'SP', 'DAX', 'FTSE', 'NIKKEI', 'EU', 'EM'])
y_train['BOVESPA'] = y_train['BOVESPA'].apply(lambda x: str(x).replace(",","."))
y_train['BOVESPA'] = y_train['BOVESPA'].astype('float64')
#visualização da tabela sem os dados 'BOVESPA' e 'date' #print(x_train.head())
#visualização dos dados da 'BOVESPA' #print(y_train.head())

#model training    *
#model description
model_lr = lm.LinearRegression()
#model training
model_lr.fit(x_train, y_train)
#prdiction
prediction = model_lr.predict(x_train)
#visualização das 100 primeiras predições #prediction[0:100]

#performance metrics    *
df1 = df_raw.drop(columns=['date', 'ISE', 'ISE.1', 'SP', 'DAX', 'FTSE', 'NIKKEI', 'EU', 'EM'])
df1['BOVESPA'] = df1['BOVESPA'].apply(lambda x: str(x).replace(",","."))
df1['BOVESPA'] = df1['BOVESPA'].astype('float64')

df1['prediction'] = prediction

df1['error'] = df1['BOVESPA'] - df1['prediction']
df1['error_abs'] = np.abs(df1['error'])

df1['error_perc'] = ((df1['BOVESPA'] - df1['prediction'])/df1['BOVESPA'])
df1['error_perc_abs'] = np.abs(df1['error_perc'])

#mean absolute error    *
mae = np.mean(df1['error_abs'])
print('MAE: {}'.format(mae))
#mean absolute percentage error
#mape = np.mean(df1['error_perc_abs'])
#print('MAPE: {}'.format(mape))

#Gráfico da predição
plt.plot(df1["prediction"],color='red',marker='o', lw='1', ms='2')
plt.legend(["Prediction"])
plt.grid()
plt.show()
#Gráfico da BOVESPA
plt.plot(df1["BOVESPA"],color='blue',marker='o', lw='1', ms='2')
plt.legend(["BOVESPA"])
plt.grid()
plt.show()
#COMPARAÇÃO DOS GRÁFICOS
plt.plot(df1["BOVESPA"],color='blue',marker='o', lw='1', ms='2')
plt.plot(df1["prediction"],color='red',marker='o', lw='1', ms='2')
plt.legend(["Prediction","BOVESPA"])
plt.grid()
plt.show()

#sklearn.metrics.auc(x, y)

