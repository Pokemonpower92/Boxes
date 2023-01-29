from scene import command
from utils import check_events
import constants
import pygame


class SceneCommand(command.Command):
    """
    This command performs the game loop for the main
    menu scene.
    """

    def __init__(self, scene):
        self._scene = scene

    def execute(self) -> None:
        """
        Run the main loop for the scene.
        This is generic, and most scenes should
        implement execute themselves.
        """

        while True:
            self._scene.surface.fill(constants.BLACK)
            for asset in self._scene.assets:
                asset.draw(self._scene.surface)

            pygame.display.update()
            if check_events():
                break
