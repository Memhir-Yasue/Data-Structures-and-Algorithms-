class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def _add_pre_order_traversal(root):
    while root.left is not None:
        root = root.left
    return root


class BinaryTree:
    def __init__(self):
        self.root = None

    def add(self, data):
        if self.root is None:
            self.root = Node(data)
            return 0
        else:
            blank_root = _add_pre_order_traversal(self.root)
            blank_root.left = Node(data)

    def print_pre_order_traversal(self):
        root = self.root
        while root is not None:
            print(root.data)
            root = root.left

if __name__ == "__main__":
    x = BinaryTree()
    x.add(1)
    x.add(8932)
    x.add(200)
    x.add(578)
    x.print_pre_order_travsersal()

