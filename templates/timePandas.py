from datetime import datetime
import pandas as pd
import openpyxl
import os
import numpy as np
import requests
from sqlalchemy import create_engine

year = 2015
moth = 1
day = 1
hr = 2
min = 30
sec = 15

mydate = datetime(year, moth, day,hr, min, sec)
print(mydate)
myser = pd.Series(['Nov 3, 1990', '2000-05-03', None])
myser = pd.to_datetime(myser, format='mixed', dayfirst=True)
print(myser)
style = ('22--Dec--2000')
print(pd.to_datetime(style, format='%d--%b--%Y'))
custm_date = '14th of Dec 2000 14:30:21'
print(pd.to_datetime(custm_date))
sales = pd.read_csv('RetailSales_BeerWineLiquor.csv',parse_dates = [0])
print(sales['DATE'])
s = sales.resample(rule='YE',on='DATE').mean()
print(s)

#input/output CSV umm die Daten schreiben df.to_csv()
#HTML read
url = 'file:///C:/Users/Student/Desktop/wk.txt'
tables = pd.read_html(url)

tb6 = tables[6].set_index('Rank')
print(tb6)
tb6.to_html('table.html', index= False)
dfexel = pd.read_excel('C:/Users/Student/Desktop/DSAR/TrendTec_DSAR_Ressourcenplanung.xlsx')
pd.set_option('display.max_rows', None)      # zeigt alle Zeilen
pd.set_option('display.max_columns', None)   # zeigt alle Spalten
pd.set_option('display.width', None)         # keine Zeilenumbrüche
pd.set_option('display.max_colwidth', None)  #
def cleanNumb(num):
    num =  num.replace('~','').split('€')
    return num[0]
dfexel['Kosten (monatlich)'] = dfexel['Kosten (monatlich)'].apply(cleanNumb)

dfexel.drop(['Umgebung / Technologie', 'Mindestanforderung'], axis=1 , inplace=True)
dfexel.rename(columns = {'Kosten (monatlich)': 'Kosten'}, inplace = True)
print(dfexel[dfexel['Verantwortlich'] == 'DevOps'])
