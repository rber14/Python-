#robertoCampos
#phys162prob1a
#oct14
import numpy as np
import matplotlib.pyplot as plt 
from scipy.optimize import brentq

def log(x):
      return np.log(x)  #givesRuntimeError    
def sin(x):
   return np.pi*np.sin(x)
def f2(x):
   return (np.pi*np.sin(x))-log(x)

print("Roots:")
root1=brentq(f2,0,5)
print("x= {}".format(root1))
root2=brentq(f2,6,7.6)
print("x= {}".format(root2))
root3=brentq(f2,8,10)
print("x= {}".format(root3))
root4=brentq(f2,12,14)
print("x= {}".format(root4))
root5=brentq(f2,14,17)
print("x= {}".format(root5))

xdata=np.linspace(0,20,200)
ydata=log(xdata)
ydata2=sin(xdata)
plt.plot(xdata,ydata)
plt.plot(xdata,ydata2)
plt.ylim(0,4)
plt.xlim(0,20)
plt.xlabel("Red dots indicate roots")
plt.title("Prob 1a")

plt.scatter(2.806,1,color='red')
plt.scatter(6.948,1.94, color='red')
plt.scatter(8.66,2.14, color='red')
plt.scatter(13.544,2.6,color='red')
plt.scatter(14.68,2.69,color='red')

plt.annotate('root1=2.8', xy=(2.806,1))
plt.annotate('root2=7', xy=(6.949,1.94))
plt.annotate('root3=8.687', xy=(8.66,2.15))
plt.annotate('root4=13.53', xy=(13.544,2.6))
plt.annotate('root5=14.68', xy=(14.68,2.69))
plt.show()

