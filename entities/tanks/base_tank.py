import arcade
from entities import BaseBullet
class BaseTank(arcade.Sprite):
    def __init__(self, controller, x, y):
        super().__init__()
        self.center_x = x
        self.center_y = y
        self.speed = 5
        self.direction = "W"
        self.controller = controller
        self.texture = arcade.load_texture("assets/images/tanks/tank_bigRed.png")
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