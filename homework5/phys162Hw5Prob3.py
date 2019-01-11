#RobertoCampos
#phys162Hw5october72018
import numpy as np
import matplotlib.pyplot as plt


#problem3 ground mod
g=9.81;#gravity
h0=1.54 #m
def traj(x,v0,th0):
   th0rad = th0 * np.pi/180.0 #radians
   return h0 + np.tan(th0rad) * x - (g * x**2)/(2*v0**2*np.cos(th0rad)**2)


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
plt.plot(xdata,ydata,color='black')


v03=[8,10,12]
th03=[40,30,50]
colors3 = ["b", "g", "r"]
xmax3 = [7.28,8.7,13.75]

for v0,th0,col,xmax in zip(v03,th03,colors3,xmax3):
   xdata = np.linspace(0.0,xmax,200)
   ydata= traj(xdata,v0,th0)
   plt.plot(xdata,ydata,color=col)
plt.title("Ground Modification")
plt.xlabel("Range")
plt.ylabel("Height")
plt.ylim(0,10)
plt.xticks([7.28,8.7,13.75],[7.2,8.7,13.7])
plt.annotate('r=7.28', xy=(7.28,.88))
plt.annotate('r=8.7', xy=(8.7,1.79))
plt.annotate('r=13.7', xy=(13.7,2.6))
plt.show()

