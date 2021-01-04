'''12.WAP to search for a number from a list with linear search'''

l=eval(input("Enter the list"))
s=int(input("Enter number to search"))

for i in l:
    if i==s:
        print("Found!!")
        break
else:
    print("Not found")