"""
Boxes is a pygame application that
runs an instance of boxes randomly 
walking, with a bias towards a certain 
point.
"""
from gamestate.game_state import GameState
from scene.main_scene import MainScene

if __name__ == "__main__":

    GameState().start_scene(MainScene())
