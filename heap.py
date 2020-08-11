import math

#Calculate the positions of the children below
def halve_space(pos):
    new_pos = []
    if len(pos) > 0:
        offset = pos[0]/2
        for i in range(len(pos)):
            left = pos[i] - offset
            right = pos[i] + offset
            new_pos.append(left)
            new_pos.append(right)

    return new_pos

#Min Heap implementation
class MinIntHeap():
    capacity = 10
    size = 0

    items = []

    #Getting related indices
    def get_left_index(self,pindex):
        return (pindex*2)+1
    def get_right_index(self,pindex):
        return (pindex*2)+2
    def get_parent_index(self,chindex):
        return int((chindex-1)/2)

    #Check related indices
    def has_left(self,index):
        return len(self.items) > self.get_left_index(index)
    def has_right(self,index):
        return len(self.items) > self.get_right_index(index)
    def has_parent(self,index):
        return self.get_parent_index(index) >= 0

    #related nodes
    def left_child(self,index):
        return self.items[self.get_left_index(index)]
    def right_child(self,index):
        return self.items[self.get_right_index(index)]
    def parent(self,index):
        return self.items[self.get_parent_index(index)]

    #swap two nodes in the heap.  usually in heapifyUp/Down
    def swap(self, indexOne, indexTwo):
        temp = self.items[indexOne]
        self.items[indexTwo] = self.items[indexOne]
        self.items[indexOne] = temp

    #see the value at the top of the heap
    def peek(self):
        if len(self.items) == 0:
            raise Exception('Nothing in heap')
        return self.items[0]

    #get the top of the heap, replacing with the last element which is heapified down.
    def poll(self):
        if len(self.items) == 0:
            raise Exception('Nothing in heap')
        oroot = self.items[0]
        self.items[0] = self.items[len(self.items)-1]
        self.items.remove(self.items[len(self.items)-1])
        self.heapifyDown()
        return oroot

    #add item to the bottom of the heap and heapify up
    def add(self, item):
        self.items.append(item)
        self.heapifyUp()

    #heapify the node at index, downward
    def heapifyDown(self,index=0):
        if self.has_right(index):
            right = self.right_child(index)
            if self.items[index] > right:
                self.swap(self.items[index],right)
                self.heapifyDown(self.get_right_index(index))
            elif self.has_left(index):
                left = self.left_child(index)
                if self.items[index] > left:
                    self.swap(self.items[index],left)
                    self.heapifyDown(self.get_left_index(index))

    #heapify the node at index, upward
    def heapifyUp(self,index=len(items)-1):
        parent = self.items[self.get_parent_index(int(index))]
        if self.items[index] < parent:
            self.swap(self.parent,self.items[index])
            self.heapifyUp(self.get_parent_index(index))

    #get all of the print positions for all nodes in the heap
    def get_all_positions(self,levels):
        all_pos = []
        prev_pos = [2**(levels)/2]
        all_pos.append(prev_pos)
        next_pos = []
        for _ in range(levels-1):
            next_pos = halve_space(prev_pos)
            all_pos.append(next_pos)
            prev_pos = next_pos

        return all_pos
        
    #string representation of the heap
    def __str__(self):
        level = 0
        print_count = 0
        s = ''
        if len(self.items) > 0:
            #bottom row width
            print('elements: ',self.items)
            levels = math.floor(math.log2(len(self.items)))+1
            print('levels: ',levels)
            #TODO handle multi-character nodes
            bwidth = 2**levels
            print('bwidth: ',bwidth)   
            levels_pos = self.get_all_positions(levels)
            print('print positions: ',levels_pos)
            for level in levels_pos:
                for cur in range(bwidth):
                    if cur in level and print_count < len(self.items):
                        s = s+str(self.items[print_count])
                        print_count+=1
                    else:
                        s = s + ' '
                s = s + '\n'
        return s

heap = MinIntHeap()
for i in range(100):
    heap.add(i%10)
print(heap)