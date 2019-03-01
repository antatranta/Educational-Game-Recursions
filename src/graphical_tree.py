"""GraphicalTree representation of a FamilyTree."""
import pygame
import pygame.gfxdraw

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

NODE_COLOR = (124, 252, 0)
SELECTED_COLOR = (34, 139, 34)

NODE_SIZE = 40

TREE_WIDTH = 0.7
TREE_HEIGHT = 0.8


class GraphicalTree:
    """Graphical representation of a FamilyTree."""
    # pylint: disable=c-extension-no-member

    def __init__(self, tree):
        self.tree = tree
        self.font = pygame.font.SysFont('Comic Sans MS', 12)

    def draw(self, screen):
        """Draw this object to screen."""
        x_pos = int((2 - TREE_WIDTH) * screen.get_width() / 2)
        y_pos = int(screen.get_height() - NODE_SIZE * 1.5)
        self._draw_node(screen, 0, self.tree.root, x_pos, y_pos)
        my_font = pygame.font.SysFont('Comic Sans MS', 20)
        text_surface_1 = my_font.render(f"recursion level: {self.tree.depth}", False, (0, 0, 0))
        #screen.blit(textsurface1, (500, 450))
        screen.blit(text_surface_1, (int(screen.get_width() * .79), int(screen.get_height() * .94)))



    def _draw_caption(self, screen, caption, font_color, x, y):
        # pylint: disable=invalid-name,too-many-arguments
        width, height = self.font.size(caption)
        text_surface = self.font.render(caption, False, font_color)
        screen.blit(text_surface, (x - int(width / 2), int(y - height / 2)))

    def _draw_node(self, screen, depth_count, node, x, y):
        # pylint: disable=invalid-name,too-many-arguments
        node_color = NODE_COLOR
        text_color = BLACK

        if node is self.tree.head:
            node_color = SELECTED_COLOR
            text_color = WHITE

        x_spread = int(TREE_WIDTH * (screen.get_width() / 2) / 2 ** (depth_count + 1))
        y_spread = int(TREE_HEIGHT * (screen.get_height()) / (self.tree.max_depth - depth_count))

        if node.father:
            pygame.draw.line(screen, BLACK, (x, y), (x - x_spread, y - y_spread), 2)
            self._draw_node(screen, depth_count + 1, node.father, x - x_spread, y - y_spread)

        if node.mother:
            pygame.draw.line(screen, BLACK, (x, y), (x + x_spread, y - y_spread), 2)
            self._draw_node(screen, depth_count + 1, node.mother, x + x_spread, y - y_spread)

        pygame.gfxdraw.aacircle(screen, x, y, NODE_SIZE, node_color)
        pygame.gfxdraw.filled_circle(screen, x, y, NODE_SIZE, node_color)
        self._draw_caption(screen, node.name, text_color, x, y)
