'''9.WAP to read a file and remove all the lines with 'a' in it'''

file=open("wordsreadfile.txt",encoding='utf8')
s=file.readlines()
w=""

for line in s:
    if 'a' in line:
        continue
    else:
        w=w+line
print(w)