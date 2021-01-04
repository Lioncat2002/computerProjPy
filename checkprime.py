'''6.Write a recursive function chkprime() which checks if a number is prime or not'''
count=0
def chkprime(n,i=1):
    global count
    if n%i==0:
        count+=1
    if n>=i:
        chkprime(n,i+1)
    if n<i:
        if count==2:
            print("Prime")
        else:
            print("Not prime")

chkprime(13)