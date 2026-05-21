class BaseController:
    def get_actions(self, game_state):
        raise NotImplementedError

    def on_key_press(self, key, modifiers):
        pass

    def on_key_release(self, key, modifiers):
        pass