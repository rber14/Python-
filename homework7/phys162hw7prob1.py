#robertoCampos
#phys162HW7Problem1

import numpy as np
import numpy.random as ran
import matplotlib.pyplot as plt
from scipy.optimize import brentq
from scipy.optimize import curve_fit

d0 = 1
mean = 5
standardDev = 1.25


def func(x,d0,mean,standardDev):
    return d0 * np.exp((-((x - mean) ** 2) / ((2 * standardDev) ** 2)))



s = ran.normal(mean, standardDev, size=1000)
(dataHist,edges,patches)=plt.hist(s,bins=10,color="yellow",density=True) #dataHist is essentialy ydata
xdata= .5*(edges[:-1]+edges[1:])
plt.scatter(xdata,dataHist,20,color='blue',zorder=2)

def g(x,a,b,c,d):
    return a+b*x+c*x**2+d*x**3
(popt,pcov)=curve_fit(g,xdata,dataHist,p0=None, bounds=(-np.inf,np.inf))
print(popt)
xfitted = np.linspace(0,10,1000)
yfitted = g(xfitted,popt[0],popt[1],popt[2],popt[3])
plt.plot(xfitted,yfitted)


#plt.plot(xdata,dataHist)
plt.title("Problem 1")
plt.show()

print(np.sqrt(2*np.pi*d0*standardDev))


