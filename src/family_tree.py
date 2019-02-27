"""Family Tree Class."""

import enum
from abc import ABC

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
    def max_depth(self):
        """Maximum depth of this tree."""
        return self._recursive_max_depth(self.root)

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

    def inorder(self, *args, **kwargs):
        """Get an generator that will traverse the tree in-order."""
        return InOrderTraverser(self, *args, **kwargs)

    def preorder(self, *args, **kwargs):
        """Get an generator that will traverse the tree pre-order."""
        return PreOrderTraverser(self, *args, **kwargs)

    def postorder(self, *args, **kwargs):
        """Get an generator that will traverse the tree post-order."""
        return PostOrderTraverser(self, *args, **kwargs)


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

    def _recursive_max_depth(self, node):
        if not node:
            return 0
        father = self._recursive_max_depth(node.father)
        mother = self._recursive_max_depth(node.mother)
        return 1 + max(father, mother)

    def _recursive_size(self, node):
        if node is None:
            return 0
        return 1 + self._recursive_size(node.father) + self._recursive_size(node.mother)

    def __str__(self):
        return f"Family Tree, root: '{self.root}'"

class TraversalStates(enum.Enum):
    """Enum to track FamilyTreeTraverser State."""
    START = enum.auto()
    FATHER = enum.auto()
    MOTHER = enum.auto()
    CHILD = enum.auto()
    ACTION = enum.auto()
    DONE = enum.auto()

class FamilyTreeTraverser(ABC):
    """Class to help traverse a FamilyTree."""

    states = TraversalStates

    def __init__(self, tree, include=None, exclude=None):
        """
        Initialize a FamilyTreeTraverser.

        :param tree:    The tree to traverse.
                        Note: This traverser will update the tree.
        :param include: List of TraversalStates to include.
                        If None, include all states.
        :param exclude: List of TraversalStates to skip.
        """
        self.tree = tree
        self.include = include
        self.exclude = exclude
        self.history = []
        self._iter = iter(self._init_iter())

    @property
    def state(self):
        """Get the current state of the Traversal"""
        return self.history[-1]

    def __iter__(self):
        return self._iter

    def __next__(self):
        return next(self._iter)

    def _include_state(self, state):
        if self.exclude is not None and state in self.exclude:
            return False

        if self.include is None:
            return True

        if state not in self.include:
            return False

        return True

    def _init_iter(self):
        self.history.append(self.states.START)
        yield self.states.START

        for state in self._traverse(self.tree.head):
            if self._include_state(state):
                self.history.append(state)
                yield state

        self.history.append(self.states.DONE)
        yield self.states.DONE

    def _traverse(self, node):
        raise NotImplementedError

    def _traverse_parent(self, parent, state, go_to_parent):
        """
        Process the recursive function on a parent node.

        :param parent:       Parent node to traverse to (eg. node.father).
        :param state:        State to switch to when processing (eg. self.states.FATHER).
        :param go_to_parent: Method to call to move to parent (eg. node.go_to_father).
        """
        # process parent
        go_to_parent()
        yield state
        yield from self._traverse(parent)

        # return to child after processing parent
        self.tree.go_to_child()
        yield self.states.CHILD

class InOrderTraverser(FamilyTreeTraverser):
    """Class to help traverse a FamilyTree In-Order."""

    def _traverse(self, node):
        if node.father:
            yield from self._traverse_parent(node.father, self.states.FATHER,
                                             self.tree.go_to_father)

        yield self.states.ACTION

        if node.mother:
            yield from self._traverse_parent(node.mother, self.states.MOTHER,
                                             self.tree.go_to_mother)

class PreOrderTraverser(FamilyTreeTraverser):
    """Class to help traverse a FamilyTree Pre-Order"""

    def _traverse(self, node):
        if node:
            yield self.states.ACTION

        if node.father:
            yield from self._traverse_parent(node.father, self.states.FATHER,
                                             self.tree.go_to_father)

        if node.mother:
            yield from self._traverse_parent(node.mother, self.states.MOTHER,
                                             self.tree.go_to_mother)

class PostOrderTraverser(FamilyTreeTraverser):
    """Class to help traverse a FamilyTree Post-Order"""

    def _traverse(self, node):
        if node.father:
            yield from self._traverse_parent(node.father, self.states.FATHER,
                                             self.tree.go_to_father)

        if node.mother:
            yield from self._traverse_parent(node.mother, self.states.MOTHER,
                                             self.tree.go_to_mother)

        if node:
            yield self.states.ACTION
