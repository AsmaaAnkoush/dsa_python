class Node:
    def __init__(self, value):
        '''this function is constructor to the class Node'''
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        '''this function is constructor to the class Stack'''
        self.top = None
        self.length: int = 0