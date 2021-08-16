#Imports scipy, pandas,pyodbc; printing; resolving equation; retrieving data from SQL Server
import scipy
from scipy import constants
print(constants.liter)
print(constants.pi)
print(dir(constants)) 

#================================================

#example Find root of equation 1
from scipy.optimize import root
from math import cos

def eqn(x):
  return x + cos(x)
myroot = root(eqn, 0)   # it looks as x+cos(x)=0 equation
print(myroot.x)
print(myroot)

#================================================
def eqn2(x):
	return x**2 + x +100

myroot2 = root(eqn2, 0)   # it looks 
print(myroot2.x)



#==================================================================================================

