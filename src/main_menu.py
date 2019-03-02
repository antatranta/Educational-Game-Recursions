""" Main menu class meant as a main menu GUI that transitions to the actual main game """
# pylint: disable=no-member
import os
import pygame
import sys

from game_console import GameConsole
from graphical.drawable import Drawable

BLACK = (0, 0, 0)
LGREEN = (124, 252, 0)
MGREEN = (50, 205, 50)
DGREEN = (34, 139, 34)
GGREEN = (0, 255, 127)

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
BACKGROUND_COLOR = (155, 155, 155)


# Moves into GUI and Console Game
class MainMenu(Drawable):

    def __init__(self):
        pygame.init()
        self.menu_options = ["Play", "Options", "Quit"]
        self.iterator = 0
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    def _draw_highlighted_buttons(self):
        mouse = pygame.mouse.get_pos()

        # Iterating so that it highlights last mouse hover over
        # also so that when user use keyboard it also highlights
        if 140 + 100 > mouse[0] > 140 and 400 + 50 > mouse[1] > 400\
                or self.menu_options[self.iterator] == "Play":
            self._draw_button(GGREEN, (140, 400, 100, 50))
            self.iterator = 0
        else:
            self._draw_button(DGREEN, (140, 400, 100, 50))
        if 270 + 100 > mouse[0] > 270 and 400 + 50 > mouse[1] > 400\
                or self.menu_options[self.iterator] == "Options":
            self._draw_button(GGREEN, (270, 400, 100, 50))
            self.iterator = 1
        else:
            self._draw_button(MGREEN, (270, 400, 100, 50))
        if 400 + 100 > mouse[0] > 400 and 400 + 50 > mouse[1] > 400\
                or self.menu_options[self.iterator] == "Quit":
            self._draw_button(GGREEN, (400, 400, 100, 50))
            self.iterator = 2
        else:
            self._draw_button(LGREEN, (400, 400, 100, 50))

    def _draw_button(self, fill_color, position):
        """ PARAMETERS:
        fill_color: the color fill of the rectangle
        position: the x and y coordinates for placing on the screen
        """
        pygame.draw.rect(self.screen, fill_color, position)

    def _draw_words(self, caption, x, y):
        """ PARAMETERS:
        caption: the text to be blitted to the screen
        x: the x coordinate of the placement of the text
        y: the y coordinate of the placement of the text
        """
        small_text = self._load_font("VarelaRound-Regular.ttf", 20)
        text_surf, text_rect = self.text_objects(caption, small_text)
        text_rect.center = (x, y)
        self.screen.blit(text_surf, text_rect)

    def _handle_events(self):
        for event in pygame.event.get():
            # Handles main menu navigation with the mouse
            if event.type == pygame.MOUSEBUTTONUP:
                mouse_pos = pygame.mouse.get_pos()

                if 140 + 100 > mouse_pos[0] > 140 and 400 + 50 > mouse_pos[1] > 400:
                    GameConsole().start_game()
                if 270 + 100 > mouse_pos[0] > 270 and 400 + 50 > mouse_pos[1] > 400:
                    pass
                if 400 + 100 > mouse_pos[0] > 400 and 400 + 50 > mouse_pos[1] > 400:
                    quit()

            # Handles main menu navigation of going up and down
            # if the player is already at Play can't go further up
            # if the player is already at Quit can't go further down
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if self.iterator > 0:
                        self.iterator -= 1
                elif event.key == pygame.K_RIGHT:
                    if self.iterator < 2:
                        self.iterator += 1
                elif event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                    if self.menu_options[self.iterator] == "Play":
                        GameConsole().start_game()
                    elif self.menu_options[self.iterator] == "Options":
                        pass
                    elif self.menu_options[self.iterator] == "Quit":
                        pygame.quit()
                        sys.exit()

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()  # exit program when closing the window

    @staticmethod
    def text_objects(text, font):
        text_surface = font.render(text, True, BLACK)
        return text_surface, text_surface.get_rect()

    def draw(self):
        background_img = pygame.image.load(os.path.join(".", "src", "graphical", "background2.png"))
        self.screen.blit(background_img, [0, 0])

        title_text = "Family Tree: A Real Life Recursive Example"
        large_text = self._load_font('VarelaRound-Regular.ttf', 30)
        text_surf, text_rect = self.text_objects(title_text, large_text)
        text_rect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 4))
        self.screen.blit(text_surf, text_rect)

        # Clock
        window_clock = pygame.time.Clock()

        stopped = False

        while not stopped:
            # Event Tasking
            # Add all your event tasking things here
            self._handle_events()

            self._draw_highlighted_buttons()

            self._draw_words(self.menu_options[0], 140 + 100 / 2, 400 + 50 / 2)
            self._draw_words(self.menu_options[1], 270 + 100 / 2, 400 + 50 / 2)
            self._draw_words(self.menu_options[2], 400 + 100 / 2, 400 + 50 / 2)

            pygame.display.update()
            window_clock.tick(60)
