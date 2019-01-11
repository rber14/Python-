'''
RobertoCampos
HW7Problem4
'''
import numpy as np
import numpy.random as ran
import matplotlib.pyplot as plt
from scipy.optimize import brentq
from scipy.optimize import curve_fit



G=[]
for line in open ('HW07-doubleGaussian.dat.txt','r'):
    values = [float(s) for s in line.split()]
    G.append(values[0])

plt.subplot(2,1,1)
xdata=np.arange(len(G))
plt.scatter(xdata,G,s=5)
plt.title("problem1")


plt.subplot(2,1,2)
(dataHist, edges, patches)= plt.hist(G,bins=50,range=None)
midPoint = .5 * (edges[:-1]+edges[1:]) #extrac midpoint from edges
ydata=dataHist #dataHist=ydata

def d(midPoint,d0,mean,standardDev):
    return d0 * np.exp((-((midPoint - mean) ** 2) / ((2 * standardDev) ** 2)))

plt.scatter(midPoint,ydata, color='yellow',s=5,linewidth=1,zorder=2)

xexact=np.linspace(0,4,100, endpoint=True)
yexact = dataHist

(popt, pcov) = curve_fit(d, midPoint,ydata, p0=None, sigma=None, bounds=(-np.inf,np.inf))
xfitted = xexact
yfitted = d(xexact, popt[0],popt[1],popt[2])
plt.plot(xfitted,yfitted,color='red',linewidth=.5,linestyle='-')
print(popt)
plt.tight_layout()
plt.show()


print(popt)