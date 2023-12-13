

# importing the libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# importing the dataset
dataset=pd.read_csv('Position_Salaries.csv')
x=dataset.iloc[:,1:-1].values
y=dataset.iloc[:,-1].values

print(x)
print(y)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc_X=StandardScaler()
sc_y=StandardScaler()

X=sc_X.fit_transform(x)
# y=sc_y.fit_transform(y)

print(X)
print(y)

# Training the SVR model on the whole dataset

from sklearn.svm import SVR
regressor=SVR(kernel='rbf')
regressor.fit(X,y)

# Predicting the new result
sc_y.inverse_transform(regressor.predict(sc_X.transform([[6.5]])).reshape(-1,1))

# Predicting the SVR result
plt.scatter(sc_X.inverse_transform(x),sc_y.inverse_transform(y),color='red')
plt.plot(sc_X.inverse_transform(x),sc_y.inverse_transform(regressor.predict(sc_X.transform(x)).reshape(-1,1)),color='blue')
plt.title('Truth or Bluff(SVR regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()

