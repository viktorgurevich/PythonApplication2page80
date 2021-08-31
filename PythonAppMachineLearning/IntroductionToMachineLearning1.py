#p 7/21
import numpy as np
x = np.array([[1, 2, 3], [4, 5, 6]])
print("x:\n{}".format(x))

y= np.array([[1, 2, 3], [4, 5, 6],[7,8,9]])
print("y:\n{}".format(y))

z= np.array([[1, 2, 3], [4, 5, 6],[7,8,9], [7,8,9,10]])  #deprecated
print("z:\n{}".format(z))

#from scipy import sparse
# Create a 2D NumPy array with a diagonal of ones, and zeros everywhere else
eye = np.eye(4)
print("NumPy array:\n{}".format(eye))

from scipy import sparse
sparse_matrix = sparse.csr_matrix(eye)
print("\nSciPy sparse CSR matrix:\n{}".format(sparse_matrix))


#%matplotlib inline
   #not clear role
import matplotlib.pyplot as plt
# Generate a sequence of numbers from -10 to 10 with 100 steps in between
x = np.linspace(-10, 10, 100)
# Create a second array using sine
y = np.sin(x)
# The plot function makes a line chart of one array against another
plt.plot(x, y, marker="x")
plt.pause(10.0)

import matplotlib.pyplot as plt

plt.scatter([0], [1])
plt.draw()
plt.show(block=False)

for i in range(10):
    plt.scatter([i], [i+1])
    plt.draw()
    plt.pause(0.001)

plt.pause(30.0) 


from IPython.display import display
import pandas as pd
# create a simple dataset of people
data = {'Name': ["John", "Anna", "Peter", "Linda"],
'Location' : ["New York", "Paris", "Berlin", "London"],
'Age' : [24, 13, 53, 33]
}
data_pandas = pd.DataFrame(data)
# IPython.display allows "pretty printing" of dataframes
# in the Jupyter notebook
display(data_pandas)


# Select all rows that have an age column greater than 30
display(data_pandas[data_pandas.Age > 30])