"""Game class that displays the game Graphically."""
# pylint: disable=no-member
import sys

import pygame
import pygame.locals

from graphical_tree import GraphicalTree
from graphical_call_stack import GraphicalCallStack

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
FPS = 60
BACKGROUND_COLOR = (155, 155, 155)

class GameGraphical:
    """Class to help in starting a new Graphical Game."""

    def __init__(self, tree):
        self.fps = pygame.time.Clock()
        self.tree = tree

    def start_game(self):
        """Start a Graphical Game."""
        pygame.init()
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

        graphical_tree = GraphicalTree(self.tree)
        call_stack = GraphicalCallStack(self.tree.call_stack, self.tree)

        while 1:
            self._handle_events()

            # Clear screen
            screen.fill(BACKGROUND_COLOR)

            # Render objects to screen
            graphical_tree.draw(screen)
            call_stack.draw(screen)

            # Redraw screen
            pygame.display.flip()
            self.fps.tick(FPS)

    @classmethod
    def _handle_events(cls):
        for event in pygame.event.get():
            if event.type is pygame.locals.QUIT:
                sys.exit() # exit program when closing the window
