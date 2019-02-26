"""GraphicalTree representation of a FamilyTree."""
import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

NODE_COLOR = (124, 252, 0)
SELECTED_COLOR = (34, 139, 34)

NODE_SIZE = 30

class GraphicalTree:
    """Graphical representation of a FamilyTree."""

    def __init__(self, tree):
        self.tree = tree
        self.font = pygame.font.SysFont('Comic Sans MS', 12)

    def draw(self, screen):
        """Draw this object to screen."""
        x_pos = int(screen.get_width() / 2)
        y_pos = int(screen.get_height() - NODE_SIZE)
        self._draw_node(screen, 0, self.tree.root, x_pos, y_pos)

    def _drawcaption(self, screen, caption, font_color, x, y):
        # pylint: disable=invalid-name,too-many-arguments
        width, height = self.font.size(caption)
        textsurface = self.font.render(caption, False, font_color)
        screen.blit(textsurface, (x - int(width / 2), int(y - height / 2)))

    def _draw_node(self, screen, depth_count, node, x, y):
        # pylint: disable=invalid-name,too-many-arguments
        node_color = NODE_COLOR
        text_color = BLACK

        if node is self.tree.head:
            node_color = SELECTED_COLOR
            text_color = WHITE

        x_spread = int((screen.get_width() / 2) / 2 ** (depth_count + 1))
        y_spread = NODE_SIZE * 4

        if node.father:
            pygame.draw.line(screen, BLACK, (x, y), (x - x_spread, y - y_spread))
            self._draw_node(screen, depth_count + 1, node.father, x - x_spread, y - y_spread)

        if node.mother:
            pygame.draw.line(screen, BLACK, (x, y), (x + x_spread, y - y_spread))
            self._draw_node(screen, depth_count + 1, node.mother, x + x_spread, y - y_spread)

        pygame.draw.circle(screen, node_color, (x, y), NODE_SIZE)
        self._drawcaption(screen, node.name, text_color, x, y)
