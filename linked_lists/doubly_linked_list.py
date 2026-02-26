class DoublyNode:
    def __init__(self, value):
        '''this function is constructor to the class Node'''
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        '''this function is constructor to the class Double Linked List'''
        self.head = None
        self.tail = None
        self.length = 0
    
    def insert_at_head(self,data):
        '''this function add the value to the begning of double linked list'''
        #Time complexity = O(1)
        #Space complexity = O(1)
        node: DoublyNode = DoublyNode(data)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        self.length += 1