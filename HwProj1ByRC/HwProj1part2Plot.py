import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit



with open('zoft.dat') as f:
   lines = f.readlines()
   t = [line.split()[0] for line in lines]
   x = [line.split()[1] for line in lines]
plt.figure()
plt.title("Proj 1 part 2")
plt.ylabel("z(s)")
plt.xlabel("s")
plt.plot(t,x, label = " x ")
plt.legend(loc = "lower right")

plt.show()

   