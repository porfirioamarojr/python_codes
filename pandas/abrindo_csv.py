import pandas as pd
import matplotlib.pyplot as plt
x = pd.read_csv(r'/home/amaroj/Downloads/2019-property-sales-data.csv')
#histograma: plt.hist(x['Sale_price'], bins=20) #variavel bins disrespeito a distanacia entre as barras
#pizza: plt.pie(x['Sale_price'],labels=x["PropType"],autopct=%1,0f%%) autopct relacionado a casas decimasi depois da ','
#grafico de linhas: plt.plot(x["Sale_price"])

print(x)

plt.show()