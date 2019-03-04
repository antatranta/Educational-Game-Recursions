""" Main menu class meant as a main menu GUI that transitions to the actual main game """
# pylint: disable=no-member
import os
import sys
import pygame

from game_console import GameConsole
from graphical.drawable import Drawable

# Color RGB values
BLACK = (0, 0, 0)
LIGHT_GREEN = (124, 252, 0)
DARK_GREEN = (34, 139, 34)
G_GREEN = (0, 255, 127)

# Screen resolution
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480


# Moves into GUI and Console Game
class MainMenu(Drawable):
    """ The main menu class that draws the main menu to be rendered to the screen.
        This acts as a intro and switches over to our game when the user hits play. """

    def __init__(self):
        pygame.init()
        super().__init__()
        self.menu_options = ["Play", "Quit"]
        self.iterator = 0
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    def _draw_highlighted_buttons(self):
        """ When mouse hovered or keyboard input, highlights menu buttons """
        mouse = pygame.mouse.get_pos()

        # Iterating so that it highlights last mouse hover over
        # also so that when user use keyboard it also highlights
        if 140 + 100 > mouse[0] > 140 and 400 + 50 > mouse[1] > 400\
                or self.menu_options[self.iterator] == "Play":
            self._draw_button(G_GREEN, (140, 400, 100, 50))
            self.iterator = 0
        else:
            self._draw_button(DARK_GREEN, (140, 400, 100, 50))
        if 400 + 100 > mouse[0] > 400 and 400 + 50 > mouse[1] > 400\
                or self.menu_options[self.iterator] == "Quit":
            self._draw_button(G_GREEN, (400, 400, 100, 50))
            self.iterator = 1
        else:
            self._draw_button(LIGHT_GREEN, (400, 400, 100, 50))

    def _draw_button(self, fill_color, position):
        """ PARAMETERS:
            fill_color: the color fill of the rectangle
            position: the x and y coordinates for placing on the screen
        """
        pygame.draw.rect(self.screen, fill_color, position)

    def _draw_words(self, caption, x_pos, y_pos):
        """ PARAMETERS:
            caption: the text to be blitted to the screen
            x_pos: the x coordinate of the placement of the text
            y_pos: the y coordinate of the placement of the text
        """
        small_text = self._load_font("VarelaRound-Regular.ttf", 20)
        text_surf, text_rect = self.text_objects(caption, small_text)
        text_rect.center = (x_pos, y_pos)
        self.screen.blit(text_surf, text_rect)

    def _handle_events(self):
        """ Handles the event input of mouse or keyboard """
        for event in pygame.event.get():
            # Handles main menu navigation with the mouse
            if event.type == pygame.MOUSEBUTTONUP:
                mouse_pos = pygame.mouse.get_pos()

                if 140 + 100 > mouse_pos[0] > 140 and 400 + 50 > mouse_pos[1] > 400:
                    GameConsole().start_game()
                if 400 + 100 > mouse_pos[0] > 400 and 400 + 50 > mouse_pos[1] > 400:
                    quit()

            # Handles main menu navigation of going up and down
            # if the player is already at Play can't go further up
            # if the player is already at Quit can't go further down
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.iterator = 0
                elif event.key == pygame.K_RIGHT:
                    self.iterator = 1
                elif event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                    if self.menu_options[self.iterator] == "Play":
                        GameConsole().start_game()
                    elif self.menu_options[self.iterator] == "Quit":
                        pygame.quit()
                        sys.exit()

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()  # exit program when closing the window

    @staticmethod
    def text_objects(text, font):
        """ Creates a text object for pygame with
            PARAMETERS:
            text: the input text for what to render to screen
            font: the font parameter of the pygame
        """
        text_surface = font.render(text, True, BLACK)
        return text_surface, text_surface.get_rect()

    def draw(self):
        # pylint: disable=arguments-differ
        """ Draws the main menu screen """
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

            # When the mouse hovers over the buttons it highlights them
            # the same as using keyboard inputs
            self._draw_highlighted_buttons()

            self._draw_words(self.menu_options[0], 140 + 100 / 2, 400 + 50 / 2)
            self._draw_words(self.menu_options[1], 400 + 100 / 2, 400 + 50 / 2)

            pygame.display.update()
            window_clock.tick(60)
