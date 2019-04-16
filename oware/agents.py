import random


class RandomAgent(object):
    """
    A random agent for testing that just plays any non empty pit. This agent just plays dummy without any intention to
    win.
    """

    def get_next_move(self, board_state):
        """
        Return the next move which would be randomly selected
        :param board_state:
        :return:
        """
        non_empty_pits = list()
        for i in range(6):
            if board_state.pits[i] > 0:
                non_empty_pits.append(i)
        return random.choice(non_empty_pits)
