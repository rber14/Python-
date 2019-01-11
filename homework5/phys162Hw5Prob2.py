#RobertoCampos
#phys162Hw5october92018
import numpy as np
import matplotlib.pyplot as plt


#prob2 flat ground
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
 

plt.show()

