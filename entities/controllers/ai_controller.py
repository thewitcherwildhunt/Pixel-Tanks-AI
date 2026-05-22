import random
from entities.controllers import BaseController


class SimpleAIController(BaseController):
    def __init__(self):
        self.current_actions = ["STOP"]
        self.action_timer = 0
        self.action_duration = 0.5  # секунд на одно действие

    def get_actions(self, game_state):
        self.action_timer += game_state.delta_time
        if self.action_timer >= self.action_duration:
            self.action_timer = 0
            self.action_duration = random.uniform(0.5, 2.0)  # случайная длительность
            self.current_actions = [random.choice([
                "W", "S", "A", "D"
            ])]
        actions = self.current_actions.copy()
        if random.random() < 0.01:
            actions.append("SHOOT")
        return actions
