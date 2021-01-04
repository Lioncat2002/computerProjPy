'''7.WAP to write a function which sums the elements of a list recursively'''
sum=0
def reclist(l,i=0):
    global sum
    if i<len(l):
        sum=sum+l[i]
        reclist(l,i+1)
    else:
        print(sum)
reclist([1,2,4,5,6,7,8,9])