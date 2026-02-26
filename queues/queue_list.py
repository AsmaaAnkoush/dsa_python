class Queue:
    def __init__(self):
        '''this function is constructor to the class Queue'''
        self.elements = []
        self.length = 0

    def enqueue(self, data):
        '''this function add data to the end of queue'''
        #Time Complexity is O(1), o(n) if list resized
        #Space complexity is o(1), o(n) if list resized
        self.elements.append(data)
        self.length += 1
    
    def dequeue(self):
        '''this function removes from the front of queue'''
        #Time Complexity O(1)
        #Space complexity O(1)
        if self.elements == []:
            raise IndexError ("The Stack is Empty")
        else:
            self.elements.pop(0)
            self.length -= 1
    
    def front(self):
        '''this function returnes the element in the head of queue'''
        #Time Complexity O(1)
        #Space complexity O(1)
        if self.length == 0:
            raise IndexError ("The Queue is Empty")
        return self.elements[0]