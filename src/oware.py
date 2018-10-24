import random

def four_four_rules(player, pit, board_state):
    """
    Play a turn of the four four rule game
    :param player:
    :param pit:
    :param board_state:
    :return:
    """

    if player == 'SOUTH' and pit > 5:
        raise ValueError("Invalid pit number %d for south player. Pit number for south must be 0 through 5" % pit)
    if player == 'NORTH' and pit < 6:
        raise ValueError("Invalid pit number %d for north player. Pit number for north must be 6 through 11" % pit)
    if player != 'SOUTH' and player !='NORTH':
        raise ValueError("Player must be either north or south")

    seeds_in_hand = board_state.pits[pit]
    board_state.pits[pit] = 0

    while seeds_in_hand > 0:
        pit = pit + 1 % 12


class BoardState(object):
    """
    Represents the state of a single board
    """

    def __init__(self, pits=None, score=None):
        self.pits = pits if pits else [4] * 12
        self.score = score if score else [0, 0]
        self.ended = False

    def clone(self):
        """
        Creates a clone of the game's board state
        """
        return BoardState(pits=self.pits[:], score=self.score[:])

    def __repr__(self):        
        repr = "=" * 42 + "\n"
        repr += "  "
        for pit in range(11, 5, -1):
            repr += " (%02d) " % self.pits[pit]
        repr += "\n(%02d)                                (%02d)\n  " % (self.score[0], self.score[1])
        for pit in range(0, 6):
            repr += " (%02d) " % self.pits[pit]
        repr += "\n" + "=" * 42 + "\n"
        return repr


class Game(object):
    """
    A Game object represents a match taking place between two agents, one representing north and the other representing
    south. This class manages the overall game state (which includes the board positions and scores), calls up agents to
    play their turns and handles interaction with UI components that display the Game.
    """

    def __init__(self, agents=None, ui=None, rules=four_four_rules):
        self.game_state = BoardState()
        self.agents = agents
        self.ui = ui
        self.rules = rules

    def run(self):
        turn = random.randint(0, 1)
        while not self.game_state.ended:
            self.agents[turn].get_next_move(self.game_state.clone())
            turn = (turn + 1) % 2



