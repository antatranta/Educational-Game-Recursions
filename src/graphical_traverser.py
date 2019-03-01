"""Graphical representation of a Traversal."""

import pygame

class GraphicalTraverser:
    """Graphical representation of a traverser."""

    def __init__(self, traverser):
        self.traverser = traverser
        self.states = traverser.states
        self.font = pygame.font.SysFont('Consolas', 12)

    def _draw_text(self, screen, text, pos, color=(0, 0, 0), *, split_char='\n', background=None):
        # pylint: disable=invalid-name
        x, y = pos

        for line in text.split(split_char):
            surface = self.font.render(line, True, color, background)
            screen.blit(surface, (x, y))

            _, height = self.font.size(line)
            y += int(height)

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
