'''
RobertoCampos
HW7 problem 2
'''
import numpy as np
import numpy.random as ran
import matplotlib.pyplot as plt
from scipy.optimize import brentq
from scipy.optimize import curve_fit

def func1(x,a,b,c,d,e,f):
    return a*x**5 + b*x**4 + c*x**3 + d*x**2 + e*x + f
def func2(x,a,b,c,d):
    return a*x**3 + b*x**2 + c*x + d
def func3(x,a,b):
    return a*x + b

xx,yy = [],[]
for line in open ('HW07-linearFit.dat.txt','r'):
    values = [float(s) for s in line.split()]
    xx.append(values[0])
    yy.append(values[1])

plt.scatter(xx,yy,label='scatter')



(popt, pcov) = curve_fit(func1,xx,yy, p0=None, sigma=None, bounds=(-np.inf,np.inf))
xexact = np.linspace(-6,5,1001)
yexact = func1(xexact,*popt)
plt.plot(xexact,yexact, color='r',label="a*x**5 + b*x**4 + c*x**3 + ...")

(popt, pcov) = curve_fit(func2,xx,yy, p0=None, sigma=None, bounds=(-np.inf,np.inf))
xexact1 = np.linspace(-6,5,1001)
yexact1 = func2(xexact,*popt)
plt.plot(xexact1,yexact1, color='yellow',label="a*x**3 + b*x**2 + c*x + d")

(popt, pcov) = curve_fit(func3,xx,yy, p0=None, sigma=None, bounds=(-np.inf,np.inf))
xexact2 = np.linspace(-6,5,1001)
yexact2 = func3(xexact,*popt)
plt.plot(xexact2,yexact2, color='green',label="a*x + b")

plt.title("Problem 2")
plt.legend(loc= 'upper right')
plt.show()