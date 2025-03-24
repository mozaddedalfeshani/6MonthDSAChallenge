# stack (LIFO) : Last In First Out

stack = []

def push(item):
    stack.append(item)
    update()

def peek():
    pass

def pop():
    pass

def update():
    print(stack)


push(20)
push(20)
push(20)


stack.append(1223)
stack.append(1223)
stack.append(1223)
stack.pop()
update()