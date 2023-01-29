from utils import constants
from utils.controls import CTRLS
import pygame, sys


class Window:
    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(Window, cls).__new__(cls)
            cls._window = get_window()
        return cls.instance

    def get_window(self):
        return self._window


def get_window():
    pygame.init()
    return pygame.display.set_mode(constants.WINDOW_DIMS, 0, 32)


def check_events():
    pressed_keys = pygame.key.get_pressed()

    if pressed_keys[pygame.K_ESCAPE] and CTRLS().can_press_button():
        return True

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    return False
