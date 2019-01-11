'''
RobertoCampos
HW7Problem1
'''
import numpy as np
import numpy.random as ran
import matplotlib.pyplot as plt
from scipy.optimize import brentq
from scipy.optimize import curve_fit

rand = ran.normal(5,1.25,100000)

(dataHist, edges, patches)= plt.hist(rand,bins=100,range=None)
midPoint = .5 * (edges[:-1]+edges[1:]) #extrac midpoint from edges
ydata=dataHist #dataHist=ydata

def d(midPoint,d0,mean,standardDev):
    return d0 * np.exp((-((midPoint - mean) ** 2) / ((2 * standardDev) ** 2)))

plt.scatter(midPoint,ydata,label = 'scatter', color='yellow',linewidth=1,zorder=2)

xexact=np.linspace(0,10,100, endpoint=True)
yexact = dataHist

(popt, pcov) = curve_fit(d, midPoint,ydata, p0=None, sigma=None, bounds=(-np.inf,np.inf))
xfitted = xexact
yfitted = d(xexact, popt[0],popt[1],popt[2])
plt.plot(xfitted,yfitted,label='fitted',color='red',linewidth=.5,linestyle='-')
plt.title("problem1")
plt.legend()
plt.show()

