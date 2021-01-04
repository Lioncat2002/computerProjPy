'''13.WAP to generate sin(x,n) to determine the value of sin(x) using pyplot'''
import matplotlib.pyplot as plt
import numpy as np
n=4
n=np.arange(0,n*np.pi,0.1)
y=np.sin(n)
plt.plot(n,y)
plt.show()