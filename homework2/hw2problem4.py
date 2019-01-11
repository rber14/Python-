#robertoCampos
#hw2
#problem4
import os
import string 

path="A"

for i in range(3):   #loopmakes3filesABC
   os.makedirs(path, exist_ok=True)
   for j in range(1,5): #fourfiles
      previous=os.getcwd()
      next=path+os.sep+str(j)
      os.makedirs(next,exist_ok=True)
      
      os.chdir(next)
      f=open("info.txt","w")
      f.write("this file is in folder"+path+os.sep+str(j))
      f.close()
      os.chdir(previous)
      
   path=chr(ord(path)+1)
      

   





   

   
      
