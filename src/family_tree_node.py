"""Family Tree Node"""

class FamilyTreeNode:
    """Family Tree Node"""
    # pylint: disable=too-few-public-methods

    def __init__(self, name, father=None, mother=None):
        self.name = name
        self.father = father
        self.mother = mother

    def __str__(self):
        return str(self.name)
