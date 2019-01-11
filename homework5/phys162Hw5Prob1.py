#RobertoCampos
#phys162Hw5october92018
import numpy as np
import matplotlib.pyplot as plt


#problem1 using 3 functions

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

