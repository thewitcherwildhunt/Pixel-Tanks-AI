import arcade
from utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE
class GameOverView(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.BLUE)
    def on_draw(self):
        self.clear()
        arcade.draw_text("GAME OVER", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, arcade.color.RED, font_size=20)