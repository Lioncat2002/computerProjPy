'''14.WAP to plot a properly labelled pie chart with pyplot'''
import matplotlib.pyplot as plt
dataset=['Cat','Lion','Tiger']
data=['50','30','20']
fig=plt.figure(figsize=(10,7))
plt.pie(data,labels=dataset)
plt.show()