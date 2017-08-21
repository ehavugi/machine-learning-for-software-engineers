# Taken from machinelearningmastery.com
# Learning how to create a Pandas Data Frame

import numpy
import pandas

myarray = numpy.array([[1,2,3],[4,5,6]])
rownames = ['a', 'b']
colnames = ['un', 'deux', 'trois']
mydataframe = pandas.DataFrame(myarray, index=rownames, columns=colnames)
print(mydataframe)