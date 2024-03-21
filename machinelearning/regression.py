import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Loading our dataset
data = pd.read_csv("C:/Users/evepo/OneDrive/Desktop/student/student-mat.csv", sep=';')

# Specifying exactly what we are looking for
data = data[['age', 'sex', 'studytime',
             'absences', 'G1', 'G2', 'G3']]

# Using a dictionary to change sex into a numeric value
data['sex'] = data['sex'].map({'F':0, 'M':1})

prediction = 'G3'

X = data.drop(columns=[prediction]).values
Y = np.array(data[prediction])

X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size=0.1)

model = LinearRegression()
model.fit(X_train, Y_train)

accuracy = model.score(X_test, Y_test)

print(accuracy)

X_new = np.array([[18,1,3,40,15,16]])
Y_new = model.predict(X_new)

print(Y_new)

plt.scatter(data['studytime'], data['G3'])

plt.title("Correlation")
plt.xlabel("Study Time")
plt.ylabel("Final Grade")
plt.show()

plt.scatter(data['G2'], data['G3'])
plt.title("Correlation")
plt.xlabel("Second Grade")
plt.ylabel("Final Grade")
plt.show()