#from transformers import pipeline
import numpy as np
import pandas as pd
import timeit
#ner = pipeline("ner", model="dslim/bert-base-NER", aggregation_strategy="simple")

#text = "Elon Musk founded SpaceX and Tesla in the United States."

#result = ner(text)

#orgs = [e for e in result if e['entity_group'] == 'ORG']
#print(orgs)

x = np.random.randint(1,10, 5)
print(x)
y = x.copy()
y[y>8] = 99
arr = np.arange(10)
arr = arr.reshape(2, 5)
print(arr[0][-1], arr[1][2:-1])
arr2 = np.arange(1, 16).reshape(3, 5)
print(arr2.sum(axis=1))
dict2 = {'name':'Alex', 'age':23, 'location':'South America', 'status': 'single'}
dicti = {'name':'John', 'age':18, 'location':'South America', 'status': 'married'}

x = pd.Series(dicti)
e =x['age']/2
print(x)
print(e)

np.random.seed(101)
mydata = np.random.randint(0,101,(4,3))
myindex = ['CA','NY','AZ','TX']
mycolumns = ['JAN','FEB','MAR']
df = pd.DataFrame(mydata, index=myindex, columns=mycolumns)

df2 = pd.read_csv('tips.csv')
print(df2.columns)
print("Total: ", df2['total_bill'].sum())
#print(df2.head())  Obere Zeile (5) aber kann mehr ausgeben auch die letzten mit .tail()
 # print(df2.describe()) beschreibt Zeilen
df2['Tip_procentage'] = np.round(100 * df2['tip'] / df2['total_bill'],2)

print(df2.head())
#df2 = df2.drop('total_bill', axis=1) axis=0 Zeile axis = 1 columns

# -----------Работа со строками ------------
df2 = df2.set_index('Payment ID')
print(df2) # column wird zu index kann nur einmal ausgegeben werden!
#df2 = df2.reset_index()  Index wird zurücksetzt
#print(df2.iloc[0:4])  man kennt den nummer der Zeilen
#print(df2.loc['Sun4458'])  aufruf per Index namen
#dfw = df2.drop(['Sun4458'], axis=0') löschen der Zeilen
#one_row = df2.iloc[0]
#df.append(one_row) #spätere Version df2.concat hinzufügt die Zeile

#----Выбор по условию --------
print(df2[(df2['sex'] == 'Male') & (df2['smoker'] == 'No')]) # 2 Bedienungen setzt es in () & ist and
print(df2[(df2['day'] == 'Sun') | (df2['day'] == 'Sat')])
options = ['Sat', 'Sun', 'Mon' ]
print(df2[df2['day'].isin(options)]) # bessere Lösung
# Methode Apply
#Apply kann die funktion in FrameData ausführen


def last_f (num):
    return str(num)[-4:]



df2['last_four'] = df2['CC Number'].apply(last_f)
print(df2)


def restoran(num):
    if num <10:
        return '$'
    elif num >= 10 and num < 30:
        return '$$'
    else:
        return '$$$'
df2['yelp'] = (df2['total_bill'] + df2['tip']).apply(restoran)
print(df2[df2['yelp']== '$'])

# aply für mehreren Columns lambda ist funk ohne Name und wird einmal benutzt

#lambda num: num * 2
print(df2['total_bill'].apply(lambda num: num * 2))
def quality (total_bil, tip):
    if tip/total_bil > 0.25:
        return "Großzugig"
    else:
        return "normal"
#df2['quality'] = df2[['total_bill','tip']].apply(lambda df2: quality(df2['total_bill'], df2['tip']),axis=1)
#df2['quality'] = np.vectorize(quality)(df2['total_bill'], df2['tip'])) vectorise oft schneller und hat leichtes Syntaxis
print(np.linspace(0,500, 100))