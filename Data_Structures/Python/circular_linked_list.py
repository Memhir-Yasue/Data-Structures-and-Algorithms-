class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
        self.prev = None


class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add(self, val):
        if self.size is 0:
            self.head = Node(val)
            self.tail = self.head
            self.size += 1
        else:
            new_node = Node(val)
            prev_node = self.tail
            self.tail = new_node
            prev_node.next = self.tail
            self.tail.prev = prev_node
            self.tail.next = self.head
            self.size += 1

    def remove(self):
        if self.size is 0:
            print("Can't remove empty list")
        elif self.size is 1:
            self.head = None
            self.tail = None
        else:
            prev_node = self.tail.prev
            prev_node.next = self.head
            self.tail = prev_node

        self.size -= 1

    def traverse_list(self):
        if self.size is 0: print("List is empty")
        elif self.size is 1: print(self.head.val)
        else:
            node = self.head
            while node.next is not None:
                print(node.val)
                node = node.next
                if node is self.head: return 0


if __name__ == "__main__":
    x = CircularLinkedList()
    x.add(1)
    x.add(999)
    x.add(78432)
    x.remove()
    x.remove()
    x.remove()
    x.traverse_list()
