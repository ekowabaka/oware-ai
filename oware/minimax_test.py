from oware.game import Game, SOUTH_PLAYER, NORTH_PLAYER
from oware.agents import Agent


class MinimaxAgent(Agent):

    def __init__(self):
        super().__init__()
        self.max_depth = 5
        self.rules = None

    def minimax(self, state, depth=5, is_max=True, get_pit=True):
        best_pit = None
        best_value = None
        if depth == 0 or state.ended:
            return self.evaluate(state)
        if is_max:
            value = -float('inf')
            for pit in range(6):
                if state.pits[pit] > 0:
                    successor = self.rules.get_next_state(state, SOUTH_PLAYER, pit)
                    value = max(value, self.minimax(successor, depth=depth-1, is_max=False, get_pit=False))
                if get_pit and best_value != value:
                    best_value = value
                    best_pit = pit
            return best_pit if get_pit else value
        else:
            value = float("inf")
            for pit in range(6, 12):
                if state.pits[pit] > 0:
                    successor = self.rules.get_next_state(state, NORTH_PLAYER, pit)
                    value = min(value, self.minimax(successor, depth=depth-1, is_max=True, get_pit=False))
            return value

    def evaluate(self, board_state):
        return board_state.score[0] - board_state.score[1]

    def get_next_move(self, board_state):
        return self.minimax(board_state, self.max_depth)
