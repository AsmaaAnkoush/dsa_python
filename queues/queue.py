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