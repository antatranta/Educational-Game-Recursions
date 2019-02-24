"""Entry point to the game."""
import threading

from game_graphical import GameGraphical
from game_console import GameConsole

from family_tree import FamilyTree
from family_tree_node import FamilyTreeNode

if __name__ == "__main__":
    B = FamilyTreeNode("B", FamilyTreeNode("A"), FamilyTreeNode("C"))
    F = FamilyTreeNode("F", FamilyTreeNode("E"), FamilyTreeNode("G"))
    D = FamilyTreeNode("D", B, F)
    TREE = FamilyTree(D)

    threading.Thread(target=GameGraphical(tree=TREE).start_game).start()
    GameConsole(tree=TREE).start_game()
