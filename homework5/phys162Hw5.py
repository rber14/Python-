#RobertoCampos
#phys162Hw5october72018
import numpy as np
import matplotlib.pyplot as plt


#problem1
'''
plt.subplot(221)
plt.title("Problem 1",)
plt.xlabel("X label title", fontsize=12)
plt.ylabel("Y label title", fontsize='large')
x=np.linspace(0,10)
y=np.sin(x)
z=np.cos(x)
plt.plot(x,y,'r--',label='sin')
plt.legend()
plt.plot(x,z,'b',label='cos', linewidth=5.0)
plt.legend()
plt.yticks([-4,-2,0,2,4])

plt.subplot(222)
def f(x):
   return x**2
x2=np.linspace(0,100,10, endpoint=True)
y2=f(x2)
plt.plot(x2,y2,'b--')
plt.show()
'''
#problem2
 
g=9.81;#gravity
h0=1.54 #m
def traj(x,v0,th0):
   th0rad = th0 * np.pi/180.0 #radians
   return h0 + np.tan(th0rad) * x - (g * x**2)/(2*v0**2*np.cos(th0rad)**2)


arrayTraj=[]
arrayTraj2=[]
colors = ["b", "g", "r","c","m","y","b","chartreuse","#eeefff","burlywood"]
colors2 = ["b", "g", "r","c","m","y","b","chartreuse","#eeefff","burlywood"]
v01=0;
th01=40;
v02=8 
th02=25;
xdata = np.linspace(0.0,20.0,50)
plt.subplot(121)
plt.xlabel("Range", fontsize=12)
plt.ylabel("Height", fontsize=12)
plt.title('Velocity: 0-10 | Degree: 40')


for i in range(10):
   v01+=1;
   ydata1 = traj(xdata,v01,th01)
   arrayTraj.append(ydata1)
   plt.plot(xdata,arrayTraj[i], color=colors[i],label="Range", linewidth=1.0,)
   plt.legend()
   plt.ylim(0.,5.)
  

plt.subplot(122) 
plt.title("Degree: 25-45 | Velocity: 8 ")
plt.xlabel("Range", fontsize=12)
plt.ylabel("Height", fontsize=12) 
for n in range(10):
   th02+=2;
   ydata2= traj(xdata, v02, th02)
   arrayTraj2.append(ydata2)
   plt.plot(xdata,arrayTraj2[n], color=colors2[n],label="Range", linewidth=1.0)
   plt.legend()
   plt.ylim(0.,5.)
 

'''
d1=6
d2=4
alph=np.radians(30)
xdata = np.linspace(0.0,20.0,200)
def gr(x,d1,d2):
   if x<d1:
      return 0
   if d1<x<d1+d2:
      return ((x-d1)*np.tan(alph))
   if x>d1+d2:
      return d2*np.tan(alph)
ydata = []
for x in xdata:
   ydata.append(gr(x,d1,d2))
ydata=np.array(ydata)
plt.plot(xdata,ydata)


v03=[8,10,12]
th03=[40,30,50]
colors3 = ["b", "g", "r"]
xmax3 = [7.28,8.7,13.75]

for v0,th0,col,xmax in zip(v03,th03,colors3,xmax3):
   print(v0,th0,"\n")
   xdata = np.linspace(0.0,xmax,200)
   ydata= traj(xdata,v0,th0)
   plt.plot(xdata,ydata,color=col)
plt.ylim(0,10)
#plt.xlim(7,8)
'''
plt.show()

