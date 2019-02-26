"""."""

import pygame
from game_console import GameConsole


class GraphicalCallStack:
    """Graphical representation of a Call Stack."""

    def __init__(self, call_stack):
        self.call_stack = call_stack

    def draw(self, screen):
        """Draw this object to screen."""
        # Useful reference for drawing circles, lines, and rectangles:
        # https://www.pygame.org/docs/ref/draw.html

        #work on getting the text to appear in diff order

        #check = GameConsole.await_command()
        x = 0;
        y = 0;

        for node in self.call_stack:
            myfont = pygame.font.SysFont('Comic Sans MS', 12)
            textsurface = myfont.render(node.name, False, (0, 0, 0))
            screen.blit(textsurface, (x, y))
            x += 12
            y += 12
