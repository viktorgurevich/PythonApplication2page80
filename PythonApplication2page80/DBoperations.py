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

