#RobertoCampos
#phys162Hw5october72018
import numpy as np
import matplotlib.pyplot as plt

#problem4

with open('HW05-ground.dat.txt') as f:
   lines=f.readlines()
   x=[line.split()[0] for line in lines]
   c=[line.split()[1] for line in lines]
   y=[line.split()[2] for line in lines]
fig=plt.figure()
ax1=fig.add_subplot(111)
ax1.plot(x,y)

plt.show()