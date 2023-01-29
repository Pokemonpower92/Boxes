from commands import command
from scene.sim_scene import SimScene
from gamestate.game_state import GameState


class StartSimCommand(command.Command):
    def __init__(self):
        self._scene = SimScene()

    def execute(self) -> None:
        """Start the sim scene."""
        GameState().switch_scene(self._scene)
