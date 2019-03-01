"""Graphical representation of a Call Stack."""
import pygame


class GraphicalCallStack:
    """Graphical representation of a Call Stack."""

    def __init__(self, call_stack):
        self.call_stack = call_stack

    def draw(self, screen):
        """Draw this object to screen."""
        # pylint: disable=invalid-name
        x = 0
        y = 0

        for node in self.call_stack:
            my_font = pygame.font.SysFont('Comic Sans MS', 12)
            text_surface = my_font.render(node.name, False, (0, 0, 0))
            screen.blit(text_surface, (x, y))
            x += 12
            y += 12
