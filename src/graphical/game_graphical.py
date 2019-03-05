"""Game class that displays the game Graphically."""
# pylint: disable=no-member
import sys
import threading

import pygame
import pygame.locals

from game_questions import GameQuestions
from .graphical_tree import GraphicalTree
from .graphical_traverser import GraphicalTraverser
from .drawable import Drawable

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
FPS = 60
TRAVERSER_TIMER = 1
BACKGROUND_COLOR = (155, 155, 155)


class GameGraphical:
    """Class to help in starting a new Graphical Game."""

    def __init__(self, tree):
        self.fps = pygame.time.Clock()
        self.tree = tree
        self._traverser = None
        self.traversal_frame_time = 1000
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
        available_actions = AvailableActions()

        while True:
            if self.end_game:
                self.quit()

            self._handle_events()

            # Clear screen
            screen.fill(BACKGROUND_COLOR)

            # Render objects to screen
            graphical_tree.draw(screen)
            available_actions.draw(screen)
            self._draw_traverser(screen)

            # Redraw screen
            pygame.display.flip()
            self.fps.tick(FPS)

    @classmethod
    def quit(cls):
        """Exit the graphical game."""
        pygame.quit()
        sys.exit()

    def _draw_traverser(self, screen):
        if self._traverser:
            try:
                self._traverser.draw(screen)
                next(self._traverser.traverser)
            except StopIteration:
                self.end_traversal()

            pygame.display.flip()
            pygame.time.wait(self.traversal_frame_time)

    def _on_keyup(self, event):
        # always allow quit
        if event.key is pygame.K_q:
            self.quit()

        # following keys not allowed during traversal
        if self._traverser:
            return

        # game
        if event.key is pygame.K_g:
            threading.Thread(target=GameQuestions(None).compare_answers, daemon=True).start()

        # begin traversals
        if event.key is pygame.K_1:
            self.start_traversal(self.tree.inorder())

        if event.key is pygame.K_2:
            self.start_traversal(self.tree.preorder())

        if event.key is pygame.K_3:
            self.start_traversal(self.tree.postorder())

        if event.key is pygame.K_m:
            self.tree.go_to_mother()

        if event.key is pygame.K_f:
            self.tree.go_to_father()

        if event.key is pygame.K_c:
            self.tree.go_to_child()

    def _handle_events(self):
        for event in pygame.event.get():
            if event.type is pygame.QUIT:
                self.quit()
            elif event.type is pygame.KEYUP:
                self._on_keyup(event)


class AvailableActions(Drawable):
    """Class to show available actions in GUI window"""
    def draw(self, screen):
        available_actions = ('M - Go to Mother\n' 
                             'F - Go to Father\n' 
                             'C - Go to Child\n'
                             '1 - In-Order Traversal\n'
                             '2 - Pre-Order Traversal\n' 
                             '3 - Post-Order Traversal\n' 
                             'G - Play Recursion Game\n'
                             'Q - Quit Game')
        self._draw_text(screen, available_actions, (10, 10))

