"""Game class that displays the game Graphically."""

import pygame
import pygame.locals

from family_tree import FamilyTree
from family_tree_node import FamilyTreeNode

from graphical_tree import GraphicalTree
from graphical_call_stack import GraphicalCallStack

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
FPS = 60
BACKGROUND_COLOR = (155, 155, 155)

class GameGraphical:
    """Class to help in starting a new Graphical Game."""

    def __init__(self):
        self.fps = pygame.time.Clock()

    def start_game(self):
        """Start a Graphical Game."""
        pygame.init()
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

        tree = self._initialize_tree()
        graphical_tree = GraphicalTree(tree)
        call_stack = GraphicalCallStack(tree.call_stack)

        while 1:
            for event in pygame.event.get():
                if event.type is pygame.locals.QUIT:
                    return # exit program when closing the window

            # Render objects to screen
            screen.fill(BACKGROUND_COLOR)

            graphical_tree.draw(screen)
            call_stack.draw(screen)

            pygame.display.flip()
            self.fps.tick(FPS)

    @classmethod
    def _initialize_tree(cls):
        father = FamilyTreeNode("Father",
                                FamilyTreeNode("Paternal Grandfather"),
                                FamilyTreeNode("Paternal Grandmother"))

        mother = FamilyTreeNode("Mother",
                                FamilyTreeNode("Maternal Grandfather"),
                                FamilyTreeNode("Maternal Grandmother"))

        player = FamilyTreeNode("Me", father, mother)
        return FamilyTree(player)
