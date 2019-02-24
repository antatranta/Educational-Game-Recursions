"""."""

import pygame

# Some Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
PINK = (255, 192, 203)

running = True

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
        pos = self.mouseposition()
        pygame.draw.circle(screen, BLUE, pos, 50)
        father = pygame.draw.circle(screen, BLUE, pos, 50)
        mother = pygame.draw.circle(screen, PINK, pos, 50)
        line = pygame.draw.line(screen, BLACK, (200, 200), pos)

    def drawcaption(self, screen):
        pos = self.mouseposition()
        myfont = pygame.font.SysFont('Comic Sans MS', 12)
        textsurface = myfont.render('Child', False, (0, 0, 0))
        screen.blit(textsurface, pos)

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
