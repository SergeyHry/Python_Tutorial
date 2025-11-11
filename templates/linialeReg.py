from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('Advertising.csv')
print(df.head())

df['Total'] = df['TV'] + df['radio'] + df['newspaper']
print(df.head())
graf = sns.regplot(data = df,x = 'Total',y = 'sales') # zeigt shon linialle Regression

# Manuel machen:
X = df['Total']
y = df['sales']
print(np.polyfit(X,y,deg= 1)) #Koofiziente b1,b2
potential_spend = np.linspace(0,500, 100)
predicted_sales = 0.04868788 * potential_spend + 4.24302822
plt.plot(potential_spend, predicted_sales)
plt.show()

# Einzelne Werte vorhersage :
Werbung = 12.5
predicted_sales = 0.04868788 * Werbung + 4.24302822
print(f'Gewinn vorhersage: {predicted_sales:.2f} €')

#SciKit-Learn
#test und learn
X = df.drop('sales', axis=1)
print(X)
y = df['sales']
X_train, X_test, y_train, y_test = train_test_split( X, y, test_size=0.33, random_state=101) #42 101 47
print(X_train)
model = LinearRegression()
model.fit(X_train, y_train)
test_prediction = model.predict(X_test)
print(mean_absolute_error(y_test,test_prediction))
test_residuals = y_test - test_prediction
print(test_residuals)
#вычесление Остатков :
sns.scatterplot(x= y_test, y= test_residuals)
plt.axhline(y=0, color='r', ls = '--')
sns.displot(test_residuals)
plt.show()