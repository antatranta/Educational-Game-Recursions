"""Entry point to the game."""
import threading

from game_graphical import GameGraphical
from game_console import GameConsole

from family_tree import FamilyTree
from family_tree_node import FamilyTreeNode

if __name__ == "__main__":
    B = FamilyTreeNode("Father", FamilyTreeNode("Dad's Dad"), FamilyTreeNode("Dad's Mom"))
    F = FamilyTreeNode("Mother", FamilyTreeNode("Mom's Dad"), FamilyTreeNode("Mom's Mom"))
    D = FamilyTreeNode("Me", B, F)
    TREE = FamilyTree(D)

    threading.Thread(target=GameConsole(tree=TREE).start_game).start()
    GameGraphical(tree=TREE).start_game()