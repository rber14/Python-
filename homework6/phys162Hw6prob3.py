#robertoCampos
#Hw6prob3
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import brentq

d = 5  #inm
H = 2 #inm
alph = np.radians(30)
h0 = 1.54 #inm
theta0 = np.radians(25)
g = 9.8

#fromHw
def traj(x, v0, th0):
    th0rad = th0 * np.pi / 180.0  # Convert to radians
    return h0 + np.tan(th0rad) * x - (g * x ** 2) / (2 * v0 ** 2 * np.cos(th0rad) ** 2)

def gr(x):          #groundGivenBy
    if x <= d:
        return 0
    elif (x - d) * np.tan(alph) < H:
        return (x - d) * np.tan(alph)
    elif x > H:
        return H

#other equation for ground
def grd1(x):
    return 1 - np.e**(-x**2/1000) + 0.28 * (1 - np.e**(-.03*x**2))*(1-np.cos(20*x**.2))

def diff(x, v0, th0):
    return traj(x, v0, th0) - gr(x)     #intersectsWithGround

def diff1(x, v0, th0):
    return traj(x, v0, th0) - grd1(x) #intersectwithGround

#numbericalUsingBrenq Finding where traj meets with ground
r=brentq(diff, 1, 5, args=(5, 25))
r1=brentq(diff, 7, 10, args=(10, 25))
r2=brentq(diff, 15, 18, args=(15, 25))
solution=[r,r1,r2]
plt.subplot(2, 1, 1)

plt.scatter(r,gr(r))
plt.scatter(r1,gr(r1))
plt.scatter(r2,gr(r2))

plt.annotate('({0:.2f}, {1:.2f})'.format(r, gr(r)), xy=(r,gr(r)), xytext=(r,gr(r)+.2))
plt.annotate('({0:.2f}, {1:.2f})'.format(r1, gr(r1)), xy=(r1,gr(r1)), xytext=(r1,gr(r1)+.7))
plt.annotate('({0:.2f}, {1:.2f})'.format(r2, gr(r2)), xy=(r2,gr(r2)), xytext=(r2,gr(r2)+.2))

xdata = np.linspace(0, solution[0], 1000)  #solution[0] gives where to stop plotting xdata
ydata = traj(xdata, 5, 25)
plt.plot(xdata, ydata, color='b', label='v0= 5m/s')
xdata = np.linspace(0, solution[1], 1000)
ydata2 = traj(xdata, 10, 25)
plt.plot(xdata, ydata2, color='red', label='v0= 10m/s')
xdata = np.linspace(0, solution[2], 1000)
ydata3 = traj(xdata, 15, 25)
plt.plot(xdata, ydata3, color='green', label='v0= 15m/s')

xdata = np.linspace(0, 100, 1000)
floor = []
for x in xdata:
    floor.append(gr(x))
plt.plot(xdata, floor, color='black', label='ground')

plt.title('Problem3\nFirst Ground')
plt.legend(loc='upper left')
plt.ylabel('Height')
plt.xlabel('Ground')
plt.ylim(0, 5)
plt.xlim(0, 21)
plt.xticks(solution)

rt=brentq(diff1, 1, 5, args=(6, 25))
rt2=brentq(diff1, 20, 25, args=(16, 25))
rt3=brentq(diff1, 50, 55, args=(26, 25))
solution2=[rt,rt2,rt3]
plt.subplot(2, 1, 2)

plt.scatter(rt,grd1(rt))
plt.scatter(rt2,grd1(rt2))
plt.scatter(rt3,grd1(rt3))

plt.annotate('({0:.2f}, {1:.2f})'.format(rt, grd1(rt)), xy=(rt,grd1(rt)), xytext=(rt,grd1(rt)+.2))
plt.annotate('({0:.2f}, {1:.2f})'.format(rt2, grd1(rt2)), xy=(rt2,grd1(rt2)), xytext=(rt2,grd1(rt2)+.7))
plt.annotate('({0:.2f}, {1:.2f})'.format(rt3, grd1(rt3)), xy=(rt3,grd1(rt3)), xytext=(rt3,grd1(rt3)+.2))

xdata = np.linspace(0, solution2[0], 1000)
ydata1 = traj(xdata, 6, 25)
plt.plot(xdata, ydata1, color='b', label='v0= 6m/s')
xdata = np.linspace(0, solution2[1], 1000)
ydata2 = traj(xdata, 16, 25)
plt.plot(xdata, ydata2, color='red', label='v0= 16m/s')
xdata= np.linspace(0, solution2[2], 1000)
ydata3 = traj(xdata, 26, 25)
plt.plot(xdata, ydata3, color='green', label='v0= 26m/s')

xdata = np.linspace(0, 100, 10000)
theGround = []
for x in xdata:
    theGround.append(grd1(x))
plt.plot(xdata, theGround, color='black', label='ground')

plt.ylim(0, 10)
plt.xlim(0, 60)
plt.xticks(solution2)
plt.ylabel('Height')
plt.xlabel('Ground')
plt.title('Second Ground')
plt.legend(loc='best')
plt.tight_layout()
plt.show()


