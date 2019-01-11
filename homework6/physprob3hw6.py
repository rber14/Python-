# Anand Rai
# Homework 6; Problem 1 part c)

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import brentq

"""The constants"""
d = 5
H = 2
alpha = np.radians(30)
h0 = 1.54
theta0 = np.radians(25)
g = 9.8


def traj(x, v0, th0):
    """This method will return the y-coordinate for a given x-coordinate and \
       initial velocity. Initial height = 1.54 m"""
    th0rad = th0 * np.pi / 180.0  # Converting to radians
    return h0 + np.tan(th0rad) * x - (g * x ** 2) / (2 * v0 ** 2 * np.cos(th0rad) ** 2)


def ground(x):
    """Returns the y-value for the first ground
    :rtype: double
    """
    if x <= d:
        return 0
    elif (x - d) * np.tan(alpha) < H:
        return (x - d) * np.tan(alpha)
    elif x > H:
        return H


def ground1(x):
    """Returns the y-value for the Second version of the Ground"""
    return 1 - np.e**(-x**2/1000) + 0.28 * (1 - np.e**(-.03*x**2))*(1-np.cos(20*x**.2))


def diff(x, v0, th0):
    return traj(x, v0, th0) - ground(x)


def diff1(x, v0, th0):
    return traj(x, v0, th0) - ground1(x)


"""Solving the equations a)"""
sol = [brentq(diff, 1, 5, args=(5, 25)), brentq(diff, 7, 10, args=(10, 25)), brentq(diff, 15, 18, args=(15, 25))]

"""a) Subplot"""
plt.subplot(2, 1, 1)
for i in sol:
    plt.scatter(i, ground(i))
    plt.annotate(text='({0:.2f}, {1:.2f})'.format(i, ground(i)), xy=(i, ground(i)), xytext=(i, ground(i)+.5))

xData = np.linspace(0, sol[0], 1000)
y1 = traj(xData, 5, 25)
plt.plot(xData, y1, color='blue', label='v0 = 5 m/s')
xData = np.linspace(0, sol[1], 1000)
y2 = traj(xData, 10, 25)
plt.plot(xData, y2, color='red', label='v0 = 10 m/s')
xData = np.linspace(0, sol[2], 1000)
y3 = traj(xData, 15, 25)
plt.plot(xData, y3, color='yellow', label='v0 = 15 m/s')

xData = np.linspace(0, 100, 1000)
floor = []
for x in xData:
    floor.append(ground(x))
plt.plot(xData, floor, color='black', label='ground')

plt.title('Ground 1')
plt.legend(loc='upper left')

plt.ylim(0, 5)
plt.xlim(0, 21)
plt.xticks(sol)
height = [ground(sol[0]), ground(sol[1]), ground(sol[2])]
plt.yticks(height)

"""Solving the equations b)"""
sol = [brentq(diff1, 1, 5, args=(6, 25)), brentq(diff1, 20, 25, args=(16, 25)), brentq(diff1, 50, 55, args=(26, 25))]

"""a) Subplot"""
plt.subplot(2, 1, 2)
for i in sol:
    plt.scatter(i, ground1(i))
    plt.annotate(text='({0:.2f}, {1:.2f})'.format(i, ground1(i)), xy=(i, ground1(i)), xytext=(i , ground1(i)+1))


xData = np.linspace(0, sol[0], 1000)
y1 = traj(xData, 6, 25)
plt.plot(xData, y1, color='blue', label='v0 = 6 m/s')
xData = np.linspace(0, sol[1], 1000)
y2 = traj(xData, 16, 25)
plt.plot(xData, y2, color='red', label='v0 = 16 m/s')
xData = np.linspace(0, sol[2], 1000)
y3 = traj(xData, 26, 25)
plt.plot(xData, y3, color='yellow', label='v0 = 26 m/s')

xData = np.linspace(0, 100, 10000)
floor1 = []
for x in xData:
    floor1.append(ground1(x))
plt.plot(xData, floor1, color='black', label='ground')

plt.ylim(0, 10)
plt.xlim(0, 60)
plt.xticks(sol)
plt.legend(loc='upper left')
plt.title('Ground 2')




plt.tight_layout()
plt.show()

