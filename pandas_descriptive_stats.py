# Taken from machinelearningmastery.com
# Learning how to use descriptive stats using Pandas helper functions

import pandas

url = "https://goo.gl/vhm1eU"
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = pandas.read_csv(url, names=names)

# 'describe' provides descriptive stats - eg count, mean, std, min, quartiles, etc.
description = data.describe()
print(description)

# 'head' renders first few rows
print(data.head())

# 'corr' calculates pairwise correlation between variables
print(data.corr())

