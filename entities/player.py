import arcade
from entities.bullet import Bullet
class Player(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.center_x = 0
        self.center_y = 0
        self.speed = 3
        self.direction = "W"
        self.texture = arcade.make_circle_texture(32, arcade.color.RED)
    def shoot(self):
        bullet = Bullet(self.center_x, self.center_y)
        if self.direction == "W":
            bullet.change_y = bullet.speed
        elif self.direction == "S":
            bullet.change_y = -bullet.speed
        elif self.direction == "D":
            bullet.change_x = bullet.speed
        elif self.direction == "A":
            bullet.change_x = -bullet.speed
        return bullet

