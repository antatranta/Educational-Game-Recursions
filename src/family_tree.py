"""Family Tree Class."""

from family_tree_node import FamilyTreeNode

class FamilyTree():
    """Represents a single FamilyTree."""

    def __init__(self, root=None):
        """
        :param root: The root FamilyTreeNode of the tree.
        """
        self.root = FamilyTreeNode(root) or FamilyTreeNode('ME')
        self.call_stack = [self.root]

    @property
    def head(self):
        """Current Family Tree head."""
        return self.call_stack[-1]

    @property
    def whole_family_tree(self):
        """Returns the family tree"""
        return self.call_stack

    def go_to_mother(self):
        """Move the `head` pointer to the current `head` mother."""
        self.call_stack.append(self.head.mother)

    def go_to_father(self):
        """Move the `head` pointer to the current `head` father."""
        self.call_stack.append(self.head.father)

    def go_to_child(self):
        """Move the `head` pointer to the current `head` child."""
        self.call_stack.pop()

    def __str__(self):
        return f"Family Tree, root: '{self.root}'"
