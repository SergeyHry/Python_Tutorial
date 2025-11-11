import numpy as np
import pandas as pd
from transformers.models.auto.image_processing_auto import model_type

df = pd.read_csv('tips.csv')
#print(df.describe().transpose())
print(df.sort_values('tip', ascending=True)) #ascending von klenen bis Großem
print(df['total_bill'].idxmin()) #finden min und max Index   corilation wie die Coluns abhängig von einander
print(df.transpose())
print(df['sex'].value_counts())# zählt die Anzahl der Werten Male 157 Female 87
print(len(df['day'].unique())) # Anzahl der Uniqe Einträge
print(df['day'].value_counts())
# ersetzen die Werten
print(df['sex'].replace(['Male','Female'], ['M','F']))
#mymap = {'Female':'F', 'Male':'M'}
# df['sex'].map(mymap)
simpedf = pd.DataFrame(np.random.randint(0,2,(4,4)), columns=['A', 'B', 'C', 'D'])
print(simpedf)
print(simpedf.duplicated())
#   A  B  C  D
#   0  1  0  1  0 False
#   1  0  0  0  0 False
#   2  1  1  0  1 False
#   3  0  0  0  0 True
#df.drop_dublicates() löscht Dublicaten

#print (df[df['total_bill'].between(10,20 , inclusive='both')]) between 10 und 20 iclusive mit 10 inclusive
print(df.nlargest(10,'tip'))
print(df.nsmallest(10, 'tip'))
# print(df.sort_values('tip', ascending = True).iloc[0:2]) gleiche aber mit sort_values
print(df.sample(10)) # 10 zufäligen Einträge

# ---Missing Data ---
#1 оставить
#2 удалить
#3 заменить

#np.nan is np.nan True
df = pd.read_csv('movie_scores.csv')
print(df)
print(df.isnull())
print(df[df['pre_movie_score'].notnull()]) # alle Zeile wo keine null gibt
print(df[(df['pre_movie_score'].isnull()) & (df['first_name'].notnull())])
df.dropna() #löscht alles wo nan ist
#df = df.dropna(thresh=2)  2 Отображение строк в которых есть по крайней мере 2 значения
#df = df.fillna(0)  alle nan ersetzen
df[['pre_movie_score', 'post_movie_score']] = df[['pre_movie_score','post_movie_score']].fillna(df['pre_movie_score'].mean())
print(df)
#interpalate заменит отсутсвующие данные интерпалированными

#Group By

df1 = pd.read_csv('mpg.csv')
df1['horsepower'] = pd.to_numeric(df1['horsepower'], errors='coerce')
print(df1[df1['cylinders'].isin([6,8])].groupby(['model_year', 'cylinders']).mean(numeric_only=True))
#df1 = df1.groupby(['model_year', 'cylinders']).mean(numeric_only=True)
print(df1.transpose()) # für bessere Übersicht
print(df1.index.names) # nindex namen multiindex

print(df1.loc[70:80])
#df3 = df1.xs(key=4, level = 'cylinders')  nur cylinders 4
# df1.agg()  функции агригации std, mean

#axis0 = pd.concat([one,two],axis=0) обьединение таблиц с одинаковой структурой
#two.columns = one.columns
#index geben df.index = range(len(df))

#Merge Обьединение как в SQL

