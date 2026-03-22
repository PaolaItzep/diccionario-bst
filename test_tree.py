import unittest
from binary_tree import BinaryTree
from association import Association


class TestBinaryTree(unittest.TestCase):

    def setUp(self):
        # Se ejecuta antes de cada test
        self.tree = BinaryTree()
        self.tree.insert(Association("dog", "perro"))
        self.tree.insert(Association("cat", "gato"))
        self.tree.insert(Association("bird", "pájaro"))

    def test_insert_and_search(self):
        result = self.tree.search("dog")
        self.assertIsNotNone(result)
        self.assertEqual(result.value, "perro")

    def test_search_not_found(self):
        result = self.tree.search("elephant")
        self.assertIsNone(result)

    def test_multiple_insert(self):
        result = self.tree.search("cat")
        self.assertEqual(result.value, "gato")

    def test_case_insensitive(self):
        result = self.tree.search("DOG")
        self.assertEqual(result.value, "perro")

    def test_insert_order(self):
        # Verifica que el árbol ordena correctamente (inorder)
        # No comparamos print, solo verificamos que existan los nodos
        self.assertEqual(self.tree.search("bird").value, "pájaro")
        self.assertEqual(self.tree.search("cat").value, "gato")
        self.assertEqual(self.tree.search("dog").value, "perro")


if __name__ == "__main__":
    unittest.main()