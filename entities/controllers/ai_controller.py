from entities.controllers import BaseController
class SimpleAIController(BaseController):
    def get_actions(self, game_state):
        actions = ["SHOOT"]
        return actions