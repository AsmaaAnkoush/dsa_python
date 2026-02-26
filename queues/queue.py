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