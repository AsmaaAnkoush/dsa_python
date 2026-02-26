class Stack:
    def __init__(self):
        '''this function is constructor to the class Stack'''
        self.elements = []
        self.length = 0
    
    def push(self, data):
        '''this function append data to the end stack list'''
        #Time Complexity is O(1), o(n) if list resized
        #Space complexity is o(1),, o(n) if list resized
        self.elements.append(data)
        self.length += 1

    def pop(self):
        '''this function return and delete the last element in stack'''
        #Time Complexity is O(1).
        #Space complexity is o(1).
        if self.elements == []:
            raise IndexError ("The Stack is Empty")
        else:
            poped_element = self.elements[-1]
            self.elements.remove(self.elements[-1])
            self.length -= 1
            return poped_element