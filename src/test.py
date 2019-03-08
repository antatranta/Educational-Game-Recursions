import unittest

from family_tree_node import FamilyTreeNode
from family_tree import FamilyTree, TraversalStates

class TestFamilyTree(unittest.TestCase):

    def test_inorder(self):
        root = FamilyTreeNode("Father", FamilyTreeNode("Dad's Dad"), FamilyTreeNode("Dad's Mom"))
        tree = FamilyTree(root)

        expected = [TraversalStates.START,
                    TraversalStates.FATHER,
                    TraversalStates.ACTION,
                    TraversalStates.CHILD,
                    TraversalStates.ACTION,
                    TraversalStates.MOTHER,
                    TraversalStates.ACTION,
                    TraversalStates.CHILD,
                    TraversalStates.DONE]

        for i, state in enumerate(tree.inorder()):
            self.assertEqual(state, expected[i])

        root = FamilyTreeNode("Father", FamilyTreeNode("Dad's Dad"), FamilyTreeNode("Dad's Mom", FamilyTreeNode("Dad's Mom's Dad")))
        tree = FamilyTree(root)

        expected = [TraversalStates.START,
                    TraversalStates.FATHER,
                    TraversalStates.ACTION,
                    TraversalStates.CHILD,
                    TraversalStates.ACTION,
                    TraversalStates.MOTHER,
                    TraversalStates.FATHER,
                    TraversalStates.ACTION,
                    TraversalStates.CHILD,
                    TraversalStates.ACTION,
                    TraversalStates.CHILD,
                    TraversalStates.DONE]

        for i, state in enumerate(tree.inorder()):
            self.assertEqual(state, expected[i])

if __name__ == "__main__":
    unittest.main()
