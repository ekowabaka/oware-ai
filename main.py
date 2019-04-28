from oware.game import Game
from oware.agents import RandomAgent
from oware.minimax_test import MinimaxAgent

game = Game(agents=(MinimaxAgent(), RandomAgent()))
game.run()
