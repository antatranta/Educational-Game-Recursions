"""Game class that displays the game Graphically."""
# pylint: disable=no-member
import sys

import pygame
import pygame.locals

from .graphical_tree import GraphicalTree
from .graphical_traverser import GraphicalTraverser

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
FPS = 60
BACKGROUND_COLOR = (155, 155, 155)


class GameGraphical:
    """Class to help in starting a new Graphical Game."""

    def __init__(self, tree):
        self.fps = pygame.time.Clock()
        self.tree = tree
        self._traverser = None
        self.end_game = False

    def start_traversal(self, traverser):
        """Display traverser graphically."""
        self._traverser = GraphicalTraverser(traverser)

    def end_traversal(self):
        """End graphical display of traversal."""
        self._traverser = None

    def start_game(self):
        """Start a Graphical Game."""
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

        graphical_tree = GraphicalTree(self.tree)

        while True:
            if self.end_game:
                self.quit()

            self._handle_events()

            # Clear screen
            screen.fill(BACKGROUND_COLOR)

            # Render objects to screen
            graphical_tree.draw(screen)
            # call_stack.draw(screen)

            if self._traverser:
                self._traverser.draw(screen)

            # Redraw screen
            pygame.display.flip()
            self.fps.tick(FPS)

    @classmethod
    def quit(cls):
        """Exit the graphical game."""
        pygame.quit()
        sys.exit()

    @classmethod
    def _handle_events(cls):
        for event in pygame.event.get():
            if event.type is pygame.QUIT:
                cls.quit()
