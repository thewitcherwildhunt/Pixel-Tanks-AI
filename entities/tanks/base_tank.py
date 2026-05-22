import arcade
from entities import BaseBullet
class BaseTank(arcade.Sprite):
    def __init__(self, controller):
        super().__init__()
        self.center_x = 100
        self.center_y = 100
        self.speed = 5
        self.direction = "W"
        self.controller = controller
        self.texture = arcade.make_circle_texture(32, arcade.color.RED)
    def shoot(self):
        bullet = BaseBullet(self.center_x, self.center_y, self)
        if self.direction == "W":
            bullet.change_y = bullet.speed
        elif self.direction == "S":
            bullet.change_y = -bullet.speed
        elif self.direction == "D":
            bullet.change_x = bullet.speed
        elif self.direction == "A":
            bullet.change_x = -bullet.speed
        return bullet