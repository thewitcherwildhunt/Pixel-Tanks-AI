import arcade
class Bullet(arcade.Sprite):
    def __init__(self,  x, y):
        super().__init__()
        self.center_x = x
        self.center_y = y
        self.speed = 3
        self.texture = arcade.make_circle_texture(8, arcade.color.WHITE)


