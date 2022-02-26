# queue implementation
class Queue:
    def __init__(self, args=None):
        self.list = list()

    def push(self, item):
        self.list.insert(0, item)

    def pop(self):
        if self.list is not None:
            # This does not work because this searches for len(self.list) - 1 by value instead of by INDEX.
            #self.list.remove(len(self.list - 1))

            #This searches self.list by index, which is what we want.
            del self.list[len(self.list) - 1]    

    def toString(self):
        print(self.list)

def main():
    Q = Queue()

    Q.toString()

    Q.push("party")
    Q.toString()
    
    Q.push("fuckin")
    Q.toString()

    Q.pop()
    Q.toString()

if __name__ == '__main__':
    main()
    