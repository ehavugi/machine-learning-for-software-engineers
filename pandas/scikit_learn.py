# Pre-processing data
# Scikit-learn library provides 2 ways to transform data: (1) Fit and Multiple Transform, and (2) Combined Fit-and-Transform

# Standardize data example - mean of 0 and sd of 1
from sklearn.preprocessing import StandardScaler 
import pandas
import numpy

url = 'https://goo.gl/vhm1eU'
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
df = pandas.read_csv(url, names=names)
array = df.values

# separate array into input/output components 
X = array[:,0:8]
Y = array[:,8]

scaler = StandardScaler().fit(X)
rescaledX = scaler.transform(X)

# summarize transformed data
numpy.set_printoptions(precision=3)
print(rescaledX[0:5, :])
