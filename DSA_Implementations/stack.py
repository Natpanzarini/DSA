# Stack implementation
class Stack:
    def __init__(self, args=None):
        self.list = list()

    def push(self, item):
        self.list.insert(0, item)

    def pop(self):
        if self.list is not None:

            item = self.list[0]
            
            #This searches self.list by index, which is what we want.
            del self.list[0]

            return item   

    def toString(self):
        print(self.list)

def main():
    Q = Stack()

    Q.toString()

    Q.push("party")
    Q.toString()
    
    Q.push("fuckin")
    Q.toString()

    Q.pop()
    Q.toString()

if __name__ == '__main__':
    main()
    