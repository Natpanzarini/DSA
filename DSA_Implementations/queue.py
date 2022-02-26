# queue implementation
class Queue:
    def __init__(self, args=None):
        self.list = list()

    def push(self, item):
        self.list.insert(0, item)

    def pop(self, item):
        self.list.remove(item, list.length() - 1)

    def toString(self):
        print(self.list)

def main():
    Q = Queue()

    Q.toString()

    Q.push("fuckin")

    Q.toString()

if __name__ == '__main__':
    main()
    