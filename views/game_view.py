import arcade
from entities import BaseTank, PlayerController, SimpleAIController
from views.game_over_view import GameOverView
from views.win_view import WinView


class GameView(arcade.View):
    def __init__(self):
        super().__init__()

    def on_show_view(self) -> None:
        arcade.set_background_color(arcade.color.GREEN)
        self.all_tanks = arcade.SpriteList()
        self.player = BaseTank(PlayerController())
        self.player.center_x = 0 # где спавнится игрок, потом понять куда надо
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
        game_state = None # это для умных ботов, пока думаем что туда конкретно положить
        for tank in self.all_tanks:
            actions = tank.controller.get_actions(game_state)
            for action in actions: # потом переделать красиво
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
        self._check_bullet_tank_collisions()

    def _check_bullet_tank_collisions(self):
        for bullet in self.bullets:
            hit_tanks = arcade.check_for_collision_with_list(bullet, self.all_tanks)
            for tank in hit_tanks:
                if bullet.owner == tank:
                    continue
                bullet.remove_from_sprite_lists()
                tank.remove_from_sprite_lists()
                if tank == self.player:
                    self.window.show_view(GameOverView())
        if len(self.all_tanks) == 1 and self.all_tanks[0] == self.player:
            self.window.show_view(WinView())
