class Rule(object):
    """
    Abstract class for rules?
    """
    def play_pit(self, board_state, player, pit):
        raise NotImplementedError("The selected rule is not complete. Ensure the update() method is implemented")


class FourFour(Rule):

    def play_pit(self, board_state, player, pit):
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
        if player != 'SOUTH' and player != 'NORTH':
            raise ValueError("Player must be either north or south")

        seeds_in_hand = board_state.pits[pit]
        board_state.pits[pit] = 0

        while seeds_in_hand > 0:
            pit = pit + 1 % 12
