
# importing the libraries
import pandas as  pd
import numpy as np
import matplotlib.pyplot as plt

# import the dataset
dataset=pd.read_csv('Salary_Data.csv')
x=dataset.iloc[:,:-1].values
y=dataset.iloc[:,-1].values

print(x)
print(y)

# working with categorical data
# working with independent data

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

ct=ColumnTransformer(transformers=[('encoder',OneHotEncoder(),[0])],remainder='passthrough')
X=ct.fit_transform(x)

# Splitting the dataset into train set and test set

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.25,random_state=0)
print('X_train :',X_train)

print('X_test :',X_test)

print('y_train',y_train)
print('y_test :',y_test)

# Training the Polynomial Regression model on the whole dataset
from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(X,y)

from sklearn.preprocessing import PolynomialFeatures

poly_reg=PolynomialFeatures(degree=2)
X_poly=poly_reg.fit_transform(x)
lin_reg2=LinearRegression()
lin_reg2.fit(X_poly,y)


#  predicting the test data
y_pred=regressor.predict(X_test)
np.set_printoptions(precision=2)
print(np.concatenate((y_pred.reshape(len(y_pred),1),y_test.reshape(len(y_test),1)),1))
# Visualising the Linear Regression results


plt.scatter(x,y,color='red')
plt.plot(x,regressor.predict(X),color='blue')
plt.title('Positon level v/s Salary')
plt.xlabel('Salary')
plt.ylabel('Position')
plt.show()

