from utils import runtime


class GameState:
    """GameState holds the main runtime context for the game."""

    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(GameState, cls).__new__(cls)
            cls._running_scene = None
        return cls.instance

    def start_scene(self, scene=None):
        if scene:
            self._running_scene = scene

        self._running_scene.run_scene()

    def switch_scene(self, scene):
        self._running_scene = scene
        self.start_scene()
