"""Family Tree Node"""

class FamilyTreeNode:
    """Family Tree Node"""

    def __init__(self, name, father=None, mother=None):
        self.name = name
        self.father = father
        self.mother = mother

    def __str__(self):
        return str(self.name)
