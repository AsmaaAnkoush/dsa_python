class Queue:
    def __init__(self):
        '''this function is constructor to the class Queue'''
        self.elements = []
        self.length = 0

    def enqueue(self, data):
        '''this function add data to the end'''
        #Time Complexity is O(1), o(n) if list resized
        #Space complexity is o(1), o(n) if list resized
        self.elements.append(data)
        self.length += 1