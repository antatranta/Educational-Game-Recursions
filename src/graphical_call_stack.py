"""Graphical representation of a Call Stack."""
import pygame

class GraphicalCallStack:
    """Graphical representation of a Call Stack."""

    def __init__(self, call_stack, tree):
        self.call_stack = call_stack
        self.tree = tree

    def draw(self, screen):
        """Draw this object to screen."""
        # pylint: disable=invalid-name
        x = 0
        y = 0

        for node in self.call_stack:
            myfont = pygame.font.SysFont('Comic Sans MS', 20)
            textsurface = myfont.render(node.name, False, (0, 0, 0))
            screen.blit(textsurface, (x, y))
            x += 12
            y += 12

