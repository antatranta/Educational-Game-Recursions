import sys
import os
import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
FPS = 60
BACKGROUND_COLOR = (155, 155, 155)

# Moves into GUI and Console Game
class MainMenu:

    def __init__(self):
        self.font = pygame.font.SysFont('Comic Sans MS', 12)

    def draw(self, screen):
        pygame.init()
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

        self._draw_button(screen)

        '''
        while 1:
            self._handle_events()

            # Clear screen
            screen.fill(BACKGROUND_COLOR)

            pygame.display.flip()
            self.fps.tick(FPS)'''


    def _draw_button(self, screen):
        pygame.draw.rect(screen, BLACK, [150, 10, 50, 20])


    def _draw_words(self, screen, caption, font_color, x, y):
        width, height = self.font.size(caption)
        text_surface = self.font.render(caption, False, font_color)
        screen.blit(text_surface, (x - int(width / 2), int(y - height / 2)))

    @classmethod
    def _handle_events(cls):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                # blocker: need quit rectangle positions

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    pass

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()  # exit program when closing the window
