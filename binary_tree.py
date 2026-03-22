from node import Node

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        self.root = self._insert(self.root, value)

    def _insert(self, node, value):
        if node is None:
            return Node(value)

        if value.key < node.data.key:
            node.left = self._insert(node.left, value)
        else:
            node.right = self._insert(node.right, value)

        return node

    def search(self, key):
        return self._search(self.root, key.lower())

    def _search(self, node, key):
        if node is None:
            return None

        if key == node.data.key:
            return node.data
        elif key < node.data.key:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)

    def inorder(self):
        self._inorder(self.root)

    def _inorder(self, node):
        if node:
            self._inorder(node.left)
            print(f"({node.data.key}, {node.data.value})")
            self._inorder(node.right)