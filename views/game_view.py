import arcade
from utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE
class GameView(arcade.View):
    def __init__(self):
        super().__init__()
    def on_show_view(self) -> None:
        arcade.set_background_color(arcade.color.GREEN)
    def on_draw(self):
        self.clear()
        arcade.draw_text('Тут будет игра', SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2, arcade.color.BLACK, 20)
