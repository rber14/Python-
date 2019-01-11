#robertoCampos
#phys162Hw4
import math
import numpy as np

"""
 *mass,length,height,gravity are pre-defined
 *xdist calculates the range and returns it
 *make sure to convert degree to radians in the xdist function
 *xdist2 prints out the output and formats it without calling print()
 
"""
mass=200; #in grams
length=6; #in cm
height=1.54; #in m 
gravity= 9.81; #in m/s^2


def xdist(velocity, degree):
   radian=degree*math.pi/180 #convertToRadian
   range= ((((velocity**2)*(math.cos(radian)**2))/gravity) #gives the range
      *(math.tan(radian)
      +(math.sqrt((math.tan(radian)**2)+((2*gravity*height)/((velocity**2)*(math.cos(radian)**2)))))))
   return range

def xdist2(n):
   (velocity,degree)=n
   x=xdist(velocity,degree)
   print (str("For v0 = {} m/s and theta0 = {} degrees, the range is: {:.3f} m.".format(velocity,degree,x)))
   return x
#3. uncomment in order to RUN
#enter how any times & enter the v0 and theta 
#n=(int(input("How many ranged do you want to calculate: ")))
#for i in range(n):
   #v0=(float(input("Enter v0: ")))
   #theta0=(float(input("Enter theta0: ")))
   #xdist2((v0,theta0))

numbers=[]
theta=[]
velocity=10      #the angle does depend on initial speed ex. when v0=10m/s the degree that gives the largest range is 41.6 for v0=8m/s it's 39.6
degree=0
max=0;
for i in range (1000):
   xdist2((velocity,degree))
   number=xdist(velocity,degree)
   numbers.append(number)
   if degree>90:
      break
   degree+=.2
   angle=degree
   theta.append(angle)
b=np.array(numbers)
a=np.array(theta)
highestDegreeIndex=numbers.index(b.max())
range1=b.max()
print('___________________________________________________')
print("The optimal degree is : {}".format(theta[highestDegreeIndex]))
print("The longest range given the optimal degree is {:.3f} m.\n ".format(b.max()))
print("The angle does depend on the speed for example if v0=8 the angle would be 39.6\n")

height=height-.06; #convert cm to m
print("We have now changed the initial height to the center of the sphere by subtracting height-Radius and converting cm to m the height is now: {}m".format(height))
xdist2((velocity,theta[highestDegreeIndex]))

differenceInRange=range1-xdist(velocity,theta[highestDegreeIndex])
print("The difference in range if we define the height to the center of the sphere is: {:.4f}".format(differenceInRange))  

  

 