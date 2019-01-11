import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import solve
from fractions import Fraction
from scipy.optimize import fsolve
def z1(r):
    (x,y)=r
    return x**5-y**3+y**2-np.sin(x)

def z2(r):
    (x,y)=r
    return y**5-x**3 - Fraction(-1/4)*np.cos(x)-0.98

def Z(r):
    #(x,y)=r
    return ( z1(r),z2(r))


xlist= np.linspace(-2,2,100, endpoint=True)
ylist= np.linspace(-2,2,100, endpoint=True)

X,Y = np.meshgrid(xlist, ylist)
Z1=z1((X,Y))
Z2=z2((X,Y))

plt.contour(X,Y,Z1,levels=[0], colors=['blue'], label='x^5-y^3+y^2=sin(x)')
plt.contour(X,Y,Z2,levels=[0], colors=['red'],label='y^5-x^3= (-1/4)cos^2(x)-.98')
plt.legend(loc='best')

plt.scatter(-1.24,-1.004,color='green') #root1
plt.scatter(.0537,.9391,color='green') #root2
plt.scatter(1.002,1.1311,color='green')  #root3

plt.annotate('root1=-1.24', xy=(-1.24,-1.004))
plt.annotate('root2=.0537', xy=(.0537,.9391))
plt.annotate('root3=1.002', xy=(1.002,1.1311))

plt.xlabel("Green dots indicate roots")
plt.title("Prob 1c")


root1=fsolve(Z, (-2,-1.1))
print("x= {}".format(root1))
#root2=fsolve(Z, (-1.06,-0.5))  # not a root
#print(root2)
root2=fsolve(Z, (0,0.3))
print("x= {}".format(root2))
root3=fsolve(Z, (0.8,2))
print("x= {}".format(root3))

plt.show()
