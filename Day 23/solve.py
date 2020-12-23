input = '739862541'

class Link (object):
    def __init__ (self, data, next = None):
        self.data = data
        self.next = next
    
    def __str__ (self):
        return str(self.data)


class CircularList(object):
    def __init__(self):
        self.head = Link(None, None)
        self.head.next = self.head
        self.max = 0
        self.dictionary = {}

    def insert_after(self, insert_node, after_node):
        insert_node.next = after_node.next
        after_node.next = insert_node
        if insert_node.data > self.max:
            self.max = insert_node.data
        if insert_node.data not in self.dictionary:
            self.dictionary[insert_node.data] = insert_node
    
    def get_node(self, label):
        return self.dictionary[label]
    
    def __str__(self):
        #Just a pretty print of the list, works well 
        #enough for Part 1. 
        str_ = ''
        current = self.head.next
        while current is not self.head:
            #print(current.data)
            str_+=str(current.data)+' -> '
            # advance to next element
            current = current.next
        return str_
    
    def part1(self):
        solution = ''
        current = self.get_node(1).next
        while current.data != 1:
            if current == self.head: 
                current = current.next
                continue
            solution+=str(current.data)
            current = current.next
        return solution
    
    def part2(self):
        one = self.get_node(1)
        i = one.next
        j = i.next
        return i.data * j.data


clist = CircularList()
previous = clist.head
for char in input:
    node = Link(int(char))
    clist.insert_after(node, previous)
    previous = node

part2 = True
if part2:
    m = clist.max
    for i in range(m+1, 1000001):
        node = Link(int(i))
        clist.insert_after(node, previous)
        previous = node


def play(cups, part2=False):
    h = cups.head
    current = cups.head.next
    loop = False
    count = 100
    if part2: count = 10000000
    for _ in range(count):
        move = []
        #Select next three cups to move. If the list loops
        #we need to skip the head node and then update links
        #accordingly after.
        node = current.next
        if node == h: 
            loop = True
            node = node.next
        #notice that after last loop node will be the next of
        #move[-1], so we can update by saying current.next=node
        for _ in range(3):
            move.append(node)
            node = node.next
            if node == h: 
                loop = True
                node = node.next
        #if there was a loop, update head links
        if loop:
            current.next = h
            h.next = node
            loop = False
        #else update links after removing the three cups
        else:
            current.next = node
        move[-1].next = None
        #find the destination. between 1 and N modulo N+1 and not
        #among the three cups we have removed.
        dest_label = current.data - 1
        if dest_label == 0: dest_label = (dest_label - 1) % (clist.max+1)
        move_labels = [n.data for n in move]
        while dest_label in move_labels:
            dest_label = (dest_label - 1) % (clist.max+1)
            if dest_label == 0: dest_label = (dest_label - 1) % (clist.max+1)
        destination = cups.get_node(dest_label)
        #Insert the three removed cups after the destination
        #should also work by doing m[-1].next = destination.next
        #and destination.next = m[0] but it was giving me issues
        for m in move:
            cups.insert_after(m, destination)
            destination = m
        #move to the next selected cup. if it's the head, skip 
        current = current.next
        if current == h: 
            current = current.next

# ----- Part 1 -------
#play(clist)
#clist.traverse()
#print(clist.part1())

# ----- Part 2 -------
play(clist, part2=True)
print(clist.part2())

