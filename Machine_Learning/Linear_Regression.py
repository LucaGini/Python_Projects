import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

#Sample data
X = np.array([50,70,90,110,130,150,170]).reshape(-1,1) #House size in square meters
y = np.array([150000,200000,250000,300000,350000,400000,450000]) #House price in dollars

#Create and fit the model
model = LinearRegression()
model.fit(X,y) #Train the model

#Make predictions
X_new = np.array([80,120,160]).reshape(-1,1)
y_pred = model.predict(X_new) #Predict the price of the houses

#Plot the data
plt.scatter(X,y,color='blue',label='Actual data') 
plt.plot(X,model.predict(X),color='red',label='Regression line') #Plot the regression line
plt.plot(X_new,y_pred,color='green',label='Predictions') #Plot the predictions
plt.xlabel('House size (m^2)')
plt.ylabel('House price ($)')
plt.legend() 
plt.show()

print(f"Predicted prices for houses of size 80, 120 and 160 square meters: {y_pred}")