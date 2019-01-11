import numpy as np
import numpy.random as ran
import matplotlib.pyplot as plt
from scipy.optimize import brentq

fig=plt.figure()

ax=fig.add_subplot(1,3,1)
j= ran.randint(0,100,10000)
ax.hist(j,bins=10)


bx=fig.add_subplot(1,3,2)
x= ran.normal(2,0.2,10000)
bx.hist(x,bins=20,color='red')
#plt.show()

(dataHist,edges,patches) = ax.hist(j)
xData = .5*(edges[:-1]+edges[1:])
cx=fig.add_subplot(1,3,3)
cx.scatter(xData,dataHist)
plt.xlim(1,3)
plt.show()

'''
d0 = 1
mean = 5
standardDev = 1.25

def d(x):
    d0 * np.exp((-((x - mean) ** 2) / ((2 * standardDev) ** 2)))


xData = np.linspace(0, 100, 1000)
random = d(xData)*np.ran(100)

plt.hist()
plt.plot()
'''