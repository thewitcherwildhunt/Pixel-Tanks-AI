import arcade
from random import randint
from entities import BaseTank, PlayerController, SimpleAIController
from views.game_over_view import GameOverView
from views.win_view import WinView
from utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT
from utils.game_state import GameState


class GameView(arcade.View):
    def __init__(self):
        super().__init__()

    def on_show_view(self) -> None:
        arcade.set_background_color(arcade.color.GREEN)
        self.all_tanks = arcade.SpriteList()
        self.player = BaseTank(PlayerController(), 0, 0)
        self.all_tanks.append(self.player)
        for _ in range(5 - len(self.all_tanks)):
            self.all_tanks.append(BaseTank(SimpleAIController(), randint(50, 100), randint(50, 100)))
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
        game_state = GameState()
        game_state.delta_time = delta_time # это для умных ботов, пока думаем что туда конкретно положить
        for tank in self.all_tanks:
            actions = tank.controller.get_actions(game_state)
            for action in actions:  # потом переделать красиво
                match action:
                    case "SHOOT":
                        bullet = tank.shoot()
                        self.bullets.append(bullet)
                    case  "W":
                        tank.change_y = tank.speed
                        tank.change_x = 0
                        tank.direction = "W"
                    case "S":
                        tank.change_y = -tank.speed
                        tank.change_x = 0
                        tank.direction = "S"
                    case "A":
                        tank.change_x = -tank.speed
                        tank.change_y = 0
                        tank.direction = "A"
                    case "D":
                        tank.change_x = tank.speed
                        tank.change_y = 0
                        tank.direction = "D"
                    case "STOP":
                        tank.change_x = 0
                        tank.change_y = 0
        for _ in range(5 - len(self.all_tanks)):
            self.all_tanks.append(BaseTank(SimpleAIController(), randint(300, 500), randint(200, 800)))
        self.all_tanks.update()
        self.bullets.update()
        self._check_boundaries()
        self._check_bullet_tank_collisions()

    def _check_bullet_tank_collisions(self):
        for bullet in self.bullets:
            hit_tanks = arcade.check_for_collision_with_list(bullet, self.all_tanks)
            for tank in hit_tanks:
                if bullet.owner == tank or tank == self.player: # потом убрать бессмертие
                    continue
                bullet.remove_from_sprite_lists()
                tank.remove_from_sprite_lists()
                #if tank == self.player:
                    #self.window.show_view(GameOverView())
        if len(self.all_tanks) == 1 and self.all_tanks[0] == self.player:
            self.window.show_view(WinView())

    def _check_boundaries(self):
        for tank in self.all_tanks:
            if tank.left < 0:
                tank.left = 0
            if tank.right > SCREEN_WIDTH:
                tank.right = SCREEN_WIDTH
            if tank.bottom < 0:
                tank.bottom = 0
            if tank.top > SCREEN_HEIGHT:
                tank.top = SCREEN_HEIGHT
