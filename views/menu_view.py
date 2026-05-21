import arcade
from arcade import View
from utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT
from views.game_view import GameView


class MenuView(View):
    def on_draw(self):
        self.clear()
        arcade.draw_text('Pixel-Tanks-AI', SCREEN_WIDTH // 4, SCREEN_HEIGHT // 3 * 2, arcade.color.WHITE, 20)
        arcade.draw_text('Нажмите Enter для начала игры', SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2, arcade.color.WHITE, 20)
    def on_key_press(self, symbol: int, modifiers: int) -> bool | None:
        if symbol == arcade.key.ENTER:
            self.window.show_view(GameView())

