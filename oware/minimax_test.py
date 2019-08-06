from oware.game import Game
from oware.agents import Agent


class MinimaxAgent(Agent):

    def __init__(self):
        super().__init__()
        self.max_depth = 5
        self.rules = None

    def minimax(state, depth=5, isMax=True):
        if depth == 0 or state.ended:
            return self.evaluate(state)

        if isMax:
            value = -float('inf')
            

    def evaluate(self, board_state):
        print(type(self.rules))

    def get_next_move(self, board_state):
        print(type(self.rules))
