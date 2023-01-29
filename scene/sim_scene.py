from scene.scene import Scene
from box.boxes import Box
from utils.runtime import Window

from pygame import sprite


class SimScene(Scene):
    """
    This the main scene for the application.
    It contains the logic for the main menu.
    """

    def __init__(self):
        """
        Loads the main menus.
        """
        self._surface = Window().get_window()
        self._all_sprites = sprite.Group()

        self._get_boxes()

    def _get_boxes(self):
        self._box_list = [Box((255, 255, 255)) for _ in range(25000)]

        for box in self._box_list:
            self._all_sprites.add(box)
