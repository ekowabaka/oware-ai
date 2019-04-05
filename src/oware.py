from copy import copy
from rules import FourFour
import random


class BoardState(object):
    """
    Represents the state of a single board
    """

    def __init__(self, pits=None, score=None):
        self.pits = pits if pits else [4] * 12
        self.score = score if score else [0, 0]
        self.ended = False

    def __copy__(self):
        """
        Creates a clone of the game's board state
        """
        return BoardState(pits=self.pits[:], score=self.score[:])

    def __repr__(self):
        board_text_image = "=" * 42 + "\n"
        board_text_image += "  "
        for pit in range(11, 5, -1):
            board_text_image += " (%02d) " % self.pits[pit]
        board_text_image += "\n(%02d)                                (%02d)\n  " % (self.score[0], self.score[1])
        for pit in range(0, 6):
            board_text_image += " (%02d) " % self.pits[pit]
        board_text_image += "\n" + "=" * 42 + "\n"
        return board_text_image

    def flip(self):
        self.score.reverse()
        self.pits = self.pits[6:12] + self.pits[0:6]


class Game(object):
    """
    A Game object represents a match taking place between two agents, one representing north and the other representing
    south. This class manages the overall game state (which includes the board positions and scores), calls up agents to
    play their turns and handles interaction with UI components that display the Game.
    """

    def __init__(self, agents=None, ui=None, rules=None):
        self.game_state = BoardState()
        self.agents = agents
        self.ui = ui
        self.rules = rules if rules else FourFour()

    def run(self):
        # Holds whose turn it is 0 for south 1 for north
        turn = random.randint(0, 1)

        while not self.game_state.ended:
            board = copy(self.game_state)

            # Since every agent assumes to be playing south, ensure the board state is appropriately oriented before
            # calling the agent
            if turn == 1:
                board.flip()

            pit = self.agents[turn].get_next_move(board)

            if turn == 1:
                pit += 6

            self.rules.play_pit(self.game_state, 'SOUTH' if turn == 0 else 'NORTH', pit)
            print(self.game_state)
            turn = (turn + 1) % 2
