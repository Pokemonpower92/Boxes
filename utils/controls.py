import pygame
from utils import constants


class CTRLS:
    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(CTRLS, cls).__new__(cls)
            cls._time_since_last_button_press = pygame.time.get_ticks()
        return cls.instance

    def _button_pressed(self):
        self._time_since_last_button_press = pygame.time.get_ticks()

    def can_press_button(self):
        current_time = pygame.time.get_ticks()
        delta_time = current_time - self._time_since_last_button_press

        if delta_time > constants.BUTTON_PRESS_COOLDOWN:
            self._button_pressed()
            return True

        return False
