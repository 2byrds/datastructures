class Node:
    next = None
    data = -1

    def __init__(self,data=-1):
        self.data = data

    def __str__(self):
        s = 'me: ' + str(self.data)
        if self.next != None:
            s += ',next: '+str(self.next.data)
        return s

class LinkedList:
    head = None

    def append(self,data):
        addme = Node(data)
        if self.head == None:
            self.head = addme
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = addme

    def prepend(self,data):
        newHead = Node(data)
        newHead.next = self.head
        self.head = newHead

    def delete_with_value(self,data):
        if self.head == None:
            print('Cannot delete data from empty LinkedList')
        else:
            current = self.head
            prev = None
            while current.data != data and current.next != None:
                prev = current
                current = current.next
            
            if current.data == data:
                if prev == None:
                    self.head = current.next
                else:
                    prev.next = current.next

    def __str__(self):
        s = ''

        if self.head == None:
            s += 'Empty Linked List'
        else:
            s += 'head'
            s += '\n |'
            s += '\n v'
            s += '\n' + str(self.head)
            
            current = self.head
            while current.next != None:
                current = current.next
                s+=' -> '
                s+=str(current)

        return s

ll = LinkedList()
print(ll)
ll.append(0)
print(ll)
ll.append(1)
print(ll)
for i in range(2,20):
    ll.append(i)
print(ll)

print('-------------------------')

ll = LinkedList()
print(ll)
ll.prepend(0)
print(ll)
ll.prepend(1)
print(ll)
for i in range(2,20):
    ll.prepend(i)
print(ll)

print('-------------------------')

ll.delete_with_value(19)
ll.delete_with_value(7)
ll.delete_with_value(0)
print(ll)
for i in range(2,20):
    ll.delete_with_value(i)
print(ll)