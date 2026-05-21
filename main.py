import arcade

from views.menu_view import MenuView
from utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE


def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    menu = MenuView()
    window.show_view(menu)
    arcade.run()


if __name__ == "__main__":
    main()
