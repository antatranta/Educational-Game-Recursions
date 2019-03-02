import sys
import time
import os
import pygame
import pygame.locals

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LGREEN = (124,252,0)
MGREEN = (50,205,50)
DGREEN = (34,139,34)
GGREEN = (0,255,127)

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
BACKGROUND_COLOR = (155, 155, 155)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#Create captions for Play, options, quit
caption1 = "Start Game"
caption2 = "Options"
caption3 = "Quit Game"

#Clock
windowclock = pygame.time.Clock()

#Add highlight and try to add array of rectangles

class MainMenu:

    def text_objects(self, text, font):
        self.text_surface = font.render(text, True, BLACK)
        return self.text_surface, self.text_surface.get_rect()

    def message_display(self, text):
        largeText = pygame.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRect = self.text_objects(text, largeText)
        TextRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
        screen.blit(TextSurf, TextRect)
        pygame.display.update()

    def draw(self, screen):

        background_img = pygame.image.load("background2.png")
        #self._draw_words(screen, caption1, BLACK)

        stopped = False

        while stopped == False:
            #screen.fill(BACKGROUND_COLOR)  # Tuple for filling display... Current is white
            screen.blit(background_img, [0, 0])

            # Event Tasking
            # Add all your event tasking things here
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            screen.fill(WHITE)

            largeText = pygame.font.Font('freesansbold.ttf', 85)
            TextSurf, TextRect = self.text_objects("Tree Traversal", largeText)
            TextRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
            screen.blit(TextSurf, TextRect)

            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()

            if 140 + 100 > mouse[0] > 140 and 400 + 50 > mouse[1] > 400:
                self._draw_button(screen, GGREEN, (140, 400, 100, 50))
                print(click)
            else:
                self._draw_button(screen, DGREEN, (140, 400, 100, 50))
            if 270 + 100 > mouse[0] > 270 and 400 + 50 > mouse[1] > 400:
                self._draw_button(screen, GGREEN, (270, 400, 100, 50))
                print(click)
            else:
                self._draw_button(screen, MGREEN, (270, 400, 100, 50))
            if 400 + 100 > mouse[0] > 400 and 400 + 50 > mouse[1] > 400:
                self._draw_button(screen, GGREEN, (400, 400, 100, 50))
                if(click[0] == 1):
                    quit()
            else:
                self._draw_button(screen, LGREEN, (400, 400, 100, 50))

            self._draw_words(screen, caption1, BLACK, 140 + 100 / 2, 400 + 50 / 2)
            self._draw_words(screen, caption2, BLACK, 270 + 100 / 2, 400 + 50 / 2)
            self._draw_words(screen, caption3, BLACK, 400 + 100 / 2, 400 + 50 / 2)

            pygame.display.update()
            windowclock.tick(60)

    #Draw button
    def _draw_button(self, screen, font_color, position):
        pygame.draw.rect(screen, font_color, position)

    def _draw_words(self, screen, caption, font_color, x, y):
        smallText = pygame.font.Font("freesansbold.ttf", 14)
        textSurf, textRect = self.text_objects(caption, smallText)
        textRect.center = (x, y)
        screen.blit(textSurf, textRect)

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

if __name__ == "__main__":
    mm = MainMenu()
    mm.draw(screen)


