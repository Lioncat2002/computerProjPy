'''5.WAP to input a list and arrange the list in ascending order with bubble sort'''

l=eval(input("Enter the list: "))
for j in range(0,len(l)):
    for i in range(0,len(l)-1):
        if(l[i]>l[i+1]):
            l[i+1],l[i]=l[i],l[i+1]
print(l)