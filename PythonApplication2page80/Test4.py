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


import pyodbc  #WORK WITH SQL SERVER 
from pyodbc import Error
#https://docs.microsoft.com/en-us/sql/connect/python/pyodbc/step-3-proof-of-concept-connecting-to-sql-using-pyodbc?view=sql-server-ver15

server = 'localhost' 
database = 'TaskDictionary' 
username = 'sa' 
password = 'kosaya' 
try:
	SQL_Connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
except Error as err:
	 print(f"Error: '{err}'")

cursor = SQL_Connection.cursor()

cursor.execute('SELECT * FROM BOOKS')

for row in cursor:
    print('row = %r' % (row,))
print ("================================================================")
#=====================================================================
#SQL_Connection = pyodbc.connect( INSERT SQL CONNECTION SETTINGS HERE)

import pandas as ps

SQL_Script = "Select TaskID, TaskName, TaskComment from Tasks"
try:
	df = ps.io.sql.read_sql(SQL_Script, SQL_Connection)
except Error as err:
	 print(f"Error: '{err}'")
SQL_Connection.close()
print (df)
print ("===================================================Print full DataFrame =============")

with ps.option_context('display.max_rows', None,
                       'display.max_columns', None,
                       'display.precision', None,
                       ):
    print(df)

#==================================================================================================

#scraping

import requests
from bs4 import BeautifulSoup
url = 'https://en.wikipedia.org/w/index.php\?title=List_of_Game_of_Thrones_episodes&oldid=802553687'

r = requests.get(url)   #manually via Browser it gives content, but via code gives 404
html_contents = r.text
html_soup = BeautifulSoup(html_contents,"html.parser")


url = 'http://www.webscrapingfordatascience.com/basichttp/'
r = requests.get(url)
print(r.text)

print(r.status_code)
# What is the textual status code?
print(r.reason)
# What were the HTTP response headers?
print(r.headers)