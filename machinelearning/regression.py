import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Loading our dataset
data = pd.read_csv('student-mat.csv', sep=';')

# Specifying exactly what we are looking for
data = data[['age', 'sex', 'studytime',
             'absences', 'G1', 'G2', 'G3']]

# Using a dictionary to change sex into a numeric value
data['sex'] = data['sex'].map({'F':0, 'M':1})

prediction = 'G3'