"""Family Tree Class."""

from family_tree_node import FamilyTreeNode


class FamilyTree:
    """Represents a single FamilyTree."""

    def __init__(self, root=None):
        """
        :param root: The root FamilyTreeNode of the tree.
        """
        self.root = root or FamilyTreeNode('ME')
        self.call_stack = [self.root]

    @property
    def head(self):
        """Current Family Tree head."""
        return self.call_stack[-1]

    @property
    def depth(self):
        """Depth of the `head` node."""
        return len(self.call_stack) - 1

    @property
    def size(self):
        """Total number of nodes in the tree."""
        return self._recursive_size(self.root)

    @property
    def tree_string(self):
        """A String representation of the Tree"""
        string = ''
        new_layer = [self.root]

        # Build a list of layers
        while not all([n is None for n in new_layer]):
            layer = new_layer
            new_layer = []

            for node in layer:
                new_layer += [None, None] if node is None else [node.father, node.mother]

                marker = "* " if node is self.head else ""
                text = f"'{node}'" if node is not None else "None"
                string += f"{marker}{text} "
            string += "\n"

        return string

    def go_to_mother(self):
        """
        Move to the current `head` mother.

        :returns: New `head` node, or None if none exists
        """
        mother = self.head.mother
        if mother:
            self.call_stack.append(mother)
        return mother

    def go_to_father(self):
        """
        Move to the current `head` father.

        :returns: New `head` node, or None if none exists
        """
        father = self.head.father
        if father:
            self.call_stack.append(father)
        return father

    def go_to_child(self):
        """
        Move the `head` pointer to the current `head` child.

        :returns: New `head` node, or None if none exists
        """
        if self.head == self.root:
            return None
        self.call_stack.pop()
        return self.head

    def _recursive_size(self, node):
        if node is None:
            return 0
        return 1 + self._recursive_size(node.father) + self._recursive_size(node.mother)

    def __str__(self):
        return f"Family Tree, root: '{self.root}'"
