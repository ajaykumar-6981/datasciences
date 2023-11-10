
# importing the libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# importing the dataset
dataset=pd.read_csv('Position_Salaries.csv')
x=dataset.iloc[:,:-1].values
y=dataset.iloc[:,-1].values

print(x)
print(y)

# Training the Linear Regression model onthe train set
from sklearn.linear_model import LinearRegression
le_reg=LinearRegression()
le_reg.fit(x,y)

# Training the Polynomial model on the whole dataset
from sklearn.preprocessing import PolynomialFeatures
poly_reg=PolynomialFeatures(degree=2)

poly_reg.fit(x,y)

sum=le_reg.fit(x,y)+poly_reg.fit(x,y)
print(sum)

