CHAPTER = 2

class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return 'Node ['+str(self.value)+']'

class First:
    pass

class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None
        self.nodes = []

    def __str__(self):
        if self.first is not None:
            current = self.first
            out = 'LinkedList [\n' +str(current.value) +'\n'
            while current.next is not None:
                current = current.next
                out += str(current.value) + '\n'
            return out + ']'
        return 'LinkedList []'

    def append(self, x):
        if self.first is None:
            self.first = Node(x, None)
            self.last = self.first
        elif self.last == self.first:
            self.last = Node(x, None)
            self.first.next = self.last
        else:
            current = Node(x, None)
            self.last.next = current
            self.last = current

    def list(self, start=First):
        if start == First:
            start = self.first

        if start is None:
            return []
        else:
            return [start] + self.list(start.next)

    def clear(self):
        self.__init__()
