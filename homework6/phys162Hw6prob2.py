#robertoCampos
#phys162problem2
#oct14
import numpy as np
import matplotlib.pyplot as plt 
from numpy.linalg import solve

A=np.array([[-11,1,3],[4,1,-9],[-2,-5,15]])
b=np.array([1,-8,7])

sol=np.linalg.solve(A,b)
print(sol)
print("a= {}".format(sol[0]))
print("b= {}".format(sol[1]))
print("c= {}".format(sol[2]))