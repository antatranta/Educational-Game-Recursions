"""Utilities to support drawble objects."""
import os
from abc import ABC

import pygame

class Drawable(ABC):
    """Base class for objects to be drawn to screen."""

    def __init__(self):
        self.font = self._load_font("VarelaRound-Regular.ttf", 14)

    def draw(self, screen):
        """Draw this object to given screen."""
        raise NotImplementedError

    def _draw_text(self, screen, text, pos, color=(0, 0, 0), *,
                   background=None, center=False, split_char='\n', font=None):
        # pylint: disable=invalid-name,too-many-locals
        x, y = pos
        font = self.font if font is None else font

        for line in text.split(split_char):
            width, height = font.size(line)
            surface = font.render(line, True, color, background)

            if center:
                screen.blit(surface, (x - int(width / 2), int(y - height / 2)))
            else:
                screen.blit(surface, (x, y))

            y += int(height)

    @classmethod
    def _load_font(cls, font, size):
        path = os.path.join(".", "src", "graphical", "fonts", font)
        return pygame.font.Font(path, size)
