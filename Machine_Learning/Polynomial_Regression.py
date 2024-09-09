import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline

#Sample data
X = np.array([5,10,15,20,25,30,35,40]).reshape(-1,1) #Temperature in Celsius
y = np.array([1,4,5,7,8,7,5,2]) #Crop yield in tons/acre

#Create and fit the model
degree = 3
model = make_pipeline(PolynomialFeatures(degree),LinearRegression()) #Create a pipeline with PolynomialFeatures and LinearRegression
model.fit(X,y) #Train the model

#Generate points for smooth curve
X_smooth = np.linspace(X.min(),X.max(),100).reshape(-1,1) #Generate 100 points between the minimum and maximum values of X
y_smooth = model.predict(X_smooth) #Predict the values for the 100 points

#Plot the results
plt.scatter(X,y,color='blue',label='Actual data') #Plot the actual data
plt.plot(X_smooth,y_smooth,color='red',label='Polynomial regression') #Plot the polynomial regression curve
plt.xlabel('Temperature (C)')
plt.ylabel('Yield (tons/acre)')
plt.legend()
plt.show()

#Predict yield for a new temperature
new_temp = np.array([22]).reshape(-1,1) 
predicted_yield = model.predict(new_temp)
print(f"Predicted yield at 22 degrees Celsius: {predicted_yield[0]:.2f} tons/acre") #Print the predicted yield