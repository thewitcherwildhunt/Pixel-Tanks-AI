import arcade
from entities.player import Player


class GameView(arcade.View):
    def __init__(self):
        super().__init__()

    def on_show_view(self) -> None:
        arcade.set_background_color(arcade.color.GREEN)
        self.player = Player()
        self.bullets = arcade.SpriteList()

    def on_draw(self):
        self.clear()
        arcade.draw_sprite(self.player)
        self.bullets.draw()

    def on_key_press(self, symbol: int, modifiers: int) -> bool | None:
        if symbol == arcade.key.W:
            self.player.change_y += self.player.speed
            self.player.direction = "W"
        elif symbol == arcade.key.S:
            self.player.change_y -= self.player.speed
            self.player.direction = "S"
        elif symbol == arcade.key.A:
            self.player.change_x -= self.player.speed
            self.player.direction = "A"
        elif symbol == arcade.key.D:
            self.player.change_x += self.player.speed
            self.player.direction = "D"
        if symbol == arcade.key.SPACE:
            self.bullets.append(self.player.shoot())

    def on_key_release(self, symbol: int, modifiers: int) -> None:
        self.player.change_x = 0
        self.player.change_y = 0

    def on_update(self, delta_time: float) -> bool | None:
        self.player.update()
        self.bullets.update()
