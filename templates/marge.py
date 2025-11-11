import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from sqlalchemy import create_engine

df = pd.read_csv('tips.csv')
df2 = pd.read_csv('movie_scores.csv')
df['sex'] = df['sex'].replace({'Male': 'm', 'Female': 'f'})
df['id'] = range(1, len(df) + 1)
df2['id'] = range(df['id'].iloc[-1] + 1, df['id'].iloc[-1] + len(df2) + 1)
margen = pd.merge(df,df2, how='outer', on='id', suffixes=('_tips', '_movie'))
print(margen.head())
tech_f = ['GOOG,APPL,AMZN', 'JPN,BAC,GS']
tickers = pd.Series(tech_f)
tickers = tickers.str.split(',', expand=True) # получаем датафрейм
print(tickers)
messy_names = pd.Series(['Andrew ', 'Bob:O', ' clair '])
messy_names = messy_names.str.replace(':', '').str.strip().str.capitalize()
print(messy_names)
user = 'root'
passwd = '1111'
host = 'localhost'
port = 3307
dbase = 'bookstore'
engine = create_engine(f"mysql+pymysql://{user}:{passwd}@{host}:{port}/{dbase}")
df = pd.read_sql('select * from baby_names', con=engine)
df = df[(df['name'] == 'Mary') & (df['year'] >2000)]

print(df)
plt.plot([1, 2, 3], [1, 4, 9])
plt.title('Matplotlib (Standard)')
plt.show()

# Seaborn (mit eigenem Stil)
sns.set_theme(style='darkgrid')
sns.lineplot(x=[1, 2, 3], y=[1, 4, 9])
plt.title('Seaborn')
plt.show()