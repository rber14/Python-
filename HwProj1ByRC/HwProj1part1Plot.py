import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit



with open('theHwProj1.dat') as f:
   lines = f.readlines()
   t = [line.split()[0] for line in lines]
   x = [line.split()[1] for line in lines]
   v = [line.split()[2] for line in lines]
   a = [line.split()[3] for line in lines]
plt.figure()
plt.title("Proj 1")
plt.ylabel("x(t), v(t), a(t)")
plt.xlabel("t")
plt.plot(t,x, label = " x ")
plt.plot(t,v, label = " velocity ")
plt.plot(t,a, label = " acceleration ")
plt.legend(loc = "lower right")

plt.show()

   