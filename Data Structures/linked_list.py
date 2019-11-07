
"""
class Node(object):

    def __init__(self, val):
        self.val = val
        self.next = None

    def print_data(self):
        node = self # start from the memory location of the head node)
        # check to make sure the current node not is not null
        while node is not None:
            print(node.val) # print value
            node = node.next # next node becomes current node (jump to the next memory location)
x = Node(5)
y = Node(10)
z = Node(20)

x.next = y  # 5 -> 9
y.next = z  # 10 -> 20

# x -> y  -> z
# 5 -> 10 -> 20

print(x.print_data())"""
# ***********************************************************************************


class Node(object):
    """
    An object containing a value to be stored. Object contains attributes pointing to the memory location of other nodes
    """
    def __init__(self, val=None):
        self.val = val
        self.next = None
        self.prev = None


class LinkedList:
    """
    An object used to organize a collection of nodes and their respective pointers (connections) to other nodes
    """
    def __init__(self):
        # start with an empty list of size 0
        self.head = None
        self.size = 0

    def traverse_linked_list(self):
        assert self.size is not 0
        node = self.head
        while node is not None:
            print(node.val)
            node = node.next

    def add(self, val):
        if self.size is 0:
            # if size is 0 (meaning list is empty), then the first node to be added is the head node
            self.head = Node(val)
            # increase size by one after successfully adding the node
            self.size += 1
        else:
            # start from head and iterate through nodes until you find a node not connected to another node \
            # (the last node in the list)
            node = self.head
            while node.next is not None:
                node = node.next

            # create the new node and make with the connections last discovered
            new_node = Node(val)
            node.next = new_node
            new_node.prev = node
            # increase size by one after successfully adding a new node
            self.size += 1

    def remove(self):
        assert self.size is not 0
        node = self.head
        while node.next is not None:
            node = node.next
        # to delete, go one step back to the previous node,
        prev_node = node.prev
        # cut the connection the previous node has with the node to be deleted, doing so deletes the node
        prev_node.next = None
        self.size -= 1




if __name__ == "__main__":
    x = LinkedList()
    x.add(10)
    x.add(999)
    x.add(632)
    x.traverse_linked_list()
    print(f"Length of list is {x.size}\n")
    x.remove()
    print(f"After removal, length of list is {x.size}")
    x.traverse_linked_list()