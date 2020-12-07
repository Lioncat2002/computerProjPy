'''3.Write a function DigitSum() that takes a number and returns the sum of the digits'''
sum=0
def DigitSum(num):
    global sum
    d=0
    while num!=0:
        d=(int)(num%10)
        num=(int)(num/10)
        sum=sum+d
    return sum

if __name__=='__main__':
    n=int(input("Enter number: "))
    n=DigitSum(n)
    print(f"Sum is {n}")