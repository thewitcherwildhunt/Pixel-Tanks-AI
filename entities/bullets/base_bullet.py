import arcade
class BaseBullet(arcade.Sprite):
    def __init__(self,  x, y, owner):
        super().__init__()
        self.center_x = x
        self.center_y = y
        self.speed = 10
        self.owner = owner
        self.texture = arcade.load_texture('assets/images/bullets/bullet.png')