'''4.WAP to write a function Dir3and5() which takes 10 numbers in a tuple and returns the sum of the elements which ae divisible by 3 and 5'''
sum=0
def Dir3and5(tup):#Function
    global sum
    for i in tup:#looping through the tuple
        k=i
        if(i%3==0 and i%5==0):#checking if divisible by 3 and 5
            sum+=k
    return sum

if __name__=='__main__':
    n=eval(input("Enter a tuple with 10 digits: "))

    print(f"The sum of the tuple is {Dir3and5(n)}")
