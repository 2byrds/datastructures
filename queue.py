class Queue:
    elements=[]

    def peek(self):
        if len(self.elements) <= 0:
            return None
        return self.elements[0]

    def enqueue(self,data):
        self.elements.append(data)

    def dequeue(self):
        if len(self.elements) <= 0:
            return None
        return self.elements.remove(self.elements[0])

    def __str__(self):
        if len(self.elements) <= 0:
            return 'Queue empty'
        else:
            s = str(self.elements[0])
            for i in range(1,len(self.elements)-1):
                s+=','+str(self.elements[i])
            return s

queue = Queue()
print(queue)
queue.dequeue()
print(queue)
queue.enqueue(1)
print(queue)
queue.dequeue()
print(queue)
for i in range(10):
    queue.enqueue(i)
print(str(queue.peek()))
print(queue)
for i in range(5):
    queue.dequeue()
print(str(queue.peek()))
print(queue)
for i in range(6):
    queue.dequeue()
print(str(queue.peek()))
print(queue)
    