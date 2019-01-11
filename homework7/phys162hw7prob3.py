'''
Roberto Campos
HW7Problem 3
'''
import numpy as np
import numpy.random as ran
import matplotlib.pyplot as plt
from scipy.optimize import brentq
from scipy.optimize import curve_fit

def func(t,w,a):
   return a*np.sin(w*t)

def func2(t,w2,b):
    a=popt[0]
    w=popt[1]
    return a*np.sin(w*t)+b*np.sin(w2*t)

x,y=[],[]
for line in open('HW07-nonLinearFit.dat.txt', 'r'):
    values = [float(s) for s in line.split()]
    x.append(values[0])
    y.append(values[1])

(popt, pcov) = curve_fit(func,x,y, p0=(3,3), sigma=None, bounds=(-np.inf,np.inf))
xexact = np.linspace(0,10,1000)
yexact = func(xexact, *popt)
plt.plot(xexact,yexact, color='r',label="Exact first part of the function")

(popt, pcov) = curve_fit(func2,x,y, p0=(-2.8,2), sigma=None, bounds=(-np.inf,np.inf))
xexact2 = np.linspace(0,10,1000)
yexact2 = func(xexact, *popt)
plt.plot(xexact2,yexact2, color='g',label="Exact full function")

plt.scatter(x,y,s = 9, label = 'scatter')
plt.legend()
plt.title('Problem 3')
plt.show()
