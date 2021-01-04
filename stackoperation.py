'''16.WAP to write a menu based program for showing operation on a stack'''
items=[]
isRunning=True
def push(data):
    items.append(data)
def pop():
    return items.pop()
while isRunning:

    print('pop \n'
          'push <value> \n'
          'quit')
    n=input("What do you want?")
    n=n.split()

    if n[0].strip().lower()=='pop':
        if items==[]:
            print("Empty stack")
        else:
            print("Popped value",pop())
    elif n[0].strip().lower() == 'push':
        push(int(n[1]))
    elif n[0].strip().lower()=='quit':
        isRunning=False



