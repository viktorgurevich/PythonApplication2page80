#HOW TO RUN THIS CODE.
#CD C:\Projects\Pr2021 --open DOS window
#py
#import Test1
#import importlib
#importlib.reload(Test1)


import datetime
import os 
os.system('cls')
print ("0. screen cleaned   at  " + str(datetime.datetime.now()))
print(" ")

import sys
sys.path.append('C:\Projects\Pr2021A')	
import Test2
#os('dir')   'module' object is not callable
#os('python -m pip list')

MyStr=' This is two texts from Pr2021 '
print ('1. INLINE  is text from Pr2021/Test1  1.1  ' + MyStr [0:23] +"  1.2  " + MyStr [-13:-1])
#print (MyStr [0:21])
#print (MyStr [-11:-1])
print(" ")


def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print("")

print ('3. Fibonacci numbers')
fib(100)    

print(" ")
print ("4. type(fib) is " + str(type(fib)))

print(" ")
print("5. import random")
import random
print ('5. random value ' + str((random.randrange (14, 2400000))))

print(" ")
print("6. set")
set = {"string1", 'string2', 'string3', 'string4', 'string5'}
print (set)

print(" ")
print("7. discard item")
set. discard ('string3')
print (set)

print(" ")
print("8. pop")
print(str(set.pop()))
print (set)

print(" ")
print ('9.dictionary')
dict = {
'key01': 'value01',
'key02': 'value02',
'key03': 'value03',
}
print (dict )

print(" ")
print("10. extract by key from dict")
dict.pop ('key01')

print(" ")
print ('10.A dictionary after operation')
print (dict)

print(" ")
print ('11. make a COPY of dictionary and print')
newdict = dict.copy ( )
print (newdict)

print(" ")
print ('12 del dictionary')
del dict
#print (dict)

print ('13 print a COPY of dictionary newdict')
print (newdict)

print(" ")
print("14. clear a Copy of dictionary and print")
if len(newdict)>0: newdict.clear()
print('newdict')
print (newdict)


class Vehicle:
	def _init_(self, name, year):
		self.name = name
		self.name = year


		
	def newfunc (self):
		print ('15. I am a proud owner of ' + self.name)
		
v1 = Vehicle()
v1.name='Vasya_Vehicle'
v1.newfunc()

the_world_is_flat = True
if the_world_is_flat:
  print('16. Be careful not to fall off!')
  
print(" ")



f=open("Test3.py")
print ("17. File Test3 ")
print(f.read())

#mydb = mysql.connector.connect(host="localhost",  user="root",  password="Kosaya0829@")
#print(mydb) 


#help("modules")   listing installed modules.
#pip does not work for me though is available on the path folder

#From the Windows command prompt, however, pip works:
#python -m pip install scipy
#python -m pip list   --list of
#python -m pip freeze  --list of
#python -m pip freeze -V  --version

#https://www.csestack.org/python/