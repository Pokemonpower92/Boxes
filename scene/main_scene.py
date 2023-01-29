from scene.scene import Scene
from commands.start_sim_command import StartSimCommand
from sprite.button_sprite import ButtonSprite
from utils.runtime import Window

from pygame import sprite


class MainScene(Scene):
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
        self._button_sprites = sprite.Group()

        self._set_buttons()

    def _set_buttons(self):
        self._start_scene_button = ButtonSprite().with_text("Start Sim").build()
        self._start_scene_button.set_command(StartSimCommand())

        self._all_sprites.add(self._start_scene_button)
        self._button_sprites.add(self._start_scene_button)
