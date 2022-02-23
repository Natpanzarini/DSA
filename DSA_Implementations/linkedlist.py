# Implementation for a singly linked list.
class SNode():
    def __init__(self):
        self.val = 0
        self.next = None

#Implementation for a doubly linked list
class DNode():
    def __init__(self):
        self.val = 0
        self.next = None      
        self.prev = None

class SLinkedList():
    def __init__(self):
        self.head = SNode()

class DLinkedList():
    def __init__(self):
        self.head = DNode()
        
def testList():
    # Test initialization of the head of the LL.
    list = SLinkedList()

    # Test assigning a value to the head of the list
    list.head.val = 69
    print(list.head.val)
    node2 = SNode()
    list.head.next = node2

    # Test adding another node to linked list
    print(list.head.next)

if __name__ == '__main__':
        testList()