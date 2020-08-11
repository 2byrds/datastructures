import math
import time

def binary_search(elements,data,start=0,end=0):
    #print('\t\tSearching ',start, ' to ', end)

    if not elements or len(elements)==0:
        return None
    elif start == end and elements[start]!=data:
        #print('\t\t',data, ' not found')
        return None

    middle = math.ceil((end+start)/2)
    #print('\t\tmiddle is: ',middle)
    
    if data == elements[middle]:
        #print('\t\tfound ',data,' at ',middle)
        return middle
    elif middle == len(elements)-1 or middle == start:
        #print('\t\t',data, ' not found')
        return None
    elif data < elements[middle]:
        return binary_search(elements,data,start,middle-1)
    elif data > elements[middle]:
        return binary_search(elements,data,middle+1,end)

size = 10000000

elements=[]
for i in range(0,size):
    elements.append(i)

find = [0,int(size/2),int(size/4),int(size/10),int(size/2+size/4), int(size-int(size/10)),size+size]
linear_total = 0
binary_total = 0

for f in find:
    print('\n\nLooking for ', f,': ')

    print('Linear')
    start = time.time()
    print('\tFound? ', f in elements)
    end = time.time()
    subtotal = end - start
    print('\tsubtotal time: ',subtotal)
    linear_total += subtotal
    
    print('Binary:')
    start = time.time()
    print('\tFound at ', binary_search(elements=elements,data=f,start=0,end=len(elements)-1))
    end = time.time()
    subtotal = end - start
    print('\tBinary subtotal time: ',subtotal)
    binary_total += subtotal

print('Linear Search Total: ',linear_total)
print('Binary Search Total: ',binary_total)