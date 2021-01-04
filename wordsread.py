'''8.WAP to read a text file and print the total number of words present in it'''

file=open("wordsreadfile.txt",encoding='utf8')
s=file.read()
s=" "+s+" "
w=str()
count=[]
count=s.split()
print(len(count))

