"""Graphical representation of a Traversal."""

import os
import pygame

from .drawable import Drawable

class GraphicalTraverser(Drawable):
    """Graphical representation of a traverser."""

    def __init__(self, traverser):
        super().__init__()
        self.traverser = traverser
        self.states = traverser.states

        ttf = os.path.join(".", "src", "graphical", "fonts", "OxygenMono-Regular.ttf")
        self.font = pygame.font.Font(ttf, 10)

    def draw(self, screen):
        """Draw traversal steps to screen."""
        history = ""
        indent = "|    "
        depth = 0

        for state in self.traverser.history:
            history += f"{indent * depth}{state}\n"

            if state in [self.states.START, self.states.FATHER, self.states.MOTHER]:
                depth += 1
            elif state in [self.states.CHILD, self.states.DONE]:
                depth -= 1

        text = (f"Function:\n"
                f"---------\n"
                f"{self.traverser.pseudo}\n"
                f"\n"
                f"History:\n"
                f"--------\n"
                f"{history}")

        if self.traverser.state is self.states.DONE:
            text += "\nPress enter in console to continue..."

        self._draw_text(screen, text, (10, 10))
