"""."""

import pygame

class GraphicalCallStack:
    """Graphical representation of a Call Stack."""

    def __init__(self, call_stack):
        self.call_stack = call_stack

    def draw(self, screen):
        """Draw this object to screen."""
        # Useful reference for drawing cirlcles, lines, and rectangles:
        # https://www.pygame.org/docs/ref/draw.html
