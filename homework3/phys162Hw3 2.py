#RobertoCampos
#phys162Hw3
#22sep2018
import math
#prblem1
#a)
def function(x):
    return math.sin(x+2)

def function1(x):
   return (10-x**3)/(10+2*(x**3))


#b)
def function2(x,y,z):
    return math.cos(x+y*z)

f=open("data.dat","w")
f.write(("{:30s} {:30s} {:30} {:30}".format("0-2pi","sin(x+2)","(10-x**3)/(10+2*(x**3))","cos(x+y*z)" )))
iterate = 0
for i in range(0,1001):
    iterate += .006277
    x=iterate
    y=function(x)
    z=function1(x)
    r=function2(x,y,z)
    f.write(("{:30s} {:30s} {:30s} {:30s}\n".format(str(x),str(y),str(z),str(r))))
f.close()






