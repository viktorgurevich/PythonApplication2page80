import datetime
import os 
os.system('cls')
print ("0. screen cleaned   at  " + str(datetime.datetime.now()))
print("================================================================================================= ")

fileName=str(datetime.datetime.now())[17:19] +".txt"
MyText=str(datetime.datetime.now())[0:19] 

f=open(fileName,"a")
f.write(MyText)
f.close()
f = open(fileName, "r")

print(f.read()) 




f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()

#open and read the file after the appending:
f = open("demofile2.txt", "r")
print(f.read()) 

#==========================
