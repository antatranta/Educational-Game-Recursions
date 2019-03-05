"""Graphical representation of a Traversal."""

from .drawable import Drawable

class GraphicalTraverser(Drawable):
    """Graphical representation of a traverser."""

    def __init__(self, traverser):
        super().__init__()
        self.traverser = traverser
        self.states = traverser.states
        self.font = self._load_font("OxygenMono-Regular.ttf", 10)

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

        if self.traverser.done:
            history += "\nPress any key to continue..."

        text = (f"Function:\n"
                f"---------\n"
                f"{self.traverser.pseudo}\n"
                f"\n"
                f"History:\n"
                f"--------\n"
                f"{history}")


        self._draw_text(screen, text, (10, 10))
