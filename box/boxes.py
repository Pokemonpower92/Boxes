import pygame

from typing import Tuple
import random


class Box(pygame.sprite.Sprite):
    def __init__(self, color):
        pygame.sprite.Sprite.__init__(self)

        randomDimension = self._create_random_dimension()
        self._width = randomDimension[0]
        self._height = randomDimension[1]
        self._centerx = 0
        self._centery = 0
        self._setCoordinates()
        self._color = color

    def _move(self):
        """Move the box randomly, baised towards the center."""

        # Calculate a new distance from center.
        translation = random.uniform(-0.1, 0.1)
        vec = [(self._centerx - 500) * translation, (self._centery - 500) * translation]

        self._setCoordinates(vec)

    def _setCoordinates(self, center=None):

        if not center:
            center = self._create_random_center()

        self._centerx += center[0]
        self._centery += center[1]

        self._top = self._centery - (self._height // 2)
        self._bottom = self._centery + (self._height // 2)
        self._left = self._centerx - (self._width // 2)
        self._right = self._centery + (self._width // 2)

    def _create_random_dimension(self) -> Tuple:
        return (random.randint(1, 1), random.randint(1, 1))

    def _create_random_center(self) -> Tuple:
        return (random.randint(1, 500) + 250, random.randint(1, 500) + 250)

    def custom_draw(self, surface):
        "Draw the box on the given surface."

        self._move()
        pygame.draw.rect(
            surface, self._color, (self._left, self._top, self._width, self._height)
        )
