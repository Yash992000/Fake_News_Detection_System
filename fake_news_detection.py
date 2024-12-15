# -*- coding: utf-8 -*-
"""Fake_News_Detection.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1fL6rOfDQ3Ev-q_Pq_e3tPDS0TpiBGbCK
"""

import numpy as np
import pandas as pd
import itertools
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.preprocessing import LabelEncoder

from google.colab import drive
drive.mount('/content/drive')
df = pd.read_csv('/content/drive/MyDrive/MIT/Sem 1/Mini Project/news.csv')
df.shape
df.head()

#DataFlair - Get the labels
labels=df.label
labels.head()

#DataFlair - Split the dataset
x_train,x_test,y_train,y_test=train_test_split(df['text'], labels, test_size=0.2, random_state=7)

#DataFlair - Initialize a TfidfVectorizer
tfidf_vectorizer=TfidfVectorizer(stop_words='english', max_df=0.7)

#DataFlair - Fit and transform train set, transform test set
tfidf_train=tfidf_vectorizer.fit_transform(x_train)
tfidf_test=tfidf_vectorizer.transform(x_test)

#DataFlair - Initialize a PassiveAggressiveClassifier
pac=PassiveAggressiveClassifier(max_iter=50)
pac.fit(tfidf_train,y_train)

#DataFlair - Predict on the test set and calculate accuracy
y_pred=pac.predict(tfidf_test)
score=accuracy_score(y_test,y_pred)
print("Passive Aggressive Classifier")
print(f'Accuracy: {round(score*100,2)}%')

#DataFlair - Build confusion matrix
confusion_matrix(y_test,y_pred, labels=['FAKE','REAL'])

from sklearn.svm import SVC


# Initialize a Support Vector Machine (SVM) model
svm_model = SVC()
svm_model.fit(tfidf_train, y_train)

# Predict on the test set
y_pred = svm_model.predict(tfidf_test)

# Encode labels for the test set
label_encoder = LabelEncoder()
y_test_encoded = label_encoder.fit_transform(y_test)
y_pred_encoded = label_encoder.transform(y_pred)

# Calculate accuracy
score = accuracy_score(y_test_encoded, y_pred_encoded)
print("Support Vector Machine")
print(f'Accuracy: {round(score * 100, 2)}%')

# Build confusion matrix
conf_matrix = confusion_matrix(y_test_encoded, y_pred_encoded, labels=np.unique(y_test_encoded))
print('Confusion Matrix:')
print(conf_matrix)

from sklearn.neighbors import KNeighborsClassifier

# Initialize a k-Nearest Neighbors (KNN) model
knn_model = KNeighborsClassifier()
knn_model.fit(tfidf_train, y_train)

# Predict on the test set
y_pred = knn_model.predict(tfidf_test)

# Encode labels for the test set
label_encoder = LabelEncoder()
y_test_encoded = label_encoder.fit_transform(y_test)
y_pred_encoded = label_encoder.transform(y_pred)

# Calculate accuracy
score = accuracy_score(y_test_encoded, y_pred_encoded)
print("K-Nearest Neighbour")
print(f'Accuracy: {round(score * 100, 2)}%')

# Build confusion matrix
conf_matrix = confusion_matrix(y_test_encoded, y_pred_encoded, labels=np.unique(y_test_encoded))
print('Confusion Matrix:')
print(conf_matrix)

from sklearn.naive_bayes import MultinomialNB

# Initialize a Multinomial Naive Bayes model
nb_model = MultinomialNB()
nb_model.fit(tfidf_train, y_train)

# Predict on the test set
y_pred = nb_model.predict(tfidf_test)

# Encode labels for the test set
label_encoder = LabelEncoder()
y_test_encoded = label_encoder.fit_transform(y_test)
y_pred_encoded = label_encoder.transform(y_pred)

# Calculate accuracy
score = accuracy_score(y_test_encoded, y_pred_encoded)
print("Naive Bayes")
print(f'Accuracy: {round(score * 100, 2)}%')

# Build confusion matrix
conf_matrix = confusion_matrix(y_test_encoded, y_pred_encoded, labels=np.unique(y_test_encoded))
print('Confusion Matrix:')
print(conf_matrix)

from sklearn.ensemble import RandomForestClassifier


# Initialize a Random Forest Classifier model
rf_model = RandomForestClassifier(random_state=42)
rf_model.fit(tfidf_train, y_train)

# Predict on the test set
y_pred = rf_model.predict(tfidf_test)

# Encode labels for the test set
label_encoder = LabelEncoder()
y_test_encoded = label_encoder.fit_transform(y_test)
y_pred_encoded = label_encoder.transform(y_pred)

# Calculate accuracy
score = accuracy_score(y_test_encoded, y_pred_encoded)
print("Random Forest")
print(f'Accuracy: {round(score * 100, 2)}%')

# Build confusion matrix
conf_matrix = confusion_matrix(y_test_encoded, y_pred_encoded, labels=np.unique(y_test_encoded))
print('Confusion Matrix:')
print(conf_matrix)

import matplotlib.pyplot as plt

# Accuracy scores for each algorithm
accuracies = [92.74, 92.9, 56.12, 84.06, 90.61]

# Algorithms names
algorithms = ['Passive Aggressive', 'Support Vector Machine', 'K-Nearest Neighbors', 'Naive Bayes', 'Random Forest']

# Plotting the bar graph
plt.figure(figsize=(10, 6))
plt.bar(algorithms, accuracies, color=['blue', 'green', 'orange', 'purple', 'red'])
plt.title('Accuracy of Different Algorithms')
plt.xlabel('Algorithms')
plt.ylabel('Accuracy (%)')
plt.ylim(0, 100)

# Display the accuracy values on top of the bars
for i, v in enumerate(accuracies):
    plt.text(i, v + 1, str(round(v, 2)) + '%', ha='center', va='bottom')

# Show the bar graph
plt.show()