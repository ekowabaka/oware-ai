from copy import copy
from oware import game

class Rules(object):

    def is_valid(self, state, player, pit):
        raise NotImplementedError("")

    def get_next_state(self, state, player, pit):
        new_state = copy(state)
        self.play_pit(new_state, player, pit)
        return new_state

    """
    Abstract class for rules?
    """
    def play_pit(self, board_state, player, pit):
        raise NotImplementedError("The selected rule is not completely implemented. Ensure the update() method exists.")


class AyoRules(Rules):

    def play_pit(self, board_state, player, pit):
        """
        Play a turn of the four four rule game
        :param player:
        :param pit:
        :param board_state:
        :return:
        """

        # Validate the move
        if player == game.SOUTH_PLAYER and pit > 5:
            raise ValueError("Invalid pit number %d for south player. Pit number for south must be 0 through 5" % pit)
        if player == game.NORTH_PLAYER and pit < 6:
            raise ValueError("Invalid pit number %d for north player. Pit number for north must be 6 through 11" % pit)
        if player != game.SOUTH_PLAYER and player != game.NORTH_PLAYER:
            raise ValueError("Player must be either north or south")
        if board_state.pits[pit] == 0:
            raise ValueError("Cannot play an empty pit")

        rounds = 0

        # Perform the entire distribution dance and update scores
        while True:
            seeds_in_hand = board_state.pits[pit]
            board_state.pits[pit] = 0
            while seeds_in_hand > 0:
                pit = (pit + 1) % 12
                board_state.pits[pit] += 1

                if board_state.pits[pit] == 4:
                    board_state.pits[pit] = 0
                    if pit < 6:
                        board_state.score[game.SOUTH_PLAYER] += 4
                    else:
                        board_state.score[game.NORTH_PLAYER] += 4

                seeds_in_hand -= 1

            if sum(board_state.score) == 44:
                board_state.ended = True

            if board_state.pits[pit] == 1 or board_state.pits[pit] == 0:
                break

            if board_state.pits[pit] == 4:
                board_state.score[player] += 4
                board_state.pits[pit] = 0
                break

            rounds += 1
            if rounds > 30:
                break
