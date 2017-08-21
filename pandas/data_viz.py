# Taken from machinelearningmastery.com
# Learning about scatter plot matrix

import matplotlib.pyplot as plt
import pandas
from pandas.tools.plotting import scatter_matrix

url = "https://goo.gl/vhm1eU"
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = pandas.read_csv(url, names=names)

# renders histogram of each attribute
data.hist()

# renders box and whiskers plot
data.plot(kind='box')

# renders scatter plot matrix
scatter_matrix(data)

# need plt.show to render the graphs 
plt.show()