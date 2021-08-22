#THIS IS Test3.py FILE
print("====================================================================")
print ('texts from Test3.py')

try:
  import sys
  sys.path.append('C:\Projects\Pr2021A')
except NameError:
  print("Variable sys is not defined")
except:
  print("Something else went wrong") 

#  import json
  dir(json)
 # print(json.dumps(sys)) --not serializable

 

 #applied C:\Projects\Pr2021>python -m pip install camelcase
import camelcase
c = camelcase.CamelCase()
txt = "hello world"

print(c.hump(txt)) 


#---------------------------------https://www.w3schools.com/python/scipy/scipy_optimizers.php
#SQL: https://docs.microsoft.com/en-us/sql/connect/python/pyodbc/step-1-configure-development-environment-for-pyodbc-python-development?view=sql-server-ver15
import pyodbc 
cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=.;"
                      "Database=home;"
                      "Trusted_Connection=yes;")


cursor = cnxn.cursor()
cursor.execute('SELECT * FROM Logins')

for row in cursor:
    print('row = %r' % (row,))