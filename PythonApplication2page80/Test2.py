print ('text1 from Test2.py')

print ('text2')

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

 
import camelcase
c = camelcase.CamelCase()
txt = "hello world"

print(c.hump(txt)) 