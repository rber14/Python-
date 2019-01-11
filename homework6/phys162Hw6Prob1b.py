#robertoCampos
#phys162prob1b
#oct14
import numpy as np
import matplotlib.pyplot as plt 
from scipy.optimize import brentq


def tan(x):
   return (0.5)*np.tan(x)-1
def t(x):
   return (.5)*np.tan(x)

def x(x):
   return x


print("Roots:")
root1=brentq(tan,0,1.4) #root1
print("x= {}".format(root1))
root2=brentq(tan,2.5,4.3) #root2
print("x= {}".format(root2))
root3=brentq(tan,6,7.7) #root3
print("x= {}".format(root3))
root4=brentq(tan,8,10.9) #root4
print("x= {}".format(root4))
root5=brentq(tan,12,13.7) #root5
print("x= {}".format(root5))

  
xdata=np.linspace(0,15,1000)
ydata=t(xdata)
plt.plot(xdata,ydata)
plt.axhline(y=1, xmin=0,xmax=5,c="blue")
plt.ylim(0,20)
plt.xlim(0,15)
plt.xlabel("Red dots indicate roots")
plt.title("Prob 1b")

plt.scatter(1.107,1,color='red') #root1
plt.scatter(4.248,1,color='red') #root2
plt.scatter(7.39,1,color='red')  #root3
plt.scatter(10.53,1,color='red') #root4
plt.scatter(13.67,1,color='red') #root5

plt.annotate('root1=1.107', xy=(1.107,1))
plt.annotate('root2=4.248', xy=(4.248,1))
plt.annotate('root3=7.39', xy=(7.39,1))
plt.annotate('root4=10.53', xy=(10.53,1))
plt.annotate('root5=13.67', xy=(13.67,1))
plt.show()

