"""Utilities to support drawble objects."""
import os
from abc import ABC

import pygame

class Drawable(ABC):
    """Base class for objects to be drawn to screen."""

    def __init__(self):
        ttf = os.path.join(".", "src", "Varela_Round", "VarelaRound-Regular.ttf")
        self.font = pygame.font.Font(ttf, 18)

    def draw(self, screen):
        """Draw this object to given screen."""
        raise NotImplementedError

    def _draw_text(self, screen, text, pos, color=(0, 0, 0), *,
                   background=None, center=False, split_char='\n'):
        # pylint: disable=invalid-name
        x, y = pos

        for line in text.split(split_char):
            width, height = self.font.size(line)
            surface = self.font.render(line, True, color, background)

            if center:
                screen.blit(surface, (x - int(width / 2), int(y - height / 2)))
            else:
                screen.blit(surface, (x, y))

            y += int(height)
