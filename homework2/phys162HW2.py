#RobertoCamposPhys162MW3
#homework2
#problem1&2
import math

#problem1
#a)
a=[]
for i in range(21,50,2):
   a.append(i)
print(a)
   
#b)
print(range(21,50,2))
print("")

#probelm3
#a)
pi=math.pi
print("pi four digits after the decimal point is {:.5}\n".format(pi))

#b)
number=100*(math.pi**2)
print("value of 100pi^2 with 10 digits after the decimal point is {:.13}\n".format(number))

#c)
a=format(math.pi, '.6f')
b=format(math.pi, '.20f')
print("Pi with 6 digits after the decimal is "+a+"\nPi with 20 digits after the decimal is  "+b+"\n" )

#d)
x= math.exp(3)
y=math.sin(((math.pi)/3))

print(format(x, '.3f'))
print(format(y, '.3f'))
print(format(x*y, '.4E')+"\n")

#e)
list=[1,5,10]

for i in reversed(list):
   print("{:03.0f}".format(i))



   



