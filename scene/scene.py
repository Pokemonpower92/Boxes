from utils import runtime, constants
from pygame import display


class Scene:
    """Scenes are the invokers for a paticular scene to be displayed."""

    def run_scene(self) -> None:
        """Executes the commands in order."""

    def _update(self):
        self._surface.fill(constants.BLACK)
        for sprite in self._all_sprites:
            sprite.update()

    def _draw_sprites(self):

        for sprite in self._all_sprites:
            sprite.custom_draw(self._surface)

    def run_scene(self) -> None:

        self._running = True
        while self._running:
            self._update()
            runtime.check_events()
            self._draw_sprites()
            display.update()
