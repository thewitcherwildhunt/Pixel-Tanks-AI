import arcade
from entities import BaseTank, PlayerController, SimpleAIController


class GameView(arcade.View):
    def __init__(self):
        super().__init__()

    def on_show_view(self) -> None:
        arcade.set_background_color(arcade.color.GREEN)
        self.all_tanks = arcade.SpriteList()
        self.player = BaseTank(PlayerController())
        self.all_tanks.append(self.player)
        self.all_tanks.append(BaseTank(SimpleAIController()))
        self.bullets = arcade.SpriteList()

    def on_draw(self):
        self.clear()
        self.all_tanks.draw()
        self.bullets.draw()

    def on_key_press(self, symbol: int, modifiers: int) -> bool | None:
        self.player.controller.on_key_press(symbol, modifiers)

    def on_key_release(self, symbol: int, modifiers: int) -> None:
        self.player.controller.on_key_release(symbol, modifiers)

    def on_update(self, delta_time: float) -> bool | None:
        game_state = None
        for tank in self.all_tanks:
            actions = tank.controller.get_actions(game_state)
            for action in actions:
                if action == "SHOOT":
                    bullet = tank.shoot()
                    self.bullets.append(bullet)
                elif action == "W":
                    tank.change_y = tank.speed
                    tank.change_x = 0
                    tank.direction = "W"
                elif action == "S":
                    tank.change_y = -tank.speed
                    tank.change_x = 0
                    tank.direction = "S"
                elif action == "A":
                    tank.change_x = -tank.speed
                    tank.change_y = 0
                    tank.direction = "A"
                elif action == "D":
                    tank.change_x = tank.speed
                    tank.change_y = 0
                    tank.direction = "D"
                elif action == "STOP":
                    tank.change_x = 0
                    tank.change_y = 0
        self.all_tanks.update()
        self.bullets.update()
