"""
Python Libraries Lab Program

This code demonstrates the use of popular Python libraries such as NumPy, 
Pandas, Matplotlib, and Scikit-learn for various data manipulation, analysis, 
and visualization tasks. It includes examples of basic operations with 
NumPy arrays, reading and analyzing data with Pandas, plotting with Matplotlib, 
and performing linear regression with Scikit-learn used for machine learning.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Basic numpy operations
arr = np.array([1, 2, 3, 4])
print(np.mean(arr)) # Mean
print(np.std(arr)) # Standard deviation
print(np.sum(arr)) # Sum
print(np.max(arr)) # Maximum value
print(np.min(arr)) # Minimum value

# Reading a CSV file using pandas
data = pd.read_csv("data.csv")
print(data.shape) # Number of rows and columns
print(data.columns) # Column names
print(data.head()) # First 5 rows
print(data.describe()) # Statistical summary
print(data.info()) # Data types and non-null counts
print(data['Score'].sum()) # Sum of the 'Score' column
print(data['Passed'].value_counts()) # Count of unique values in 'Passed' column

# Plotting example
plt.plot([1,2,3], [4,5,6]) # Simple line plot
plt.xlabel("X-axis") # Label for X-axis
plt.ylabel("Y-axis") # Label for Y-axis
plt.show() # Display the plot

# Linear Regression example
X = np.array([[1], [2], [3], [4]]) # Feature matrix (independent variable)
y = np.array([2, 4, 6, 8]) # Target vector (dependent variable)
model = LinearRegression() # Create a linear regression model
model.fit(X, y) # Fit the model to the data
print(model.predict([[5]])) # Predicting the value for X=5



# Output:

# 2.5
# 1.118033988749895
# 10
# 4
# 1
# (10, 6)
# Index(['ID', 'Name', 'Age', 'City', 'Score', 'Passed'], dtype='str')
#    ID     Name  Age       City  Score  Passed
# 0   1    Alice   22  Bangalore   85.5    True
# 1   2      Bob   24    Chennai   15.0   False
# 2   3  Charlie   23  Hyderabad   82.0    True
# 3   4    David   25     Mumbai   90.7    True
# 4   5      Eva   21      Delhi   30.0   False
#              ID        Age      Score
# count  10.00000  10.000000  10.000000
# mean    5.50000  23.200000  64.170000
# std     3.02765   1.549193  29.831194
# min     1.00000  21.000000  15.000000
# 25%     3.25000  22.000000  41.250000
# 50%     5.50000  23.000000  79.750000
# 75%     7.75000  24.000000  83.500000
# max    10.00000  26.000000  90.700000
# <class 'pandas.DataFrame'>
# RangeIndex: 10 entries, 0 to 9
# Data columns (total 6 columns):
#  #   Column  Non-Null Count  Dtype
# ---  ------  --------------  -----
#  0   ID      10 non-null     int64
#  1   Name    10 non-null     str
#  2   Age     10 non-null     int64
#  3   City    10 non-null     str
#  4   Score   10 non-null     float64
#  5   Passed  10 non-null     bool
# dtypes: bool(1), float64(1), int64(2), str(2)
# memory usage: 542.0 bytes
# None
# 641.7
# Passed
# True     7
# False    3
# Name: count, dtype: int64
# [10.]