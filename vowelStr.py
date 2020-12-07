'''2.WAP to take a strng as input and output and count the vowels in the string'''

s=input("Enter String: ")
count=0
for chr in s:
    chr=chr.lower()
    if(chr=='a'or chr=='e'or chr=='i' or chr=='o' or chr=='u'):
        count=count+1
print(f"There are {count} vowels in the string")