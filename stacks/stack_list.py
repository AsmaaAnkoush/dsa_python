class Stack:
    def __init__(self):
        '''this function is constructor to the class Stack'''
        self.elements = []
        self.length = 0
    
    def push(self, data):
        '''this function append data to the stack list'''
        #Time Complexity is O(1), o(n) if list resized
        #Space complexity is o(1),, o(n) if list resized
        self.elements.append(data)
        self.length += 1