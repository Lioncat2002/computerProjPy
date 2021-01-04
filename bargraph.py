'''15.WAP to plot a properly labelled bar graph with pyplot'''
import matplotlib.pyplot as plt
pet=["Cat","Dog","Lion","Tiger"]
values=[20,30,10,5]

plt.bar(pet,values,color='green',width=0.4)
plt.xlabel("Animals")
plt.ylabel("Numbers")
plt.show()

