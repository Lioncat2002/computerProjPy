'''11.WAP to plot the function y=x^2 with pyplot library'''

import matplotlib.pyplot as plt
x=range(-100,100)
y=[i*i for i in x]

plt.plot(x,y)
plt.show()