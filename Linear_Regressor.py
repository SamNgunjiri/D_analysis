# -*- coding: utf-8 -*-


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics


#Importing the Data
data = pd.read_csv('./Book1.csv')

#Data Visualization
data.plot(x='Hours', y='Scores', style='o')
plt.xlabel('Hours')
plt.ylabel('Scores')
plt.show()

#Feature Selection
X = pd.DataFrame(data['Hours'])
Y = pd.DataFrame(data['Scores'])

#Seperating the Data into Training and Testing Data
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, random_state=0, train_size = .75)
print('The shape dimensions of the training data', X_train.shape)
print('The shape dimensions of the test data',X_test.shape)
print('The shape dimensions of the Y_training data',Y_train.shape)
print('The shape dimensions of the Y_test data',Y_test.shape)

#Linear Regression Model Development
model = LinearRegression()
model.fit(X_train, Y_train)

#Model Testing for Accuracy
print('The Model score in prediction:', model.score(X, Y))

#Model Testing for the Intercept and coefficient Values (Y = b0 + b1x)
print('Model Intercept (b0);', model.intercept_)
print('Model Coefficiet (b1)', model.coef_)

#Model Prediction
Y_pred = model.predict(Y_test)
print('Predicted Responses for the Scores accordig to hours are: {}'.format(Y_pred))

#Metrics and Accuracy Testing
print('Mean Absolute Error:', metrics.mean_absolute_error(Y_test, Y_pred))
print('Mean Squared Error:', metrics.mean_squared_error(Y_test, Y_pred))
print('Root Mean Square:', np.sqrt(metrics.mean_absolute_error(Y_test, Y_pred)))

