"""Graphical representation of a Call Stack."""
from .drawable import Drawable

class GraphicalCallStack(Drawable):
    """Graphical representation of a Call Stack."""

    def __init__(self, call_stack, tree):
        super().__init__()
        self.call_stack = call_stack
        self.tree = tree

    def draw(self, screen):
        """Draw this object to screen."""
        # pylint: disable=invalid-name
        x = 0
        y = 0

        for node in self.call_stack:
            self._draw_text(screen, node.name, (x, y))
            x += 12
            y += 12
