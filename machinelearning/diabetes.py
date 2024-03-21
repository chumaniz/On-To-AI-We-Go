import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_diabetes

# Extracting our data and loading it
data = load_diabetes()

# Prints out feature names
print("Feature names:", data.feature_names)

# Declaring our data
X = np.array(data.data)
Y = np.array(data.target)

# Splitting our data for training and testing
X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size=0.1)

# Initializing classifiers...or the classifying algorithms
clf1 = KNeighborsClassifier(n_neighbors=5) # setting K value
clf2 = GaussianNB()
clf3 = LogisticRegression()
clf4 = DecisionTreeClassifier()
clf5 = RandomForestClassifier()

# Our Train Classifiers
clf1.fit(X_train, Y_train)
clf2.fit(X_train, Y_train)
clf3.fit(X_train, Y_train)
clf4.fit(X_train, Y_train)
clf5.fit(X_train, Y_train)

# Printing out the results
print("KNN score:", clf1.score(X_test, Y_test))
print("GNB score:", clf2.score(X_test, Y_test))
print("LR score:", clf3.score(X_test, Y_test))
print("DTC score:", clf4.score(X_test, Y_test))
print("RFC score:", clf5.score(X_test, Y_test))