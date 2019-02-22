"""."""

import pygame

class GraphicalTree:
    """Graphical representation of a FamilyTree."""

    def __init__(self, tree):
        self.tree = tree

    def draw(self, screen):
        """Draw this object to screen."""
        # Useful reference for drawing cirlcles, lines, and rectangles:
        # https://www.pygame.org/docs/ref/draw.html
