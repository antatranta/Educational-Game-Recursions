"""."""

import pygame

# Some Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

PINK = (255, 192, 203)
YELLOW = (255, 255, 0)

NODE_COLOR = (124,252,0)
SELECTED_COLOR = (34,139,34)

running = True

NODE_SIZE = 30
level_one = (320,140)

class GraphicalTree:

    """Graphical representation of a FamilyTree."""

    # Useful reference for drawing cirlcles, lines, and rectangles:
    # https://www.pygame.org/docs/ref/draw.html
    def __init__(self, tree):
        self.tree = tree

    def mouseposition(self):
        pos = pygame.mouse.get_pos()
        return pos

    def draw(self, screen):
        """Draw this object to screen."""
        '''root = pygame.draw.circle(screen, YELLOW, level_one, 50)
        father = pygame.draw.circle(screen, BLUE, level_one, 50)
        mother = pygame.draw.circle(screen, PINK, level_one, 50)
        #line = pygame.draw.line(screen, BLACK, (200, 200), pos)
        '''
        self._draw_node(screen, 0, self.tree.root, int(screen.get_width()/2), int(screen.get_height()- NODE_SIZE))

    def drawcaption(self, screen, caption, font_color, x, y):
        myfont = pygame.font.SysFont('Comic Sans MS', 12)
        width,height = myfont.size(caption)
        textsurface = myfont.render(caption, False, font_color)
        screen.blit(textsurface, (x - int(width/2), int(y - height/2)))

    def _draw_node(self, screen, depth_count, node, x, y):
        node_color = NODE_COLOR
        text_color = BLACK

        if node is self.tree.head:
            node_color = SELECTED_COLOR
            text_color = WHITE


        x_spread = int((screen.get_width()/2)/2**(depth_count + 1))
        y_spread = NODE_SIZE*2 * 2
        if node.father:
            pygame.draw.line(screen, BLACK, (x,y), (x - x_spread, y - y_spread))
            self._draw_node(screen, depth_count+1, node.father, x - x_spread, y - y_spread)

        if node.mother:
            pygame.draw.line(screen, BLACK, (x, y), (x + x_spread, y - y_spread))
            self._draw_node(screen, depth_count+1, node.mother, x + x_spread, y - y_spread)

        pygame.draw.circle(screen, node_color, (x, y), NODE_SIZE)
        self.drawcaption(screen, node.name, text_color, x, y)


    def main():
        global running
        #a = GraphicalTree()

        pygame.init()  # Initialize the display module
        (width, height) = (800, 600)
        pygame.display.set_caption("Display Tree")

        screen = pygame.display.set_mode((width, height))
        screen.fill(WHITE)

        pygame.display.update()  # Update portions of the screen for software displays

        while running:
            click = pygame.event.get()
            for event in click:
                if event.type == pygame.MOUSEBUTTONUP:
                    #a.draw()
                    #GraphicalTree.draw()
                    pos = pygame.mouse.get_pos()
                    pygame.draw.circle(screen, BLUE, pos, 50)
                    myfont = pygame.font.SysFont('Comic Sans MS', 12)
                    textsurface = myfont.render('Child', False, (0, 0, 0))
                    screen.blit(textsurface, pos)

                if event.type == pygame.QUIT:
                    running = False
            pygame.display.update()

    if __name__ == '__main__':
        main()
