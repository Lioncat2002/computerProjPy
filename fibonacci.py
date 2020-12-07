'''1.WAP to print the fibonacci series upto n terms and also find the sum of the series'''
a,b=1,1
c=0
sum=0
n=int(input("Enter limit: "))
print("Fibonacci series:")
for i in range (0,n):
    a=b
    b=c
    c=a+b
    print(c,end=',')
    sum=sum+c
print()
print(f"Sum of fibonacci series is {sum}")
