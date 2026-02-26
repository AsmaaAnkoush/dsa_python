class Node:
    def __init__(self, value):
        '''this function is constructor to the class Node'''
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        '''this function is constructor to the class Queue'''
        self.head = None
        self.tail = None
        self.length: int = 0

    def enqueue(self, data):
        '''this function add data to the end of queue'''
        #Time Complexity O(1)
        #Space complexity O(1)
        node: Node = Node(data)
        if self.length == 0:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.length += 1
    
    def dequeue(self):
        '''this function removes from the front of queue'''
        #Time Complexity O(1)
        #Space complexity O(1)
        if self.head == None:
            raise IndexError ("The Queue is Empty")
        else:
            self.head = self.head.next
            self.length -= 1
        if self.head is None:
            self.tail = None

    def front(self):
        '''this function returnes the element in the head of queue'''
        #Time Complexity O(1)
        #Space complexity O(1)
        if self.head == None:
            raise IndexError ("The Queue is Empty")
        return self.head.value
    
    def size(self) -> int:
        '''this function return the size of queue'''
        #Time Complexity is O(1)
        #Space complexity is o(1)
        return self.length

    def clear(self):
        '''this function remove all element in queue'''
        #Time Complexity is O(1)
        #Space complexity is o(1)
        self.head = None
        self.tail = None
        self.length = 0

