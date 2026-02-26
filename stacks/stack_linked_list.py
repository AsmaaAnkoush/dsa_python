from linked_lists.linked_list import LinkedList

class Stack:
    def __init__(self):
        '''this function is constructor to the class Stack'''
        self.elments: LinkedList = LinkedList()
    
    def push(self, data):
        '''this function append_end data to the stack linked list'''
        #Time Complexity is O(n)
        #Space complexity is o(1)
        self.elments.append_end(data)
    
    def pop(self):
        '''this function return and delete the last element in stack'''
        #Time Complexity is O(n).
        #Space complexity is o(1).
        return self.elments.remove_at(self.elments.length-1)
    
    def peek(self):
        '''this function return the top element in stack'''
        #Time Complexity is O(n)
        #Space complexity is o(1)
        element = self.elments.remove_at(self.elments.length-1)
        self.elments.append_end(element)
        return element
    
    def is_empty(self) -> bool:
        '''this function check if the stack is empty or not'''
        #Time Complexity is O(1)
        #Space complexity is o(1)
        if self.elments.length == 0:
            return True
        else:
            return False
        
    def size(self) -> int:
        '''this function return the size of stack'''
        #Time Complexity is O(1)
        #Space complexity is o(1)
        return self.elments.length
    
    def clear(self):
        '''this function remove all element in stack'''
        #Time Complexity is O(1)
        #Space complexity is o(1)
        self.elments.clear()
