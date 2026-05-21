import arcade
from entities.controllers import BaseController


class PlayerController(BaseController):
    def __init__(self):
        self.keys = set()

    def on_key_press(self, symbol: int, modifiers: int) -> bool | None:
        self.keys.add(symbol)

    def on_key_release(self, symbol: int, modifiers: int) -> None:
        self.keys.discard(symbol)

    def get_actions(self, game_state):
        actions = []
        if arcade.key.W in self.keys:
            actions.append("W")
        elif arcade.key.S in self.keys:
            actions.append("S")
        elif arcade.key.A in self.keys:
            actions.append("A")
        elif arcade.key.D in self.keys:
            actions.append("D")
        else:
            actions.append("STOP")
        if arcade.key.SPACE in self.keys:
            actions.append("SHOOT")
        return actions
