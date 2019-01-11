#robertoCampos
#phys162Hw3
#prblm2
import math

def nextElement(x,y):
    return x+y





list=[]  #created empty array
print("enter two positive integers")
aa = input("first element")
b = input("second element")
if aa+b>100:
   print('more than 100')
else:
   list.append(aa)   #appends the first two numbers to the beg of the list
   list.append(b)    
   n = (int(input("how many elements should be added to the list"))) #n stores the length of the list the user wants
   
   def add2List(list,n):
       for i in range(n):  
           b=nextElement(list[i],list[i+1]) #list[i],list[i+1] takes the numbers on the list that you want to add
           list.append(b) #the two numbers added
   add2List(list,n)  #calls the function
   print(list) #prints the list
