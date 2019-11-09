# 2.1 Remove Dups! Write code to remove duplicates from an unsorted linked list.
from Data_Structures.linked_list import LinkedList


def remove_duplicate_fast(ll: LinkedList):
    # fast implementation but additional spacing required for dict
    nodes = {}
    node = ll.head
    while node is not None:
        if node.val not in nodes:
            nodes[node.val] = 1
        else:
            if node.next is not None:
                next_node = node.next
                node = node.prev
                node.next = next_node
                next_node.prev = node
            else:
                node = node.prev
                node.next = None
        node = node.next

# FOLLOW UP
# How would you solve this problem if a temporary buffer is not allowed?
def remove_duplicate_constant_space(ll:LinkedList):
    node = ll.head
    while node is not None:
        next_node = node.next
        while next_node is not None:
            if next_node.val == node.val:
                if next_node.next is not None:
                    prev_node = next_node.prev
                    next_next_node = next_node.next
                    prev_node.next = next_next_node
                    next_next_node.prev = prev_node
                else:
                    prev_node = next_node.prev
                    prev_node.next = None
            next_node = next_node.next
        node = node.next

if __name__ == "__main__":
    x = LinkedList()
    x.add(1)
    x.add(3)
    x.add(8)
    x.add(3)
    x.add(5)
    x.traverse_linked_list()
    print("==="*5)
    remove_duplicate_constant_space(x)
    x.traverse_linked_list()
