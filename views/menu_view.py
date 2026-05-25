import arcade
from arcade import View
from utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT
from views.game_view import GameView


class MenuView(View):
    def __init__(self):
        super().__init__()
        self.texture = arcade.load_texture('assets/views_texture/menutexture.avif')
        self.dct_color = {i: arcade.color.WHITE for i in range(1, 5)} | {0: arcade.color.GOLD}
        self.dct_views = {0: GameView, 1: GameView, 2: GameView, 3: GameView, 4: None}  # позже добавить нужные views
        self.choice = 0

    def on_draw(self):
        self.clear()
        arcade.draw_texture_rect(self.texture,
                                 arcade.rect.XYWH(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, SCREEN_WIDTH, SCREEN_HEIGHT))
        arcade.draw_text('Pixel-Tanks-AI', SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT - 40, arcade.color.WHITE, 20)
        arcade.draw_text('Играть', SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT - 80, self.dct_color[0], 20)
        arcade.draw_text('Выбор уровня', SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT - 120, self.dct_color[1], 20)
        arcade.draw_text('Настройки', SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT - 160, self.dct_color[2], 20)
        arcade.draw_text('Рекорды', SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT - 200, self.dct_color[3], 20)
        arcade.draw_text('Выход', SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT - 240, self.dct_color[4], 20)
        arcade.draw_text('"↑↓ выбор, ENTER подтвердить"', 10, 10, arcade.color.WHITE, 20)

    def on_key_press(self, symbol: int, modifiers: int) -> bool | None:
        match symbol:
            case arcade.key.ENTER:
                view = self.dct_views[self.choice]
                if view is None:
                    arcade.exit()
                else:
                    self.window.show_view(view())
            case arcade.key.DOWN:
                self.choice += 1
                self.choice %= 5
                self.dct_color[self.choice] = arcade.color.GOLD
                self.dct_color[(self.choice - 1) % 5] = arcade.color.WHITE
            case arcade.key.UP:
                self.choice -= 1
                self.choice %= 5
                self.dct_color[self.choice] = arcade.color.GOLD
                self.dct_color[(self.choice + 1) % 5] = arcade.color.WHITE
