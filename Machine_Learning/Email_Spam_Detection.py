import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, confusion_matrix

#There's an error, check later!!! 

#Sample data
emails = ['Send us your password', 'Send us your review', 'Review your password',
          'Send your password', 'Send us your account', 'Review us', 'Send us your password',
          'Send us your account', 'Free review', 'Review your account', 'Your package is ready',
          'Your account status', 'Your account is locked', 'Your account is suspended',
          'Your account is disabled'] #Emails
labels = np.array([1,1,0,1,1,0,1,0,1,0,1,0,0]) #0: not spam 1: Spam

#Split the data
X_train, X_test, y_train, y_test = train_test_split(emails,labels,test_size=0.3,random_state=42) #Split the data

#Vectorize the text
vectorizer = CountVectorizer()
X_train_vectorized = vectorizer.fit_transform(X_train)
X_test_vectorized = vectorizer.transform(X_test)

#Train the model
model = MultinomialNB()
model.fit(X_train_vectorized,y_train)

#Make predictions
y_pred = model.predict(X_test_vectorized)

#Evaluate the model
accuracy = accuracy_score(y_test,y_pred)
conf_matrix = confusion_matrix(y_test,y_pred)

print(f"Accuracy: {accuracy}")
print(f"Confusion matrix: \n{conf_matrix}")

#Predict the outcome for a new email
new_email = ['Your account is under review']
new_email_vectorized = vectorizer.transform(new_email)
prediction = model.predict(new_email_vectorized)
print(f"Prediction for new email: {'Spam' if prediction[0] == 1 else 'Not spam'}")