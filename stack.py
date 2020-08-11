class Stack:
    elements=[]

    def peek(self):
        if len(self.elements) <= 0:
            return None
        return self.elements[len(self.elements)-1]

    def push(self,data):
        self.elements.append(data)

    def pop(self):
        if len(self.elements) <= 0:
            return None
        return self.elements.remove(self.elements[len(self.elements)-1])

    def __str__(self):
        if len(self.elements) <= 0:
            return 'Stack empty'
        else:
            s = str(self.elements[len(self.elements)-1])
            for i in reversed(range(len(self.elements)-1)):
                s+=','+str(self.elements[i])
            return s

stack = Stack()
print(stack)
stack.pop()
print(stack)
stack.push(1)
print(stack)
stack.pop()
print(stack)
for i in range(10):
    stack.push(i)
print(str(stack.peek()))
print(stack)
for i in range(5):
    stack.pop()
print(str(stack.peek()))
print(stack)
for i in range(6):
    stack.pop()
print(str(stack.peek()))
print(stack)
    