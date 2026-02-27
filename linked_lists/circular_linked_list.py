class CircularNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.length = 0
    
    def insert(self, data):
        '''this function insert to the end of circular linkef list'''
        #Time Complexity = O(n)
        #Space Complexity = O(1)
        node: CircularNode = CircularNode(data)

        if self.head == None:
            self.head = node
            node.next = self.head
            self.length += 1
        else:
            current: CircularNode = self.head
            while current.next != self.head:
                current = current.next
            current.next = node
            node.next = self.head
            self.length += 1
    
    def delete(self, data) -> bool:
        pass

    def containes(self, data) -> bool:
        '''this function check if the data exist in the circular linked list'''
        #Time Complexity = O(n)
        #Space Complexity = O(1)
        if self.head == None:
            return False
        current: CircularNode = self.head
        if current.data == data:
            current = current.next
            return True
        else:
            current = current.next
        while current != self.head:
            if current.data == data:
                return True
            else:
                pass
            current = current.next
        return False

    def __str__(self):
        '''this function for human-readable representation'''
        if self.head == None:
            return "Empty List"
        string: str = "head -> "
        current: CircularNode = self.head
        string = string + f"{current.data} -> "
        while current.next != self.head:
                current = current.next
                string = string + f"{current.data} -> "
        string = string + "head" 
        return string
